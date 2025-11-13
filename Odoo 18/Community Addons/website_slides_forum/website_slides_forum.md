<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Forum on Courses

- Version: v18
- Category: community
- Source: odoo/addons/website_slides_forum
- Dependencies: [[Odoo 18/Community Addons/website_slides/website_slides|website_slides]], [[Odoo 18/Community Addons/website_forum/website_forum|website_forum]]

## Summary

Allows to link forum on a course

## XML Artifacts (detected)

- Views: 5
- Actions: 2
- Menus: 3
- Rules (ir.rule): 9
- Access CSV entries: 1

## Detected Models

- `Forum`
- `Channel`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Forum on Courses - Models and Relations
class Forum
class Channel
class "slide.channel" as slide_channel
Forum --|> slide_channel : one2many
Forum --> slide_channel : many2one
class "forum.forum" as forum_forum
Channel --> forum_forum : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
