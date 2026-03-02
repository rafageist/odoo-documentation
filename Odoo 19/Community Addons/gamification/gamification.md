<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Gamification

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/gamification
- Dependencies: [[Odoo 19/Community Addons/mail/mail|mail]]

## XML Artifacts (detected)

- Views: 26
- Actions: 12
- Menus: 7
- Rules (ir.rule): 3
- Access CSV entries: 36

## Detected Models

- `gamification.badge`
- `gamification.badge.user`
- `gamification.challenge`
- `gamification.challenge.line`
- `gamification.goal`
- `gamification.goal.definition`
- `gamification.karma.rank`
- `gamification.karma.tracking`
- `ResUsers`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Gamification - Models and Relations
class "gamification.badge" as gamification_badge
class "gamification.badge.user" as gamification_badge_user
class "gamification.challenge" as gamification_challenge
class "gamification.challenge.line" as gamification_challenge_line
class "gamification.goal" as gamification_goal
class "gamification.goal.definition" as gamification_goal_definition
class "gamification.karma.rank" as gamification_karma_rank
class "gamification.karma.tracking" as gamification_karma_tracking
class ResUsers
class "res.users" as res_users
gamification_badge .. res_users : many2many
gamification_badge .. gamification_badge : many2many
gamification_badge --|> gamification_challenge : one2many
gamification_badge .. gamification_goal_definition : many2many
gamification_badge --|> gamification_badge_user : one2many
gamification_badge .. res_users : many2many
gamification_badge_user --> res_users : many2one
class "res.partner" as res_partner
gamification_badge_user --> res_partner : many2one
gamification_badge_user --> res_users : many2one
gamification_badge_user --> gamification_badge : many2one
gamification_badge_user --> gamification_challenge : many2one
gamification_challenge --> res_users : many2one
gamification_challenge .. res_users : many2many
gamification_challenge .. res_users : many2many
gamification_challenge --|> gamification_challenge_line : one2many
gamification_challenge --> gamification_badge : many2one
gamification_challenge --> gamification_badge : many2one
gamification_challenge --> gamification_badge : many2one
gamification_challenge --> gamification_badge : many2one
class "discuss.channel" as discuss_channel
gamification_challenge --> discuss_channel : many2one
class "mail.template" as mail_template
gamification_challenge --> mail_template : many2one
gamification_challenge_line --> gamification_challenge : many2one
gamification_challenge_line --> gamification_goal_definition : many2one
gamification_goal --> gamification_goal_definition : many2one
gamification_goal --> res_users : many2one
gamification_goal --> res_partner : many2one
gamification_goal --> gamification_challenge_line : many2one
class "ir.model" as ir_model
gamification_goal_definition --> ir_model : many2one
gamification_goal_definition .. ir_model : many2many
class "ir.model.fields" as ir_model_fields
gamification_goal_definition --> ir_model_fields : many2one
gamification_goal_definition --> ir_model_fields : many2one
gamification_goal_definition --> ir_model_fields : many2one
class "ir.actions.act_window" as ir_actions_act_window
gamification_goal_definition --> ir_actions_act_window : many2one
gamification_karma_rank --|> res_users : one2many
gamification_karma_tracking --> res_users : many2one
ResUsers --|> gamification_karma_tracking : one2many
ResUsers --|> gamification_badge_user : one2many
ResUsers --> gamification_karma_rank : many2one
ResUsers --> gamification_karma_rank : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


