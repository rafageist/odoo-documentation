<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# HR Gamification

- Version: v19
- Category: community
- Source: odoo19/addons/hr_gamification
- Dependencies: [[Odoo 19/Community Addons/gamification/gamification|gamification]], [[Odoo 19/Community Addons/hr/hr|hr]]
## XML Artifacts (detected)

- Views: 6
- Actions: 5
- Menus: 4
- Rules (ir.rule): 4
- Access CSV entries: 5

## Detected Models

- `GamificationBadgeUser`
- `GamificationBadge`
- `HrEmployee`
- `HrEmployeePublic`
- `ResUsers`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title HR Gamification - Models and Relations
class GamificationBadgeUser
class GamificationBadge
class HrEmployee
class HrEmployeePublic
class ResUsers
class "hr.employee" as hr_employee
GamificationBadgeUser --> hr_employee : many2one
class "gamification.goal" as gamification_goal
HrEmployee --|> gamification_goal : one2many
class "gamification.badge.user" as gamification_badge_user
HrEmployee --|> gamification_badge_user : one2many
HrEmployee --|> gamification_badge_user : one2many
HrEmployeePublic --|> gamification_badge_user : one2many
ResUsers --|> gamification_goal : one2many
ResUsers --|> gamification_badge_user : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
