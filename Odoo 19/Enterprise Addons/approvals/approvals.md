<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Approvals

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/approvals
- Dependencies: [[Odoo 19/Community Addons/mail/mail|mail]], [[Odoo 19/Community Addons/hr/hr|hr]], [[Odoo 19/Community Addons/product/product|product]]

## Summary

Create and validate approvals requests

## XML Artifacts (detected)

- Views: 13
- Actions: 11
- Menus: 12
- Rules (ir.rule): 17
- Access CSV entries: 14

## Detected Models

- `approval.approver`
- `approval.category`
- `approval.category.approver`
- `approval.product.line`
- `approval.request`
- `IrAttachment`
- `MailActivity`
- `MailActivityType`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Approvals - Models and Relations
class "approval.approver" as approval_approver
class "approval.category" as approval_category
class "approval.category.approver" as approval_category_approver
class "approval.product.line" as approval_product_line
class "approval.request" as approval_request
class IrAttachment
class MailActivity
class MailActivityType
class "res.users" as res_users
approval_approver --> res_users : many2one
approval_approver .. res_users : many2many
approval_approver --> approval_request : many2one
class "res.company" as res_company
approval_category --> res_company : many2one
approval_category .. res_users : many2many
approval_category --|> approval_category_approver : one2many
class "ir.sequence" as ir_sequence
approval_category --> ir_sequence : many2one
approval_category_approver --> approval_category : many2one
approval_category_approver --> res_company : many2one
approval_category_approver --> res_users : many2one
approval_category_approver .. res_users : many2many
approval_product_line --> approval_request : many2one
class "product.product" as product_product
approval_product_line --> product_product : many2one
class "uom.uom" as uom_uom
approval_product_line --> uom_uom : many2one
approval_request --> approval_category : many2one
approval_request --|> approval_approver : one2many
approval_request .. res_users : many2many
class "res.partner" as res_partner
approval_request --> res_partner : many2one
approval_request --> res_users : many2one
class "ir.attachment" as ir_attachment
approval_request --|> ir_attachment : one2many
approval_request --|> approval_product_line : one2many
MailActivity --> approval_request : many2one
MailActivity --> approval_approver : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

