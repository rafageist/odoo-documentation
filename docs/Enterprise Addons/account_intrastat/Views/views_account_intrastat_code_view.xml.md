<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_intrastat_code_view.xml

- Module: [[docs/Enterprise Addons/account_intrastat/account_intrastat|account_intrastat]]
- Scope: Enterprise Addons
- Source file: `views/account_intrastat_code_view.xml`
- Views: 6
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_intrastat_code_restricted_type_form`
- Name: account.intrastat.code.restricted.type.form
- Model: `account.intrastat.code`
- Type: inferred from arch
- Inherits: `view_report_intrastat_code_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `country_id`, `type`
- XPath or positional patches: 0

### `view_report_intrastat_code_form`
- Name: account.intrastat.code.form
- Model: `account.intrastat.code`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `code`, `country_id`, `description`, `expiry_date`, `name`, `start_date`, `supplementary_unit`, `type`
- XPath or positional patches: 0

### `view_intrastat_code_restricted_type_search`
- Name: account.intrastat.transport.code.search
- Model: `account.intrastat.code`
- Type: inferred from arch
- Inherits: `view_intrastat_code_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 6

### `view_report_intrastat_code_kanban`
- Name: account.intrastat.code.kanban
- Model: `account.intrastat.code`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `description`, `name`
- XPath or positional patches: 0

### `view_intrastat_code_search`
- Name: account.intrastat.code.search
- Model: `account.intrastat.code`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `code`, `country_id`, `description`, `name`, `supplementary_unit`
- XPath or positional patches: 0

### `view_report_intrastat_code_tree`
- Name: account.intrastat.code.list
- Model: `account.intrastat.code`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `code`, `country_id`, `description`, `expiry_date`, `name`, `start_date`, `supplementary_unit`
- XPath or positional patches: 0

## Actions

- `action_report_intrastat_code_tree`: `act_window` Intrastat Code

## Menus

- `menu_report_intrastat_code`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_intrastat/Views]]

<!-- GENERATED:VIEWFILE -->
