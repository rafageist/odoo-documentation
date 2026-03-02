<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/whatsapp_account_views.xml

- Module: [[docs/Enterprise Addons/whatsapp/whatsapp|whatsapp]]
- Scope: Enterprise Addons
- Source file: `views/whatsapp_account_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `whatsapp_account_view_search`
- Name: whatsapp.account.view.search
- Model: `whatsapp.account`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `account_uid`, `app_uid`, `name`, `phone_uid`
- XPath or positional patches: 0

### `whatsapp_account_view_form`
- Name: whatsapp.account.view.form
- Model: `whatsapp.account`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `account_uid`, `active`, `allowed_company_ids`, `app_secret`, `app_uid`, `callback_url`, `name`, `notify_user_ids`, `phone_number`, `phone_uid`, and 3 more
- Buttons: `action_debug`, `action_open_templates`, `action_stop_debug`, `button_sync_whatsapp_account_templates`, `button_test_connection`
- XPath or positional patches: 0

### `whatsapp_account_view_tree`
- Name: whatsapp.account.view.list
- Model: `whatsapp.account`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `account_uid`, `allowed_company_ids`, `app_uid`, `name`, `phone_uid`
- XPath or positional patches: 0

## Actions

- `whatsapp_account_action`: `act_window` WhatsApp Business Account

## Navigation

- **Parent:** [[docs/Enterprise Addons/whatsapp/Views]]

<!-- GENERATED:VIEWFILE -->
