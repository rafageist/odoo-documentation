<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.company

- Module: [[docs/Community Addons/l10n_es_edi_tbai/l10n_es_edi_tbai|l10n_es_edi_tbai]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_company.py`
- Python classes: `ResCompany`

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 2, `Html` x 1, `Many2one` x 2, `One2many` x 1, `Selection` x 1
- Relation fields: 3

## Sample fields

- `l10n_es_tbai_certificate_id`: `Many2one` (comodel `certificate.certificate`, compute `_compute_l10n_es_tbai_certificate`, store `True`)
- `l10n_es_tbai_certificate_ids`: `One2many` (comodel `certificate.certificate`)
- `l10n_es_tbai_chain_sequence_id`: `Many2one` (comodel `ir.sequence`)
- `l10n_es_tbai_is_enabled`: `Boolean` (compute `_compute_l10n_es_tbai_is_enabled`)
- `l10n_es_tbai_license_html`: `Html` (compute `_compute_l10n_es_tbai_license_html`)
- `l10n_es_tbai_tax_agency`: `Selection`
- `l10n_es_tbai_test_env`: `Boolean`

## Method hints

- Detected methods: 7
- Action methods: none
- Compute methods: `_compute_l10n_es_tbai_certificate`, `_compute_l10n_es_tbai_is_enabled`, `_compute_l10n_es_tbai_license_html`
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
class "certificate.certificate" as certificate_certificate
class "ir.sequence" as ir_sequence
res_company --> certificate_certificate : l10n_es_tbai_certificate_id
res_company --|> certificate_certificate : l10n_es_tbai_certificate_ids
res_company --> ir_sequence : l10n_es_tbai_chain_sequence_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/l10n_es_edi_tbai/Models]]

<!-- GENERATED:MODEL -->
