# Client Performance Report

Generate a performance report for a specific client.

## Input
The user provides: client slug (from clients/ directory)

## Steps

1. **Load client config** from `clients/<client-slug>/config.json`

2. **Gather metrics** (use available data sources):
   - Count articles: published, drafts, in research
   - If GA4/GSC configured: pull traffic and ranking data
   - If DataForSEO configured: pull SERP positions for target keywords
   - Count keyword clusters covered vs. planned

3. **Assess content pipeline health**:
   - Articles published this period vs. target
   - Average SEO quality score of published articles
   - Topic cluster completion percentage

4. **Identify wins**:
   - Keywords that moved to page 1
   - Traffic increases on published content
   - New ranking keywords

5. **Identify gaps**:
   - Planned clusters with no content yet
   - Declining positions that need rewrites
   - Technical issues found

6. **Generate next-action items**:
   - Priority articles to write next
   - Content to rewrite/update
   - Technical fixes needed

7. **Format as human-readable report** and save to:
   - `clients/<client-slug>/reports/YYYY-MM-DD-report.md`
   - Also output to terminal for the user
