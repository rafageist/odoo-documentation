<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_track_visitor_views.xml

- Module: [[docs/Community Addons/website_event_track_quiz/website_event_track_quiz|website_event_track_quiz]]
- Scope: Community Addons
- Source file: `views/event_track_visitor_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `event_track_visitor_view_list`
- Name: event.track.visitor.view.list.inherit.quiz
- Model: `event.track.visitor`
- Type: inferred from arch
- Inherits: `website_event_track.event_track_visitor_view_list`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `quiz_completed`, `quiz_points`
- XPath or positional patches: 1

### `event_track_visitor_view_form`
- Name: event.track.visitor.view.form.inherit.quiz
- Model: `event.track.visitor`
- Type: inferred from arch
- Inherits: `website_event_track.event_track_visitor_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `quiz_completed`, `quiz_points`
- XPath or positional patches: 1

### `event_track_visitor_view_search`
- Name: event.track.visitor.view.search.inherit.quiz
- Model: `event.track.visitor`
- Type: inferred from arch
- Inherits: `website_event_track.event_track_visitor_view_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `quiz_completed`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/website_event_track_quiz/Views]]

<!-- GENERATED:VIEWFILE -->
