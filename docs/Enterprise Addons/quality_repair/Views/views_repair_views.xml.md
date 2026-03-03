---
tags: [odoo, enterprise, generated, views]
---

# views/repair_views.xml

- Module: [[docs/Enterprise Addons/quality_repair/quality_repair|quality_repair]]
- Scope: Enterprise Addons
- Source file: `views/repair_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_repair_order_form_inherit_quality`
- Name: repair.form.inherit.quality
- Model: `repair.order`
- Type: inferred from arch
- Inherits: `repair.view_repair_order_form`
- Root tag: `button`
- Field references: 1
- Sample fields: `quality_alert_count`
- Buttons: `action_check_quality`, `action_open_quality_alerts`, `action_open_quality_checks`, `action_repair_cancel`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/quality_repair/Views]]

