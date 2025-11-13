<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# HR Gamification

- Version: v18
- Category: community
- Source: odoo/addons/hr_gamification
- Dependencies: [[Odoo 18/Community Addons/gamification/gamification|gamification]], [[Odoo 18/Community Addons/hr/hr|hr]]
## XML Artifacts (detected)

- Views: 5
- Actions: 5
- Menus: 4
- Rules (ir.rule): 1
- Access CSV entries: 4

## Detected Models

- `GamificationBadgeUser`
- `GamificationBadge`
- `ResUsers`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title HR Gamification - Models and Relations
class GamificationBadgeUser
class GamificationBadge
class ResUsers
class "hr.employee" as hr_employee
GamificationBadgeUser --> hr_employee : many2one
class "gamification.goal" as gamification_goal
ResUsers --|> gamification_goal : one2many
class "gamification.badge.user" as gamification_badge_user
ResUsers --|> gamification_badge_user : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
