---
tags: [odoo, enterprise, generated, views]
---

# views/worksheet_template_views.xml

- Module: [[docs/Enterprise Addons/industry_fsm_report/industry_fsm_report|industry_fsm_report]]
- Scope: Enterprise Addons
- Source file: `views/worksheet_template_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_worksheet_template_kanban`
- Name: worksheet.template.kanban
- Model: `worksheet.template`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `company_id`, `name`, `sequence`, `worksheet_count`
- XPath or positional patches: 0

### `worksheet_template_view_form_inherit_fsm_report`
- Name: worksheet.template.view.form.inherit.fsm.report
- Model: `worksheet.template`
- Type: inferred from arch
- Inherits: `worksheet.worksheet_template_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `worksheet_template_view_form_footer_design_button`
- Name: worksheet.template.view.form.no_design_button
- Model: `worksheet.template`
- Type: inferred from arch
- Inherits: `worksheet.worksheet_template_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 4

## Actions

- `fsm_worksheets_action_settings`: `act_window` Worksheet Templates
- `action_fsm_worksheets`: `act_window` Worksheet Templates

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm_report/Views]]

