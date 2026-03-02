<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# CRM

- Scope: Community Addons
- Source: odoo/addons/crm
- Dependencies: [[docs/Community Addons/base_setup/base_setup|base_setup]], [[docs/Community Addons/sales_team/sales_team|sales_team]], [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/calendar/calendar|calendar]], [[docs/Community Addons/resource/resource|resource]], [[docs/Community Addons/utm/utm|utm]], [[docs/Community Addons/web_tour/web_tour|web_tour]], [[docs/Community Addons/contacts/contacts|contacts]], [[docs/Community Addons/digest/digest|digest]], [[docs/Community Addons/phone_validation/phone_validation|phone_validation]]

## Summary

Track leads and close opportunities

## XML Artifacts (detected)

- Views: 55
- Actions: 60
- Menus: 27
- Rules (ir.rule): 8
- Access CSV entries: 32

## Detected Models

- `CalendarEvent`
- `crm.lead`
- `crm.lead.scoring.frequency`
- `crm.lead.scoring.frequency.field`
- `crm.lost.reason`
- `crm.recurring.plan`
- `crm.stage`
- `crm.team`
- `CrmTeamMember`
- `DigestDigest`
- `IrConfig_Parameter`
- `MailActivity`
- `ResPartner`
- `ResUsers`
- `UtmCampaign`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title CRM - Models and Relations
class CalendarEvent
class "crm.lead" as crm_lead
class "crm.lead.scoring.frequency" as crm_lead_scoring_frequency
class "crm.lead.scoring.frequency.field" as crm_lead_scoring_frequency_field
class "crm.lost.reason" as crm_lost_reason
class "crm.recurring.plan" as crm_recurring_plan
class "crm.stage" as crm_stage
class "crm.team" as crm_team
class CrmTeamMember
class DigestDigest
class IrConfig_Parameter
class MailActivity
class ResPartner
class ResUsers
class UtmCampaign
CalendarEvent --> crm_lead : many2one
class "res.users" as res_users
crm_lead --> res_users : many2one
class "res.company" as res_company
crm_lead .. res_company : many2many
crm_lead --> crm_team : many2one
crm_lead --> res_company : many2one
crm_lead --> crm_stage : many2one
class "crm.tag" as crm_tag
crm_lead .. crm_tag : many2many
crm_lead --> crm_recurring_plan : many2one
class "res.currency" as res_currency
crm_lead --> res_currency : many2one
class "res.partner" as res_partner
crm_lead --> res_partner : many2one
crm_lead --> res_partner : many2one
class "res.lang" as res_lang
crm_lead --> res_lang : many2one
class "res.country.state" as res_country_state
crm_lead --> res_country_state : many2one
class "res.country" as res_country
crm_lead --> res_country : many2one
crm_lead --> crm_lost_reason : many2one
class "calendar.event" as calendar_event
crm_lead --|> calendar_event : one2many
crm_lead .. crm_lead : many2many
crm_lead_scoring_frequency --> crm_team : many2one
class "ir.model.fields" as ir_model_fields
crm_lead_scoring_frequency_field --> ir_model_fields : many2one
crm_stage .. crm_team : many2many
ResPartner --|> crm_lead : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





