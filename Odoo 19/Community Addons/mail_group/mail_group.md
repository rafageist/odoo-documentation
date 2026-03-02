<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Mail Group

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/mail_group
- Dependencies: [[Odoo 19/Community Addons/mail/mail|mail]], [[Odoo 19/Community Addons/portal/portal|portal]]

## Summary

Manage your mailing lists

## XML Artifacts (detected)

- Views: 12
- Actions: 6
- Menus: 2
- Rules (ir.rule): 10
- Access CSV entries: 9

## Detected Models

- `mail.group`
- `mail.group.member`
- `mail.group.message`
- `mail.group.moderation`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Mail Group - Models and Relations
class "mail.group" as mail_group
class "mail.group.member" as mail_group_member
class "mail.group.message" as mail_group_message
class "mail.group.moderation" as mail_group_moderation
mail_group --|> mail_group_message : one2many
mail_group --|> mail_group_member : one2many
class "res.partner" as res_partner
mail_group .. res_partner : many2many
mail_group --|> mail_group_moderation : one2many
class "res.users" as res_users
mail_group .. res_users : many2many
class "res.groups" as res_groups
mail_group --> res_groups : many2one
mail_group_member --> mail_group : many2one
mail_group_member --> res_partner : many2one
mail_group_message --> mail_group : many2one
class "mail.message" as mail_message
mail_group_message --> mail_message : many2one
mail_group_message --> mail_group_message : many2one
mail_group_message --|> mail_group_message : one2many
mail_group_message --> res_users : many2one
mail_group_moderation --> mail_group : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


