# Leo Tan SEO Agency -- Capabilities & Services

## Core Services

### 1. Technical SEO Audit & Fix
- **What**: Full crawl analysis, Core Web Vitals, indexation issues, schema markup, security headers
- **Outcome**: Clean technical foundation that search engines can crawl and index efficiently
- **Tools**: seo-audit-tool (our Next.js dashboard), DataForSEO, Google Search Console

### 2. AI-Powered Content Engine
- **What**: Research > Brief > Write > Optimize > Publish pipeline, fully automated
- **Outcome**: 20-50 SEO-optimized articles per month per client, each targeting specific keyword clusters
- **Tools**: seomachine (this repo), Claude, DataForSEO, WordPress REST API

### 3. Keyword Research & Strategy
- **What**: Topic cluster mapping, competitor gap analysis, SERP analysis, opportunity scoring
- **Outcome**: Prioritized keyword roadmap with estimated traffic value and difficulty
- **Tools**: DataForSEO, Google Analytics 4, Google Search Console

### 4. Competitor Intelligence
- **What**: Content gap analysis, backlink profile comparison, SERP position tracking
- **Outcome**: Actionable list of keywords competitors rank for that client doesn't
- **Tools**: research_competitor_gaps.py, seo_competitor_analysis.py

### 5. Performance Monitoring & Reporting
- **What**: Rankings tracking, traffic trends, content performance scoring, ROI attribution
- **Outcome**: Monthly reports with clear metrics and next-action items
- **Tools**: GA4, GSC, DataForSEO, automated Lark/Sheet reporting

### 6. AI Citation Optimization (GEO/AEO)
- **What**: Optimize content for AI search engines (Google AI Overviews, ChatGPT, Perplexity)
- **Outcome**: Brand appears in AI-generated answers and citations
- **Tools**: /research-ai-citations command, ai-citation-targets.md

## Technical Stack

### Content Pipeline
- **seomachine**: Claude Code workspace with 24 commands, 11 agents, 26 marketing skills
- **Python analytics**: GA4, GSC, DataForSEO integrations for data-driven decisions
- **WordPress publishing**: Automated via REST API with Yoast SEO metadata

### Audit & Dashboard
- **seo-audit-tool**: Next.js + Supabase web app for client-facing audit reports
- **DataForSEO**: Live SERP data, keyword metrics, backlink profiles
- **Chat agent**: Claude-powered assistant for on-demand SEO questions

### Client Platform
- **build-the-best**: AutoSEO management platform with onboarding, blog feed, roadmap

## Competitive Differentiators

### vs. Traditional SEO Agencies
- **Fully automated content pipeline** (they use manual writers at $0.10/word)
- **Real-time data integrations** (they pull monthly spreadsheets)
- **AI-native from day one** (they're bolting AI onto legacy processes)
- **Transparent pricing** (no retainer mystery, pay per output)

### vs. SEO Tools (Ahrefs, SEMrush)
- **We execute, not just report** (tools show problems, we fix them)
- **Content creation included** (tools don't write articles)
- **Strategy + implementation** (tools are self-serve, we're done-for-you)

### vs. AI Content Tools (Jasper, SurferSEO)
- **Full pipeline, not just writing** (research + strategy + publish + monitor)
- **Data-driven prioritization** (we pick what to write based on ROI, not guesses)
- **Technical SEO included** (content tools ignore site health)

## Client Segments

### SMBs (5-50 employees)
- Need affordable SEO without hiring in-house
- Want to see results within 3-6 months
- Budget: $1,500-5,000/month

### SaaS Companies
- Need programmatic SEO at scale
- Want topic clusters around product features
- Budget: $3,000-10,000/month

### Local Businesses
- Need local SEO + Google Business Profile optimization
- Want to rank for "[service] in [city]" keywords
- Budget: $500-2,000/month

### E-commerce
- Need product page optimization + category content
- Want to compete on long-tail product keywords
- Budget: $2,000-8,000/month
