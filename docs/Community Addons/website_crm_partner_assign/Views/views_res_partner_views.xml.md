<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/website_crm_partner_assign/website_crm_partner_assign|website_crm_partner_assign]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_crm_partner_assign_form`
- Name: res.partner.assign.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base_geolocalize.view_crm_partner_geo_form`
- Root tag: `data`
- Field references: 6
- Sample fields: `activation`, `assigned_partner_id`, `date_partnership`, `date_review`, `date_review_next`, `partner_weight`
- XPath or positional patches: 2

### `view_res_partner_filter_assign_tree`
- Name: res.partner.geo.inherit.list
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `activation`, `date_review_next`, `vat`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/website_crm_partner_assign/Views]]

<!-- GENERATED:VIEWFILE -->
