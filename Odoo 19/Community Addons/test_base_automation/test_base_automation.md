<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Test - Base Automation

- Version: v19
- Category: community
- Source: odoo19/addons/test_base_automation
- Dependencies: [[Odoo 19/Community Addons/base_automation/base_automation|base_automation]]

## Summary

Base Automation Tests: Ensure Flow Robustness

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 11

## Detected Models

- `base.automation.lead.test`
- `base.automation.lead.thread.test`
- `base.automation.line.test`
- `base.automation.link.test`
- `base.automation.linked.test`
- `test_base_automation.project`
- `test_base_automation.task`
- `test_base_automation.stage`
- `test_base_automation.tag`
- `base.automation.model.with.recname.char`
- `base.automation.model.with.recname.m2o`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Test - Base Automation - Models and Relations
class "base.automation.lead.test" as base_automation_lead_test
class "base.automation.lead.thread.test" as base_automation_lead_thread_test
class "base.automation.line.test" as base_automation_line_test
class "base.automation.link.test" as base_automation_link_test
class "base.automation.linked.test" as base_automation_linked_test
class "test_base_automation.project" as test_base_automation_project
class "test_base_automation.task" as test_base_automation_task
class "test_base_automation.stage" as test_base_automation_stage
class "test_base_automation.tag" as test_base_automation_tag
class "base.automation.model.with.recname.char" as base_automation_model_with_recname_char
class "base.automation.model.with.recname.m2o" as base_automation_model_with_recname_m2o
class "res.users" as res_users
base_automation_lead_test --> res_users : many2one
base_automation_lead_test .. test_base_automation_tag : many2many
class "res.partner" as res_partner
base_automation_lead_test --> res_partner : many2one
base_automation_lead_test --|> base_automation_line_test : one2many
base_automation_lead_test --> test_base_automation_stage : many2one
base_automation_lead_thread_test --> res_users : many2one
base_automation_line_test --> base_automation_lead_test : many2one
base_automation_line_test --> res_users : many2one
base_automation_link_test --> base_automation_linked_test : many2one
test_base_automation_project --|> test_base_automation_task : one2many
test_base_automation_project --> test_base_automation_stage : many2one
test_base_automation_project .. test_base_automation_tag : many2many
test_base_automation_project .. res_users : many2many
test_base_automation_task --> test_base_automation_task : many2one
test_base_automation_task --> test_base_automation_project : many2one
base_automation_model_with_recname_char --> res_users : many2one
base_automation_model_with_recname_m2o --> base_automation_model_with_recname_char : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
