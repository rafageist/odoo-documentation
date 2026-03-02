<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# slide.slide.resource

- Module: [[docs/Community Addons/website_slides/website_slides|website_slides]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/slide_slide_resource.py`
- Python classes: `SlideSlideResource`
- Description: Additional resource for a particular slide

## Field footprint

- Detected fields: 8
- Field types: `Binary` x 1, `Char` x 4, `Integer` x 1, `Many2one` x 1, `Selection` x 1
- Relation fields: 1

## Sample fields

- `data`: `Binary` (comodel `Resource`, compute `_compute_reset_resources`, store `True`)
- `download_url`: `Char` (comodel `Download URL`, compute `_compute_download_url`)
- `file_name`: `Char` (store `True`)
- `link`: `Char` (comodel `Link`, compute `_compute_reset_resources`, store `True`)
- `name`: `Char` (comodel `Name`, compute `_compute_name`, store `True`)
- `resource_type`: `Selection`
- `sequence`: `Integer`
- `slide_id`: `Many2one` (comodel `slide.slide`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_download_url`, `_compute_name`, `_compute_reset_resources`
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
title slide.slide.resource - Direct Relations
class "slide.slide.resource" as slide_slide_resource
class "slide.slide" as slide_slide
slide_slide_resource --> slide_slide : slide_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/website_slides/Models]]

<!-- GENERATED:MODEL -->
