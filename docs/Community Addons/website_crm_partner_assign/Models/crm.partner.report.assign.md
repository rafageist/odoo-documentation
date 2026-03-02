<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# crm.partner.report.assign

- Module: [[docs/Community Addons/website_crm_partner_assign/website_crm_partner_assign|website_crm_partner_assign]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `report/crm_partner_report.py`
- Python classes: `CrmPartnerReportAssign`
- Description: CRM Partnership Analysis

## Field footprint

- Detected fields: 10
- Field types: `Date` x 3, `Float` x 1, `Integer` x 1, `Many2one` x 5
- Relation fields: 5

## Sample fields

- `activation`: `Many2one` (comodel `res.partner.activation`)
- `country_id`: `Many2one` (comodel `res.country`)
- `date`: `Date` (comodel `Invoice Account Date`)
- `date_partnership`: `Date` (comodel `Partnership Date`)
- `date_review`: `Date` (comodel `Latest Partner Review`)
- `grade_id`: `Many2one` (comodel `res.partner.grade`)
- `nbr_opportunities`: `Integer` (comodel `# of Opportunity`)
- `partner_id`: `Many2one` (comodel `res.partner`)
- `turnover`: `Float` (comodel `Turnover`)
- `user_id`: `Many2one` (comodel `res.users`)

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Direct relation diagram

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title crm.partner.report.assign - Direct Relations
class "crm.partner.report.assign" as crm_partner_report_assign
class "res.country" as res_country
class "res.partner" as res_partner
class "res.partner.activation" as res_partner_activation
class "res.partner.grade" as res_partner_grade
class "res.users" as res_users
crm_partner_report_assign --> res_partner : partner_id
crm_partner_report_assign --> res_partner_grade : grade_id
crm_partner_report_assign --> res_partner_activation : activation
crm_partner_report_assign --> res_users : user_id
crm_partner_report_assign --> res_country : country_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/website_crm_partner_assign/Models]]

<!-- GENERATED:MODEL -->
