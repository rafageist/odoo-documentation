<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Studio

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/web_studio
- Dependencies: [[Odoo 19/Community Addons/base_automation/base_automation|base_automation]], [[Odoo 19/Community Addons/base_import_module/base_import_module|base_import_module]], [[Odoo 19/Community Addons/mail/mail|mail]], [[Odoo 19/Community Addons/web/web|web]], [[Odoo 19/Enterprise Addons/web_enterprise/web_enterprise|web_enterprise]], [[Odoo 19/Community Addons/html_editor/html_editor|html_editor]], [[Odoo 19/Enterprise Addons/web_map/web_map|web_map]], [[Odoo 19/Enterprise Addons/web_gantt/web_gantt|web_gantt]], [[Odoo 19/Enterprise Addons/web_cohort/web_cohort|web_cohort]], [[Odoo 19/Community Addons/sms/sms|sms]]

## Summary

Create and customize your Odoo apps

## XML Artifacts (detected)

- Views: 17
- Actions: 8
- Menus: 3
- Rules (ir.rule): 2
- Access CSV entries: 10

## Detected Models

- `base.automation`
- `ir.actions.actions`
- `ir.actions.act_window`
- `ir.actions.act_window.view`
- `ir.actions.report`
- `ir.actions.server`
- `ir.default`
- `ir.filters`
- `ir.model`
- `ir.model.fields`
- `ir.model.access`
- `IrModelData`
- `IrModuleModule`
- `ir.rule`
- `ir.ui.menu`
- `ir.ui.view`
- `MailActivity`
- `mail.template`
- `report.paperformat`
- `ResCompany`
- `res.groups`
- `studio.approval.rule.approver`
- `studio.approval.rule`
- `studio.approval.entry`
- `studio.approval.request`
- `studio.export.model`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Studio - Models and Relations
class "base.automation" as base_automation
class "ir.actions.actions" as ir_actions_actions
class "ir.actions.act_window" as ir_actions_act_window
class "ir.actions.act_window.view" as ir_actions_act_window_view
class "ir.actions.report" as ir_actions_report
class "ir.actions.server" as ir_actions_server
class "ir.default" as ir_default
class "ir.filters" as ir_filters
class "ir.model" as ir_model
class "ir.model.fields" as ir_model_fields
class "ir.model.access" as ir_model_access
class IrModelData
class IrModuleModule
class "ir.rule" as ir_rule
class "ir.ui.menu" as ir_ui_menu
class "ir.ui.view" as ir_ui_view
class MailActivity
class "mail.template" as mail_template
class "report.paperformat" as report_paperformat
class ResCompany
class "res.groups" as res_groups
class "studio.approval.rule.approver" as studio_approval_rule_approver
class "studio.approval.rule" as studio_approval_rule
class "studio.approval.entry" as studio_approval_entry
class "studio.approval.request" as studio_approval_request
class "studio.export.model" as studio_export_model
MailActivity --> studio_approval_request : many2one
class "res.users" as res_users
studio_approval_rule_approver --> res_users : many2one
studio_approval_rule_approver --> studio_approval_rule : many2one
studio_approval_rule --> ir_model : many2one
studio_approval_rule --> ir_actions_actions : many2one
studio_approval_rule .. res_users : many2many
studio_approval_rule --|> studio_approval_rule_approver : one2many
studio_approval_rule --> res_groups : many2one
studio_approval_rule .. res_users : many2many
studio_approval_rule --|> studio_approval_entry : one2many
studio_approval_entry --> res_users : many2one
studio_approval_entry --> studio_approval_rule : many2one
studio_approval_entry --> ir_actions_actions : many2one
class "mail.activity" as mail_activity
studio_approval_request --> mail_activity : many2one
studio_approval_request --> studio_approval_rule : many2one
studio_export_model --> ir_model : many2one
studio_export_model .. ir_model_fields : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

