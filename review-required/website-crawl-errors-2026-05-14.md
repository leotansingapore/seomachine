# Website crawl errors: how to find and fix every type

**Meta title**: Website crawl errors: how to find and fix them
**Meta description**: Website crawl errors stop Google from indexing your pages. Here's a complete guide to every error type, how to find them, and how to fix them -- fast.
**URL slug**: `/blog/website-crawl-errors`
**Primary keyword**: website crawl errors
**Cluster**: Cluster 1 -- Technical SEO (supporting article #2)
**Word count**: ~2,400 words
**Date**: 2026-05-14

---

Google won't rank what it can't crawl. When Googlebot hits a wall trying to access your pages, those pages disappear from the index -- silently, without warning, until you check your coverage report.

Crawl errors are one of the most common causes of unexplained ranking drops. A site migration gone wrong, a deleted product page, a server hiccup during peak traffic -- any of these can generate dozens of crawl errors overnight. Most of them are fixable in under an hour. The problem is knowing which ones to fix first.

This guide covers every type of website crawl error, where to find them, how to fix each one, and -- most importantly -- a triage framework for prioritizing your time. Not all crawl errors are equal. Some will cost you rankings; others can stay broken indefinitely with no SEO impact.

> **Key takeaways**:
> - Crawl errors happen when Googlebot requests a URL and can't retrieve it properly
> - The most common types: 4xx errors, 5xx errors, soft 404s, redirect chains, and DNS/server errors
> - Fix errors on pages that had traffic or inbound links. Ignore errors on pages that never ranked.
> - Most 404 fixes take under five minutes. Redirect chains take longer but have a higher ROI.
> - Set up GSC email alerts -- catch errors before they compound into index gaps

---

## What are website crawl errors?

A **website crawl error** occurs when Googlebot (or any other crawler) sends a request to a URL on your site and encounters a problem retrieving it. The crawler can't get what it expected, so the page either can't be indexed or gets removed from the index.

There are two categories:

**Hard errors**: The crawler couldn't reach the page at all. DNS failures, server outages, and connection timeouts fall here. These block crawling entirely.

**Soft errors**: The page technically returned a response, but the response signals a problem. A 404 Not Found is a hard error in terms of HTTP status, but a soft 404 -- a page that returns HTTP 200 but has minimal content -- is a soft error. Google may still crawl it, but it won't rank.

Why crawl errors matter: Google has a [crawl budget](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget) for every domain -- a limit on how many pages it will crawl in a given period. Crawl errors waste that budget. High error rates mean Google spends time hitting broken URLs instead of discovering and indexing your good content.

---

## Types of website crawl errors

### 4xx errors (client-side errors)

These mean the requested URL doesn't exist or the server is refusing to serve it. The problem is on the URL side, not the server.

**404 Not Found**: The most common crawl error. The page existed at some point (or was linked to) but no longer returns content. Causes: deleted pages, moved content without redirects, typos in internal links.

**410 Gone**: Tells Googlebot the page was intentionally removed and won't return. Functionally similar to 404, but Google processes 410s faster -- it stops trying to recrawl the URL sooner. Use 410 when you're permanently removing content with no replacement.

**403 Forbidden**: The server understood the request but refuses to serve the page. Causes: incorrect file permissions, password-protected content, IP blocking rules. If you see 403s on public-facing pages, investigate your server configuration.

**401 Unauthorized**: The page requires authentication. Googlebot can't log in, so the page won't be indexed. Check that your staging environment or gated content isn't accidentally accessible to crawlers.

### 5xx errors (server-side errors)

These mean the server is up but something went wrong processing the request. The problem is on the server, not the URL.

**500 Internal Server Error**: Generic server failure. Causes range from PHP errors to misconfigured `.htaccess` files to plugin conflicts (common in WordPress). Check your server error logs immediately.

**503 Service Unavailable**: The server is temporarily unavailable -- usually overload or maintenance. If you return a 503 with a `Retry-After` header during planned maintenance, Googlebot will respect it and try again. If 503s appear during normal traffic, your hosting can't handle the load.

**504 Gateway Timeout**: The server didn't respond in time -- common with slow database queries or overloaded upstream servers. Googlebot will retry, but persistent 504s will remove pages from the index.

### DNS errors

Googlebot can't resolve your domain to an IP address. This is a complete crawl block -- no pages can be crawled until DNS resolves. Causes: expired domain registration, misconfigured nameservers, DNS propagation delays after a server migration.

DNS errors are urgent. If you see them in GSC, contact your domain registrar or hosting provider immediately.

### Soft 404 errors

A soft 404 is a page that returns HTTP 200 (success) but has little or no meaningful content. Google detects these algorithmically and may remove them from the index despite the 200 status.

Common causes:
- Search result pages with no results (e.g., `/search?q=xyz` with no matches)
- Empty category pages
- "Coming soon" placeholder pages
- Thin content pages (under ~300 words with no media or structured data)

Google's John Mueller has noted that soft 404s are one of the most underestimated indexation problems on e-commerce sites.

### Redirect errors

**Redirect chains**: When URL A redirects to URL B, which redirects to URL C. Each hop adds latency (~200ms per redirect) and dilutes link equity passing through the chain. Three or more hops is a problem.

**Redirect loops**: URL A redirects to URL B, which redirects back to URL A. Infinite loop -- Googlebot gives up and can't index either.

**Redirect to 4xx**: A redirect pointing to a destination that itself returns a 404 or other error. You've sent Googlebot down a dead end.

---

## How to find website crawl errors

### Google Search Console (free, most authoritative)

1. Open [Google Search Console](https://search.google.com/search-console)
2. Navigate to **Indexing > Pages** (previously called Coverage)
3. Look at the four tabs: Error, Valid with warning, Excluded, Valid
4. Click **Error** -- these are pages Google tried to crawl and couldn't
5. Click each error type to see the list of affected URLs
6. Use the **Validate Fix** button after resolving issues -- this triggers Googlebot to recheck

GSC shows errors Google has actually encountered. This is the most reliable source.

**Set up email alerts**: In GSC Settings > Preferences, enable email notifications for coverage issues. You'll get an alert within 24-48 hours of new errors appearing -- before they compound.

### Screaming Frog (crawl simulator)

Screaming Frog crawls your site the way Googlebot does. Use the free version (up to 500 URLs) or the paid version for larger sites.

1. Enter your domain and run a crawl
2. Click the **Response Codes** tab
3. Filter by **4xx** to see all not-found pages
4. Filter by **5xx** to see server errors
5. Filter by **3xx** to audit your redirect chains (check the chain column for hops > 1)
6. Export to CSV for prioritization

### Ahrefs Site Audit

Ahrefs Site Audit runs a comprehensive crawl and scores your Site Health (0-100). For crawl errors specifically:

1. Run a Site Audit on your domain
2. Go to **Issues > All Issues**
3. Filter by "Errors" category
4. Look for: broken pages (4xx), 5xx errors, redirect chains, soft 404s

Ahrefs adds a useful layer: it shows which broken pages have backlinks pointing to them, making prioritization easier.

---

## How to fix the most common crawl errors

### Fixing 404 errors

**Step 1**: Export all 404 URLs from GSC or Screaming Frog.

**Step 2**: For each 404, determine if it was ever linked to (internally or externally) or received traffic. Check Ahrefs for backlinks, check GA4 for historical traffic.

**Step 3**:
- If the page has backlinks or traffic history: 301 redirect to the most relevant live page. If no equivalent exists, redirect to the parent category. As a last resort, redirect to the homepage -- but this is a weak signal.
- If the page has no backlinks and no traffic history: Leave it as a 404. Don't redirect to an irrelevant page just to clear the error. Google will stop crawling it eventually.

**Do not** chain your 404s to the homepage reflexively. A homepage redirect from an irrelevant deleted page wastes crawl budget and tells Google the homepage is relevant for keywords it isn't.

### Fixing 410 errors

No action required if intentional. Return 410 when you've permanently removed content with no replacement. Google processes 410s faster than 404s and stops revisiting the URL sooner.

If you see unexpected 410s, investigate your CMS or server configuration -- something is deliberately signalling "gone" for pages that should be live.

### Fixing 5xx errors

**500 errors**: Check your server error logs immediately. In WordPress, common causes are plugin conflicts and memory limit exhaustion. Try deactivating recently-added plugins. Check `wp-config.php` for the `WP_DEBUG` setting to expose the root error.

**503 errors during maintenance**: Return 503 with a `Retry-After` header. Example for Apache `.htaccess`:
```
Header set Retry-After "3600"
```

**503/504 during normal traffic**: Your server is undersized for your traffic load. Upgrade hosting tier, add caching (Cloudflare, WP Rocket), or optimize database queries.

### Fixing soft 404 errors

- **Empty or thin pages**: Either add substantial content (400+ words, structured data, relevant internal links) or 301 redirect to the nearest parent category.
- **No-result search pages**: Add `noindex` to search result pages. You don't want Googlebot indexing `/search?q=xyz` queries anyway.
- **"Coming soon" pages**: Either add real content or use `noindex`. Don't let placeholder pages consume crawl budget.

### Fixing redirect chains

**Step 1**: Use Screaming Frog or Ahrefs to identify chains (3+ hops).

**Step 2**: For each chain, identify the final destination URL.

**Step 3**: Update the first redirect to point directly to the final destination. Cut out the middle hops.

Example: A redirects to B redirects to C. Update A to redirect directly to C. Remove the A-to-B redirect once A-to-C is live.

**Step 4**: If the chain originates from external backlinks or internal links, update the source URL to point directly to the final destination.

### Fixing redirect loops

Trace the redirect chain manually or with a tool like [Redirect Checker](https://www.redirect-checker.org). Identify where the loop closes and break it by updating one of the redirects to point to a non-redirecting destination.

---

## Crawl error prioritization: which to fix first

Not all crawl errors have equal SEO impact. Use this triage framework:

**Priority 1 -- Fix this week**:
- 404 errors on pages with inbound backlinks (link equity is leaking)
- 404 errors on pages that previously received organic traffic
- All 5xx errors on any page (server errors affect your entire site's crawlability)
- DNS errors (complete crawl block -- fix immediately)

**Priority 2 -- Fix this month**:
- Soft 404s on pillar content or product pages
- Redirect chains of 3+ hops on high-authority pages
- 403 errors on pages that should be publicly accessible

**Priority 3 -- Monitor, don't prioritize**:
- 404 errors on pages with no backlinks and no traffic history
- 410 errors (intentional, no action needed)
- Legacy redirect chains (2 hops) on low-traffic pages

**The practical decision rule**: Fix errors on pages that had traffic or links. Ignore errors on pages that never ranked.

This sounds obvious. In practice, most teams waste hours fixing 404s on orphaned pages that were never indexed, while leaving 404s with external backlinks unresolved for months.

---

## How to prevent crawl errors

### Redirect planning before URL changes

Before any URL restructure, site migration, or CMS change: map every current URL to its new destination and set up redirects before the old URLs go offline. A redirect mapping spreadsheet takes two hours. Cleaning up a migration without one takes two weeks.

### Monthly crawl schedule

Run Screaming Frog or a Ahrefs Site Audit monthly. Catch new 404s and redirect chain growth before they compound. Set a GSC email alert so problems surface immediately rather than during quarterly reviews.

### Pre-launch crawl testing

Before launching a new site, redesign, or migration:
1. Crawl the staging environment with Screaming Frog
2. Check for internal broken links and misconfigured redirects
3. Verify robots.txt doesn't block Googlebot from critical pages
4. Test canonical tags -- make sure they point to the live domain, not staging

### Server monitoring

Add uptime monitoring (UptimeRobot is free) so 5xx errors trigger an alert within minutes rather than hours. Persistent 5xx errors during normal traffic are a hosting problem that compounds quickly.

---

## Crawl error FAQ

**Do crawl errors hurt SEO?**
Yes -- for the pages affected. A 404 error on a single low-traffic page has minimal site-wide impact. But 5xx server errors and DNS errors can block Googlebot from crawling your entire site, which affects rankings across the board. Prioritize accordingly.

**What's the difference between a crawl error and a coverage error?**
In Google Search Console, the Coverage report (now called "Pages") includes both crawl errors and indexation issues. Crawl errors are a subset: they're specifically instances where Googlebot couldn't retrieve a page. Coverage errors also include pages that were crawled successfully but excluded from the index for other reasons (noindex tag, duplicate content, etc.).

**How long does it take Google to recrawl after fixing a crawl error?**
Typically one to four weeks for standard pages. For important pages, use the URL Inspection tool in GSC and click "Request Indexing" to trigger a faster recheck. After fixing a batch of errors, click "Validate Fix" in the Coverage report -- this signals GSC to prioritize recrawling the affected URLs.

**Should I fix all 404 errors?**
No. Fix 404s on pages that had backlinks or traffic. Leave 404s on pages that were never indexed and received no traffic -- redirecting them to unrelated live pages wastes crawl budget and sends confusing signals to Google.

**How many crawl errors is too many?**
There's no universal threshold. Context matters: a 10,000-page e-commerce site with 200 404s (2%) is in reasonable shape. A 500-page B2B site with 200 404s (40%) has a serious crawlability problem. Focus on the ratio and on whether errors are affecting linked/trafficked pages.

---

## Conclusion

Crawl errors are a mechanical problem with mechanical solutions. Google can't rank what it can't crawl -- but most crawl errors are fixable in under an hour once you know what you're looking at.

The key takeaways:
- 4xx errors mean the URL doesn't exist or is blocked; 5xx errors mean the server failed
- Soft 404s are the most underdiagnosed crawl issue, especially on large sites
- Prioritize by link equity and traffic history -- not by raw error count
- GSC email alerts + monthly crawls catch problems before they compound into ranking losses

If you're running a [technical SEO audit](/blog/technical-seo-audit) and want a systematic approach to crawl error diagnosis alongside on-page factors, read our [technical SEO audit guide](/blog/technical-seo-audit). For the full on-page layer, see the [on-page SEO checklist](/blog/on-page-seo-checklist).

Ready to audit your crawl health? [Brief us on your site](/contact) and we'll identify the errors that are actually costing you rankings.
