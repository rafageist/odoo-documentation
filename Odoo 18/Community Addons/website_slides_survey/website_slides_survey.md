<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Course Certifications

- Version: v18
- Category: community
- Source: odoo/addons/website_slides_survey
- Dependencies: [[Odoo 18/Community Addons/website_slides/website_slides|website_slides]], [[Odoo 18/Community Addons/survey/survey|survey]]

## Summary

Add certification capabilities to your courses

## XML Artifacts (detected)

- Views: 12
- Actions: 5
- Menus: 1
- Rules (ir.rule): 5
- Access CSV entries: 5

## Detected Models

- `ChannelUsersRelation`
- `Channel`
- `SlidePartnerRelation`
- `Slide`
- `Survey`
- `SurveyUserInput`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Course Certifications - Models and Relations
class ChannelUsersRelation
class Channel
class SlidePartnerRelation
class Slide
class Survey
class SurveyUserInput
class "survey.user_input" as survey_user_input
SlidePartnerRelation --|> survey_user_input : one2many
class "survey.survey" as survey_survey
Slide --> survey_survey : many2one
class "slide.slide" as slide_slide
Survey --|> slide_slide : one2many
class "slide.channel" as slide_channel
Survey --|> slide_channel : one2many
SurveyUserInput --> slide_slide : many2one
class "slide.slide.partner" as slide_slide_partner
SurveyUserInput --> slide_slide_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
