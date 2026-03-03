---
tags: [odoo, community, generated, views]
---

# views/mrp_bom_views.xml

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Source file: `views/mrp_bom_views.xml`
- Views: 6
- Actions: 4
- Menus: 1
- Rules: 0

## View records

### `mrp_bom_line_view_form`
- Name: mrp.bom.line.view.form
- Model: `mrp.bom.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `allowed_operation_ids`, `bom_product_template_attribute_value_ids`, `company_id`, `operation_id`, `parent_product_tmpl_id`, `possible_bom_product_template_attribute_value_ids`, `product_id`, `product_qty`, `product_uom_id`, `sequence`
- XPath or positional patches: 0

### `view_mrp_bom_filter`
- Name: mrp.bom.select
- Model: `mrp.bom`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `bom_line_ids`, `code`, `product_tmpl_id`
- XPath or positional patches: 0

### `mrp_bom_kanban_view`
- Name: mrp.bom.kanban
- Model: `mrp.bom`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `code`, `product_qty`, `product_tmpl_id`, `product_uom_id`
- XPath or positional patches: 0

### `mrp_bom_tree_view`
- Name: mrp.bom.list
- Model: `mrp.bom`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `active`, `code`, `company_id`, `product_id`, `product_qty`, `product_tmpl_id`, `product_uom_id`, `sequence`, `type`
- XPath or positional patches: 0

### `mrp_bom_form_view`
- Name: mrp.bom.form
- Model: `mrp.bom`
- Type: inferred from arch
- Root tag: `form`
- Field references: 27
- Sample fields: `active`, `allow_operation_dependencies`, `allowed_operation_ids`, `attachments_count`, `batch_size`, `bom_line_ids`, `bom_product_template_attribute_value_ids`, `byproduct_ids`, `code`, `company_id`, and 17 more
- Buttons: `%(action_mrp_routing_time)d`, `%(action_report_mrp_bom)d`, `action_add_from_catalog`, `action_compute_bom_days`, `action_open_operation_form`, `action_see_attachments`
- XPath or positional patches: 0

### `mrp_bom_byproduct_form_view`
- Name: mrp.bom.byproduct.form
- Model: `mrp.bom.byproduct`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `allowed_operation_ids`, `bom_product_template_attribute_value_ids`, `company_id`, `operation_id`, `possible_bom_product_template_attribute_value_ids`, `product_id`, `product_qty`, `product_uom_id`
- XPath or positional patches: 0

## Actions

- `product_open_bom`: `act_window` Bill of Materials
- `template_open_bom`: `act_window` Bill of Materials
- `mrp_bom_form_action`: `act_window` Bills of Materials
- `action_report_mrp_bom`: `client` BoM Overview

## Menus

- `menu_mrp_bom_form_action`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Views]]

