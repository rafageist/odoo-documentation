<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# eCommerce

- Scope: Community Addons
- Source: odoo/addons/website_sale
- Dependencies: [[docs/Community Addons/website/website|website]], [[docs/Community Addons/sale/sale|sale]], [[docs/Community Addons/website_payment/website_payment|website_payment]], [[docs/Community Addons/website_mail/website_mail|website_mail]], [[docs/Community Addons/portal_rating/portal_rating|portal_rating]], [[docs/Community Addons/digest/digest|digest]], [[docs/Community Addons/delivery/delivery|delivery]], [[docs/Community Addons/html_builder/html_builder|html_builder]]

## Summary

Sell your products online

## Generated coverage

- Models: 34
- XML files with UI/data artifacts: 23
- Views: 56
- Actions: 28
- Menus: 24
- Rules (ir.rule): 6
- Access CSV entries: 67
- Controller units: 11
- Frontend asset files: 115

## Module map

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
title eCommerce - Generated Coverage
component "Module Overview" as overview
component "Models\n34" as models
component "Views / XML\n56 views\n23 files" as views
component "Controllers\n57 routes" as controllers
component "Frontend\n115 files" as frontend
component "Security / Data\n6 rules\n67 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_sale/Models|Models]] (34)
- Views and XML: [[docs/Community Addons/website_sale/Views|Views]] (23 files)
- Controllers: [[docs/Community Addons/website_sale/Controllers|Controllers]] (11)
- Frontend: [[docs/Community Addons/website_sale/Frontend|Frontend]] (115 files)

## Key models

- `account.move`
- `crm.team`
- `delivery.carrier`
- `digest.digest`
- `ir.http`
- `payment.token`
- `product.attribute`
- `product.document`
- `product.feed`
- `product.image`
- `product.pricelist`
- `product.pricelist.item`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




## Curated analysis

### Functional role
- `website_sale` is the public commerce layer that turns products, prices, delivery methods, and payment-ready orders into a storefront experience.
- It is not just a website skin over `sale`; it adds website-specific pricing, checkout steps, product feeds, ribbons, visitor tracking, and cart/session behavior.

### Operational footprint
- The controller layer is broad: cart, checkout, delivery, payment, variant resolution, product configurator, reorder, and feeds each have their own entry point.
- The model layer extends both website and sales concepts, especially around `website.py`, `sale_order.py`, pricelists, and product presentation metadata.

### Evidence
- Source files: `odoo19/addons/website_sale/controllers/cart.py`, `odoo19/addons/website_sale/controllers/payment.py`, `odoo19/addons/website_sale/models/website.py`, `odoo19/addons/website_sale/models/sale_order.py`
- UI and frontend: `odoo19/addons/website_sale/views/templates.xml`, `odoo19/addons/website_sale/views/website_views.xml`, `odoo19/addons/website_sale/models/product_pricelist.py`
- Tests: `odoo19/addons/website_sale/tests/test_address.py`, `odoo19/addons/website_sale/tests/test_website_sale_pricelist.py`, `odoo19/addons/website_sale/tests/test_website_sale_product_configurator.py`

### Related notes
- `[[docs/Community Addons/sale_management/sale_management|sale_management]]`
- `[[docs/Community Addons/website/website|website]]`

### Risks and follow-up
- Anonymous sessions, multi-company pricelists, taxes, and delivery costs interact in checkout, so storefront bugs often trace back to configuration rather than controller code alone.
- Product configurator and pricing behavior should always be tested with the same website, fiscal position, and visitor state that production users will actually have.
- Legacy comparison backlog was retired on 2026-03-02; keep this note focused on the current codebase.

