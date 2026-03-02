<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/worksheet_template_view.xml

- Module: [[docs/Enterprise Addons/worksheet/worksheet|worksheet]]
- Scope: Enterprise Addons
- Source file: `views/worksheet_template_view.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `worksheet_template_view_search`
- Name: worksheet.template.view.search
- Model: `worksheet.template`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `company_id`, `name`
- XPath or positional patches: 0

### `worksheet_template_view_list`
- Name: worksheet.template.view.list
- Model: `worksheet.template`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `company_id`, `name`, `sequence`, `worksheet_count`
- Buttons: `action_analysis_report`
- XPath or positional patches: 0

### `worksheet_template_view_form`
- Name: worksheet.template.view.form
- Model: `worksheet.template`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `active`, `company_id`, `model_id`, `name`, `res_model`, `worksheet_count`
- Buttons: `action_analysis_report`, `action_view_worksheets`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/worksheet/Views]]

<!-- GENERATED:VIEWFILE -->
