<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/base_automation_views.xml

- Module: [[docs/Community Addons/base_automation/base_automation|base_automation]]
- Scope: Community Addons
- Source file: `views/base_automation_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_base_automation_search`
- Name: base.automation.search
- Model: `base.automation`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `model_id`, `name`
- XPath or positional patches: 0

### `view_base_automation_kanban`
- Name: base.automation.kanban
- Model: `base.automation`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 14
- Sample fields: `action_server_ids`, `active`, `model_id`, `name`, `on_change_field_ids`, `trg_date_calendar_id`, `trg_date_id`, `trg_date_range`, `trg_date_range_mode`, `trg_date_range_type`, and 4 more
- XPath or positional patches: 0

### `view_base_automation_tree`
- Name: base.automation.list
- Model: `base.automation`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `model_id`, `name`, `trigger`
- XPath or positional patches: 0

### `view_base_automation_form`
- Name: Automations
- Model: `base.automation`
- Type: inferred from arch
- Root tag: `form`
- Field references: 23
- Sample fields: `action_server_ids`, `active`, `description`, `filter_domain`, `filter_pre_domain`, `log_webhook_calls`, `model_id`, `model_name`, `name`, `on_change_field_ids`, and 13 more
- Buttons: `action_open_scheduled_action`, `action_rotate_webhook_uuid`, `action_view_webhook_logs`
- XPath or positional patches: 0

## Actions

- `base_automation_act`: `act_window` Automation Rules

## Menus

- `menu_base_automation_form`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/base_automation/Views]]

<!-- GENERATED:VIEWFILE -->
