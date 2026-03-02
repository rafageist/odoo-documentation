<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/website_customer/website_customer|website_customer]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `res_partner_tag_view_search`
- Name: res.partner.tag.view.search
- Model: `res.partner.tag`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_partner_tag_list`
- Name: Website Tags
- Model: `res.partner.tag`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `active`, `classname`, `is_published`, `name`
- XPath or positional patches: 0

### `view_partner_tag_form`
- Name: Website Tags
- Model: `res.partner.tag`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `active`, `classname`, `is_published`, `name`
- XPath or positional patches: 0

### `view_partners_form_website`
- Name: view.res.partner.form.website.tags
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `website_partner.view_partners_form_website`
- Root tag: `data`
- Field references: 1
- Sample fields: `website_tag_ids`
- XPath or positional patches: 1

## Actions

- `action_partner_tag_form`: `act_window` Website Tags

## Menus

- `menu_partner_tag_form`: Website Tags

## Navigation

- **Parent:** [[docs/Community Addons/website_customer/Views]]

<!-- GENERATED:VIEWFILE -->
