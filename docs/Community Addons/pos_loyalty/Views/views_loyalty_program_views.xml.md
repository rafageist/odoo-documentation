<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/loyalty_program_views.xml

- Module: [[docs/Community Addons/pos_loyalty/pos_loyalty|pos_loyalty]]
- Scope: Community Addons
- Source file: `views/loyalty_program_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `loyalty_program_view_tree_inherit_pos_loyalty`
- Name: loyalty.program.view.list.inherit.pos.loyalty
- Model: `loyalty.program`
- Type: inferred from arch
- Inherits: `loyalty.loyalty_program_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `company_id`, `pos_config_ids`
- XPath or positional patches: 0

### `loyalty_program_view_form_inherit_pos_loyalty`
- Name: loyalty.program.view.form.inherit.pos.loyalty
- Model: `loyalty.program`
- Type: inferred from arch
- Inherits: `loyalty.loyalty_program_view_form`
- Root tag: `field`
- Field references: 4
- Sample fields: `mail_template_id`, `pos_config_ids`, `pos_ok`, `pos_report_print_id`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Community Addons/pos_loyalty/Views]]

<!-- GENERATED:VIEWFILE -->
