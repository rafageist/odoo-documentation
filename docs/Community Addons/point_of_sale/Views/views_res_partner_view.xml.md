<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_partner_view.xml

- Module: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
- Scope: Community Addons
- Source file: `views/res_partner_view.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_partner_property_form`
- Name: res.partner.pos.form.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `div`
- Field references: 2
- Sample fields: `barcode`, `pos_order_count`
- Buttons: `action_view_pos_order`
- XPath or positional patches: 2

## Actions

- `res_partner_action_edit_pos`: `act_window` Edit Partner

## Navigation

- **Parent:** [[docs/Community Addons/point_of_sale/Views]]

<!-- GENERATED:VIEWFILE -->
