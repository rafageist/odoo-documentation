<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_hk_ird_views.xml

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll/l10n_hk_hr_payroll|l10n_hk_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_hk_ird_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_hk_ird_view_list`
- Name: l10n_hk.ird.view.list
- Model: `l10n_hk.ird`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_payroll_declaration_mixin_view_list`
- Root tag: `field`
- Field references: 2
- Sample fields: `display_name`, `year`
- XPath or positional patches: 0

### `l10n_hk_ird_view_form`
- Name: l10n_hk_ird.view.form
- Model: `l10n_hk.ird`
- Type: inferred from arch
- Inherits: `hr_payroll.hr_payroll_declaration_mixin_view_form`
- Root tag: `group`
- Field references: 11
- Sample fields: `designation_of_signer`, `error_message`, `name_of_signer`, `pdf_error`, `start_month`, `start_year`, `submission_date`, `type_of_form`, `xml_file`, `xml_validation_state`, and 1 more
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
