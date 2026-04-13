# New Client Onboarding

Set up a new client in the seomachine multi-client system.

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

4. **Research the client's website** using available tools:
   - Run a quick site crawl to understand structure
   - Identify existing content and top pages
   - Find current ranking keywords via DataForSEO if available
   - Identify 3-5 competitor domains

5. **Fill in brand voice override** (clients/<client-slug>/context/brand-voice.md):
   - Analyze the website's existing content for tone and style
   - Document their target audience
   - Set appropriate voice adjustments

6. **Create initial keyword clusters** based on:
   - Industry analysis
   - Competitor gap analysis
   - Website's existing content gaps

7. **Generate a 30-day content plan** with prioritized topics

8. **Output a summary** to the user with:
   - Client setup confirmation
   - Initial keyword opportunities found
   - Suggested first 5 articles
   - Estimated monthly traffic opportunity

Save all research to `clients/<client-slug>/research/`.
