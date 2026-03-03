---
tags: [odoo, enterprise, generated, views]
---

# views/utm_campaign_views.xml

- Module: [[docs/Enterprise Addons/social/social|social]]
- Scope: Enterprise Addons
- Source file: `views/utm_campaign_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `utm_campaign_view_kanban`
- Name: utm.campaign.view.kanban.inherit.social
- Model: `utm.campaign`
- Type: inferred from arch
- Inherits: `utm.utm_campaign_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `social_posts_count`
- XPath or positional patches: 1

### `utm_campaign_view_form_quick_create_social`
- Name: utm.campaign.view.form.quick.create.social
- Model: `utm.campaign`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `name`, `tag_ids`, `user_id`
- XPath or positional patches: 0

### `utm_campaign_view_form`
- Name: utm.campaign.view.form.inherit.social
- Model: `utm.campaign`
- Type: inferred from arch
- Inherits: `utm.utm_campaign_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `social_engagement`, `social_post_ids`, `social_posts_count`
- Buttons: `action_create_new_post`, `action_redirect_to_social_media_posts`
- XPath or positional patches: 3

## Actions

- `action_view_utm_campaigns`: `act_window` Campaigns

## Menus

- `menu_social_campaign`: Campaigns

## Navigation

- **Parent:** [[docs/Enterprise Addons/social/Views]]

