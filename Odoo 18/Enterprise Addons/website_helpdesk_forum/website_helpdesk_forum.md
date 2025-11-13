<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Helpdesk: Help Center

- Version: v18
- Category: enterprise
- Source: enterprise18/website_helpdesk_forum
- Dependencies: [[Odoo 18/Community Addons/website_forum/website_forum|website_forum]], [[Odoo 18/Enterprise Addons/website_helpdesk/website_helpdesk|website_helpdesk]]

## Summary

Help Center for helpdesk based on Odoo Forum

## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `ForumForum`
- `ForumPost`
- `HelpdeskTeam`
- `HelpdeskTicket`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Helpdesk: Help Center - Models and Relations
class ForumForum
class ForumPost
class HelpdeskTeam
class HelpdeskTicket
class "helpdesk.team" as helpdesk_team
ForumForum .. helpdesk_team : many2many
class "helpdesk.ticket" as helpdesk_ticket
ForumPost --> helpdesk_ticket : many2one
class "forum.forum" as forum_forum
HelpdeskTeam .. forum_forum : many2many
class "forum.post" as forum_post
HelpdeskTeam .. forum_post : many2many
HelpdeskTicket .. forum_post : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
