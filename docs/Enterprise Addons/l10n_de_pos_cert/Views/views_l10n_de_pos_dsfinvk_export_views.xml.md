---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_de_pos_dsfinvk_export_views.xml

- Module: [[docs/Enterprise Addons/l10n_de_pos_cert/l10n_de_pos_cert|l10n_de_pos_cert]]
- Scope: Enterprise Addons
- Source file: `views/l10n_de_pos_dsfinvk_export_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `l10n_de_pos_dsfinvk_export_view_list`
- Name: l10n_de_pos.dsfinvk_export.list.view
- Model: `l10n_de_pos.dsfinvk_export`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `config_id`, `end_datetime`, `start_datetime`, `state`
- XPath or positional patches: 0

### `l10n_de_pos_dsfinvk_export_view_search`
- Name: l10n_de_pos.dsfinvk_export.search.view
- Model: `l10n_de_pos.dsfinvk_export`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `config_id`
- XPath or positional patches: 0

### `l10n_de_pos_dsfinvk_export_view_form`
- Name: l10n_de_pos.dsfinvk_export.form.view
- Model: `l10n_de_pos.dsfinvk_export`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `config_id`, `end_datetime`, `l10n_de_fiskaly_export_uuid`, `start_datetime`, `state`
- Buttons: `l10n_de_action_download_export`, `l10n_de_action_refresh_state`
- XPath or positional patches: 0

## Actions

- `action_l10n_de_pos_dsfinvk_export`: `act_window` DSFinV-K Exports

## Menus

- `menu_l10n_de_pos_dsfinvk_export`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_de_pos_cert/Views]]

