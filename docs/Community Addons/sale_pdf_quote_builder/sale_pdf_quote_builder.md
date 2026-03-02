<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sales PDF Quotation Builder

- Scope: Community Addons
- Source: odoo/addons/sale_pdf_quote_builder
- Dependencies: [[docs/Community Addons/sale_management/sale_management|sale_management]]

## XML Artifacts (detected)

- Views: 10
- Actions: 3
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 4

## Detected Models

- `IrActionsReport`
- `ProductDocument`
- `quotation.document`
- `SaleOrder`
- `SaleOrderLine`
- `SaleOrderTemplate`
- `sale.pdf.form.field`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Sales PDF Quotation Builder - Models and Relations
class IrActionsReport
class ProductDocument
class "quotation.document" as quotation_document
class SaleOrder
class SaleOrderLine
class SaleOrderTemplate
class "sale.pdf.form.field" as sale_pdf_form_field
ProductDocument .. sale_pdf_form_field : many2many
class "ir.attachment" as ir_attachment
quotation_document --> ir_attachment : many2one
class "sale.order.template" as sale_order_template
quotation_document .. sale_order_template : many2many
quotation_document .. sale_pdf_form_field : many2many
SaleOrder .. quotation_document : many2many
SaleOrder .. quotation_document : many2many
class "product.document" as product_document
SaleOrderLine .. product_document : many2many
SaleOrderLine .. product_document : many2many
SaleOrderTemplate .. quotation_document : many2many
sale_pdf_form_field .. product_document : many2many
sale_pdf_form_field .. quotation_document : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




