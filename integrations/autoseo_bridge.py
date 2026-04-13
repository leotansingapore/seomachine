#!/usr/bin/env python3
"""
Bridge: seomachine -> build-the-best (AutoSEO)

Pushes published articles from seomachine into AutoSEO's article system
via the receive-article Supabase edge function, and reads client website
configs to inform content generation.

Usage:
    from integrations.autoseo_bridge import AutoSEOBridge
    bridge = AutoSEOBridge()
    bridge.push_article("client-slug", article_data)
    websites = bridge.get_websites()
    keywords = bridge.get_keywords(website_id)
"""

import json
import os
import re
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()
load_dotenv("data_sources/config/.env")


class AutoSEOBridge:
    def __init__(self):
        self.supabase_url = os.getenv(
            "AUTOSEO_SUPABASE_URL",
            "https://ebglgluymcrovoqdhgvn.supabase.co",
        )
        self.supabase_key = os.getenv("AUTOSEO_SUPABASE_SERVICE_KEY", "")
        self.receive_article_url = os.getenv(
            "AUTOSEO_RECEIVE_ARTICLE_URL",
            f"{self.supabase_url}/functions/v1/receive-article",
        )

    def _headers(self):
        return {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json",
        }

    def get_websites(self):
        """Fetch all client websites from AutoSEO."""
        resp = requests.get(
            f"{self.supabase_url}/rest/v1/websites",
            headers=self._headers(),
            params={"select": "*", "order": "created_at.desc"},
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    def get_website_by_domain(self, domain):
        """Find a website by its URL domain."""
        clean = domain.replace("https://", "").replace("http://", "").rstrip("/")
        resp = requests.get(
            f"{self.supabase_url}/rest/v1/websites",
            headers=self._headers(),
            params={"select": "*", "url": f"like.*{clean}*"},
            timeout=30,
        )
        resp.raise_for_status()
        sites = resp.json()
        return sites[0] if sites else None

    def get_keywords(self, website_id):
        """Fetch keywords for a website."""
        resp = requests.get(
            f"{self.supabase_url}/rest/v1/keywords",
            headers=self._headers(),
            params={
                "select": "*",
                "website_id": f"eq.{website_id}",
                "order": "monthly_volume.desc",
            },
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    def get_articles(self, website_id, status=None):
        """Fetch articles for a website, optionally filtered by status."""
        params = {
            "select": "*",
            "website_id": f"eq.{website_id}",
            "order": "created_at.desc",
        }
        if status:
            params["status"] = f"eq.{status}"
        resp = requests.get(
            f"{self.supabase_url}/rest/v1/articles",
            headers=self._headers(),
            params=params,
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    def push_article(self, draft_path, website_id=None):
        """Push a seomachine draft to AutoSEO via receive-article webhook.

        Reads the markdown draft, extracts frontmatter, converts to the
        receive-article payload format.
        """
        with open(draft_path) as f:
            content = f.read()

        # Extract frontmatter and body
        meta = self._parse_frontmatter(content)
        body_html = self._md_to_html(content)

        payload = {
            "title": meta.get("title", os.path.basename(draft_path).replace("-", " ").replace(".md", "")),
            "slug": meta.get("slug", self._slugify(meta.get("title", "untitled"))),
            "content_html": body_html,
            "summary": meta.get("meta_description", ""),
            "meta_description": meta.get("meta_description", ""),
            "meta_keywords": meta.get("keywords", "").split(", ") if meta.get("keywords") else [],
            "tags": meta.get("tags", "").split(", ") if meta.get("tags") else [],
            "reading_time": max(1, len(body_html.split()) // 200),
            "faq_schema": meta.get("faq_schema", None),
        }

        if website_id:
            payload["website_id"] = website_id

        resp = requests.post(
            self.receive_article_url,
            headers=self._headers(),
            json=payload,
            timeout=60,
        )
        resp.raise_for_status()
        print(f"Article pushed to AutoSEO: {payload['title']}")
        return resp.json()

    def sync_keywords_to_seomachine(self, website_id, output_path):
        """Pull AutoSEO keywords and write them to a seomachine target-keywords file."""
        keywords = self.get_keywords(website_id)
        if not keywords:
            print("No keywords found")
            return

        lines = ["# Target Keywords (synced from AutoSEO)\n"]
        lines.append(f"# Last synced: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")

        selected = [k for k in keywords if k.get("selected")]
        unselected = [k for k in keywords if not k.get("selected")]

        if selected:
            lines.append("## Priority Keywords\n")
            lines.append("| Keyword | Volume | Difficulty |\n")
            lines.append("|---------|--------|------------|\n")
            for k in selected:
                lines.append(f"| {k['term']} | {k.get('monthly_volume', 'N/A')} | {k.get('difficulty', 'N/A')} |\n")

        if unselected:
            lines.append("\n## Additional Keywords\n")
            lines.append("| Keyword | Volume | Difficulty |\n")
            lines.append("|---------|--------|------------|\n")
            for k in unselected[:50]:
                lines.append(f"| {k['term']} | {k.get('monthly_volume', 'N/A')} | {k.get('difficulty', 'N/A')} |\n")

        with open(output_path, "w") as f:
            f.writelines(lines)
        print(f"Synced {len(keywords)} keywords to {output_path}")

    def _parse_frontmatter(self, content):
        """Extract YAML-like frontmatter from markdown."""
        meta = {}
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                for line in parts[1].strip().split("\n"):
                    if ":" in line:
                        key, val = line.split(":", 1)
                        meta[key.strip().lower().replace(" ", "_")] = val.strip().strip('"').strip("'")
        return meta

    def _md_to_html(self, content):
        """Basic markdown to HTML. For full conversion, use the markdown library."""
        # Strip frontmatter
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                content = parts[2]
        try:
            import markdown
            return markdown.markdown(content, extensions=["tables", "fenced_code"])
        except ImportError:
            # Minimal fallback
            return f"<div>{content}</div>"

    def _slugify(self, text):
        text = text.lower().strip()
        text = re.sub(r"[^\w\s-]", "", text)
        text = re.sub(r"[\s_]+", "-", text)
        return text[:80]


if __name__ == "__main__":
    bridge = AutoSEOBridge()
    sites = bridge.get_websites()
    print(f"Found {len(sites)} websites in AutoSEO:")
    for s in sites:
        print(f"  - {s.get('brand_name', 'unnamed')} ({s.get('url', 'no url')})")
