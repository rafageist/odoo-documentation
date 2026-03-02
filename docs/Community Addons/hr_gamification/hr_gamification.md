<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# HR Gamification

- Scope: Community Addons
- Source: odoo/addons/hr_gamification
- Dependencies: [[docs/Community Addons/gamification/gamification|gamification]], [[docs/Community Addons/hr/hr|hr]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





