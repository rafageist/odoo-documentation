<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/social_post_views.xml

- Module: [[docs/Enterprise Addons/social/social|social]]
- Scope: Enterprise Addons
- Source file: `views/social_post_views.xml`
- Views: 6
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `social_post_view_form`
- Name: social.post.view.form
- Model: `social.post`
- Type: inferred from arch
- Inherits: `social_post_template_view_form`
- Root tag: `xpath`
- Field references: 15
- Sample fields: `account_allowed_ids`, `account_id`, `click_count`, `company_id`, `engagement`, `failure_reason`, `image_ids`, `live_post_ids`, `live_post_link`, `message`, and 5 more
- Buttons: `action_post`, `action_redirect_to_clicks`, `action_retry_post`, `action_schedule`, `action_set_draft`, `social_stream_post_action_my`
- XPath or positional patches: 11

### `social_post_view_list`
- Name: social.post.view.list
- Model: `social.post`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `account_ids`, `message`, `state`
- XPath or positional patches: 0

### `social_post_view_pivot`
- Name: social.post.view.pivot
- Model: `social.post`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 1
- Sample fields: `create_date`
- XPath or positional patches: 0

### `social_post_view_calendar`
- Name: social.post.view.calendar
- Model: `social.post`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 3
- Sample fields: `is_hatched`, `message`, `utm_campaign_id`
- XPath or positional patches: 0

### `social_post_view_search`
- Name: social.post.view.search
- Model: `social.post`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `account_ids`, `company_id`, `create_uid`, `message`, `state`, `utm_campaign_id`
- XPath or positional patches: 0

### `social_post_view_kanban`
- Name: social.post.view.kanban
- Model: `social.post`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 14
- Sample fields: `account_ids`, `click_count`, `create_uid`, `display_message`, `engagement`, `has_post_errors`, `image_ids`, `image_urls`, `live_posts_by_media`, `media_ids`, and 4 more
- XPath or positional patches: 0

## Actions

- `action_social_post`: `act_window` Social Posts

## Menus

- `menu_social_post`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/social/Views]]

<!-- GENERATED:VIEWFILE -->
