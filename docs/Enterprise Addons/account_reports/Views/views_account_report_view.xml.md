<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_report_view.xml

- Module: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]
- Scope: Enterprise Addons
- Source file: `views/account_report_view.xml`
- Views: 12
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `account_report_budget_form`
- Name: account.report.budget.form
- Model: `account.report.budget`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `account_id`, `amount`, `date`, `item_ids`, `name`
- XPath or positional patches: 0

### `account_report_budget_tree`
- Name: account.report.budget.list
- Model: `account.report.budget`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `company_id`, `name`, `sequence`
- XPath or positional patches: 0

### `account_report_external_value_tree`
- Name: account.report.external.value.list
- Model: `account.report.external.value`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `company_id`, `date`, `name`, `report_country_id`, `target_report_expression_id`, `target_report_expression_label`, `target_report_line_id`, `text_value`, `value`
- XPath or positional patches: 0

### `account_report_horizontal_group_tree`
- Name: account.report.horizontal.group.list
- Model: `account.report.horizontal.group`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `name`, `report_ids`
- XPath or positional patches: 0

### `account_report_horizontal_group_form`
- Name: account.report.horizontal.group.form
- Model: `account.report.horizontal.group`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `domain`, `field_name`, `name`, `report_ids`, `res_model_name`, `rule_ids`
- XPath or positional patches: 0

### `account_report_expression_form`
- Name: account.report.expression.form
- Model: `account.report.expression`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `blank_if_zero`, `carryover_target`, `date_scope`, `engine`, `figure_type`, `formula`, `green_on_positive`, `label`, `subformula`
- XPath or positional patches: 0

### `account_report_line_form`
- Name: account.report.line.form
- Model: `account.report.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `action_id`, `code`, `date_scope`, `display_custom_groupby_warning`, `engine`, `expression_ids`, `foldable`, `formula`, `groupby`, `hide_if_zero`, and 6 more
- Buttons: `action_reset_custom_groupby`
- XPath or positional patches: 0

### `account_report_form`
- Name: account.report.form
- Model: `account.report`
- Type: inferred from arch
- Root tag: `form`
- Field references: 46
- Sample fields: `active`, `availability_condition`, `blank_if_zero`, `chart_template`, `code`, `column_ids`, `country_id`, `currency_translation`, `custom_handler_model_id`, `default_opening_date_filter`, and 36 more
- Buttons: `action_download_xlsx_accounts_coverage_report`
- XPath or positional patches: 0

### `view_account_coa`
- Name: account.view.coa
- Model: `account.account`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `account_type`, `code`, `company_ids`, `current_balance`, `name`, `tag_ids`, `tax_ids`
- XPath or positional patches: 0

### `view_account_report_search`
- Name: account.report.search
- Model: `account.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `root_report_id`
- XPath or positional patches: 0

### `account_report_add_sections_tree`
- Name: account.report.add.sections.list
- Model: `account.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `active`, `country_id`, `name`, `sequence`
- XPath or positional patches: 0

### `account_report_tree`
- Name: account.report.list
- Model: `account.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `country_id`, `name`, `root_report_id`, `sequence`
- XPath or positional patches: 0

## Actions

- `action_create_composite_report_list`: `server` Create Composite Report

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_reports/Views]]

<!-- GENERATED:VIEWFILE -->
