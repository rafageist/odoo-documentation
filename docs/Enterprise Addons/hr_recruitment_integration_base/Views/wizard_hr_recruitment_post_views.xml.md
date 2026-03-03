---
tags: [odoo, enterprise, generated, views]
---

# wizard/hr_recruitment_post_views.xml

- Module: [[docs/Enterprise Addons/hr_recruitment_integration_base/hr_recruitment_integration_base|hr_recruitment_integration_base]]
- Scope: Enterprise Addons
- Source file: `wizard/hr_recruitment_post_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `hr_recruitment_post_job_wizard_view_job_selectable_form`
- Name: hr.recruitment.post.job.wizard.job.selectable.form
- Model: `hr.recruitment.post.job.wizard`
- Type: inferred from arch
- Inherits: `hr_recruitment_integration_base.hr_recruitment_post_job_wizard_view_form`
- Root tag: `field`
- Field references: 1
- Sample fields: `job_id`
- XPath or positional patches: 0

### `hr_recruitment_post_job_wizard_view_form`
- Name: hr.recruitment.post.job.wizard.form
- Model: `hr.recruitment.post.job.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `campaign_end_date`, `campaign_start_date`, `date_from`, `industry_id`, `job_apply_mail`, `job_id`, `platform_ids`, `post_html`
- Buttons: `action_post_job`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_recruitment_integration_base/Views]]

