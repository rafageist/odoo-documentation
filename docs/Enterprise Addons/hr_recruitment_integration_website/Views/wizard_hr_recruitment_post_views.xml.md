<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# wizard/hr_recruitment_post_views.xml

- Module: [[docs/Enterprise Addons/hr_recruitment_integration_website/hr_recruitment_integration_website|hr_recruitment_integration_website]]
- Scope: Enterprise Addons
- Source file: `wizard/hr_recruitment_post_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_recruitment_post_job_wizard_view_form`
- Name: hr.recruitment.post.job.wizard.form
- Model: `hr.recruitment.post.job.wizard`
- Type: inferred from arch
- Inherits: `hr_recruitment_integration_base.hr_recruitment_post_job_wizard_view_form`
- Root tag: `field`
- Field references: 5
- Sample fields: `apply_method`, `job_apply_mail`, `job_apply_url`, `platform_ids`, `post_html`
- Buttons: `action_generate_post`
- XPath or positional patches: 1

## Actions

- `hr_recruitment_post_job_wizard_action_regenerate_post`: `server` Regenerate Post

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_recruitment_integration_website/Views]]

<!-- GENERATED:VIEWFILE -->
