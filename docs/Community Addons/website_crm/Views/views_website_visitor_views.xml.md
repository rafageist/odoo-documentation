<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/website_visitor_views.xml

- Module: [[docs/Community Addons/website_crm/website_crm|website_crm]]
- Scope: Community Addons
- Source file: `views/website_visitor_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `website_visitor_view_kanban`
- Name: website.visitor.view.kanban.inherit.website.crm
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `lead_count`
- XPath or positional patches: 1

### `website_visitor_view_search`
- Name: website.visitor.view.search.inherit.website.crm
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `website_visitor_view_tree`
- Name: website.visitor.view.list.inherit.website.crm
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `lead_count`
- XPath or positional patches: 1

### `website_visitor_view_form`
- Name: website.visitor.view.form.inherit.website.crm
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `lead_count`
- Buttons: `%(website_crm.crm_lead_action_from_visitor)d`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/website_crm/Views]]

<!-- GENERATED:VIEWFILE -->
