---
tags: [odoo, community, generated, views]
---

# views/res_partner_grade_views.xml

- Module: [[docs/Community Addons/partnership/partnership|partnership]]
- Scope: Community Addons
- Source file: `views/res_partner_grade_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_partner_grade_form`
- Name: res.partner.grade.form
- Model: `res.partner.grade`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `default_pricelist_id`, `name`, `partners_count`, `partners_label`
- Buttons: `partnership.action_grade_partners`
- XPath or positional patches: 0

### `res_partner_grade_view_search`
- Name: res.partner.grade.view.search
- Model: `res.partner.grade`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_partner_grade_tree`
- Name: res.partner.grade.list
- Model: `res.partner.grade`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `name`, `sequence`
- XPath or positional patches: 0

## Actions

- `res_partner_grade_action`: `act_window` Levels

## Navigation

- **Parent:** [[docs/Community Addons/partnership/Views]]

