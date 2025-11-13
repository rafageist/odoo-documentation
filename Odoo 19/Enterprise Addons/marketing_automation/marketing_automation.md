<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Marketing Automation

- Version: v19
- Category: enterprise
- Source: enterprise19/marketing_automation
- Dependencies: [[Odoo 19/Community Addons/mass_mailing/mass_mailing|mass_mailing]]

## Summary

Build automated mailing campaigns

## XML Artifacts (detected)

- Views: 21
- Actions: 13
- Menus: 8
- Rules (ir.rule): 0
- Access CSV entries: 6

## Detected Models

- `MailingMailing`
- `MailingTrace`
- `marketing.activity`
- `marketing.campaign`
- `marketing.participant`
- `marketing.trace`
- `UtmCampaign`
- `UtmSource`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Marketing Automation - Models and Relations
class MailingMailing
class MailingTrace
class "marketing.activity" as marketing_activity
class "marketing.campaign" as marketing_campaign
class "marketing.participant" as marketing_participant
class "marketing.trace" as marketing_trace
class UtmCampaign
class UtmSource
MailingMailing --|> marketing_activity : one2many
MailingTrace --> marketing_trace : many2one
class "mailing.mailing" as mailing_mailing
marketing_activity --> mailing_mailing : many2one
class "ir.actions.server" as ir_actions_server
marketing_activity --> ir_actions_server : many2one
marketing_activity --> marketing_campaign : many2one
class "utm.campaign" as utm_campaign
marketing_activity --> utm_campaign : many2one
class "ir.model" as ir_model
marketing_activity --> ir_model : many2one
marketing_activity --> marketing_activity : many2one
marketing_activity .. marketing_activity : many2many
marketing_activity --|> marketing_activity : one2many
marketing_activity --|> marketing_trace : one2many
marketing_campaign --> utm_campaign : many2one
marketing_campaign --> ir_model : many2one
class "ir.model.fields" as ir_model_fields
marketing_campaign --> ir_model_fields : many2one
class "mailing.filter" as mailing_filter
marketing_campaign --> mailing_filter : many2one
marketing_campaign --|> marketing_activity : one2many
marketing_campaign --|> marketing_participant : one2many
marketing_participant --> marketing_campaign : many2one
marketing_participant --> ir_model : many2one
marketing_participant --|> marketing_trace : one2many
marketing_trace --> marketing_participant : many2one
marketing_trace --> marketing_activity : many2one
marketing_trace --> marketing_trace : many2one
marketing_trace --|> marketing_trace : one2many
class "mailing.trace" as mailing_trace
marketing_trace --|> mailing_trace : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
