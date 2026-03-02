<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_feed_views.xml

- Module: [[docs/Community Addons/website_sale/website_sale|website_sale]]
- Scope: Community Addons
- Source file: `views/product_feed_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `product_feed_form`
- Name: product.feed.view.form
- Model: `product.feed`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `lang_id`, `name`, `pricelist_id`, `product_category_ids`, `url`, `website_id`
- XPath or positional patches: 0

### `product_feed_list`
- Name: product.feed.view.list
- Model: `product.feed`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `lang_id`, `name`, `pricelist_id`, `product_category_ids`, `url`, `website_id`
- XPath or positional patches: 0

### `product_feed_search`
- Name: product.feed.view.search
- Model: `product.feed`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `lang_id`, `pricelist_id`, `product_category_ids`, `website_id`
- XPath or positional patches: 0

## Actions

- `action_invalidate_cache`: `server` Reset Cache
- `action_product_feeds`: `act_window` Product Feeds

## Navigation

- **Parent:** [[docs/Community Addons/website_sale/Views]]

<!-- GENERATED:VIEWFILE -->
