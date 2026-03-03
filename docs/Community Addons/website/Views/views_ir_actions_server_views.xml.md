---
tags: [odoo, community, generated, views]
---

# views/ir_actions_server_views.xml

- Module: [[docs/Community Addons/website/website|website]]
- Scope: Community Addons
- Source file: `views/ir_actions_server_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_server_action_search_website`
- Name: ir.actions.server.search.website
- Model: `ir.actions.server`
- Type: inferred from arch
- Inherits: `base.view_server_action_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_server_action_form_website`
- Name: ir.actions.server.form.website
- Model: `ir.actions.server`
- Type: inferred from arch
- Inherits: `base.view_server_action_form`
- Root tag: `data`
- Field references: 4
- Sample fields: `website_path`, `website_published`, `website_url`, `xml_id`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/website/Views]]

