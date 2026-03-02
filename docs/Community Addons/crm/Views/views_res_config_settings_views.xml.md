<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_config_settings_views.xml

- Module: [[docs/Community Addons/crm/crm|crm]]
- Scope: Community Addons
- Source file: `views/res_config_settings_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `res_config_settings_view_form`
- Name: res.config.settings.view.form.inherit.crm
- Model: `res.config.settings`
- Type: inferred from arch
- Inherits: `base.res_config_settings_view_form`
- Root tag: `xpath`
- Field references: 17
- Sample fields: `crm_auto_assignment_action`, `crm_auto_assignment_interval_number`, `crm_auto_assignment_interval_type`, `crm_auto_assignment_run_datetime`, `crm_use_auto_assignment`, `group_use_lead`, `group_use_recurring_revenues`, `is_membership_multi`, `lead_enrich_auto`, `module_crm_iap_enrich`, and 7 more
- Buttons: `%(crm_lead_pls_update_action)d`, `action_crm_assign_leads`, `crm.crm_recurring_plan_action`
- XPath or positional patches: 1

## Actions

- `crm_config_settings_action`: `act_window` Settings

## Navigation

- **Parent:** [[docs/Community Addons/crm/Views]]

<!-- GENERATED:VIEWFILE -->
