<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# VVM Strider Flows

- Version: v18
- Category: community
- Source: odoo/addons/vvm_strider_flows
- Dependencies: vvm_core (not documented), [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/web/web|web]]

## Summary

VVM Strider Flows

## XML Artifacts (detected)

- Views: 4
- Actions: 2
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 7

## Detected Models

- `vvm_strider_flows.flow`
- `vvm_strider_flows.job`
- `vvm_strider_flows.job_context`
- `vvm_strider_flows.job_file`
- `vvm_strider_flows.log`
- `vvm_strider_flows.map`
- `vvm_strider_flows.map.tag`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title VVM Strider Flows - Models and Relations
class "vvm_strider_flows.flow" as vvm_strider_flows_flow
class "vvm_strider_flows.job" as vvm_strider_flows_job
class "vvm_strider_flows.job_context" as vvm_strider_flows_job_context
class "vvm_strider_flows.job_file" as vvm_strider_flows_job_file
class "vvm_strider_flows.log" as vvm_strider_flows_log
class "vvm_strider_flows.map" as vvm_strider_flows_map
class "vvm_strider_flows.map.tag" as vvm_strider_flows_map_tag
vvm_strider_flows_job --> vvm_strider_flows_flow : many2one
class "res.users" as res_users
vvm_strider_flows_job --> res_users : many2one
vvm_strider_flows_job --|> vvm_strider_flows_job_context : one2many
vvm_strider_flows_job --|> vvm_strider_flows_job_file : one2many
vvm_strider_flows_job --|> vvm_strider_flows_log : one2many
vvm_strider_flows_job_context --> vvm_strider_flows_job : many2one
vvm_strider_flows_job_file --> vvm_strider_flows_job : many2one
vvm_strider_flows_log --> vvm_strider_flows_job : many2one
vvm_strider_flows_map .. vvm_strider_flows_map_tag : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
