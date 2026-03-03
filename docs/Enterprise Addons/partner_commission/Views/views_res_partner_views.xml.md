---
tags: [odoo, enterprise, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Enterprise Addons/partner_commission/partner_commission|partner_commission]]
- Scope: Enterprise Addons
- Source file: `views/res_partner_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_crm_partner_assign_form_inherit_partner_commission`
- Name: res.partner.form.partner.commission
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `website_crm_partner_assign.view_crm_partner_assign_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `activation`, `commission_plan_id`
- XPath or positional patches: 0

### `view_partner_grade_tree_inherit_partner_commission`
- Name: res.partner.grade.tree.partner.commission
- Model: `res.partner.grade`
- Type: inferred from arch
- Inherits: `partnership.view_partner_grade_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `default_commission_plan_id`
- XPath or positional patches: 1

### `view_partner_grade_form_inherit_partner_commission`
- Name: res.partner.grade.form.partner.commission
- Model: `res.partner.grade`
- Type: inferred from arch
- Inherits: `website_crm_partner_assign.view_partner_grade_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `default_commission_plan_id`, `partner_weight`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/partner_commission/Views]]

