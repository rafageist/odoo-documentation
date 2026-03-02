<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/quality_views.xml

- Module: [[docs/Enterprise Addons/quality_repair/quality_repair|quality_repair]]
- Scope: Enterprise Addons
- Source file: `views/quality_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `quality_alert_view_form_inherit_repairp`
- Name: quality.alert.view.form.inherit.repair
- Model: `quality.alert`
- Type: inferred from arch
- Inherits: `quality_control.quality_alert_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `repair_id`
- XPath or positional patches: 1

### `quality_check_view_form_inherit_repair`
- Name: quality.check.view.form.inherit.repair
- Model: `quality.check`
- Type: inferred from arch
- Inherits: `quality_control.quality_check_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `repair_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/quality_repair/Views]]

<!-- GENERATED:VIEWFILE -->
