<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_es_reports.aeat.mod347.manual.partner.data

- Module: [[docs/Enterprise Addons/l10n_es_reports/l10n_es_reports|l10n_es_reports]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/aeat_boe_export_wizards.py`
- Python classes: `L10n_Es_ReportsAeatMod347ManualPartnerData`
- Description: Manually Entered Data for Mod 347 Report

## Field footprint

- Detected fields: 6
- Field types: `Many2one` x 3, `Monetary` x 1, `Selection` x 2
- Relation fields: 3

## Sample fields

- `currency_id`: `Many2one` (comodel `res.currency`)
- `operation_class`: `Selection`
- `operation_key`: `Selection`
- `parent_wizard_id`: `Many2one` (comodel `l10n_es_reports.aeat.boe.mod347.export.wizard`)
- `partner_id`: `Many2one` (comodel `res.partner`)
- `perceived_amount`: `Monetary`

## Method hints

- Detected methods: 0
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
title l10n_es_reports.aeat.mod347.manual.partner.data - Direct Relations
class "l10n_es_reports.aeat.mod347.manual.partner.data" as l10n_es_reports_aeat_mod347_manual_partner_data
class "l10n_es_reports.aeat.boe.mod347.export.wizard" as l10n_es_reports_aeat_boe_mod347_export_wizard
class "res.currency" as res_currency
class "res.partner" as res_partner
l10n_es_reports_aeat_mod347_manual_partner_data --> l10n_es_reports_aeat_boe_mod347_export_wizard : parent_wizard_id
l10n_es_reports_aeat_mod347_manual_partner_data --> res_partner : partner_id
l10n_es_reports_aeat_mod347_manual_partner_data --> res_currency : currency_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_es_reports/Models]]

<!-- GENERATED:MODEL -->
