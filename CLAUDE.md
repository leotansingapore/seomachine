# CLAUDE.md

## Project Overview

SEO Machine -- forked and adapted as Leo Tan's autonomous SEO agency content engine. Multi-client system that researches, writes, optimizes, and publishes SEO content at scale.

Part of a 3-repo agency system:
- **seomachine** (this repo): Content engine -- research, write, optimize, publish
- **seo-audit-tool**: Client-facing audit dashboard (Next.js + Supabase)
- **build-the-best**: Client SEO management platform (AutoSEO)

## Multi-Client Architecture

```
clients/
  .template/          # Copy this for new clients
    config.json       # Client settings (CMS, GA4, GSC, competitors)
    context/          # Brand voice overrides
    research/         # Client-specific research
    drafts/           # Client drafts
    published/        # Published content
  <client-slug>/      # Each client gets their own directory
```

Client context overrides agency defaults in `context/`. Load client config before any content work.

## Setup

```bash
pip install -r data_sources/requirements.txt
```

API credentials: `data_sources/config/.env` (GA4, GSC, DataForSEO, WordPress).

## Commands

### Agency Commands (new)
- `/new-client [name, url, industry]` - Onboard a new client, research their site, create content plan
- `/client-report [client-slug]` - Generate performance report for a client

### Content Commands (from upstream)
- `/research [topic]` - Keyword/competitor research, generates brief in `research/`
- `/write [topic]` - Create full article in `drafts/`, auto-triggers optimization agents
- `/rewrite [topic]` - Update existing content, saves to `rewrites/`
- `/optimize [file]` - Final SEO polish pass
- `/analyze-existing [URL or file]` - Content health audit
- `/performance-review` - Analytics-driven content priorities
- `/publish-draft [file]` - Publish to WordPress via REST API
- `/article [topic]` - Simplified article creation
- `/cluster [topic]` - Topic cluster strategy with pillar + supporting articles
- `/priorities` - Content prioritization matrix
- `/research-serp`, `/research-gaps`, `/research-trending`, `/research-performance`, `/research-topics` - Specialized research
- `/research-ai-citations [topic]` - AI citation audit
- `/repurpose [file]` - Adapt for LinkedIn, Medium, Reddit, Quora
- `/landing-write`, `/landing-audit`, `/landing-research`, `/landing-publish`, `/landing-competitor` - Landing pages

## Architecture

### Command-Agent Model

**Commands** (`.claude/commands/`) orchestrate workflows. **Agents** (`.claude/agents/`) are specialized roles. After `/write`, these agents auto-run: SEO Optimizer, Meta Creator, Internal Linker, Keyword Mapper.

Agents: content-analyzer, seo-optimizer, meta-creator, internal-linker, keyword-mapper, editor, headline-generator, cro-analyst, performance, cluster-strategist.

### Python Analysis Pipeline

Located in `data_sources/modules/`:
1. `search_intent_analyzer.py` - Query intent classification
2. `keyword_analyzer.py` - Density, distribution, stuffing detection
3. `content_length_comparator.py` - Benchmarks against top 10 SERP results
4. `readability_scorer.py` - Flesch Reading Ease, grade level
5. `seo_quality_rater.py` - Comprehensive 0-100 SEO score

### Data Integrations

- `google_analytics.py` - GA4 traffic/engagement data
- `google_search_console.py` - Rankings and impressions
- `dataforseo.py` - SERP positions, keyword metrics
- `data_aggregator.py` - Combines all sources
- `wordpress_publisher.py` - Publishes with Yoast SEO metadata

### Opportunity Scoring

`opportunity_scorer.py`: Volume (25%), Position (20%), Intent (20%), Competition (15%), Cluster (10%), CTR (5%), Freshness (5%), Trend (5%).

## Content Pipeline

`topics/` -> `research/` -> `drafts/` -> `review-required/` -> `published/`

For clients: `clients/<slug>/research/` -> `clients/<slug>/drafts/` -> `clients/<slug>/published/`

## Context Files

`context/` contains agency defaults. Client overrides in `clients/<slug>/context/`.
- `brand-voice.md` - Agency voice (data-driven, systems-focused, direct, proof-driven)
- `style-guide.md` - Editorial standards
- `seo-guidelines.md` - SEO requirements
- `internal-links-map.md` - Internal linking strategy
- `features.md` - Agency capabilities and services
- `competitor-analysis.md` - Competitive intelligence
- `cro-best-practices.md` - Conversion optimization
- `ai-citation-targets.md` - AI citation targets
- `reddit-strategy.md` - Reddit/community strategy

## Reporting

Status reports auto-send every 3 days (Mon + Thu 9am) to:
- Lark webhook (LARK_SEO_AGENCY_WEBHOOK)
- Google Sheet (17XNZrWmJqWY8fLq5NHSwpl_IiMIZwsBsZdz2uWfUYKw)

Script: `~/Documents/New project/tools/seo_agency_status_report.py`
