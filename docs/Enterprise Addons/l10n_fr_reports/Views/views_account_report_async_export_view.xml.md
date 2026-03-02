<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_report_async_export_view.xml

- Module: [[docs/Enterprise Addons/l10n_fr_reports/l10n_fr_reports|l10n_fr_reports]]
- Scope: Enterprise Addons
- Source file: `views/account_report_async_export_view.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_account_report_async_export_search`
- Name: account.report.async.export.search
- Model: `account.report.async.export`
- Type: inferred from arch
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 0

### `view_account_report_async_export_form`
- Name: account.report.async.export.view.form
- Model: `account.report.async.export`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `attachment`, `attachment_name`, `date_from`, `date_to`, `document_ids`, `message`, `name`, `recipient`, `state`
- Buttons: `button_process_report`
- XPath or positional patches: 0

### `view_account_report_async_export_tree`
- Name: account.report.async.export.view.list
- Model: `account.report.async.export`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `date_from`, `date_to`, `name`, `state`
- XPath or positional patches: 0

## Actions

- `action_account_report_async_export`: `act_window` EDI exports

## Menus

- `menu_action_account_report_async_export`: EDI exports

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_fr_reports/Views]]

<!-- GENERATED:VIEWFILE -->
