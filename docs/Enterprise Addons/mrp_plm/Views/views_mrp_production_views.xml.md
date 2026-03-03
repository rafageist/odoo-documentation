---
tags: [odoo, enterprise, generated, views]
---

# views/mrp_production_views.xml

- Module: [[docs/Enterprise Addons/mrp_plm/mrp_plm|mrp_plm]]
- Scope: Enterprise Addons
- Source file: `views/mrp_production_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mrp_plm_production_form_view`
- Name: mrp.plm.production.form
- Model: `mrp.production`
- Type: inferred from arch
- Inherits: `mrp.mrp_production_form_view`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `eco_count`, `latest_bom_id`
- Buttons: `action_open_eco`
- XPath or positional patches: 3

## Actions

- `action_production_order_create_eco`: `server` Create ECO

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_plm/Views]]

