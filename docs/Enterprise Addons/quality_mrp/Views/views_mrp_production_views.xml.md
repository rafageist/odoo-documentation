---
tags: [odoo, enterprise, generated, views]
---

# views/mrp_production_views.xml

- Module: [[docs/Enterprise Addons/quality_mrp/quality_mrp|quality_mrp]]
- Scope: Enterprise Addons
- Source file: `views/mrp_production_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mrp_production_view_form_inherit_quality`
- Name: mrp.production.view.form.inherit.quality
- Model: `mrp.production`
- Type: inferred from arch
- Inherits: `mrp.mrp_production_form_view`
- Root tag: `button`
- Field references: 4
- Sample fields: `check_ids`, `quality_alert_count`, `quality_check_fail`, `quality_check_todo`
- Buttons: `%(quality_check_action_mo)d`, `action_cancel`, `button_quality_alert`, `check_quality`, `open_quality_alert_mo`
- XPath or positional patches: 1

## Actions

- `mrp_production_action_quality_check_on_demand`: `server` Quality Check

## Navigation

- **Parent:** [[docs/Enterprise Addons/quality_mrp/Views]]

