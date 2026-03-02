<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# test.model

- Module: [[docs/Community Addons/test_website/test_website|test_website]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/model.py`
- Python classes: `TestModel`
- Description: Website Model Test
- Inherits: `website.published.mixin`, `website.searchable.mixin`, `website.seo.metadata`

## Field footprint

- Detected fields: 4
- Field types: `Char` x 1, `Html` x 1, `Many2one` x 1, `One2many` x 1
- Relation fields: 2

## Sample fields

- `name`: `Char`
- `submodel_ids`: `One2many` (comodel `test.submodel`)
- `tag_id`: `Many2one` (comodel `test.tag`)
- `website_description`: `Html`

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: none
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
title test.model - Direct Relations
class "test.model" as test_model
class "test.submodel" as test_submodel
class "test.tag" as test_tag
test_model --|> test_submodel : submodel_ids
test_model --> test_tag : tag_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/test_website/Models]]

<!-- GENERATED:MODEL -->
