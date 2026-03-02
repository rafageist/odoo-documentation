
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Commission in Payslips

- Scope: Enterprise Addons
- Source: enterprise/hr_payroll_sale_commission
- Dependencies: [[docs/Enterprise Addons/sale_commission/sale_commission|sale_commission]], [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]

## Summary

Autofill employee commission

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `SaleCommissionPlan`
- `HrPayslip`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Commission in Payslips - Models and Relations
class SaleCommissionPlan
class HrPayslip
class "hr.payslip.input.type" as hr_payslip_input_type
SaleCommissionPlan --> hr_payslip_input_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

