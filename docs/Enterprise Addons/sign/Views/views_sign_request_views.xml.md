---
tags: [odoo, enterprise, generated, views]
---

# views/sign_request_views.xml

- Module: [[docs/Enterprise Addons/sign/sign|sign]]
- Scope: Enterprise Addons
- Source file: `views/sign_request_views.xml`
- Views: 9
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `sign_request_item_view_form`
- Name: sign.request.item.form
- Model: `sign.request.item`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `access_token`, `color`, `latitude`, `longitude`, `partner_id`, `role_id`, `signer_email`, `signing_date`, `sms_number`, `state`
- XPath or positional patches: 0

### `sign_request_item_view_tree`
- Name: sign.request.item.list
- Model: `sign.request.item`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `change_authorized`, `is_mail_sent`, `partner_id`, `role_id`, `signer_email`, `state`
- Buttons: `send_signature_accesses`
- XPath or positional patches: 0

### `sign_request_view_activity`
- Name: sign.request.actvity
- Model: `sign.request`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 2
- Sample fields: `subject`, `template_id`
- XPath or positional patches: 0

### `sign_request_view_search`
- Name: sign.request.search
- Model: `sign.request`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `reference`, `template_id`
- XPath or positional patches: 0

### `sign_request_view_form`
- Name: sign.request.form
- Model: `sign.request`
- Type: inferred from arch
- Root tag: `form`
- Field references: 23
- Sample fields: `action`, `active`, `cc_partner_ids`, `completed_document_ids`, `email`, `favorited_ids`, `integrity`, `ip`, `latitude`, `log_date`, and 13 more
- Buttons: `cancel`, `go_to_document`
- XPath or positional patches: 0

### `sign_request_view_graph`
- Name: sign.request.graph
- Model: `sign.request`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `create_date`, `state`
- XPath or positional patches: 0

### `sign_request_view_pivot`
- Name: sign.request.pivot
- Model: `sign.request`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `create_date`, `state`
- XPath or positional patches: 0

### `sign_request_view_tree`
- Name: sign.request.list
- Model: `sign.request`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `activity_exception_decoration`, `create_date`, `create_uid`, `need_my_signature`, `reference`, `reference_doc`, `request_item_ids`, `state`, `template_document_ids`, `template_tags`
- Buttons: `get_formview_action`, `get_sign_request_documents`, `go_to_signable_document`, `send_signature_accesses`
- XPath or positional patches: 0

### `sign_request_view_kanban`
- Name: sign.request.kanban
- Model: `sign.request`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 10
- Sample fields: `active`, `activity_ids`, `color`, `create_date`, `create_uid`, `favorited_ids`, `reference`, `request_item_infos`, `state`, `template_tags`
- XPath or positional patches: 0

## Actions

- `base.open_menu`: `todo`
- `sign_request_item_action`: `act_window` Signature Request Items
- `sign_all_request_action`: `act_window` All Documents
- `sign_request_action`: `act_window` Documents

## Navigation

- **Parent:** [[docs/Enterprise Addons/sign/Views]]

