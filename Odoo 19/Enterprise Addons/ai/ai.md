<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# AI

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/ai
- Dependencies: [[Odoo 19/Community Addons/mail/mail|mail]]

## Summary

Base module for AI features

## XML Artifacts (detected)

- Views: 5
- Actions: 10
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 12

## Detected Models

- `ai.agent`
- `ai.agent.source`
- `ai.composer`
- `ai.embedding`
- `ai.prompt.button`
- `ai.topic`
- `discuss.channel`
- `IrActionsServer`
- `IrAttachment`
- `MailTemplateAI`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title AI - Models and Relations
class "ai.agent" as ai_agent
class "ai.agent.source" as ai_agent_source
class "ai.composer" as ai_composer
class "ai.embedding" as ai_embedding
class "ai.prompt.button" as ai_prompt_button
class "ai.topic" as ai_topic
class "discuss.channel" as discuss_channel
class IrActionsServer
class IrAttachment
class MailTemplateAI
class ResPartner
ai_agent .. ai_topic : many2many
class "res.partner" as res_partner
ai_agent --> res_partner : many2one
ai_agent --|> ai_agent_source : one2many
ai_agent_source --> ai_agent : many2one
class "ir.attachment" as ir_attachment
ai_agent_source --> ir_attachment : many2one
class "ir.model" as ir_model
ai_composer .. ir_model : many2many
ai_composer --> ai_agent : many2one
ai_composer --|> ai_prompt_button : one2many
ai_embedding --> ir_attachment : many2one
ai_prompt_button --> ai_composer : many2one
class "ir.actions.server" as ir_actions_server
ai_topic .. ir_actions_server : many2many
discuss_channel --> ai_agent : many2one
IrActionsServer .. ir_actions_server : many2many
ResPartner --|> ai_agent : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

