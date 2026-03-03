---
tags: [odoo, enterprise, generated, views]
---

# views/hr_recruitment_views.xml

- Module: [[docs/Enterprise Addons/hr_referral/hr_referral|hr_referral]]
- Scope: Enterprise Addons
- Source file: `views/hr_recruitment_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_recruitment_stage_form_inherit_referral`
- Name: hr.recruitment.stage.form.inherit.referral
- Model: `hr.recruitment.stage`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_recruitment_stage_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `points`, `use_in_referral`
- XPath or positional patches: 1

### `hr_recruitment_stage_tree_inherit_referral`
- Name: hr.recruitment.stage.list.inherit.referral
- Model: `hr.recruitment.stage`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_recruitment_stage_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `points`, `use_in_referral`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_referral/Views]]

