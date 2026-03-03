---
tags: [odoo, community, generated, views]
---

# views/website_visitor_views.xml

- Module: [[docs/Community Addons/website_event/website_event|website_event]]
- Scope: Community Addons
- Source file: `views/website_visitor_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `website_visitor_view_form`
- Name: website.visitor.view.form.inherit.event
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `event_registration_count`
- Buttons: `%(website_event.event_registration_action_from_visitor)d`
- XPath or positional patches: 1

### `website_visitor_view_tree`
- Name: website.visitor.view.list.inherit.event
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `event_registration_count`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/website_event/Views]]

