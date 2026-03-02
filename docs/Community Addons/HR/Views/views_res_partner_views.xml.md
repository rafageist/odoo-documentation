<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/hr/hr|hr]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_partner_view_search`
- Name: res.partner.search.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_res_partner_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `res_partner_view_form`
- Name: res.partner.view.form.inherit.hr
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `div`
- Field references: 1
- Sample fields: `employees_count`
- Buttons: `action_open_employees`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/hr/Views]]

<!-- GENERATED:VIEWFILE -->
