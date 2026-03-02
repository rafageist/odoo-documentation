<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/website_visitor_views.xml

- Module: [[docs/Community Addons/website_sms/website_sms|website_sms]]
- Scope: Community Addons
- Source file: `views/website_visitor_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `website_visitor_view_tree`
- Name: website.visitor.view.list.inherit.website.sms
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `mobile`
- Buttons: `action_send_sms`
- XPath or positional patches: 2

### `website_visitor_view_kanban`
- Name: website.visitor.view.kanban.inherit.website.sms
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_kanban`
- Root tag: `field`
- Field references: 2
- Sample fields: `country_id`, `mobile`
- Buttons: `action_send_sms`
- XPath or positional patches: 1

### `website_visitor_view_form`
- Name: website.visitor.view.form.inherit.website.mass.mailing.sms
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_send_sms`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/website_sms/Views]]

<!-- GENERATED:VIEWFILE -->
