<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Quizzes on Tracks

- Scope: Community Addons
- Source: odoo/addons/website_event_track_quiz
- Dependencies: [[docs/Community Addons/website_profile/website_profile|website_profile]], [[docs/Community Addons/website_event_track/website_event_track|website_event_track]]

## Summary

Quizzes on tracks

## XML Artifacts (detected)

- Views: 14
- Actions: 2
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `EventEvent`
- `event.quiz`
- `event.quiz.question`
- `event.quiz.answer`
- `EventTrack`
- `EventTrackVisitor`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Quizzes on Tracks - Models and Relations
class EventEvent
class "event.quiz" as event_quiz
class "event.quiz.question" as event_quiz_question
class "event.quiz.answer" as event_quiz_answer
class EventTrack
class EventTrackVisitor
event_quiz --|> event_quiz_question : one2many
class "event.track" as event_track
event_quiz --> event_track : many2one
class "event.event" as event_event
event_quiz --> event_event : many2one
event_quiz_question --> event_quiz : many2one
event_quiz_question --|> event_quiz_answer : one2many
event_quiz_question --|> event_quiz_answer : one2many
event_quiz_answer --> event_quiz_question : many2one
EventTrack --> event_quiz : many2one
EventTrack --|> event_quiz : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



