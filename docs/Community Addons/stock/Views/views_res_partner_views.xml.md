---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_partner_stock_warnings_form`
- Name: res.partner.stock.warning
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `group`
- Field references: 1
- Sample fields: `picking_warn_msg`
- Buttons: `action_view_stock_serial`
- XPath or positional patches: 2

### `view_partner_stock_form`
- Name: res.partner.stock.property.form.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `mail.res_partner_view_form_inherit_mail`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `property_stock_customer`, `property_stock_supplier`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

