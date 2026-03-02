<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Forum on Courses

- Scope: Community Addons
- Source: odoo/addons/website_slides_forum
- Dependencies: [[docs/Community Addons/website_slides/website_slides|website_slides]], [[docs/Community Addons/website_forum/website_forum|website_forum]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




