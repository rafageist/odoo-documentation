<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/mrp_views.xml

- Module: [[docs/Enterprise Addons/mrp_maintenance/mrp_maintenance|mrp_maintenance]]
- Scope: Enterprise Addons
- Source file: `views/mrp_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `mrp_production_view_form_inherit_maintenance`
- Name: mrp.production.view.form.inherit.maintenance
- Model: `mrp.production`
- Type: inferred from arch
- Inherits: `mrp.mrp_production_form_view`
- Root tag: `div`
- Field references: 1
- Sample fields: `maintenance_count`
- Buttons: `open_maintenance_request_mo`
- XPath or positional patches: 1

### `mrp_workcenter_view_kanban_inherit_maintenance`
- Name: mrp.workcenter.view.kanban.inherit.maintenance
- Model: `mrp.workcenter`
- Type: inferred from arch
- Inherits: `mrp.mrp_workcenter_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `mrp_workcenter_view_form_inherit_maintenance`
- Name: mrp.workcenter.form.inherit.maintenance
- Model: `mrp.workcenter`
- Type: inferred from arch
- Inherits: `mrp.mrp_workcenter_view`
- Root tag: `xpath`
- Field references: 12
- Sample fields: `category_id`, `effective_date`, `equipment_ids`, `estimated_next_failure`, `expected_mtbf`, `latest_failure_date`, `maintenance_open_count`, `maintenance_team_id`, `mtbf`, `mttr`, and 2 more
- Buttons: `%(mrp_workcenter_request_action_from_workcenter)d`
- XPath or positional patches: 3

## Actions

- `action_production_maintenance_request`: `server` Maintenance Request
- `mrp_workcenter_request_action_from_workcenter`: `act_window` Maintenance Requests

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_maintenance/Views]]

<!-- GENERATED:VIEWFILE -->
