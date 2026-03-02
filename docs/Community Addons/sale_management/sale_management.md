<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sales

- Scope: Community Addons
- Source: odoo/addons/sale_management
- Dependencies: [[docs/Community Addons/sale/sale|sale]], [[docs/Community Addons/digest/digest|digest]]

## Summary

From quotations to invoices

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 5

## Detected Models

- `DigestDigest`
- `ResCompany`
- `SaleOrder`
- `SaleOrderLine`
- `sale.order.template`
- `sale.order.template.line`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Sales - Models and Relations
class DigestDigest
class ResCompany
class SaleOrder
class SaleOrderLine
class "sale.order.template" as sale_order_template
class "sale.order.template.line" as sale_order_template_line
ResCompany --> sale_order_template : many2one
SaleOrder --> sale_order_template : many2one
class "res.company" as res_company
sale_order_template --> res_company : many2one
class "mail.template" as mail_template
sale_order_template --> mail_template : many2one
sale_order_template --|> sale_order_template_line : one2many
class "account.journal" as account_journal
sale_order_template --> account_journal : many2one
sale_order_template_line --> sale_order_template : many2one
class "product.product" as product_product
sale_order_template_line --> product_product : many2one
class "uom.uom" as uom_uom
sale_order_template_line .. uom_uom : many2many
sale_order_template_line --> uom_uom : many2one
sale_order_template_line --> sale_order_template_line : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




## Curated analysis

### Functional role
- Turns the lower-level `sale` module into the app-facing sales workspace with quotation templates, digest metrics, and portal refinements for commercial teams.
- The dedicated template models let teams standardize optional products, descriptions, and invoicing defaults before an order is confirmed.

### Operational footprint
- Core logic lives in `sale_order.py`, `sale_order_line.py`, and the template models; these files shape how commercial defaults reach the quotation.
- Security is not trivial: `security/sale_management_security.xml` adds a template-specific group and company rule, while portal templates extend the customer-facing order review.

### Evidence
- Source files: `odoo19/addons/sale_management/models/sale_order.py`, `odoo19/addons/sale_management/models/sale_order_template.py`, `odoo19/addons/sale_management/models/res_config_settings.py`
- UI and security: `odoo19/addons/sale_management/views/sale_order_template_views.xml`, `odoo19/addons/sale_management/views/sale_order_views.xml`, `odoo19/addons/sale_management/security/sale_management_security.xml`
- Tests: `odoo19/addons/sale_management/tests/test_sale_order.py`, `odoo19/addons/sale_management/tests/test_sale_ui.py`

### Related notes
- `[[docs/Community Addons/sale/sale|sale]]`
- `[[docs/Community Addons/website_sale/website_sale|website_sale]]`

### Risks and follow-up
- Template-heavy deployments need strong pricing governance because pricelists, optional products, and journal defaults interact before the user notices inconsistencies.
- Portal customizations should be validated together with `website_sale` and payment flows when the sales channel is public-facing.
- Legacy comparison backlog was retired on 2026-03-02; keep this note focused on the current codebase.


