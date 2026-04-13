# Publish to AutoSEO

Push a finished article from seomachine's pipeline into AutoSEO (build-the-best) for client delivery.

## Input
The user provides: path to a draft or published markdown file, and optionally a client slug.

## Steps

1. **Read the article** from the provided path

2. **Determine the client**:
   - If client slug provided, load `clients/<slug>/config.json`
   - If not, check the file path for a client directory
   - Get `autoseo_website_id` from the client config

3. **Push via AutoSEO bridge**:
   ```python
   from integrations.autoseo_bridge import AutoSEOBridge
   bridge = AutoSEOBridge()
   result = bridge.push_article(article_path, website_id=autoseo_website_id)
   ```

4. **Move the file** from `drafts/` to `published/` if not already there

5. **Update the client's content plan** to mark this topic as published

6. **Report success** with:
   - Article title and slug
   - AutoSEO status
   - Link to the article in AutoSEO dashboard (if available)
