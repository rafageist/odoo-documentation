---
tags: [odoo, enterprise, generated, views]
---

# views/hr_applicant_views.xml

- Module: [[docs/Enterprise Addons/hr_recruitment_extract/hr_recruitment_extract|hr_recruitment_extract]]
- Scope: Enterprise Addons
- Source file: `views/hr_applicant_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_recruitment_extract_view_list`
- Name: hr.applicant.extract.view.list
- Model: `hr.applicant`
- Type: inferred from arch
- Inherits: `hr_recruitment.crm_case_tree_view_job`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `extract_state_processed`
- XPath or positional patches: 2

### `hr_recruitment_extract_view_form`
- Name: hr.applicant.extract.view.form
- Model: `hr.applicant`
- Type: inferred from arch
- Inherits: `hr_recruitment.hr_applicant_view_form`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `extract_can_show_send_button`, `extract_document_uuid`, `extract_error_message`, `extract_state`, `is_in_extractable_state`
- Buttons: `action_manual_send_for_digitization`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_recruitment_extract/Views]]

