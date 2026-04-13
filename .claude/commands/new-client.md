# New Client Onboarding

Set up a new client in the seomachine multi-client system. This command orchestrates across all 3 agency repos.

## Input
The user provides: client name, website URL, industry, and any initial keywords.

## Steps

1. **Create client slug** from the company name (lowercase, hyphens, no spaces)

2. **Create client directory** by copying the template:
   ```
   cp -r clients/.template clients/<client-slug>
   ```

3. **Fill in config.json** with the provided details:
   - client_name, client_slug, website, industry
   - Detect CMS from the website (check for /wp-admin, Shopify patterns, etc.)
   - Set monthly_article_target based on industry (default: 10)

4. **Run discovery via seo-audit-tool bridge**:
   ```python
   from integrations.seo_audit_bridge import SEOAuditBridge
   bridge = SEOAuditBridge()
   discovery = bridge.discover(website_url, country)
   ```
   This returns: competitors, top keywords, inferred services, site description.
   Save the raw discovery result to `clients/<client-slug>/research/discovery.json`.

5. **Run full audit + keyword analysis via seo-audit-tool**:
   ```python
   result = bridge.run_full_analysis(website_url, country, discovery["competitors"][:3])
   ```
   This creates Google Sheets with 20+ tabs of audit data and keyword analysis.
   Save the sheet URLs to config.json (`audit_sheet_url`, `keyword_sheet_url`).

6. **Check AutoSEO for existing website data**:
   ```python
   from integrations.autoseo_bridge import AutoSEOBridge
   autoseo = AutoSEOBridge()
   website = autoseo.get_website_by_domain(website_url)
   if website:
       # Sync existing keywords to seomachine
       autoseo.sync_keywords_to_seomachine(
           website["id"],
           f"clients/<client-slug>/context/target-keywords.md"
       )
       # Save website_id for article push later
       # Add autoseo_website_id to config.json
   ```

7. **Fill in brand voice override** (clients/<client-slug>/context/brand-voice.md):
   - Use the discovery data to understand the business
   - Crawl 2-3 blog posts to analyze tone and style
   - Document their target audience
   - Set appropriate voice adjustments

8. **Create initial keyword clusters** based on:
   - Discovery keywords + audit keyword data
   - Competitor gap analysis from the audit sheets
   - Website's existing content gaps

9. **Generate a 30-day content plan** with prioritized topics:
   - Save to `clients/<client-slug>/research/content-plan-30d.md`
   - Prioritize by: search volume x difficulty x intent match
   - Include 1 pillar article + 4-5 cluster articles per week

10. **Output a summary** to the user with:
    - Client setup confirmation
    - Google Sheet links (audit + keywords)
    - Initial keyword opportunities found
    - Suggested first 5 articles with estimated traffic
    - AutoSEO sync status (if website exists there)

Save all research to `clients/<client-slug>/research/`.
