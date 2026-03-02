<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# CrmClient

- Module: [[docs/Community Addons/crm_mail_plugin/crm_mail_plugin|crm_mail_plugin]]
- Scope: Community Addons
- Source file: `controllers/crm_client.py`
- Base classes: `MailPluginController`
- Routes: 5

## Routes

### `log_single_mail_content`
- Paths: `<dynamic>`
- Type: `jsonrpc`
- Auth: `outlook`

### `crm_lead_get_by_partner_id`
- Paths: `/mail_client_extension/lead/get_by_partner_id`
- Type: `jsonrpc`
- Auth: `outlook`

### `crm_lead_redirect_create_form_view`
- Paths: `/mail_client_extension/lead/create_from_partner`
- Type: `http`
- Auth: `user`

### `crm_lead_create`
- Paths: `/mail_plugin/lead/create`
- Type: `jsonrpc`
- Auth: `outlook`

### `crm_lead_open`
- Paths: `/mail_client_extension/lead/open`
- Type: `http`
- Auth: `user`

## Navigation

- **Parent:** [[docs/Community Addons/crm_mail_plugin/Controllers]]

<!-- GENERATED:CONTROLLER -->
