<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_payslip_views.xml

- Module: [[docs/Enterprise Addons/l10n_mx_hr_payroll_account_edi/l10n_mx_hr_payroll_account_edi|l10n_mx_hr_payroll_account_edi]]
- Scope: Enterprise Addons
- Source file: `views/hr_payslip_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_mx_hr_payslip_view_form`
- Name: hr.payslip.inherit.form
- Model: `hr.payslip`
- Type: inferred from arch
- Inherits: `hr_payroll_account.hr_payslip_view_form`
- Root tag: `button`
- Field references: 13
- Sample fields: `attachment_origin`, `attachment_uuid`, `cancellation_reason`, `datetime`, `l10n_mx_edi_cfdi_cancel_id`, `l10n_mx_edi_cfdi_origin`, `l10n_mx_edi_cfdi_sat_state`, `l10n_mx_edi_cfdi_state`, `l10n_mx_edi_cfdi_uuid`, `l10n_mx_edi_document_ids`, and 3 more
- Buttons: `action_cancel`, `action_download_file`, `action_download_payment_receipt`, `action_force_payment_cfdi`, `action_generate_cfdi`, `action_payslip_done`, `action_print_cfdi`, `action_print_payslip`, `action_retry`, `action_show_document`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_hr_payroll_account_edi/Views]]

<!-- GENERATED:VIEWFILE -->
