<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/analytic_plan_views.xml

- Module: [[docs/Community Addons/analytic/analytic|analytic]]
- Scope: Community Addons
- Source file: `views/analytic_plan_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `account_analytic_plan_tree_view`
- Name: account.analytic.plan.list
- Model: `account.analytic.plan`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `color`, `default_applicability`, `name`, `sequence`
- XPath or positional patches: 0

### `account_analytic_plan_form_view`
- Name: account.analytic.plan.form
- Model: `account.analytic.plan`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `all_account_count`, `applicability`, `applicability_ids`, `business_domain`, `children_count`, `color`, `company_id`, `default_applicability`, `name`, `parent_id`
- Buttons: `action_view_analytical_accounts`, `action_view_children_plans`
- XPath or positional patches: 0

## Actions

- `account_analytic_plan_action`: `act_window` Analytic Plans

## Navigation

- **Parent:** [[docs/Community Addons/analytic/Views]]

<!-- GENERATED:VIEWFILE -->
