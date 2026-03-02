<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.company

- Module: [[docs/Enterprise Addons/l10n_au_hr_payroll_api/l10n_au_hr_payroll_api|l10n_au_hr_payroll_api]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/res_company.py`
- Python classes: `ResCompany`
- Inherits: `l10n_au.audit.logging.mixin`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 1, `Many2one` x 2, `One2many` x 1, `Selection` x 2
- Relation fields: 3

## Sample fields

- `l10n_au_abn_valid`: `Boolean` (comodel `ABN Validation State`)
- `l10n_au_employer_registration_id`: `Many2one` (comodel `l10n_au.employer.registration`, compute `_compute_l10n_au_employer_registration_id`, store `True`)
- `l10n_au_employer_registration_ids`: `One2many` (comodel `l10n_au.employer.registration`)
- `l10n_au_payroll_mode`: `Selection`
- `l10n_au_payroll_proxy_user_id`: `Many2one` (comodel `account_edi_proxy_client.user`, compute `_compute_l10n_au_payroll_proxy_user_id`)
- `l10n_au_registration_status`: `Selection` (compute `_compute_l10n_au_employer_registration`)

## Method hints

- Detected methods: 11
- Action methods: `action_check_abn`, `action_view_payroll_onboarding`
- Compute methods: `_compute_l10n_au_employer_registration`, `_compute_l10n_au_employer_registration_id`, `_compute_l10n_au_payroll_proxy_user_id`
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
title res.company - Direct Relations
class "res.company" as res_company
class "account_edi_proxy_client.user" as account_edi_proxy_client_user
class "l10n_au.employer.registration" as l10n_au_employer_registration
res_company --> account_edi_proxy_client_user : l10n_au_payroll_proxy_user_id
res_company --|> l10n_au_employer_registration : l10n_au_employer_registration_ids
res_company --> l10n_au_employer_registration : l10n_au_employer_registration_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_au_hr_payroll_api/Models]]

<!-- GENERATED:MODEL -->
