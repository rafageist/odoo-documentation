---
tags: [odoo, enterprise, generated, views]
---

# views/sign_template_views.xml

- Module: [[docs/Enterprise Addons/sign/sign|sign]]
- Scope: Enterprise Addons
- Source file: `views/sign_template_views.xml`
- Views: 13
- Actions: 7
- Menus: 11
- Rules: 0

## View records

### `sign_item_role_view_form`
- Name: sign.item.role.form
- Model: `sign.item.role`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `assign_to`, `auth_method`, `change_authorized`, `name`
- XPath or positional patches: 0

### `sign_item_type_view_search`
- Name: sign.item.type.search
- Model: `sign.item.type`
- Type: inferred from arch
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 0

### `sign_item_type_view_form`
- Name: sign.item.type.form
- Model: `sign.item.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `active`, `auto_field`, `field_size`, `item_type`, `model_id`, `name`, `placeholder`, `tip`
- XPath or positional patches: 0

### `sign_item_type_view_tree`
- Name: sign.item.type.list
- Model: `sign.item.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `auto_field`, `item_type`, `model_id`, `name`
- XPath or positional patches: 0

### `sign_item_view_form`
- Name: sign.item.form
- Model: `sign.item`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `height`, `page`, `posX`, `posY`, `required`, `responsible_id`, `type_id`, `width`
- XPath or positional patches: 0

### `sign_item_view_tree`
- Name: sign.item.list
- Model: `sign.item`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `height`, `page`, `posX`, `posY`, `required`, `responsible_id`, `type_id`, `width`
- XPath or positional patches: 0

### `sign_template_view_search`
- Name: sign.template.search
- Model: `sign.template`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `tag_ids`
- XPath or positional patches: 0

### `sign_template_tag_view_form`
- Name: sign.template.tag.view.form
- Model: `sign.template.tag`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `color`, `name`
- XPath or positional patches: 0

### `sign_template_tag_view_tree`
- Name: sign.template.tag.view.list
- Model: `sign.template.tag`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `color`, `name`
- XPath or positional patches: 0

### `sign_template_view_form`
- Name: sign.template.form
- Model: `sign.template`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `active`, `authorized_ids`, `group_ids`, `message`, `model_id`, `name`, `redirect_url`, `redirect_url_text`, `responsible_count`, `signature_request_validity`, and 3 more
- Buttons: `open_requests`
- XPath or positional patches: 0

### `sign_template_view_inherit_tree`
- Name: sign.template.primary.inherit.list
- Model: `sign.template`
- Type: inferred from arch
- Inherits: `sign.sign_template_view_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `sign_template_view_tree`
- Name: sign.template.list
- Model: `sign.template`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `active`, `create_date`, `document_ids`, `name`, `responsible_count`, `sign_item_ids`, `signed_count`, `tag_ids`, `user_id`
- Buttons: `open_shared_sign_request`, `open_sign_send_dialog`, `stop_sharing`
- XPath or positional patches: 0

### `sign_template_view_kanban`
- Name: sign.template.kanban
- Model: `sign.template`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 12
- Sample fields: `active`, `color`, `create_date`, `create_uid`, `display_name`, `favorited_ids`, `in_progress_count`, `is_sharing`, `responsible_count`, `signed_count`, and 2 more
- Buttons: `open_shared_sign_request`, `open_sign_send_dialog`
- XPath or positional patches: 0

## Actions

- `sign_report_green_savings_action`: `report` Ecological Savings by using Electronic Signatures
- `sign_settings_action`: `act_window` Settings
- `sign_template_tag_action`: `act_window` Tags
- `sign_item_option_action`: `act_window` Signature Item Options
- `sign_item_type_action`: `act_window` Signature Fields
- `sign_template_action`: `act_window` Templates
- `sign_template_tour_trigger_action`: `server` Template Sample Contract.pdf trigger

## Menus

- `sign_request_documents`: All Documents
- `sign_request_my_documents`: My Documents
- `sign_report_green_savings`: Green Savings
- `sign.sign_template_tag_menu`: Tags
- `sign.sign_item_type_menu`: Fields
- `sign.sign_item_settings_menu`: Settings
- `menu_sign_configuration`: Configuration
- `sign_reports`: Reports
- `sign_template_menu`: Templates
- `sign_request_menu`: Documents
- `menu_document`: Sign

## Navigation

- **Parent:** [[docs/Enterprise Addons/sign/Views]]

