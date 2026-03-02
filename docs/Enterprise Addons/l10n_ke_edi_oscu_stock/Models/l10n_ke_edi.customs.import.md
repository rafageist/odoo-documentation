<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_ke_edi.customs.import

- Module: [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/l10n_ke_edi_oscu_stock|l10n_ke_edi_oscu_stock]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/l10n_ke_edi_customs_import.py`
- Python classes: `L10n_Ke_EdiCustomsImport`
- Description: Kenya Customs Import
- Inherits: `mail.thread`

## Field footprint

- Detected fields: 21
- Field types: `Char` x 5, `Date` x 1, `Float` x 1, `Integer` x 2, `Json` x 1, `Many2one` x 9, `Selection` x 1, `Text` x 1
- Relation fields: 9

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `declaration_date`: `Date` (comodel `Declaration Date`)
- `declaration_number`: `Char` (comodel `Declaration Number`)
- `export_country_id`: `Many2one` (comodel `res.country`)
- `hs_code`: `Char` (comodel `HS Code`)
- `item_name`: `Char` (comodel `Item Name`)
- `item_seq`: `Integer` (comodel `Item Sequence`)
- `number_packages`: `Integer` (comodel `Number of Packages`)
- `origin_country_id`: `Many2one` (comodel `res.country`)
- `package_unit_code_id`: `Many2one` (comodel `l10n_ke_edi_oscu.code`)
- `partner_id`: `Many2one` (comodel `res.partner`)
- `product_id`: `Many2one` (comodel `product.product`)
- `purchase_id`: `Many2one` (comodel `purchase.order`)
- `quantity`: `Float` (comodel `Quantity`)
- `remark`: `Text` (comodel `Remark`)
- `state`: `Selection`
- `supplier_name`: `Char` (comodel `Vendor`)
- `task_code`: `Char` (comodel `Task Code`)
- `uom_code_id`: `Many2one` (comodel `l10n_ke_edi_oscu.code`)
- `uom_id`: `Many2one` (comodel `uom.uom`, compute `_compute_uom_id`)

## Method hints

- Detected methods: 11
- Action methods: `action_create_purchase_order`, `action_view_purchase_order`
- Compute methods: `_compute_uom_id`, `_compute_warning_msg`
- Onchange methods: none

## Direct relation diagram

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title l10n_ke_edi.customs.import - Direct Relations
class "l10n_ke_edi.customs.import" as l10n_ke_edi_customs_import
class "l10n_ke_edi_oscu.code" as l10n_ke_edi_oscu_code
class "product.product" as product_product
class "purchase.order" as purchase_order
class "res.company" as res_company
class "res.country" as res_country
class "res.partner" as res_partner
class "uom.uom" as uom_uom
l10n_ke_edi_customs_import --> res_country : origin_country_id
l10n_ke_edi_customs_import --> res_country : export_country_id
l10n_ke_edi_customs_import --> l10n_ke_edi_oscu_code : package_unit_code_id
l10n_ke_edi_customs_import --> l10n_ke_edi_oscu_code : uom_code_id
l10n_ke_edi_customs_import --> uom_uom : uom_id
l10n_ke_edi_customs_import --> product_product : product_id
l10n_ke_edi_customs_import --> res_company : company_id
l10n_ke_edi_customs_import --> purchase_order : purchase_id
l10n_ke_edi_customs_import --> res_partner : partner_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/Models]]

<!-- GENERATED:MODEL -->
