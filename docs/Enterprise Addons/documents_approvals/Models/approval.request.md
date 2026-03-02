<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# approval.request

- Module: [[docs/Enterprise Addons/documents_approvals/documents_approvals|documents_approvals]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/approval_request.py`
- Python classes: `ApprovalRequest`
- Inherits: `documents.mixin`

## Field footprint

- Detected fields: 2
- Field types: `Boolean` x 1, `Integer` x 1
- Relation fields: 0

## Sample fields

- `documents_count`: `Integer` (compute `_compute_documents_count`)
- `documents_enabled`: `Boolean` (related `company_id.documents_approvals_settings`)

## Method hints

- Detected methods: 9
- Action methods: `action_get_attachment_view`
- Compute methods: `_compute_documents_count`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/documents_approvals/Models]]

<!-- GENERATED:MODEL -->
