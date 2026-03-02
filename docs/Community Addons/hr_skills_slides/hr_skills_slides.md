<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Skills e-learning

- Scope: Community Addons
- Source: odoo/addons/hr_skills_slides
- Dependencies: [[docs/Community Addons/hr_skills/hr_skills|hr_skills]], [[docs/Community Addons/website_slides/website_slides|website_slides]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





