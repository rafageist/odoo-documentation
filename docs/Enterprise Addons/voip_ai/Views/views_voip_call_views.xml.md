---
tags: [odoo, enterprise, generated, views]
---

# views/voip_call_views.xml

- Module: [[docs/Enterprise Addons/voip_ai/voip_ai|voip_ai]]
- Scope: Enterprise Addons
- Source file: `views/voip_call_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `voip_call_view_list_summary`
- Name: voip.call.list.summary
- Model: `voip.call`
- Type: inferred from arch
- Inherits: `voip.voip_call_tree_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `summary`
- XPath or positional patches: 1

### `voip_call_view_form_transcript`
- Name: voip.call.form.transcript
- Model: `voip.call`
- Type: inferred from arch
- Inherits: `voip.voip_call_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `transcript`
- XPath or positional patches: 1

### `voip_call_view_form_summary`
- Name: voip.call.form.summary
- Model: `voip.call`
- Type: inferred from arch
- Inherits: `voip.voip_call_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `summary`
- XPath or positional patches: 1

### `voip_call_view_form_transcription_status`
- Name: voip.call.form.transcription_status
- Model: `voip.call`
- Type: inferred from arch
- Inherits: `voip.voip_call_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `transcription_status`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/voip_ai/Views]]

