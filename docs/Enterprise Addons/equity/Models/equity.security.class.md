<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# equity.security.class

- Module: [[docs/Enterprise Addons/equity/equity|equity]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/equity_security_class.py`
- Python classes: `EquitySecurityClass`
- Description: Security Class

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 1, `Char` x 1, `Integer` x 2, `Selection` x 1
- Relation fields: 0

## Sample fields

- `class_type`: `Selection`
- `dividend_payout`: `Boolean` (compute `_compute_dividend_payout`, store `True`)
- `name`: `Char`
- `sequence`: `Integer`
- `share_votes`: `Integer` (compute `_compute_share_votes`, store `True`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_display_name`, `_compute_dividend_payout`, `_compute_share_votes`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/equity/Models]]

<!-- GENERATED:MODEL -->
