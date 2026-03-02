<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Blog

- Scope: Community Addons
- Source: odoo/addons/website_blog
- Dependencies: [[docs/Community Addons/website_mail/website_mail|website_mail]], [[docs/Community Addons/website_partner/website_partner|website_partner]], [[docs/Community Addons/html_builder/html_builder|html_builder]]

## Summary

Publish blog posts, announces, news

## XML Artifacts (detected)

- Views: 12
- Actions: 7
- Menus: 5
- Rules (ir.rule): 2
- Access CSV entries: 16

## Detected Models

- `Website`
- `blog.blog`
- `blog.tag.category`
- `blog.tag`
- `blog.post`
- `WebsiteSnippetFilter`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Blog - Models and Relations
class Website
class "blog.blog" as blog_blog
class "blog.tag.category" as blog_tag_category
class "blog.tag" as blog_tag
class "blog.post" as blog_post
class WebsiteSnippetFilter
blog_blog --|> blog_post : one2many
blog_tag_category --|> blog_tag : one2many
blog_tag --> blog_tag_category : many2one
blog_tag .. blog_post : many2many
class "res.partner" as res_partner
blog_post --> res_partner : many2one
blog_post --> blog_blog : many2one
blog_post .. blog_tag : many2many
class "res.users" as res_users
blog_post --> res_users : many2one
blog_post --> res_users : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




