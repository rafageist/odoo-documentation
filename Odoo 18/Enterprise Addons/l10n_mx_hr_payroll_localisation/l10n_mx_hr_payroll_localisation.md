<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Mexico - Payroll - Localisation

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_mx_hr_payroll_localisation
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_mx_hr_payroll/l10n_mx_hr_payroll|l10n_mx_hr_payroll]]
## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 2

## Detected Models

- `HrContract`
- `HrPayrollStructure`
- `HrPayrollStructureType`
- `HrPayslip`
- `HrPayslipWorkedDays`
- `l10n.mx.hr.fonacot`
- `l10n.mx.hr.infonavit`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Mexico - Payroll - Localisation - Models and Relations
class HrContract
class HrPayrollStructure
class HrPayrollStructureType
class HrPayslip
class HrPayslipWorkedDays
class "l10n.mx.hr.fonacot" as l10n_mx_hr_fonacot
class "l10n.mx.hr.infonavit" as l10n_mx_hr_infonavit
HrContract --|> l10n_mx_hr_infonavit : one2many
HrContract --|> l10n_mx_hr_fonacot : one2many
class "hr.contract" as hr_contract
l10n_mx_hr_fonacot --> hr_contract : many2one
l10n_mx_hr_infonavit --> hr_contract : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
