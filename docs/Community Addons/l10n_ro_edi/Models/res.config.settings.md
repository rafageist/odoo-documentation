<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.config.settings

- Module: [[docs/Community Addons/l10n_ro_edi/l10n_ro_edi|l10n_ro_edi]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 9
- Field types: `Boolean` x 1, `Char` x 5, `Date` x 2, `Many2one` x 1
- Relation fields: 1

## Sample fields

- `l10n_ro_edi_access_expiry_date`: `Date` (related `company_id.l10n_ro_edi_access_expiry_date`)
- `l10n_ro_edi_access_token`: `Char` (related `company_id.l10n_ro_edi_access_token`)
- `l10n_ro_edi_anaf_imported_inv_journal_id`: `Many2one` (related `company_id.l10n_ro_edi_anaf_imported_inv_journal_id`)
- `l10n_ro_edi_callback_url`: `Char` (related `company_id.l10n_ro_edi_callback_url`)
- `l10n_ro_edi_client_id`: `Char` (related `company_id.l10n_ro_edi_client_id`)
- `l10n_ro_edi_client_secret`: `Char` (related `company_id.l10n_ro_edi_client_secret`)
- `l10n_ro_edi_refresh_expiry_date`: `Date` (related `company_id.l10n_ro_edi_refresh_expiry_date`)
- `l10n_ro_edi_refresh_token`: `Char` (related `company_id.l10n_ro_edi_refresh_token`)
- `l10n_ro_edi_test_env`: `Boolean` (related `company_id.l10n_ro_edi_test_env`)

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
title res.config.settings - Direct Relations
class "res.config.settings" as res_config_settings
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/l10n_ro_edi/Models]]

<!-- GENERATED:MODEL -->
