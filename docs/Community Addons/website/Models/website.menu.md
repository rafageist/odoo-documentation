<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# website.menu

- Module: [[docs/Community Addons/website/website|website]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/theme_models.py`, `models/website_menu.py`
- Python classes: `WebsiteMenu`
- Description: Website Menu

## Field footprint

- Detected fields: 16
- Field types: `Boolean` x 3, `Char` x 4, `Html` x 1, `Integer` x 1, `Many2many` x 1, `Many2one` x 5, `One2many` x 1
- Relation fields: 7

## Sample fields

- `child_id`: `One2many` (comodel `website.menu`)
- `controller_page_id`: `Many2one` (comodel `website.controller.page`)
- `group_ids`: `Many2many` (comodel `res.groups`)
- `is_mega_menu`: `Boolean`
- `is_visible`: `Boolean` (compute `_compute_visible`)
- `mega_menu_classes`: `Char`
- `mega_menu_content`: `Html`
- `name`: `Char` (comodel `Menu`)
- `new_window`: `Boolean` (comodel `New Window`)
- `page_id`: `Many2one` (comodel `website.page`)
- `parent_id`: `Many2one` (comodel `website.menu`)
- `parent_path`: `Char`
- `sequence`: `Integer`
- `theme_template_id`: `Many2one` (comodel `theme.website.menu`)
- `url`: `Char` (comodel `Url`, compute `_compute_url`, store `True`)
- `website_id`: `Many2one` (comodel `website`)

## Method hints

- Detected methods: 15
- Action methods: none
- Compute methods: `_compute_display_name`, `_compute_field_is_mega_menu`, `_compute_url`, `_compute_visible`
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
title website.menu - Direct Relations
class "website.menu" as website_menu
class "res.groups" as res_groups
class "theme.website.menu" as theme_website_menu
class "website" as website
class "website.controller.page" as website_controller_page
class "website.menu" as website_menu
class "website.page" as website_page
website_menu --> theme_website_menu : theme_template_id
website_menu --> website_page : page_id
website_menu --> website_controller_page : controller_page_id
website_menu --> website : website_id
website_menu --> website_menu : parent_id
website_menu --|> website_menu : child_id
website_menu .. res_groups : group_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/website/Models]]

<!-- GENERATED:MODEL -->
