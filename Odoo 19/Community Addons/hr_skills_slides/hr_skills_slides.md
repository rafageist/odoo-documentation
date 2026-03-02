<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Skills e-learning

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/hr_skills_slides
- Dependencies: [[Odoo 19/Community Addons/hr_skills/hr_skills|hr_skills]], [[Odoo 19/Community Addons/website_slides/website_slides|website_slides]]

## Summary

Add completed courses to resume of your employees

## XML Artifacts (detected)

- Views: 8
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrEmployee`
- `HrEmployeePublic`
- `HrResumeLine`
- `SlideChannelPartner`
- `SlideChannel`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Skills e-learning - Models and Relations
class HrEmployee
class HrEmployeePublic
class HrResumeLine
class SlideChannelPartner
class SlideChannel
class "slide.channel" as slide_channel
HrEmployee .. slide_channel : many2many
HrResumeLine --> slide_channel : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


