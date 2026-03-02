<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# CRM Livechat

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/crm_livechat
- Dependencies: [[Odoo 19/Community Addons/crm/crm|crm]], [[Odoo 19/Community Addons/im_livechat/im_livechat|im_livechat]]

## Summary

Create lead from livechat conversation

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 0

## Detected Models

- `ChatbotScript`
- `ChatbotScriptStep`
- `CrmLead`
- `DiscussChannel`
- `ResUsers`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title CRM Livechat - Models and Relations
class ChatbotScript
class ChatbotScriptStep
class CrmLead
class DiscussChannel
class ResUsers
class "crm.team" as crm_team
ChatbotScriptStep --> crm_team : many2one
class "discuss.channel" as discuss_channel
CrmLead --> discuss_channel : many2one
class "crm.lead" as crm_lead
DiscussChannel --|> crm_lead : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


