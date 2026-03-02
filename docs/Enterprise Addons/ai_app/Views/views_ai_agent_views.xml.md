<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/ai_agent_views.xml

- Module: [[docs/Enterprise Addons/ai_app/ai_app|ai_app]]
- Scope: Enterprise Addons
- Source file: `views/ai_agent_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `ai_agent_view_search`
- Name: ai.agent.search
- Model: `ai.agent`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `name`, `sources_ids`, `system_prompt`, `topic_ids`
- XPath or positional patches: 0

### `ai_agent_view_form`
- Name: ai.agent.form
- Model: `ai.agent`
- Type: inferred from arch
- Root tag: `form`
- Field references: 17
- Sample fields: `error_details`, `file_size`, `image_128`, `is_active`, `llm_model`, `mimetype`, `name`, `response_style`, `restrict_to_sources`, `sources_ids`, and 7 more
- Buttons: `action_open_sources_dialog`, `action_refresh_sources`, `action_reprocess_index`, `action_retry_failed_source`, `open_agent_chat`
- XPath or positional patches: 0

### `ai_agent_view_tree`
- Name: ai.agent.list
- Model: `ai.agent`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `llm_model`, `name`, `subtitle`, `topic_ids`
- XPath or positional patches: 0

### `ai_agent_view_kanban`
- Name: ai.agent.kanban
- Model: `ai.agent`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `active`, `id`, `image_128`, `llm_model`, `name`, `subtitle`, `topic_ids`
- XPath or positional patches: 0

## Actions

- `ai_agent_action`: `act_window` Agents

## Navigation

- **Parent:** [[docs/Enterprise Addons/ai_app/Views]]

<!-- GENERATED:VIEWFILE -->
