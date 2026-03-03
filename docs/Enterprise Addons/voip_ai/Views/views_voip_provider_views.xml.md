---
tags: [odoo, enterprise, generated, views]
---

# views/voip_provider_views.xml

- Module: [[docs/Enterprise Addons/voip_ai/voip_ai|voip_ai]]
- Scope: Enterprise Addons
- Source file: `views/voip_provider_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `voip_provider_view_form`
- Name: voip.provider.view.form.inherit.voip_ai
- Model: `voip.provider`
- Type: inferred from arch
- Inherits: `voip.voip_provider_view_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `mode`, `transcription_policy`
- XPath or positional patches: 0

### `voip_provider_tree_view`
- Name: voip.provider.tree.inherit.ai.voip
- Model: `voip.provider`
- Type: inferred from arch
- Inherits: `voip.voip_provider_tree_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `recording_policy`, `transcription_policy`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/voip_ai/Views]]

