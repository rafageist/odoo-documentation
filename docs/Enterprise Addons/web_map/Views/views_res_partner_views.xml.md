<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Enterprise Addons/web_map/web_map|web_map]]
- Scope: Enterprise Addons
- Source file: `views/res_partner_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_res_partner_filter_inherit_map`
- Name: res.partner.search.inherit.map
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_res_partner_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `contact_address_complete`
- XPath or positional patches: 1

### `res_partner_view_form_inherit_map`
- Name: res.partner.form.inherit.map
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `sheet`
- Field references: 2
- Sample fields: `partner_latitude`, `partner_longitude`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/web_map/Views]]

<!-- GENERATED:VIEWFILE -->
