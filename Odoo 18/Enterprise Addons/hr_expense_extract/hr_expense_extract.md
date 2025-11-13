<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Hr Expense Extract

- Version: v18
- Category: enterprise
- Source: enterprise18/hr_expense_extract
- Dependencies: [[Odoo 18/Community Addons/hr_expense/hr_expense|hr_expense]], [[Odoo 18/Enterprise Addons/iap_extract/iap_extract|iap_extract]], [[Odoo 18/Community Addons/iap_mail/iap_mail|iap_mail]], [[Odoo 18/Enterprise Addons/mail_enterprise/mail_enterprise|mail_enterprise]], [[Odoo 18/Enterprise Addons/hr_expense_predict_product/hr_expense_predict_product|hr_expense_predict_product]]

## Summary

Extract data from expense scans to fill them automatically

## XML Artifacts (detected)

- Views: 7
- Actions: 3
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `hr.expense`
- `HrExpenseSheet`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Hr Expense Extract - Models and Relations
class "hr.expense" as hr_expense
class HrExpenseSheet
class ResCompany
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
