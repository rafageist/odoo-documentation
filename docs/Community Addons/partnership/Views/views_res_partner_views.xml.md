<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/partnership/partnership|partnership]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_res_partner_form`
- Name: res.partner.relation
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `grade_id`, `vat`
- XPath or positional patches: 0

### `view_res_partner_grade_tree`
- Name: res.partner.inherit.list
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `grade_id`, `vat`
- XPath or positional patches: 0

### `view_res_partner_filter_assign`
- Name: res.partner.inherit.search
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_res_partner_filter`
- Root tag: `field`
- Field references: 3
- Sample fields: `grade_id`, `specific_property_product_pricelist`, `user_id`
- XPath or positional patches: 1

## Actions

- `action_grade_partners`: `act_window` Members / Partners
- `action_pricelist_partners`: `act_window` Members / Partners

## Navigation

- **Parent:** [[docs/Community Addons/partnership/Views]]

<!-- GENERATED:VIEWFILE -->
