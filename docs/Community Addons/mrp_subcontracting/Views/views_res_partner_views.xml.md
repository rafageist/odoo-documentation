<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/mrp_subcontracting/mrp_subcontracting|mrp_subcontracting]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_partner_mrp_subcontracting_filter`
- Name: res.partner.select.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_res_partner_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_partner_mrp_subcontracting_form`
- Name: res.partner.mrp_subcontracting.property.form.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `stock.view_partner_stock_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `property_stock_subcontractor`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/mrp_subcontracting/Views]]

<!-- GENERATED:VIEWFILE -->
