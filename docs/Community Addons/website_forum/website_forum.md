<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Forum

- Scope: Community Addons
- Source: odoo/addons/website_forum
- Dependencies: [[docs/Community Addons/auth_signup/auth_signup|auth_signup]], [[docs/Community Addons/website_mail/website_mail|website_mail]], [[docs/Community Addons/website_profile/website_profile|website_profile]]

## Summary

Manage a forum with FAQ and Q&A

## XML Artifacts (detected)

- Views: 14
- Actions: 9
- Menus: 7
- Rules (ir.rule): 12
- Access CSV entries: 15

## Detected Models

- `forum.forum`
- `forum.post`
- `forum.post.reason`
- `forum.post.vote`
- `forum.tag`
- `GamificationChallenge`
- `GamificationKarmaTracking`
- `IrAttachment`
- `ResUsers`
- `Website`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Forum - Models and Relations
class "forum.forum" as forum_forum
class "forum.post" as forum_post
class "forum.post.reason" as forum_post_reason
class "forum.post.vote" as forum_post_vote
class "forum.tag" as forum_tag
class GamificationChallenge
class GamificationKarmaTracking
class IrAttachment
class ResUsers
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



