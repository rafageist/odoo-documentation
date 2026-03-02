<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Indian - Accounting Reports

- Scope: Enterprise Addons
- Source: enterprise/l10n_in_reports
- Dependencies: [[docs/Community Addons/l10n_in/l10n_in|l10n_in]], [[docs/Enterprise Addons/account_reports/account_reports|account_reports]], [[docs/Enterprise Addons/accountant/accountant|accountant]], [[docs/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]], [[docs/Community Addons/barcodes/barcodes|barcodes]], [[docs/Enterprise Addons/account_invoice_extract/account_invoice_extract|account_invoice_extract]]

## Generated coverage

- Models: 17
- XML files with UI/data artifacts: 12
- Views: 15
- Actions: 3
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 7
- Controller units: 0
- Frontend asset files: 5

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
title Indian - Accounting Reports - Generated Coverage
component "Module Overview" as overview
component "Models\n17" as models
component "Views / XML\n15 views\n12 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n5 files" as frontend
component "Security / Data\n0 rules\n7 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/l10n_in_reports/Models|Models]] (17)
- Views and XML: [[docs/Enterprise Addons/l10n_in_reports/Views|Views]] (12 files)
- Frontend: [[docs/Enterprise Addons/l10n_in_reports/Frontend|Frontend]] (5 files)

## Key models

- `account.batch.payment`
- `account.journal`
- `account.move`
- `account.payment`
- `account.payment.method`
- `account.report`
- `account.return`
- `account.return.check`
- `account.return.type`
- `enet.bank.template`
- `ir.attachment`
- `l10n_in.gst.otp.validation`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




