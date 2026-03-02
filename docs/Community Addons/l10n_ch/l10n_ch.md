<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Switzerland - Accounting

- Scope: Community Addons
- Source: odoo/addons/l10n_ch
- Dependencies: [[docs/Community Addons/account/account|account]], [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[docs/Community Addons/base_iban/base_iban|base_iban]], [[docs/Community Addons/l10n_din5008/l10n_din5008|l10n_din5008]]

## Generated coverage

- Models: 9
- XML files with UI/data artifacts: 5
- Views: 4
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1
- Controller units: 0
- Frontend asset files: 0

## Module map

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
title Switzerland - Accounting - Generated Coverage
component "Module Overview" as overview
component "Models\n9" as models
component "Views / XML\n4 views\n5 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/l10n_ch/Models|Models]] (9)
- Views and XML: [[docs/Community Addons/l10n_ch/Views|Views]] (5 files)

## Key models

- `account.chart.template`
- `account.journal`
- `account.move`
- `account.payment`
- `account.setup.bank.manual.config`
- `ir.actions.report`
- `l10n_ch.qr_invoice.wizard`
- `report.l10n_ch.qr_report_main`
- `res.partner.bank`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






