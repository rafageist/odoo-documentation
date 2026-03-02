<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Belgium - Payroll - Dimona - Automation

- Scope: Enterprise Addons
- Source: enterprise/l10n_be_hr_payroll_dimona_auto
- Dependencies: [[docs/Enterprise Addons/l10n_be_hr_payroll_dimona/l10n_be_hr_payroll_dimona|l10n_be_hr_payroll_dimona]], [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]

## XML Artifacts (detected)

- Views: 12
- Actions: 10
- Menus: 3
- Rules (ir.rule): 3
- Access CSV entries: 3

## Detected Models

- `HrEmployee`
- `HrVersion`
- `l10n.be.dimona.declaration`
- `l10n.be.dimona.period`
- `l10n.be.dimona.relation`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Belgium - Payroll - Dimona - Automation - Models and Relations
class HrEmployee
class HrVersion
class "l10n.be.dimona.declaration" as l10n_be_dimona_declaration
class "l10n.be.dimona.period" as l10n_be_dimona_period
class "l10n.be.dimona.relation" as l10n_be_dimona_relation
HrEmployee --> l10n_be_dimona_relation : many2one
HrVersion --> l10n_be_dimona_declaration : many2one
HrVersion --> l10n_be_dimona_declaration : many2one
class "res.company" as res_company
l10n_be_dimona_declaration --> res_company : many2one
class "hr.employee" as hr_employee
l10n_be_dimona_declaration --> hr_employee : many2one
class "hr.version" as hr_version
l10n_be_dimona_declaration --> hr_version : many2one
l10n_be_dimona_declaration --> l10n_be_dimona_period : many2one
l10n_be_dimona_period --> res_company : many2one
l10n_be_dimona_period --> l10n_be_dimona_relation : many2one
l10n_be_dimona_period --|> l10n_be_dimona_declaration : one2many
l10n_be_dimona_period --> hr_employee : many2one
l10n_be_dimona_relation --> res_company : many2one
l10n_be_dimona_relation --|> l10n_be_dimona_period : one2many
l10n_be_dimona_relation --> hr_employee : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


