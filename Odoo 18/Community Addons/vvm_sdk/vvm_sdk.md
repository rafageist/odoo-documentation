<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# VVM SDK

- Version: v18
- Category: community
- Source: odoo/addons/vvm_sdk
- Dependencies: vvm_core (not documented), [[Odoo 18/Community Addons/vvm_strider_flows/vvm_strider_flows|vvm_strider_flows]]

## Summary

VVM SDK

## XML Artifacts (detected)

- Views: 19
- Actions: 8
- Menus: 9
- Rules (ir.rule): 0
- Access CSV entries: 10

## Detected Models

- `vvm_sdk.flow_definition`
- `vvm_sdk.function`
- `vvm_sdk.function_category`
- `github.repo`
- `VvmStriderFlowsJobLogSDK`
- `vvm_sdk.package`
- `vvm_sdk.release`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title VVM SDK - Models and Relations
class "vvm_sdk.flow_definition" as vvm_sdk_flow_definition
class "vvm_sdk.function" as vvm_sdk_function
class "vvm_sdk.function_category" as vvm_sdk_function_category
class "github.repo" as github_repo
class VvmStriderFlowsJobLogSDK
class "vvm_sdk.package" as vvm_sdk_package
class "vvm_sdk.release" as vvm_sdk_release
vvm_sdk_function --> vvm_sdk_function_category : many2one
vvm_sdk_function .. vvm_sdk_package : many2many
class "vvm_strider_flows.job" as vvm_strider_flows_job
vvm_sdk_release .. vvm_strider_flows_job : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
