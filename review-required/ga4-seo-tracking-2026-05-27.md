---
title: "GA4 SEO Tracking: 5 Configurations and the Weekly Review Routine"
date: 2026-05-27
author: "Leo Tan"
primary_keyword: "GA4 SEO tracking"
secondary_keywords:
  - "how to track SEO in GA4"
  - "GA4 organic traffic"
  - "Google Analytics 4 SEO"
  - "GA4 GSC integration"
  - "GA4 SEO dashboard"
  - "track organic conversions GA4"
excerpt: "Most SEO teams use GA4 with the default settings — and wonder why the organic data doesn't match GSC. Here are the 5 configurations that make GA4 actually useful for SEO, plus a 15-minute weekly review routine."
slug: "ga4-seo-tracking"
cluster: "Cluster 5 — SEO Reporting & Analytics"
cluster_role: "Supporting #2"
word_count_target: 2500
internal_links:
  - /blog/seo-reporting
  - /blog/google-search-console-tutorial
  - /blog/keyword-research-for-seo
  - /blog/technical-seo-audit
  - /blog/seo-content-strategy
  - /contact
status: review-required
---

# GA4 SEO Tracking: 5 Configurations and the Weekly Review Routine

GA4 works out of the box. The problem is that "out of the box" means generic — built for every marketing channel, optimised for none of them.

For SEO teams, the default setup has three concrete problems: your organic channel grouping may be mislabelling traffic from Bing, DuckDuckGo, or AI referrers as "Unassigned." Your GA4 property almost certainly has no conversion events tied to organic search goals. And your Search Console data — the only source of keyword-level organic data — isn't linked to GA4, so you're making decisions with half the picture.

Most "GA4 for SEO" guides describe the standard reports you can browse. This one covers what to configure first, and what the right weekly review routine looks like once you have it set up.

Five configuration steps. One repeatable workflow. That's the difference between a generic analytics tool and an SEO analytics stack.

---

## Why Default GA4 Settings Underserve SEO Teams

GA4 was built for all channels simultaneously — paid search, social, email, direct, and organic search all share the same session model, the same conversion events, and the same channel grouping rules. That's not a flaw. It's the product GA4 is.

The problem is that each channel has different measurement needs. Paid search teams care about ROAS and cost-per-conversion. Email teams care about open-attributed sessions. SEO teams care about keyword-level performance, landing page engagement, and whether organic traffic is converting to leads and revenue.

Three default settings create the most friction for SEO:

**Default channel grouping is imprecise.** GA4's built-in "Organic Search" rule works for Google — but Bing, DuckDuckGo, Yahoo, and AI-driven referrers like Perplexity often land in "Unassigned." This means your organic traffic report is understating actual organic sessions, sometimes by 5–15%.

**No conversion events are configured for organic-specific goals.** GA4 ships with purchase and generate_lead as default conversions. For B2B service and SaaS businesses, the relevant conversions are form submits, demo requests, trial signups, and consultation bookings. Until those are marked as conversions in GA4, organic traffic is measured in sessions only — making it impossible to report organic ROI to a business stakeholder.

**GSC keyword data doesn't appear in GA4 natively.** There is no default organic keyword dimension in GA4. The keyword data that matters for SEO — what queries your pages rank for, how those clicks translate to engaged sessions — requires a manual integration step between Search Console and GA4.

These five configurations fix all three problems.

---

## Configuration 1: Link Google Search Console to GA4

This is the single highest-value configuration step, and fewer than half of GA4 properties have it done.

When GSC is linked to GA4, two new reports appear under the "Search Console" section in GA4's left navigation: **Google organic search queries** and **Google organic search traffic**. Both reports combine GSC data (impressions, clicks, queries, CTR) with GA4 data (sessions, engagement rate, conversions) in a single view.

The combined report answers questions neither tool can answer alone:

- Which pages rank and get impressions but don't get clicked? (High impressions, low CTR → fix your title tags)
- Which pages get clicked but immediately bounce? (High clicks, low engagement rate → content doesn't match search intent)
- Which pages rank well but generate zero conversions despite strong traffic? (High sessions, zero conversions → weak CTA or wrong audience)

**How to link:**

1. In GA4, go to **Admin** (gear icon, bottom left)
2. Under Property, click **Service Links**
3. Click **Search Console Links**
4. Click **Link** and choose your GSC property
5. Select the web data stream
6. Click **Save**

**Important**: You must have **Owner** access to the GSC property to complete the link. Editor-level GSC access is not sufficient. If you're linking on behalf of a client, have them complete this step or temporarily grant you Owner access.

Data from the combined report appears within 24–48 hours of linking. The reports populate historical data back to when your GSC property started collecting data — you don't lose historical comparison.

For the parallel GSC-side setup — verifying your property, submitting a sitemap, and understanding the Performance report — see our complete [Google Search Console tutorial](/blog/google-search-console-tutorial).

---

## Configuration 2: Audit and Fix Your Organic Channel Grouping

Before you trust any organic traffic number in GA4, verify that "Organic Search" means what you think it means.

**How to check:**

1. Go to **Reports → Acquisition → Traffic Acquisition**
2. Set the dimension to "Session default channel group"
3. Look at the full list, not just the top 5

You're looking for two problems:

- **"Unassigned" rows with meaningful volume.** If Unassigned is your third or fourth largest channel, traffic is being miscategorised. Click on Unassigned and change the secondary dimension to "Session source / medium" — you'll see where it's coming from.
- **Missing organic sources.** Bing, DuckDuckGo, Yahoo, Baidu, and AI referrers (Perplexity, You.com, ChatGPT) often don't match the default Organic Search rules and fall through to Unassigned.

**How to fix:**

1. Go to **Admin → Data Display → Channel Groups**
2. Click **Default Channel Group** to edit it
3. Add new conditions to the "Organic Search" channel:
   - Session source matches regex: `bing|duckduckgo|yahoo|baidu|yandex|perplexity|you\.com`
   - Session medium exactly matches: `organic`
4. Save and publish

Allow 24–48 hours for the new grouping rules to apply to incoming data. Historical data does not retroactively regroup — going forward, your "Organic Search" channel will be accurate.

**Why this matters for reporting:** If you're reporting organic traffic growth to a client or stakeholder and Bing organic is sitting in "Unassigned," you're understating performance. Fixing this also improves the accuracy of the GA4 + GSC linked report from Configuration 1.

---

## Configuration 3: Build an Organic Traffic Exploration

Standard GA4 reports use fixed dimensions and limited filtering. Explorations — GA4's free-form analysis section — let you build custom reports that persist and can be revisited each week.

**Build the core SEO Exploration:**

1. Go to **Explore** in the left navigation (compass icon)
2. Click **Blank** to start a free-form exploration
3. In the Variables column (left), add:
   - **Segments**: Click + and add a segment where "Session medium = organic"
   - **Dimensions**: Landing page, country, device category, session default channel group
   - **Metrics**: Sessions, engaged sessions, engagement rate, conversions, total revenue (if applicable)
4. Apply the "organic" segment to your exploration
5. Set the rows to Landing page and metrics to Sessions + Conversions
6. Click the three-dot menu and **Rename** the exploration: "SEO: Organic Landing Page Analysis"

**Pro tip — add a date comparison:** Duplicate this exploration (three-dot menu → Duplicate). In the duplicate, add a date comparison in the date range settings: "Compare to previous period." This becomes your week-over-week organic traffic tracker. Rename it "SEO: Weekly Organic Comparison."

Save both explorations. They live in your Explore section and can be accessed directly from the left nav each week without rebuilding.

---

## Configuration 4: Set Up SEO-Relevant Conversion Events

Tracking organic sessions is table stakes. Tracking organic conversions is what makes [SEO reporting](/blog/seo-reporting) credible to business stakeholders.

The default GA4 conversion events — `purchase` and `generate_lead` — cover e-commerce and basic lead gen. For B2B service businesses and SaaS companies, the conversion events that matter for SEO are:

- Contact form submission
- Demo request or free trial signup
- Consultation booking
- Content download (if gated)
- Phone call click (if trackable)

**If you use Google Tag Manager (recommended):**

1. In GTM, create a trigger that fires when your form submission succeeds (a "Thank you" page load, a custom dataLayer push on success, or a DOM element visibility trigger on the success message)
2. Create a GA4 Event tag with Event Name: `form_submit` (or `book_consultation`, `request_demo` — whatever matches your CRM taxonomy)
3. Publish the GTM container
4. In GA4, go to **Admin → Events** and verify the event is appearing
5. Toggle the event to **Mark as conversion**

**Important note on GA4's built-in form tracking:** GA4's Enhanced Measurement includes a "Form interactions" toggle that tracks form submits automatically. Don't rely on it for conversion events — it fires inconsistently across different form builders and doesn't distinguish between form views and successful submissions. GTM-based tracking is more reliable.

Once conversion events are live, your organic Exploration from Configuration 3 will populate with real conversion data. This is the point where GA4 transitions from a traffic reporting tool to an SEO ROI reporting tool.

---

## Configuration 5: Create the SEO Landing Page Conversion Report

This is the most actionable SEO report GA4 can produce — and it requires the previous four configurations to work correctly.

**Build it in Explorations:**

1. Open Explore and start a new Free Form exploration
2. Apply your "organic" session segment
3. Set dimensions: Landing page + date range
4. Set metrics: Sessions, conversions, conversion rate, engagement rate, avg. session duration
5. Sort by conversions descending
6. Rename: "SEO: Landing Page Conversions"

**What this report tells you every week:**

| Scenario | What it means | What to do |
|---|---|---|
| High sessions, zero conversions | Traffic doesn't match conversion intent, or CTA is weak | Audit the page CTA; check if the keyword intent matches the offer |
| High conversion rate, low sessions | Strong page, low visibility | Prioritise for link building and internal linking; consider promoting with content distribution |
| Sessions dropped week-over-week | Possible ranking drop or technical issue | Cross-reference with GSC Performance report; run a [technical SEO audit](/blog/technical-seo-audit) on the page |
| New page appearing in top 10 | Recent content is ranking | Note the keyword from GSC; monitor week-over-week |

This report, combined with the GSC linked report from Configuration 1, gives you a complete picture: what queries drive traffic (GSC), which landing pages receive that traffic, and whether those sessions convert (GA4).

---

## The 15-Minute Weekly GA4 SEO Review

Once the five configurations are in place, the weekly review takes 15 minutes. Here's the routine:

**Step 1 — Search Console organic traffic report (5 minutes)**  
Go to Reports → Search Console → Google organic search traffic. Set to last 7 days, compare to previous 7 days. Scan landing pages for week-over-week session changes. Flag any page that dropped more than 20%. These are your investigation priorities.

**Step 2 — SEO Landing Page Conversion report (3 minutes)**  
Open your saved Exploration. Review which pages converted from organic this week. Are your expected high-performers appearing? Any pages with strong conversion rates that deserve more promotion? Any previous converters that dropped to zero (possible ranking or crawl issue)?

**Step 3 — Organic Traffic Exploration — weekly comparison (2 minutes)**  
Open your "SEO: Weekly Organic Comparison" Exploration. Check total organic sessions vs. prior week. Review engagement rate trend. Look for device or country anomalies (a sudden spike from a specific country could indicate bot traffic or a viral referral).

**Step 4 — Channel grouping quality check (2 minutes)**  
Open Traffic Acquisition. Look at the "Unassigned" row. If it spiked this week, change the secondary dimension to session source/medium and investigate. New traffic from an uncategorised source may need a channel grouping rule update.

**Step 5 — Log your findings (3 minutes)**  
In your weekly SEO notes (a simple doc or your agency CRM), record: total organic sessions, conversion count, best performing page, biggest drop, any anomalies. Three minutes of logging builds the data for your monthly [SEO reporting](/blog/seo-reporting) deck without requiring a two-hour data pull at the end of the month.

The GSC side of this routine — checking the Performance report, diagnosing traffic drops, reviewing the Coverage report — runs in parallel in a separate 15-minute block. Both routines together give you a complete weekly picture of organic performance without analytics overwhelm.

---

## GA4 SEO Data Quality: What the Numbers Don't Tell You

Honest analytics means knowing where the data is wrong.

**Direct traffic inflation.** GA4 sessions that lose their source attribution — UTM parameters stripped by a redirect, browser storage cleared, mobile app referral that doesn't carry UTM — default to "Direct." Some organic traffic will always appear as direct. A 5–10% undercount of organic sessions is normal and expected.

**Keyword (not provided).** GA4 does not provide organic keyword data natively. The GSC linked report gives you Google queries only — not Bing, not DuckDuckGo. For non-Google organic [keyword research](/blog/keyword-research-for-seo) purposes, you need separate Bing Webmaster Tools access.

**GSC vs. GA4 discrepancy.** GSC counts clicks. GA4 counts sessions. One click can generate multiple sessions (user clicks, browses, leaves, returns within the same click attribution window). Bots are filtered differently in each tool. A 10–30% discrepancy between GSC clicks and GA4 organic sessions is normal. If your gap is larger, investigate your channel grouping configuration.

**Sampling in free GA4.** Explorations in free GA4 sample data above approximately 500,000 events per date range. If your site generates high traffic volumes, your Explorations may show approximate data rather than exact counts. GA4 360 removes sampling — relevant if you're at scale. For smaller sites, this is not a concern.

**Session timeout default.** GA4's default session timeout is 30 minutes of inactivity. A user who reads a long organic article, pauses for 35 minutes, and continues reading generates two sessions from one visit. This inflates session counts and deflates engagement metrics slightly. It's a known limitation of session-based measurement.

Understanding these limitations doesn't undermine your reporting — it makes it more credible. A stakeholder who hears you explain why GSC and GA4 numbers differ has more confidence in your analysis than one who receives unexplained discrepancies.

---

## Frequently Asked Questions

**Does GA4 replace Google Search Console for SEO tracking?**

No — they measure different things at different stages. GSC measures what Google sees before a click: impressions, rankings, CTR, crawl and indexation status. GA4 measures what happens after a click: sessions, behavior, conversions. The two tools are complementary. Link them (Configuration 1) to get the best of both in a single report.

**Why doesn't GA4 show me my organic keywords?**

GA4 does not include keyword data by default — this is the "(not provided)" limitation that has existed since 2013. The GSC link in Configuration 1 is the closest available solution: it pulls Google organic query data from Search Console and displays it alongside GA4 engagement metrics. You still won't see Bing or DuckDuckGo query data.

**How do I know if my organic traffic data in GA4 is accurate?**

Compare organic sessions in GA4 with GSC clicks for the same date range and property. A 10–30% gap is normal. If you're seeing a 50%+ gap, check your channel grouping (Configuration 2) — there's likely organic traffic sitting in "Unassigned." Also verify that your GA4 tag fires correctly on all pages (use GA4 DebugView or Tag Assistant to confirm).

**Can I track branded vs. non-branded organic traffic in GA4?**

Not natively. Non-branded organic tracking requires a workaround: in Looker Studio, create a calculated field that flags GSC queries containing your brand name, then filter by "does not contain brand name" to isolate non-branded performance. Alternatively, use a GSC filter directly in the Search Console interface. Pure GA4-native branded/non-branded segmentation isn't available.

**Should I use Looker Studio instead of GA4 for SEO reporting?**

For weekly monitoring: use GA4 directly. The Explorations and standard reports are faster to navigate once configured. For monthly client reporting and executive dashboards: Looker Studio adds value — it connects to both GA4 and GSC simultaneously, allows date comparisons, and creates shareable views that don't require GA4 access. Build the weekly workflow in GA4; build the monthly report in Looker Studio.

---

## Summary: The 5 Configurations

GA4 isn't an SEO analytics tool by default. These five configurations change that:

1. **Link Google Search Console** — unlocks the combined query + engagement report that neither tool provides alone
2. **Audit and fix organic channel grouping** — ensures "Organic Search" captures all organic sources, not just Google
3. **Build an organic traffic Exploration** — creates a persistent, filter-ready report for weekly organic analysis
4. **Set up conversion events for organic goals** — converts GA4 from a traffic tool to an ROI measurement tool
5. **Create the SEO landing page conversion report** — shows which pages earn organic traffic and which of those convert

Pair the weekly GA4 review with the parallel [Google Search Console tutorial](/blog/google-search-console-tutorial) routine and you have a complete 30-minute weekly SEO measurement practice — the data foundation for credible monthly reporting.

If you'd rather have this configured correctly from the start, [get in touch with our team](/contact). We set up the full SEO analytics stack — GA4, GSC, Looker Studio dashboards, and conversion tracking — as part of our SEO retainer.
