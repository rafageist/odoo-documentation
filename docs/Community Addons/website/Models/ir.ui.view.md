<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# ir.ui.view

- Module: [[docs/Community Addons/website/website|website]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/ir_ui_view.py`, `models/theme_models.py`
- Python classes: `IrUiView`
- Inherits: `website.seo.metadata`

## Field footprint

- Detected fields: 9
- Field types: `Boolean` x 1, `Char` x 2, `Many2one` x 3, `One2many` x 2, `Selection` x 1
- Relation fields: 5

## Sample fields

- `controller_page_ids`: `One2many` (comodel `website.controller.page`)
- `first_page_id`: `Many2one` (comodel `website.page`, compute `_compute_first_page_id`)
- `page_ids`: `One2many` (comodel `website.page`)
- `theme_template_id`: `Many2one` (comodel `theme.ir.ui.view`)
- `track`: `Boolean`
- `visibility`: `Selection`
- `visibility_password`: `Char`
- `visibility_password_display`: `Char` (compute `_get_pwd`)
- `website_id`: `Many2one` (comodel `website`)

## Method hints

- Detected methods: 36
- Action methods: none
- Compute methods: `_compute_display_name`, `_compute_first_page_id`
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
title ir.ui.view - Direct Relations
class "ir.ui.view" as ir_ui_view
class "theme.ir.ui.view" as theme_ir_ui_view
class "website" as website
class "website.controller.page" as website_controller_page
class "website.page" as website_page
ir_ui_view --> website : website_id
ir_ui_view --|> website_page : page_ids
ir_ui_view --|> website_controller_page : controller_page_ids
ir_ui_view --> website_page : first_page_id
ir_ui_view --> theme_ir_ui_view : theme_template_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/website/Models]]

<!-- GENERATED:MODEL -->
