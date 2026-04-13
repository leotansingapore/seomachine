#!/usr/bin/env python3
"""
Bridge: seomachine -> seo-audit-tool

Calls the seo-audit-tool API to run audits and keyword analysis,
then pulls results back into seomachine's pipeline.

Usage:
    from integrations.seo_audit_bridge import SEOAuditBridge
    bridge = SEOAuditBridge()
    result = bridge.discover("example.com", "sg")
    result = bridge.run_audit("example.com", "sg")
    result = bridge.run_keyword_analysis("example.com", "sg", ["comp1.com"])
    history = bridge.get_analyses("example.com")
"""

import json
import os
import time
from urllib.parse import urljoin

import requests
from dotenv import load_dotenv

load_dotenv()
load_dotenv("data_sources/config/.env")

DEFAULT_BASE_URL = "https://seo-audit-tool-leotansingapores-projects.vercel.app"


class SEOAuditBridge:
    def __init__(self, base_url=None):
        self.base_url = base_url or os.getenv("SEO_AUDIT_TOOL_URL", DEFAULT_BASE_URL)
        self.supabase_url = os.getenv("SEO_AUDIT_SUPABASE_URL", "")
        self.supabase_key = os.getenv("SEO_AUDIT_SUPABASE_SERVICE_KEY", "")

    def _api(self, path):
        return urljoin(self.base_url.rstrip("/") + "/", path.lstrip("/"))

    def discover(self, url, country="sg"):
        """Quick discovery: competitors, keywords, services for a domain.
        Returns structured JSON -- lightest entry point."""
        resp = requests.post(
            self._api("/api/discover"),
            json={"url": f"https://{url}" if not url.startswith("http") else url, "country": country},
            timeout=60,
        )
        resp.raise_for_status()
        return resp.json()

    def run_audit(self, url, country="sg", max_pages=100, include_pagespeed=True):
        """Run full technical SEO audit. Returns SSE events, final event has sheet_url."""
        return self._stream_request("/api/audit", {
            "url": f"https://{url}" if not url.startswith("http") else url,
            "country": country,
            "sheetName": f"Audit - {url} - {time.strftime('%Y-%m-%d')}",
            "maxPages": max_pages,
            "includePageSpeed": include_pagespeed,
        })

    def run_keyword_analysis(self, url, country="sg", competitors=None):
        """Run keyword analysis with competitor comparison. Returns SSE events."""
        return self._stream_request("/api/analyze", {
            "url": f"https://{url}" if not url.startswith("http") else url,
            "country": country,
            "competitors": competitors or [],
            "mode": "keywords",
            "sheetName": f"Keywords - {url} - {time.strftime('%Y-%m-%d')}",
        })

    def run_full_analysis(self, url, country="sg", competitors=None):
        """Run both audit + keywords. Returns SSE events."""
        return self._stream_request("/api/analyze", {
            "url": f"https://{url}" if not url.startswith("http") else url,
            "country": country,
            "competitors": competitors or [],
            "mode": "both",
            "sheetName": f"Full Analysis - {url} - {time.strftime('%Y-%m-%d')}",
        })

    def get_analyses(self, domain=None, limit=20):
        """Fetch analysis history from Supabase directly."""
        if self.supabase_url and self.supabase_key:
            headers = {
                "apikey": self.supabase_key,
                "Authorization": f"Bearer {self.supabase_key}",
            }
            params = {"limit": limit, "order": "created_at.desc"}
            if domain:
                params["domain"] = f"eq.{domain}"
            resp = requests.get(
                f"{self.supabase_url}/rest/v1/analyses",
                headers=headers,
                params=params,
                timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        # Fallback to API
        resp = requests.get(
            self._api("/api/analyses"),
            params={"limit": limit},
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    def _stream_request(self, path, payload):
        """Send POST, consume SSE stream, return final result."""
        resp = requests.post(
            self._api(path),
            json=payload,
            stream=True,
            timeout=600,
        )
        resp.raise_for_status()

        result = {}
        for line in resp.iter_lines(decode_unicode=True):
            if not line or not line.startswith("data: "):
                continue
            data_str = line[6:]
            if data_str == "[DONE]":
                break
            try:
                event = json.loads(data_str)
                event_type = event.get("type", "")
                if event_type == "status":
                    print(f"  [{event_type}] {event.get('message', '')}")
                elif event_type == "progress":
                    print(f"  [{event_type}] {event.get('step', '')} {event.get('progress', '')}%")
                elif event_type == "done":
                    result = event
                elif event_type == "error":
                    result = {"error": event.get("message", "Unknown error")}
                elif event_type == "analysisId":
                    result["analysisId"] = event.get("id", "")
            except json.JSONDecodeError:
                continue

        return result


if __name__ == "__main__":
    import sys
    bridge = SEOAuditBridge()
    if len(sys.argv) < 2:
        print("Usage: python seo_audit_bridge.py <domain> [country]")
        sys.exit(1)
    domain = sys.argv[1]
    country = sys.argv[2] if len(sys.argv) > 2 else "sg"
    print(f"Discovering {domain} ({country})...")
    result = bridge.discover(domain, country)
    print(json.dumps(result, indent=2))
