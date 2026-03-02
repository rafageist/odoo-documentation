<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# WebsiteForum

- Module: [[docs/Community Addons/website_forum/website_forum|website_forum]]
- Scope: Community Addons
- Source file: `controllers/website_forum.py`
- Base classes: `WebsiteProfile`
- Routes: 39

## Routes

### `forum`
- Paths: `/forum`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `questions`
- Paths: `/forum/<model("forum.forum"):forum>`, `/forum/<model("forum.forum"):forum>/page/<int:page>`, `/forum/<model("forum.forum"):forum>/tag/<model("forum.tag"):tag>/questions`, `/forum/<model("forum.forum"):forum>/tag/<model("forum.tag"):tag>/questions/page/<int:page>`, `/forum/all`, `/forum/all/page/<int:page>`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `forum_faq`
- Paths: `/forum/<model("forum.forum"):forum>/faq`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `forum_faq_karma`
- Paths: `/forum/<model("forum.forum"):forum>/faq/karma`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `tag_read`
- Paths: `/forum/get_tags`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `tags`
- Paths: `/forum/<model("forum.forum"):forum>/tag`, `/forum/<model("forum.forum"):forum>/tag/<string:tag_char>`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `get_url_title`
- Paths: `/forum/get_url_title`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `old_question`
- Paths: `/forum/<model("forum.forum"):forum>/question/<model("forum.post", "[('forum_id','=',forum.id),('parent_id','=',False),('can_view', '=', True)]"):question>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `question`
- Paths: `/forum/<model("forum.forum"):forum>/<model("forum.post"):question>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `question_toggle_favorite`
- Paths: `/forum/<model("forum.forum"):forum>/question/<model("forum.post"):question>/toggle_favourite`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `question_ask_for_close`
- Paths: `/forum/<model("forum.forum"):forum>/question/<model("forum.post"):question>/ask_for_close`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `question_edit_answer`
- Paths: `/forum/<model("forum.forum"):forum>/question/<model("forum.post"):question>/edit_answer`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `question_close`
- Paths: `/forum/<model("forum.forum"):forum>/question/<model("forum.post"):question>/close`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `question_reopen`
- Paths: `/forum/<model("forum.forum"):forum>/question/<model("forum.post"):question>/reopen`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `question_delete`
- Paths: `/forum/<model("forum.forum"):forum>/question/<model("forum.post"):question>/delete`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `question_undelete`
- Paths: `/forum/<model("forum.forum"):forum>/question/<model("forum.post"):question>/undelete`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `forum_post`
- Paths: `/forum/<model("forum.forum"):forum>/ask`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `post_create`
- Paths: `/forum/<model("forum.forum"):forum>/<model("forum.post"):post_parent>/reply`, `/forum/<model("forum.forum"):forum>/new`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `post_comment`
- Paths: `/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/comment`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `post_toggle_correct`
- Paths: `/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/toggle_correct`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `post_delete`
- Paths: `/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/delete`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `post_edit`
- Paths: `/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/edit`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `post_save`
- Paths: `/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/save`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `post_upvote`
- Paths: `/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/upvote`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `post_downvote`
- Paths: `/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/downvote`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `validation_queue`
- Paths: `/forum/<model("forum.forum"):forum>/validation_queue`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `flagged_queue`
- Paths: `/forum/<model("forum.forum"):forum>/flagged_queue`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `offensive_posts`
- Paths: `/forum/<model("forum.forum"):forum>/offensive_posts`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `closed_posts`
- Paths: `/forum/<model("forum.forum"):forum>/closed_posts`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `post_accept`
- Paths: `/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/validate`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `post_refuse`
- Paths: `/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/refuse`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `post_flag`
- Paths: `/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/flag`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `post_json_ask_for_mark_as_offensive`
- Paths: `/forum/<model("forum.post"):post>/ask_for_mark_as_offensive`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `post_http_ask_for_mark_as_offensive`
- Paths: `/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/ask_for_mark_as_offensive`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `post_mark_as_offensive`
- Paths: `/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/mark_as_offensive`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `open_partner`
- Paths: `/forum/<model("forum.forum"):forum>/partner/<int:partner_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `convert_comment_to_answer`
- Paths: `/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/comment/<model("mail.message"):comment>/convert_to_answer`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `convert_answer_to_comment`
- Paths: `/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/convert_to_comment`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `delete_comment`
- Paths: `/forum/<model("forum.forum"):forum>/post/<model("forum.post"):post>/comment/<model("mail.message"):comment>/delete`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/website_forum/Controllers]]

<!-- GENERATED:CONTROLLER -->
