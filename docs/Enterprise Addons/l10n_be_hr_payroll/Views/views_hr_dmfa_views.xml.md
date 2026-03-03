---
tags: [odoo, enterprise, generated, views]
---

# views/hr_dmfa_views.xml

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_dmfa_views.xml`
- Views: 3
- Actions: 2
- Menus: 3
- Rules: 0

## View records

### `l10n_be_dmfa_view_tree`
- Name: l10n_be.dmfa
- Model: `l10n_be.dmfa`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `quarter`, `reference`, `validation_state`, `year`
- XPath or positional patches: 0

### `l10n_be_dmfa_location_unit_view_tree`
- Name: l10n_be.dmfa.location.unit
- Model: `l10n_be.dmfa.location.unit`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `code`, `company_id`, `partner_id`
- XPath or positional patches: 0

### `l10n_be_dmfa_view_form`
- Name: l10n_be_hr_payroll.dmfa.report
- Model: `l10n_be.dmfa`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `declaration_type`, `dmfa_go`, `dmfa_go_filename`, `dmfa_pdf`, `dmfa_pdf_filename`, `dmfa_signature`, `dmfa_signature_filename`, `dmfa_xml`, `dmfa_xml_filename`, `error_message`, and 6 more
- Buttons: `action_create_onss_declaration`, `action_open_onss_declaration`, `generate_dmfa_pdf_report`, `generate_dmfa_xml_report`
- XPath or positional patches: 0

## Actions

- `hr_payslip_report_action_dmfa`: `act_window` DMFA
- `l10n_be_hr_payroll_action_work_address_codes`: `act_window` Work address DMFA codes

## Menus

- `menu_hr_payroll_dmfa`: unnamed
- `menu_l10n_be_dmfa_location_unit`: DMFA: Work Locations
- `menu_l10n_be_hr_payroll_configuration`: Belgium

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Views]]

