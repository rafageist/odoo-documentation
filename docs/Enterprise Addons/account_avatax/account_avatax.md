
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Avatax

- Scope: Enterprise Addons
- Source: enterprise/account_avatax
- Dependencies: [[docs/Community Addons/payment/payment|payment]], [[docs/Enterprise Addons/account_external_tax/account_external_tax|account_external_tax]]

## Generated coverage

- Models: 15
- XML files with UI/data artifacts: 9
- Views: 13
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 5
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
title Avatax - Generated Coverage
component "Module Overview" as overview
component "Models\n15" as models
component "Views / XML\n13 views\n9 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n5 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/account_avatax/Models|Models]] (15)
- Views and XML: [[docs/Enterprise Addons/account_avatax/Views|Views]] (9 files)

## Key models

- `account.avatax.unique.code`
- `account.chart.template`
- `account.external.tax.mixin`
- `account.fiscal.position`
- `account.move`
- `avatax.connection.test.result`
- `avatax.exemption`
- `avatax.validate.address`
- `product.avatax.category`
- `product.category`
- `product.product`
- `product.template`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


