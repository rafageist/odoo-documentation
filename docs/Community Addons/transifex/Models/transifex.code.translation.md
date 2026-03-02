<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# transifex.code.translation

- Module: [[docs/Community Addons/transifex/transifex|transifex]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/transifex_code_translation.py`
- Python classes: `TransifexCodeTranslation`
- Description: Code Translation

## Field footprint

- Detected fields: 5
- Field types: `Char` x 2, `Selection` x 1, `Text` x 2
- Relation fields: 0

## Sample fields

- `lang`: `Selection`
- `module`: `Char`
- `source`: `Text`
- `transifex_url`: `Char` (comodel `Transifex URL`, compute `_compute_transifex_url`)
- `value`: `Text`

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_transifex_url`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/transifex/Models]]

<!-- GENERATED:MODEL -->
