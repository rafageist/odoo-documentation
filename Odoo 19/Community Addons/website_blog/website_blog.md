<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Blog

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/website_blog
- Dependencies: [[Odoo 19/Community Addons/website_mail/website_mail|website_mail]], [[Odoo 19/Community Addons/website_partner/website_partner|website_partner]], [[Odoo 19/Community Addons/html_builder/html_builder|html_builder]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

