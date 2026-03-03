---
tags: [odoo, community, generated, views]
---

# views/website_visitor_views.xml

- Module: [[docs/Community Addons/website_event_track/website_event_track|website_event_track]]
- Scope: Community Addons
- Source file: `views/website_visitor_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `website_visitor_view_form`
- Name: website.visitor.view.form.inherit.event.track
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website_event.website_visitor_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `event_track_wishlisted_count`
- Buttons: `%(website_event_track.event_track_action_from_visitor)d`
- XPath or positional patches: 1

### `website_visitor_view_tree`
- Name: website.visitor.view.list.inherit.event.track
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website_event.website_visitor_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `event_track_wishlisted_count`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/website_event_track/Views]]

