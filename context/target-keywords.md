# Target Keywords

> **Multi-client system**: Target keywords are client-specific. Load from `clients/<slug>/context/target-keywords.md` for any active client engagement.
>
> This file contains agency-level seed keywords for content about SEO services. Use these to build out agency marketing content, case study topics, and service landing pages.

---

## Agency Seed Keywords

These keywords describe SEO services and attract potential clients searching for SEO help.

| Keyword | Intent | Notes |
|---|---|---|
| technical SEO audit | Commercial | High-value service entry point |
| content strategy for SEO | Informational/Commercial | Broad, top-of-funnel |
| keyword research service | Commercial | Direct service keyword |
| link building service | Commercial | High competition, high value |
| SEO agency | Commercial | Branded + location modifiers needed |
| on-page SEO optimization | Informational/Commercial | Mid-funnel |
| local SEO services | Commercial | Location-based modifier required |
| SEO content writing | Commercial | Pairs with content service |
| competitor SEO analysis | Informational/Commercial | Ties to audit service |
| SEO reporting dashboard | Informational | Tool/platform keyword |
| ecommerce SEO | Commercial | Vertical-specific |
| B2B SEO strategy | Informational/Commercial | Vertical-specific |
| SEO for SaaS companies | Informational/Commercial | Vertical-specific, growing |
| programmatic SEO | Informational | Emerging tactic, lower competition |
| SEO ROI calculator | Informational/Tool | Lead magnet keyword |

---

## Topic Cluster Structure

Each topic cluster should have:
- **Pillar Keyword**: Main, high-volume keyword (typically competitive)
- **Cluster Keywords**: 5-10 related keywords (subtopics)
- **Long-Tail Keywords**: 10-15 specific, lower-volume phrases
- **Search Intent**: What users want (informational, commercial, transactional)

---

## Cluster 1: Technical SEO

### Pillar Keyword
- **Keyword**: technical SEO audit
- **Intent**: Commercial
- **Pillar Content**: [URL when created]

### Cluster Keywords
1. technical SEO checklist
2. site speed optimization
3. crawl budget optimization
4. Core Web Vitals
5. structured data markup
6. canonical tags
7. mobile SEO
8. JavaScript SEO
9. XML sitemap optimization
10. robots.txt best practices

### Long-Tail Keywords
- how to do a technical SEO audit
- technical SEO issues that hurt rankings
- fix crawl errors Google Search Console
- what is a technical SEO audit
- technical SEO for ecommerce sites
- Core Web Vitals failing how to fix
- how to improve page speed for SEO

---

## Cluster 2: Keyword Research

### Pillar Keyword
- **Keyword**: keyword research
- **Intent**: Informational/Commercial

### Cluster Keywords
1. long-tail keywords
2. keyword difficulty
3. search volume
4. keyword gap analysis
5. semantic keywords
6. keyword clustering
7. search intent analysis

### Long-Tail Keywords
- how to find low competition keywords
- keyword research tools comparison
- how to group keywords into clusters
- transactional vs informational keywords
- how to prioritize keywords by business value

---

## Cluster 3: Content Strategy

### Pillar Keyword
- **Keyword**: SEO content strategy
- **Intent**: Informational/Commercial

### Cluster Keywords
1. topic clusters
2. pillar pages
3. content gap analysis
4. content brief
5. content calendar for SEO
6. evergreen content
7. content refresh

### Long-Tail Keywords
- how to build a content strategy for SEO
- content gap analysis step by step
- how to write SEO-optimized content
- when to update old blog posts for SEO
- how long should SEO articles be

---

## Cluster 4: Link Building

### Pillar Keyword
- **Keyword**: link building
- **Intent**: Commercial/Informational

### Cluster Keywords
1. backlink analysis
2. guest posting
3. digital PR
4. broken link building
5. link prospecting
6. domain authority
7. toxic backlinks

### Long-Tail Keywords
- how to get high quality backlinks
- link building outreach templates
- link building for new websites
- how to disavow toxic backlinks
- what is a good domain rating

---

## Cluster 5: SEO Reporting & Analytics

### Pillar Keyword
- **Keyword**: SEO reporting
- **Intent**: Informational/Commercial

### Cluster Keywords
1. Google Search Console tutorial
2. GA4 SEO tracking
3. rank tracking
4. SEO dashboard
5. organic traffic analysis
6. SEO KPIs
7. conversion tracking for SEO

### Long-Tail Keywords
- how to report SEO results to clients
- best SEO metrics to track
- how to set up rank tracking
- Google Search Console vs GA4 for SEO
- what SEO KPIs matter most

---

## Competitor Keyword Gaps

Track keywords where competitors rank but the agency does not. Populate per client engagement.

| Keyword | Competitor | Their Position | Agency Position | Opportunity |
|---|---|---|---|---|
| [keyword] | [competitor] | [rank] | Not ranking | [High/Med/Low] |

---

## Keyword Opportunity Pipeline

### High Priority (Create Soon)
Populate based on current agency focus and client verticals.

### Medium Priority (Next Quarter)
[Add from keyword research]

### Low Priority (Future)
[Add from keyword research]

---

## Usage Guidelines

### When Writing New Agency Content
1. Check which cluster the topic belongs to
2. Target the appropriate cluster or long-tail keyword
3. Reference pillar content in that cluster
4. Include semantic keywords naturally
5. Link to related cluster articles

### When Onboarding a New Client
1. Copy `clients/.template/context/target-keywords.md` to `clients/<slug>/context/`
2. Run keyword research for their industry and competitors
3. Populate the client file -- do not overwrite this agency file
4. Sync AutoSEO keywords via `integrations/autoseo_bridge.py`

---

## Maintenance

**Last Updated**: 2026-04-13
**Next Review**: 2026-07-13

Update this file when the agency adds new service lines or shifts positioning. Keep client keyword files separate.
