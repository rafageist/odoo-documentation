---
tags: [odoo, enterprise, generated, views]
---

# views/voip_provider_views.xml

- Module: [[docs/Enterprise Addons/voip/voip|voip]]
- Scope: Enterprise Addons
- Source file: `views/voip_provider_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `voip_provider_view_form`
- Name: voip.provider.view.form
- Model: `voip.provider`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `mode`, `name`, `pbx_ip`, `recording_enabled`, `recording_policy_option`, `ws_server`
- XPath or positional patches: 0

### `voip_provider_tree_view`
- Name: VoIP Provider List View
- Model: `voip.provider`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `company_id`, `mode`, `name`, `pbx_ip`, `recording_policy`, `ws_server`
- XPath or positional patches: 0

## Actions

- `action_voip_provider_view`: `act_window` VoIP Providers

## Menus

- `voip_provider_view_menu`: VoIP Providers

## Navigation

- **Parent:** [[docs/Enterprise Addons/voip/Views]]

