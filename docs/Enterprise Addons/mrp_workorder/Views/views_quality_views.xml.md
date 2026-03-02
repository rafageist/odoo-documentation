<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/quality_views.xml

- Module: [[docs/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]]
- Scope: Enterprise Addons
- Source file: `views/quality_views.xml`
- Views: 10
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `quality_alert_view_search_inherit_mrp_workorder`
- Name: quality.alert.view.search.inherit.mrp.workorder
- Model: `quality.alert`
- Type: inferred from arch
- Inherits: `quality.quality_alert_view_search`
- Root tag: `field`
- Field references: 2
- Sample fields: `tag_ids`, `workcenter_id`
- XPath or positional patches: 0

### `quality_point_view_tree`
- Name: quality.point.view.list.inherit.mrp.workorder
- Model: `quality.point`
- Type: inferred from arch
- Inherits: `quality.quality_point_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `operation_id`, `picking_type_ids`
- XPath or positional patches: 0

### `quality_alert_view_tree`
- Name: quality.alert.view.list.inherit.mrp.workorder
- Model: `quality.alert`
- Type: inferred from arch
- Inherits: `quality.quality_alert_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `workcenter_id`
- XPath or positional patches: 1

### `add_quality_check_from_tablet`
- Name: add.quality.check.from.tablet
- Model: `quality.check`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `company_id`, `note`, `product_id`, `test_type_id`, `title`, `workorder_id`, `worksheet_document`
- Buttons: `add_check_in_chain`
- XPath or positional patches: 0

### `quality_check_workorder_form`
- Name: quality.check.workorder.form
- Model: `quality.check`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `company_id`, `component_id`, `lot_ids`, `note`, `picture`, `point_id`, `product_id`, `production_id`, `team_id`, `test_type`, and 3 more
- XPath or positional patches: 0

### `quality_point_worksheet_document_preview_form`
- Name: quality.point.worksheet.document.preview.form
- Model: `quality.point`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `worksheet_document`
- XPath or positional patches: 0

### `quality_point_routing_view_form`
- Name: quality.point.routing.view.form
- Model: `quality.point`
- Type: inferred from arch
- Inherits: `quality.quality_point_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 7

### `quality_point_routing_view_tree`
- Name: quality.point.routing.view.list
- Model: `quality.point`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `name`, `sequence`, `test_type_id`, `title`, `worksheet_document`
- Buttons: `action_view_worksheet_document`
- XPath or positional patches: 0

### `step_view_form`
- Name: quality.point.view.form.inherit.mrp
- Model: `quality.point`
- Type: inferred from arch
- Inherits: `mrp_workorder.quality_point_view_form_inherit_mrp`
- Root tag: `field`
- Field references: 1
- Sample fields: `picking_type_ids`
- XPath or positional patches: 0

### `quality_point_view_form_inherit_mrp`
- Name: quality.point.view.form.inherit.mrp
- Model: `quality.point`
- Type: inferred from arch
- Inherits: `quality.quality_point_view_form`
- Root tag: `field`
- Field references: 10
- Sample fields: `bom_product_ids`, `component_id`, `component_ids`, `is_workorder_step`, `operation_id`, `picking_type_ids`, `product_category_ids`, `test_report_type`, `test_type_id`, `worksheet_document`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_workorder/Views]]

<!-- GENERATED:VIEWFILE -->
