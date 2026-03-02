<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# WebsiteBlog

- Module: [[docs/Community Addons/website_blog/website_blog|website_blog]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 4

## Routes

### `blog`
- Paths: `/blog`, `/blog/<model("blog.blog"):blog>`, `/blog/<model("blog.blog"):blog>/page/<int:page>`, `/blog/<model("blog.blog"):blog>/tag/<string:tag>`, `/blog/<model("blog.blog"):blog>/tag/<string:tag>/page/<int:page>`, `/blog/page/<int:page>`, `/blog/tag/<string:tag>`, `/blog/tag/<string:tag>/page/<int:page>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `blog_feed`
- Paths: `/blog/<model("blog.blog"):blog>/feed`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `old_blog_post`
- Paths: `/blog/<model("blog.blog"):blog>/post/<model("blog.post"):blog_post>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `blog_post`
- Paths: `/blog/<model("blog.blog"):blog>/<model("blog.post", "[('blog_id','=',blog.id)]"):blog_post>`
- Type: `http`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/website_blog/Controllers]]

<!-- GENERATED:CONTROLLER -->
