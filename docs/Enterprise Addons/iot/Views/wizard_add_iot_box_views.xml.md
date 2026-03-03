---
tags: [odoo, enterprise, generated, views]
---

# wizard/add_iot_box_views.xml

- Module: [[docs/Enterprise Addons/iot/iot|iot]]
- Scope: Enterprise Addons
- Source file: `wizard/add_iot_box_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_no_iot_box_found`
- Name: No IoT Box Found
- Model: `add.iot.box`
- Type: inferred from arch
- Root tag: `form`
- Field references: 0
- Buttons: `add_iot_box_wizard_action`, `cancel`, `open_documentation_url`, `pair_offline`
- XPath or positional patches: 0

### `view_select_box_to_connect`
- Name: Select Box To Connect
- Model: `add.iot.box`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `iot_box_to_connect`
- Buttons: `add_iot_box_wizard_action`
- XPath or positional patches: 0

### `view_pair_offline`
- Name: Pair an IoT Box offline
- Model: `add.iot.box`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `offline_pairing_token`
- Buttons: `cancel`, `pair_offline`
- XPath or positional patches: 0

### `view_enter_pairing_code`
- Name: Enter Pairing Code
- Model: `add.iot.box`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `pairing_code`
- Buttons: `add_iot_box_wizard_action`, `cancel`, `pair_offline`
- XPath or positional patches: 0

### `view_add_iot_box`
- Name: Add IoT box
- Model: `add.iot.box`
- Type: inferred from arch
- Root tag: `form`
- Field references: 0
- Buttons: `cancel`
- XPath or positional patches: 0

## Actions

- `action_add_iot_box`: `act_window` Connect my IoT Box

## Navigation

- **Parent:** [[docs/Enterprise Addons/iot/Views]]

