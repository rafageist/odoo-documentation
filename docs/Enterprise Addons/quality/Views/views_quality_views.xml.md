<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/quality_views.xml

- Module: [[docs/Enterprise Addons/quality/quality|quality]]
- Scope: Enterprise Addons
- Source file: `views/quality_views.xml`
- Views: 5
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `quality_point_view_tree`
- Name: quality.point.view.list
- Model: `quality.point`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `company_id`, `name`, `picking_type_ids`, `product_category_ids`, `product_ids`, `sequence`, `team_id`, `test_type_id`, `title`, `user_id`
- XPath or positional patches: 0

### `quality_alert_view_search`
- Name: quality.alert.view.search
- Model: `quality.alert`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `name`, `product_id`, `tag_ids`, `user_id`
- XPath or positional patches: 0

### `quality_alert_view_tree`
- Name: quality.alert.view.list
- Model: `quality.alert`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `date_assign`, `lot_ids`, `name`, `partner_id`, `priority`, `product_id`, `product_tmpl_id`, `reason_id`, `tag_ids`, `team_id`, and 1 more
- XPath or positional patches: 0

### `quality_point_view_form`
- Name: quality.point.view.form
- Model: `quality.point`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `active`, `company_id`, `failure_location_ids`, `name`, `note`, `picking_type_ids`, `product_category_ids`, `product_ids`, `reason`, `team_id`, and 4 more
- XPath or positional patches: 0

### `quality_check_view_activity`
- Name: quality.check.activity
- Model: `quality.check`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 2
- Sample fields: `control_date`, `name`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/quality/Views]]

<!-- GENERATED:VIEWFILE -->
