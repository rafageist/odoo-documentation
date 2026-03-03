---
tags: [odoo, enterprise, generated, views]
---

# views/mrp_eco_views.xml

- Module: [[docs/Enterprise Addons/mrp_plm/mrp_plm|mrp_plm]]
- Scope: Enterprise Addons
- Source file: `views/mrp_eco_views.xml`
- Views: 16
- Actions: 10
- Menus: 14
- Rules: 0

## View records

### `mrp_eco_tag_view_tree`
- Name: mrp.eco.tag.view.list
- Model: `mrp.eco.tag`
- Type: inferred from arch
- Root tag: `list`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `mrp_eco_tag_view_search`
- Name: mrp.ecp.tag.view.search
- Model: `mrp.eco.tag`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `mrp_eco_stage_view_form`
- Name: mrp.eco.stage.view.form
- Model: `mrp.eco.stage`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `allow_apply_change`, `approval_template_ids`, `approval_type`, `description`, `final_stage`, `folded`, `legend_blocked`, `legend_done`, `legend_normal`, `name`, and 3 more
- XPath or positional patches: 0

### `view_mrp_eco_stage_kanban`
- Name: mrp.eco.stage.kanban
- Model: `mrp.eco.stage`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `mrp_eco_stage_view_tree`
- Name: mrp.eco.stage.view.list
- Model: `mrp.eco.stage`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `approval_roles`, `folded`, `name`, `sequence`, `type_ids`
- XPath or positional patches: 0

### `mrp_eco_view_graph`
- Name: mrp.eco.view.graph
- Model: `mrp.eco`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `product_tmpl_id`, `stage_id`
- XPath or positional patches: 0

### `mrp_eco_view_pivot`
- Name: mrp.eco.view.pivot
- Model: `mrp.eco`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `color`, `product_tmpl_id`, `stage_id`
- XPath or positional patches: 0

### `mrp_eco_view_calendar`
- Name: mrp.eco.view.calendar
- Model: `mrp.eco`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 4
- Sample fields: `product_tmpl_id`, `stage_id`, `type`, `user_id`
- XPath or positional patches: 0

### `mrp_eco_view_form`
- Name: mrp.eco.view.form
- Model: `mrp.eco`
- Type: inferred from arch
- Root tag: `form`
- Field references: 52
- Sample fields: `active`, `allow_apply_change`, `allow_change_kanban_state`, `approval_date`, `approval_ids`, `bom_change_ids_on_byproduct`, `bom_change_ids_on_line`, `bom_id`, `bom_rebase_ids`, `change_type`, and 42 more
- Buttons: `action_apply`, `action_new_revision`, `action_open_byproduct_change`, `action_open_component_change`, `action_open_production`, `action_open_routing_change_operation`, `action_see_attachments`, `apply_rebase`, `approve`, `conflict_resolve`, and 2 more
- XPath or positional patches: 0

### `mrp_eco_kanban`
- Name: mrp.eco.kanban
- Model: `mrp.eco`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 14
- Sample fields: `activity_ids`, `allow_change_kanban_state`, `bom_id`, `color`, `displayed_image_attachment_id`, `effectivity_date`, `kanban_state`, `legend_done`, `name`, `priority`, and 4 more
- XPath or positional patches: 0

### `mrp_eco_search`
- Name: mrp.eco.search
- Model: `mrp.eco`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `product_tmpl_id`, `stage_id`, `tag_ids`
- XPath or positional patches: 0

### `mrp_eco_view_tree`
- Name: mrp.eco.view.list
- Model: `mrp.eco`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `activity_exception_decoration`, `bom_id`, `company_id`, `effectivity`, `effectivity_date`, `name`, `product_tmpl_id`, `stage_id`, `tag_ids`, `type`, and 1 more
- Buttons: `action_apply`
- XPath or positional patches: 0

### `mrp_eco_type_dashboard_view_kanban`
- Name: mrp.eco.type.view.kanban
- Model: `mrp.eco.type`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 9
- Sample fields: `alias_domain`, `alias_id`, `alias_name`, `color`, `name`, `nb_approvals`, `nb_approvals_my`, `nb_ecos`, `nb_validation`
- Buttons: `%(mrp_eco_action)d`
- XPath or positional patches: 0

### `mrp_eco_type_view_kanban`
- Name: mrp.eco.type.view.kanban
- Model: `mrp.eco.type`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `mrp_eco_type_view_form`
- Name: mrp.eco.type.view.form
- Model: `mrp.eco.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `alias_domain_id`, `alias_id`, `alias_name`, `name`
- XPath or positional patches: 0

### `mrp_eco_type_view_tree`
- Name: mrp.eco.type.view.list
- Model: `mrp.eco.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `name`, `sequence`
- XPath or positional patches: 0

## Actions

- `mrp_eco_tag_action`: `act_window` ECO Tags
- `mrp_eco_stage_action`: `act_window` ECO Stages
- `mrp_eco_action_report`: `act_window` ECOs Analysis
- `mrp_eco_action_main`: `act_window` Engineering Change Orders
- `mrp_eco_type_action_form`: `act_window` ECO Types
- `mrp_eco_type_action_dashboard`: `act_window` PLM Overview
- `mrp_eco_action_late`: `act_window` Engineering Change Orders
- `mrp_eco_action_approval`: `act_window` Engineering Change Orders
- `mrp_eco_action_approval_my`: `act_window` Engineering Change Orders
- `mrp_eco_action`: `act_window` Engineering Change Orders

## Menus

- `menu_mrp_plm_eco_tag`: ECO Tags
- `menu_mrp_plm_eco_types`: ECO Types
- `menu_mrp_plm_eco_stages`: ECO Stages
- `menu_mrp_plm_configuration`: Configuration
- `menu_mrp_plm_eco_report`: ECOs
- `menu_mrp_plm_reporting`: Reporting
- `menu_mrp_plm_search`: Search
- `menu_mrp_plm_workcenters`: Work Centers
- `menu_mrp_plm_boms`: Bill of Materials
- `menu_mrp_plm_products`: Products
- `menu_mrp_plm_master_data`: Master Data
- `menu_mrp_plm_changes`: Changes
- `menu_mrp_plm_dashboard`: Overview
- `menu_mrp_plm_root`: PLM

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_plm/Views]]

