<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# project.template.create.wizard

- Module: [[docs/Community Addons/project/project|project]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/project_template_create_wizard.py`
- Python classes: `ProjectTemplateCreateWizard`
- Description: Project Template create Wizard

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 1, `Char` x 2, `Date` x 2, `Many2one` x 2, `One2many` x 1
- Relation fields: 3

## Sample fields

- `alias_domain_id`: `Many2one` (comodel `mail.alias.domain`)
- `alias_name`: `Char`
- `date`: `Date`
- `date_start`: `Date`
- `name`: `Char`
- `role_to_users_ids`: `One2many` (comodel `project.template.role.to.users.map`)
- `template_has_dates`: `Boolean` (compute `_compute_template_has_dates`)
- `template_id`: `Many2one` (comodel `project.project`)

## Method hints

- Detected methods: 6
- Action methods: `action_open_template_view`
- Compute methods: `_compute_template_has_dates`
- Onchange methods: none

## Direct relation diagram

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title project.template.create.wizard - Direct Relations
class "project.template.create.wizard" as project_template_create_wizard
class "mail.alias.domain" as mail_alias_domain
class "project.project" as project_project
class "project.template.role.to.users.map" as project_template_role_to_users_map
project_template_create_wizard --> mail_alias_domain : alias_domain_id
project_template_create_wizard --> project_project : template_id
project_template_create_wizard --|> project_template_role_to_users_map : role_to_users_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/project/Models]]

<!-- GENERATED:MODEL -->
