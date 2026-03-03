---
tags: [odoo, community, generated, views]
---

# wizard/mrp_production_split.xml

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Source file: `wizard/mrp_production_split.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_mrp_production_split_form`
- Name: Split Production
- Model: `mrp.production.split`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `date`, `max_batch_size`, `num_splits`, `product_id`, `product_qty`, `product_uom_id`, `production_detailed_vals_ids`, `production_id`, `production_split_multi_id`, `quantity`, and 2 more
- Buttons: `action_return_to_list`, `action_split`
- XPath or positional patches: 0

### `view_mrp_production_split_multi_form`
- Name: mrp.production.split.multi.form
- Model: `mrp.production.split.multi`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `product_id`, `product_qty`, `product_uom_id`, `production_capacity`, `production_id`, `production_ids`
- Buttons: `action_prepare_split`
- XPath or positional patches: 0

## Actions

- `action_mrp_production_split`: `act_window` Split production
- `action_mrp_production_split_multi`: `act_window` Split productions

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Views]]

