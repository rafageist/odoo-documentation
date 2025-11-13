<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# CRM Livechat

- Version: v18
- Category: community
- Source: odoo/addons/crm_livechat
- Dependencies: [[Odoo 18/Community Addons/crm/crm|crm]], [[Odoo 18/Community Addons/im_livechat/im_livechat|im_livechat]]

## Summary

Create lead from livechat conversation

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ChatbotScript`
- `ChatbotScriptStep`
- `DiscussChannel`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title CRM Livechat - Models and Relations
class ChatbotScript
class ChatbotScriptStep
class DiscussChannel
class "crm.team" as crm_team
ChatbotScriptStep --> crm_team : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
