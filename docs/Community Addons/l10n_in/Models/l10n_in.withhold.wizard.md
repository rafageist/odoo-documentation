<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# l10n_in.withhold.wizard

- Module: [[docs/Community Addons/l10n_in/l10n_in|l10n_in]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/l10n_in_withhold_wizard.py`
- Python classes: `L10n_InWithholdWizard`
- Description: Withhold Wizard

## Field footprint

- Detected fields: 14
- Field types: `Char` x 3, `Date` x 1, `Json` x 1, `Many2one` x 6, `Monetary` x 2, `Selection` x 1
- Relation fields: 6

## Sample fields

- `amount`: `Monetary` (compute `_compute_amount`)
- `base`: `Monetary` (compute `_compute_base`, store `True`)
- `company_id`: `Many2one` (comodel `res.company`, compute `_compute_company_id`)
- `currency_id`: `Many2one` (related `company_id.currency_id`)
- `date`: `Date`
- `journal_id`: `Many2one` (comodel `account.journal`, compute `_compute_journal`, store `True`)
- `l10n_in_tds_tax_type`: `Char` (compute `_compute_l10n_in_tds_tax_type`)
- `l10n_in_withholding_warning`: `Json` (compute `_compute_l10n_in_withholding_warning`)
- `reference`: `Char`
- `related_move_id`: `Many2one` (comodel `account.move`)
- `related_payment_id`: `Many2one` (comodel `account.payment`)
- `tax_id`: `Many2one` (comodel `account.tax`, compute `_compute_tax_id`, store `True`)
- `tds_deduction`: `Selection` (compute `_compute_tds_deduction`)
- `type_name`: `Char` (compute `_compute_type_name`)

## Method hints

- Detected methods: 16
- Action methods: `action_create_and_post_withhold`
- Compute methods: `_compute_amount`, `_compute_base`, `_compute_company_id`, `_compute_journal`, `_compute_l10n_in_tds_tax_type`, `_compute_l10n_in_withholding_warning`, `_compute_tax_id`, `_compute_tds_deduction`, and 1 more
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
title l10n_in.withhold.wizard - Direct Relations
class "l10n_in.withhold.wizard" as l10n_in_withhold_wizard
class "account.journal" as account_journal
class "account.move" as account_move
class "account.payment" as account_payment
class "account.tax" as account_tax
class "res.company" as res_company
l10n_in_withhold_wizard --> account_move : related_move_id
l10n_in_withhold_wizard --> account_payment : related_payment_id
l10n_in_withhold_wizard --> res_company : company_id
l10n_in_withhold_wizard --> account_journal : journal_id
l10n_in_withhold_wizard --> account_tax : tax_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/l10n_in/Models]]

<!-- GENERATED:MODEL -->
