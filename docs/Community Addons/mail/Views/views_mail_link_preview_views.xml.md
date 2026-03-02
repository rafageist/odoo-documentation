<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mail_link_preview_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/mail_link_preview_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `message_link_preview_list`
- Name: mail.message.link.preview.list
- Model: `mail.message.link.preview`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `author_id`, `is_hidden`
- XPath or positional patches: 0

### `mail_link_preview_view_tree`
- Name: mail.link.preview.list
- Model: `mail.link.preview`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `id`, `image_mimetype`, `og_title`, `og_type`, `source_url`
- XPath or positional patches: 0

### `mail_link_preview_view_form`
- Name: mail.link.preview.form
- Model: `mail.link.preview`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `create_date`, `image_mimetype`, `message_link_preview_ids`, `og_description`, `og_image`, `og_mimetype`, `og_title`, `og_type`, `source_url`
- XPath or positional patches: 0

## Actions

- `mail_link_preview_action`: `act_window` Link Previews

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

<!-- GENERATED:VIEWFILE -->
