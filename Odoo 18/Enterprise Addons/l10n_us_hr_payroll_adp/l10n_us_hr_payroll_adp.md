<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# United States - Payroll - Export to ADP

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_us_hr_payroll_adp
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_us_hr_payroll/l10n_us_hr_payroll|l10n_us_hr_payroll]]

## Summary

Export Work Entries to ADP

## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `HrEmployee`
- `l10n.us.adp.export`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title United States - Payroll - Export to ADP - Models and Relations
class HrEmployee
class "l10n.us.adp.export" as l10n_us_adp_export
class ResCompany
class "res.company" as res_company
l10n_us_adp_export --> res_company : many2one
class "hr.employee" as hr_employee
l10n_us_adp_export .. hr_employee : many2many
class "hr.work.entry" as hr_work_entry
l10n_us_adp_export .. hr_work_entry : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
