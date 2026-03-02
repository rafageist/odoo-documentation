<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Forum on Courses

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/website_slides_forum
- Dependencies: [[Odoo 19/Community Addons/website_slides/website_slides|website_slides]], [[Odoo 19/Community Addons/website_forum/website_forum|website_forum]]

## Summary

Allows to link forum on a course

## XML Artifacts (detected)

- Views: 5
- Actions: 2
- Menus: 3
- Rules (ir.rule): 9
- Access CSV entries: 1

## Detected Models

- `ForumForum`
- `SlideChannel`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Forum on Courses - Models and Relations
class ForumForum
class SlideChannel
class "slide.channel" as slide_channel
ForumForum --|> slide_channel : one2many
ForumForum --> slide_channel : many2one
class "forum.forum" as forum_forum
SlideChannel --> forum_forum : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

