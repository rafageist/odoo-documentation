<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_ar_afipws_connection_view.xml

- Module: [[docs/Enterprise Addons/l10n_ar_edi/l10n_ar_edi|l10n_ar_edi]]
- Scope: Enterprise Addons
- Source file: `views/l10n_ar_afipws_connection_view.xml`
- Views: 2
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `view_afipws_auth_tree`
- Name: afipws.auth.list
- Model: `l10n_ar.afipws.connection`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `company_id`, `expiration_time`, `generation_time`, `l10n_ar_afip_ws`, `type`, `uniqueid`
- XPath or positional patches: 0

### `view_afipws_auth_form`
- Name: afipws.auth.form
- Model: `l10n_ar.afipws.connection`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `company_id`, `expiration_time`, `generation_time`, `l10n_ar_afip_ws`, `sign`, `token`, `type`, `uniqueid`
- XPath or positional patches: 0

## Actions

- `act_afipws_auth`: `act_window` ARCA Connections

## Menus

- `menu_action_afipws_auth`: Connections
- `menu_afipws`: ARCA Web Services

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ar_edi/Views]]

<!-- GENERATED:VIEWFILE -->
