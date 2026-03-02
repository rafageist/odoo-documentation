<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/social_post_views.xml

- Module: [[docs/Enterprise Addons/social_youtube/social_youtube|social_youtube]]
- Scope: Enterprise Addons
- Source file: `views/social_post_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `social_post_view_form`
- Name: social.post.view.form.inherit.youtube
- Model: `social.post`
- Type: inferred from arch
- Inherits: `social.social_post_view_form`
- Root tag: `xpath`
- Field references: 9
- Sample fields: `youtube_access_token`, `youtube_accounts_count`, `youtube_accounts_other_count`, `youtube_description`, `youtube_preview`, `youtube_title`, `youtube_video`, `youtube_video_id`, `youtube_video_privacy`
- XPath or positional patches: 10

### `social_post_view_kanban`
- Name: social.post.view.kanban.inherit.youtube
- Model: `social.post`
- Type: inferred from arch
- Inherits: `social.social_post_view_kanban`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `youtube_description`, `youtube_thumbnail_url`, `youtube_video_id`, `youtube_video_url`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_youtube/Views]]

<!-- GENERATED:VIEWFILE -->
