<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Forum

- Version: v18
- Category: community
- Source: odoo/addons/website_forum
- Dependencies: [[Odoo 18/Community Addons/auth_signup/auth_signup|auth_signup]], [[Odoo 18/Community Addons/website_mail/website_mail|website_mail]], [[Odoo 18/Community Addons/website_profile/website_profile|website_profile]]

## Summary

Manage a forum with FAQ and Q&A

## XML Artifacts (detected)

- Views: 15
- Actions: 9
- Menus: 7
- Rules (ir.rule): 10
- Access CSV entries: 16

## Detected Models

- `forum.forum`
- `forum.post`
- `forum.post.reason`
- `forum.post.vote`
- `forum.tag`
- `Challenge`
- `KarmaTracking`
- `Attachment`
- `Users`
- `Website`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Forum - Models and Relations
class "forum.forum" as forum_forum
class "forum.post" as forum_post
class "forum.post.reason" as forum_post_reason
class "forum.post.vote" as forum_post_vote
class "forum.tag" as forum_tag
class Challenge
class KarmaTracking
class Attachment
class Users
class Website
class "res.groups" as res_groups
forum_forum --> res_groups : many2one
forum_forum --|> forum_post : one2many
forum_forum --> forum_post : many2one
forum_forum --|> forum_tag : one2many
forum_forum --|> forum_tag : one2many
forum_forum --|> forum_tag : one2many
forum_post --> forum_forum : many2one
forum_post .. forum_tag : many2many
class "res.users" as res_users
forum_post --> res_users : many2one
forum_post --> res_users : many2one
forum_post --|> forum_post_vote : one2many
forum_post .. res_users : many2many
forum_post --> forum_post : many2one
forum_post --|> forum_post : one2many
forum_post --> res_users : many2one
forum_post --> res_users : many2one
forum_post --> forum_post_reason : many2one
forum_post --> res_users : many2one
forum_post_vote --> forum_post : many2one
forum_post_vote --> res_users : many2one
forum_post_vote --> forum_forum : many2one
forum_post_vote --> res_users : many2one
forum_tag --> forum_forum : many2one
forum_tag .. forum_post : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
