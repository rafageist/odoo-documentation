---
tags: [odoo, enterprise, generated, views]
---

# views/social_stream_views.xml

- Module: [[docs/Enterprise Addons/social/social|social]]
- Scope: Enterprise Addons
- Source file: `views/social_stream_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `social_stream_view_search`
- Name: social.stream.view.search
- Model: `social.stream`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `company_id`
- XPath or positional patches: 0

### `social_stream_view_form_wizard`
- Name: social.stream.view.form.wizard
- Model: `social.stream`
- Type: inferred from arch
- Inherits: `social_stream_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `social_stream_view_form`
- Name: social.stream.view.form
- Model: `social.stream`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `account_id`, `company_id`, `media_id`, `name`, `stream_type_id`, `stream_type_type`
- XPath or positional patches: 0

### `social_stream_view_tree`
- Name: social.stream.view.list
- Model: `social.stream`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `company_id`, `create_uid`, `media_id`, `name`, `stream_type_id`
- XPath or positional patches: 0

## Actions

- `action_social_stream`: `act_window` Social Streams

## Menus

- `menu_social_stream`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/social/Views]]

