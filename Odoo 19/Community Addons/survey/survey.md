<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Surveys

- Version: v19
- Category: community
- Source: odoo19/addons/survey
- Dependencies: [[Odoo 19/Community Addons/auth_signup/auth_signup|auth_signup]], [[Odoo 19/Community Addons/http_routing/http_routing|http_routing]], [[Odoo 19/Community Addons/mail/mail|mail]], [[Odoo 19/Community Addons/web_tour/web_tour|web_tour]], [[Odoo 19/Community Addons/gamification/gamification|gamification]]

## Summary

Send your surveys or share them live.

## XML Artifacts (detected)

- Views: 23
- Actions: 8
- Menus: 7
- Rules (ir.rule): 12
- Access CSV entries: 22

## Detected Models

- `GamificationBadge`
- `GamificationChallenge`
- `ResLang`
- `ResPartner`
- `survey.question`
- `survey.question.answer`
- `survey.survey`
- `survey.user_input`
- `survey.user_input.line`
- `SurveySurvey`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Surveys - Models and Relations
class GamificationBadge
class GamificationChallenge
class ResLang
class ResPartner
class "survey.question" as survey_question
class "survey.question.answer" as survey_question_answer
class "survey.survey" as survey_survey
class "survey.user_input" as survey_user_input
class "survey.user_input.line" as survey_user_input_line
class SurveySurvey
GamificationBadge --|> survey_survey : one2many
GamificationBadge --> survey_survey : many2one
survey_question --> survey_survey : many2one
survey_question --|> survey_question : one2many
survey_question --> survey_question : many2one
survey_question --|> survey_question_answer : one2many
survey_question --|> survey_question_answer : one2many
survey_question --|> survey_user_input_line : one2many
survey_question .. survey_question : many2many
survey_question .. survey_question : many2many
survey_question .. survey_question_answer : many2many
survey_question_answer --> survey_question : many2one
survey_question_answer --> survey_question : many2one
class "res.lang" as res_lang
survey_survey .. res_lang : many2many
class "res.users" as res_users
survey_survey --> res_users : many2one
survey_survey .. res_users : many2many
survey_survey --|> survey_question : one2many
survey_survey --|> survey_question : one2many
survey_survey --|> survey_question : one2many
survey_survey --|> survey_user_input : one2many
class "mail.template" as mail_template
survey_survey --> mail_template : many2one
class "gamification.badge" as gamification_badge
survey_survey --> gamification_badge : many2one
survey_survey --> survey_question : many2one
survey_user_input --> survey_survey : many2one
survey_user_input --> res_lang : many2one
survey_user_input --> survey_question : many2one
class "res.partner" as res_partner
survey_user_input --> res_partner : many2one
survey_user_input --|> survey_user_input_line : one2many
survey_user_input .. survey_question : many2many
survey_user_input_line --> survey_user_input : many2one
survey_user_input_line --> survey_question : many2one
survey_user_input_line --> res_lang : many2one
survey_user_input_line --> survey_question_answer : many2one
survey_user_input_line --> survey_question_answer : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
