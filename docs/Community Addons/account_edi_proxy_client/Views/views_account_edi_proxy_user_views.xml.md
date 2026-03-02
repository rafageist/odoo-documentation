<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_edi_proxy_user_views.xml

- Module: [[docs/Community Addons/account_edi_proxy_client/account_edi_proxy_client|account_edi_proxy_client]]
- Scope: Community Addons
- Source file: `views/account_edi_proxy_user_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_tree_account_edi_proxy_client_user`
- Name: EDI Proxy Users
- Model: `account_edi_proxy_client.user`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `company_id`, `edi_identification`, `id_client`, `private_key_id`, `refresh_token`
- XPath or positional patches: 0

### `view_form_account_edi_proxy_client_user`
- Name: EDI Proxy User
- Model: `account_edi_proxy_client.user`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `company_id`, `edi_identification`, `id_client`, `private_key_id`, `proxy_type`, `refresh_token`
- XPath or positional patches: 0

## Actions

- `action_tree_account_edi_proxy_client_user`: `act_window` EDI Proxy User

## Menus

- `menu_account_proxy_client_user`: EDI Proxy Users

## Navigation

- **Parent:** [[docs/Community Addons/account_edi_proxy_client/Views]]

<!-- GENERATED:VIEWFILE -->
