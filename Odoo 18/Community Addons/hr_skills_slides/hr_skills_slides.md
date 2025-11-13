<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Skills e-learning

- Version: v18
- Category: community
- Source: odoo/addons/hr_skills_slides
- Dependencies: [[Odoo 18/Community Addons/hr_skills/hr_skills|hr_skills]], [[Odoo 18/Community Addons/website_slides/website_slides|website_slides]]

## Summary

Add completed courses to resume of your employees

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `Employee`
- `ResumeLine`
- `SlideChannelPartner`
- `Channel`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Skills e-learning - Models and Relations
class Employee
class ResumeLine
class SlideChannelPartner
class Channel
class "slide.channel" as slide_channel
Employee .. slide_channel : many2many
ResumeLine --> slide_channel : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
