<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# l10n_it_edi_doi.declaration_of_intent

- Module: [[docs/Community Addons/l10n_it_edi_doi/l10n_it_edi_doi|l10n_it_edi_doi]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/declaration_of_intent.py`
- Python classes: `L10n_It_Edi_DoiDeclaration_Of_Intent`
- Description: Declaration of Intent
- Inherits: `mail.activity.mixin`, `mail.thread.main.attachment`

## Field footprint

- Detected fields: 15
- Field types: `Char` x 2, `Date` x 3, `Many2one` x 3, `Monetary` x 4, `One2many` x 2, `Selection` x 1
- Relation fields: 5

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `currency_id`: `Many2one` (comodel `res.currency`)
- `end_date`: `Date`
- `invoice_ids`: `One2many` (comodel `account.move`)
- `invoiced`: `Monetary` (compute `_compute_invoiced`, store `True`)
- `issue_date`: `Date`
- `not_yet_invoiced`: `Monetary` (compute `_compute_not_yet_invoiced`, store `True`)
- `partner_id`: `Many2one` (comodel `res.partner`)
- `protocol_number_part1`: `Char`
- `protocol_number_part2`: `Char`
- `remaining`: `Monetary` (compute `_compute_remaining`, store `True`)
- `sale_order_ids`: `One2many` (comodel `sale.order`)
- `start_date`: `Date`
- `state`: `Selection`
- `threshold`: `Monetary`

## Method hints

- Detected methods: 16
- Action methods: `action_open_invoice_ids`, `action_open_sale_order_ids`, `action_reactivate`, `action_reset_to_draft`, `action_revoke`, `action_terminate`, `action_validate`
- Compute methods: `_compute_display_name`, `_compute_invoiced`, `_compute_not_yet_invoiced`, `_compute_remaining`
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
title l10n_it_edi_doi.declaration_of_intent - Direct Relations
class "l10n_it_edi_doi.declaration_of_intent" as l10n_it_edi_doi_declaration_of_intent
class "account.move" as account_move
class "res.company" as res_company
class "res.currency" as res_currency
class "res.partner" as res_partner
class "sale.order" as sale_order
l10n_it_edi_doi_declaration_of_intent --> res_company : company_id
l10n_it_edi_doi_declaration_of_intent --> res_partner : partner_id
l10n_it_edi_doi_declaration_of_intent --> res_currency : currency_id
l10n_it_edi_doi_declaration_of_intent --|> account_move : invoice_ids
l10n_it_edi_doi_declaration_of_intent --|> sale_order : sale_order_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/l10n_it_edi_doi/Models]]

<!-- GENERATED:MODEL -->
