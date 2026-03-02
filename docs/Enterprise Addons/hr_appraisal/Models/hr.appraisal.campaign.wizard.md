<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.appraisal.campaign.wizard

- Module: [[docs/Enterprise Addons/hr_appraisal/hr_appraisal|hr_appraisal]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/hr_appraisal_campaign_wizard.py`
- Python classes: `HrAppraisalCampaignWizard`
- Description: Appraisal Campaign Wizard
- Inherits: `hr.mixin`

## Field footprint

- Detected fields: 10
- Field types: `Char` x 1, `Date` x 1, `Many2many` x 2, `Many2one` x 4, `Selection` x 2
- Relation fields: 6

## Sample fields

- `appraisal_date`: `Date`
- `appraisal_template_id`: `Many2one` (comodel `hr.appraisal.template`)
- `category_id`: `Many2one` (comodel `hr.employee.category`)
- `company_id`: `Many2one` (comodel `res.company`)
- `department_id`: `Many2one` (comodel `hr.department`)
- `employee_ids`: `Many2many` (comodel `hr.employee`)
- `manager`: `Selection`
- `manager_ids`: `Many2many` (comodel `hr.employee`)
- `mode`: `Selection`
- `warning`: `Char` (compute `_compute_warning`)

## Method hints

- Detected methods: 6
- Action methods: `action_generate_appraisals`
- Compute methods: `_compute_warning`
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
title hr.appraisal.campaign.wizard - Direct Relations
class "hr.appraisal.campaign.wizard" as hr_appraisal_campaign_wizard
class "hr.appraisal.template" as hr_appraisal_template
class "hr.department" as hr_department
class "hr.employee" as hr_employee
class "hr.employee.category" as hr_employee_category
class "res.company" as res_company
hr_appraisal_campaign_wizard .. hr_employee : employee_ids
hr_appraisal_campaign_wizard --> hr_department : department_id
hr_appraisal_campaign_wizard --> res_company : company_id
hr_appraisal_campaign_wizard --> hr_employee_category : category_id
hr_appraisal_campaign_wizard .. hr_employee : manager_ids
hr_appraisal_campaign_wizard --> hr_appraisal_template : appraisal_template_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal/Models]]

<!-- GENERATED:MODEL -->
