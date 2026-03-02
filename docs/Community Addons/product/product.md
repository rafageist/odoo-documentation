<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Products & Pricelists

- Scope: Community Addons
- Source: odoo/addons/product
- Dependencies: base (not documented), [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/uom/uom|uom]]

## XML Artifacts (detected)

- Views: 60
- Actions: 24
- Menus: 0
- Rules (ir.rule): 6
- Access CSV entries: 38

## Detected Models

- `IrAttachment`
- `product.attribute`
- `product.attribute.custom.value`
- `product.attribute.value`
- `product.category`
- `product.combo`
- `product.combo.item`
- `product.document`
- `product.pricelist`
- `product.pricelist.item`
- `product.product`
- `product.supplierinfo`
- `product.tag`
- `product.template`
- `product.template.attribute.exclusion`
- `product.template.attribute.line`
- `product.template.attribute.value`
- `product.uom`
- `ResCompany`
- `ResCountryGroup`
- `ResCurrency`
- `ResPartner`
- `UomUom`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Products & Pricelists - Models and Relations
class IrAttachment
class "product.attribute" as product_attribute
class "product.attribute.custom.value" as product_attribute_custom_value
class "product.attribute.value" as product_attribute_value
class "product.category" as product_category
class "product.combo" as product_combo
class "product.combo.item" as product_combo_item
class "product.document" as product_document
class "product.pricelist" as product_pricelist
class "product.pricelist.item" as product_pricelist_item
class "product.product" as product_product
class "product.supplierinfo" as product_supplierinfo
class "product.tag" as product_tag
class "product.template" as product_template
class "product.template.attribute.exclusion" as product_template_attribute_exclusion
class "product.template.attribute.line" as product_template_attribute_line
class "product.template.attribute.value" as product_template_attribute_value
class "product.uom" as product_uom
class ResCompany
class ResCountryGroup
class ResCurrency
class ResPartner
class UomUom
product_attribute --|> product_attribute_value : one2many
product_attribute --|> product_template_attribute_value : one2many
product_attribute --|> product_template_attribute_line : one2many
product_attribute .. product_template : many2many
product_attribute_custom_value --> product_template_attribute_value : many2one
product_attribute_value --> product_attribute : many2one
product_attribute_value .. product_template_attribute_line : many2many
product_category --> product_category : many2one
product_category --|> product_category : one2many
class "res.company" as res_company
product_combo --> res_company : many2one
product_combo --|> product_combo_item : one2many
class "res.currency" as res_currency
product_combo --> res_currency : many2one
product_combo_item --> product_combo : many2one
product_combo_item --> product_product : many2one
product_combo_item --> res_currency : many2one
class "ir.attachment" as ir_attachment
product_document --> ir_attachment : many2one
product_pricelist --> res_currency : many2one
product_pricelist --> res_company : many2one
class "res.country.group" as res_country_group
product_pricelist .. res_country_group : many2many
product_pricelist --|> product_pricelist_item : one2many
product_pricelist_item --> product_pricelist : many2one
product_pricelist_item --> res_company : many2one
product_pricelist_item --> res_currency : many2one
product_pricelist_item --> product_category : many2one
product_pricelist_item --> product_template : many2one
product_pricelist_item --> product_product : many2one
product_pricelist_item --> product_pricelist : many2one
product_product --> product_template : many2one
product_product --|> product_uom : one2many
product_product .. product_template_attribute_value : many2many
product_product .. product_template_attribute_value : many2many
product_product --|> product_pricelist_item : one2many
product_product --|> product_document : one2many
product_product .. product_tag : many2many
product_product .. product_tag : many2many
class "res.partner" as res_partner
product_supplierinfo --> res_partner : many2one
class "uom.uom" as uom_uom
product_supplierinfo --> uom_uom : many2one
product_supplierinfo --> res_company : many2one
product_supplierinfo --> res_currency : many2one
product_supplierinfo --> product_product : many2one
product_supplierinfo --> product_template : many2one
product_tag .. product_template : many2many
product_tag .. product_product : many2many
product_tag .. product_product : many2many
product_template .. product_combo : many2many
product_template --> product_category : many2one
product_template --> res_currency : many2one
product_template --> res_currency : many2one
product_template --> uom_uom : many2one
product_template .. uom_uom : many2many
product_template --> res_company : many2one
product_template --|> product_supplierinfo : one2many
product_template --|> product_supplierinfo : one2many
product_template --|> product_template_attribute_line : one2many
product_template .. product_template_attribute_line : many2many
product_template --|> product_product : one2many
product_template --> product_product : many2one
product_template --|> product_pricelist_item : one2many
product_template --|> product_document : one2many
product_template .. product_tag : many2many
product_template_attribute_exclusion --> product_template_attribute_value : many2one
product_template_attribute_exclusion --> product_template : many2one
product_template_attribute_exclusion .. product_template_attribute_value : many2many
product_template_attribute_line --> product_template : many2one
product_template_attribute_line --> product_attribute : many2one
product_template_attribute_line .. product_attribute_value : many2many
product_template_attribute_line --|> product_template_attribute_value : one2many
product_template_attribute_value --> product_attribute_value : many2one
product_template_attribute_value --> product_template_attribute_line : many2one
product_template_attribute_value --|> product_template_attribute_exclusion : one2many
product_template_attribute_value .. product_product : many2many
product_uom --> uom_uom : many2one
product_uom --> product_product : many2one
product_uom --> res_company : many2one
ResCountryGroup .. product_pricelist : many2many
ResPartner --> product_pricelist : many2one
ResPartner --> product_pricelist : many2one
UomUom --|> product_uom : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





