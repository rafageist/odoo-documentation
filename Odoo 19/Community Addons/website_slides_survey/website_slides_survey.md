<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Course Certifications

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/website_slides_survey
- Dependencies: [[Odoo 19/Community Addons/website_slides/website_slides|website_slides]], [[Odoo 19/Community Addons/survey/survey|survey]]

## Summary

Add certification capabilities to your courses

## XML Artifacts (detected)

- Views: 12
- Actions: 5
- Menus: 1
- Rules (ir.rule): 5
- Access CSV entries: 5

## Detected Models

- `SlideChannelPartner`
- `SlideChannel`
- `SlideSlidePartner`
- `SlideSlide`
- `SurveySurvey`
- `SurveyUser_Input`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Course Certifications - Models and Relations
class SlideChannelPartner
class SlideChannel
class SlideSlidePartner
class SlideSlide
class SurveySurvey
class SurveyUser_Input
class "survey.user_input" as survey_user_input
SlideSlidePartner --|> survey_user_input : one2many
class "survey.survey" as survey_survey
SlideSlide --> survey_survey : many2one
class "slide.slide" as slide_slide
SurveySurvey --|> slide_slide : one2many
class "slide.channel" as slide_channel
SurveySurvey --|> slide_channel : one2many
SurveyUser_Input --> slide_slide : many2one
class "slide.slide.partner" as slide_slide_partner
SurveyUser_Input --> slide_slide_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

