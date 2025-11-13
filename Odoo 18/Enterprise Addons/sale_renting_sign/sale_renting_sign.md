<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Rental/Sign Bridge

- Version: v18
- Category: enterprise
- Source: enterprise18/sale_renting_sign
- Dependencies: [[Odoo 18/Enterprise Addons/sign/sign|sign]], [[Odoo 18/Enterprise Addons/sale_renting/sale_renting|sale_renting]]

## Summary

Bridge Sign functionalities with the Rental application

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `ResCompany`
- `RentalOrder`
- `SignRequest`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Rental/Sign Bridge - Models and Relations
class ResCompany
class RentalOrder
class SignRequest
class "sign.template" as sign_template
ResCompany --> sign_template : many2one
class "sign.request" as sign_request
RentalOrder --|> sign_request : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
