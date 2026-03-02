<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.ar.vat.line

- Module: [[docs/Enterprise Addons/l10n_ar_reports/l10n_ar_reports|l10n_ar_reports]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `report/account_ar_vat_line.py`
- Python classes: `AccountArVatLine`
- Description: VAT line for Analysis in Argentinean Localization

## Field footprint

- Detected fields: 32
- Field types: `Char` x 4, `Date` x 2, `Many2one` x 7, `Monetary` x 17, `Selection` x 2
- Relation fields: 7

## Sample fields

- `afip_responsibility_type_id`: `Many2one` (comodel `l10n_ar.afip.responsibility.type`)
- `afip_responsibility_type_name`: `Char`
- `base_10`: `Monetary`
- `base_21`: `Monetary`
- `base_25`: `Monetary`
- `base_27`: `Monetary`
- `base_5`: `Monetary`
- `city_tax`: `Monetary`
- `company_currency_id`: `Many2one` (related `company_id.currency_id`)
- `company_id`: `Many2one` (comodel `res.company`)
- `cuit`: `Char`
- `date`: `Date`
- `document_type_id`: `Many2one` (comodel `l10n_latam.document.type`)
- `invoice_date`: `Date`
- `journal_id`: `Many2one` (comodel `account.journal`)
- `move_id`: `Many2one` (comodel `account.move`)
- `move_name`: `Char`
- `move_type`: `Selection`
- `not_taxed`: `Monetary`
- `other_taxes`: `Monetary`

## Method hints

- Detected methods: 4
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
title account.ar.vat.line - Direct Relations
class "account.ar.vat.line" as account_ar_vat_line
class "account.journal" as account_journal
class "account.move" as account_move
class "l10n_ar.afip.responsibility.type" as l10n_ar_afip_responsibility_type
class "l10n_latam.document.type" as l10n_latam_document_type
class "res.company" as res_company
class "res.partner" as res_partner
account_ar_vat_line --> l10n_latam_document_type : document_type_id
account_ar_vat_line --> account_journal : journal_id
account_ar_vat_line --> res_partner : partner_id
account_ar_vat_line --> l10n_ar_afip_responsibility_type : afip_responsibility_type_id
account_ar_vat_line --> res_company : company_id
account_ar_vat_line --> account_move : move_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ar_reports/Models]]

<!-- GENERATED:MODEL -->
