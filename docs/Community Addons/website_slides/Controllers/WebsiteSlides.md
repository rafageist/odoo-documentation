<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# WebsiteSlides

- Module: [[docs/Community Addons/website_slides/website_slides|website_slides]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `WebsiteProfile`
- Routes: 38

## Routes

### `slides_channel`
- Paths: `/slides`, `/slides/page/<int:page>`, `/slides/tag/<string:slug_tags>`, `/slides/tag/<string:slug_tags>/page/<int:page>`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `channel`
- Paths: `/slides/<int:channel_id>`, `/slides/<int:channel_id>/category/<int:category_id>`, `/slides/<int:channel_id>/category/<int:category_id>/page/<int:page>`, `/slides/<model("slide.channel"):channel>`, `/slides/<model("slide.channel"):channel>/category/<model("slide.slide"):category>`, `/slides/<model("slide.channel"):channel>/category/<model("slide.slide"):category>/page/<int:page>`, `/slides/<model("slide.channel"):channel>/page/<int:page>`, `/slides/<model("slide.channel"):channel>/tag/<model("slide.tag"):tag>`, `/slides/<model("slide.channel"):channel>/tag/<model("slide.tag"):tag>/page/<int:page>`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `slide_channel_invite`
- Paths: `/slides/<int:channel_id>/invite`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `slide_channel_identify_from_invite`
- Paths: `/slides/<int:channel_id>/identify`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `slide_channel_join`
- Paths: `/slides/channel/join`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `slide_channel_leave`
- Paths: `/slides/channel/leave`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slide_channel_tag_search_read`
- Paths: `/slides/channel/tag/search_read`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slide_channel_tag_group_search_read`
- Paths: `/slides/channel/tag/group/search_read`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slide_channel_tag_add`
- Paths: `/slides/channel/tag/add`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slide_channel_send_share_email`
- Paths: `/slides/channel/send_share_email`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slide_channel_subscribe`
- Paths: `/slides/channel/subscribe`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slide_channel_unsubscribe`
- Paths: `/slides/channel/unsubscribe`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slide_view`
- Paths: `/slides/slide/<model("slide.slide"):slide>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `slide_shared_view`
- Paths: `/slides/slide/<int:slide_id>/share`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `slide_get_pdf_content`
- Paths: `/slides/slide/<model("slide.slide"):slide>/pdf_content`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `slide_get_image`
- Paths: `/slides/slide/<int:slide_id>/get_image`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `get_html_content`
- Paths: `/slides/slide/get_html_content`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `slide_set_completed_and_redirect`
- Paths: `/slides/slide/<model("slide.slide"):slide>/set_completed`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `slide_set_completed`
- Paths: `/slides/slide/set_completed`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `slide_set_uncompleted_and_redirect`
- Paths: `/slides/slide/<model("slide.slide"):slide>/set_uncompleted`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `slide_set_uncompleted`
- Paths: `/slides/slide/set_uncompleted`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `slide_like`
- Paths: `/slides/slide/like`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `slide_archive`
- Paths: `/slides/slide/archive`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slide_preview`
- Paths: `/slides/slide/toggle_is_preview`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slide_send_share_email`
- Paths: `/slides/slide/send_share_email`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slide_channel_tag_create_or_get`
- Paths: `/slide_channel_tag/add`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slide_quiz_question_add_or_update`
- Paths: `/slides/slide/quiz/question_add_or_update`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slide_quiz_get`
- Paths: `/slides/slide/quiz/get`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `slide_quiz_reset`
- Paths: `/slides/slide/quiz/reset`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slide_quiz_submit`
- Paths: `/slides/slide/quiz/submit`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `slide_quiz_save_to_session`
- Paths: `/slides/slide/quiz/save_to_session`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `slide_category_search_read`
- Paths: `/slides/category/search_read`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slide_category_add`
- Paths: `/slides/category/add`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `prepare_preview`
- Paths: `/slides/prepare_preview`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `create_slide`
- Paths: `/slides/add_slide`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slide_tag_search_read`
- Paths: `/slides/tag/search_read`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `slides_embed`
- Paths: `/slides/embed/<int:slide_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `slides_embed_external`
- Paths: `/slides/embed_external/<int:slide_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/website_slides/Controllers]]

<!-- GENERATED:CONTROLLER -->
