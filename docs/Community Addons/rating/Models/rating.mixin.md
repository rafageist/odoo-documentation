<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# rating.mixin

- Module: [[docs/Community Addons/rating/rating|rating]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/rating_mixin.py`
- Python classes: `RatingMixin`
- Description: Rating Mixin
- Inherits: `mail.thread`

## Field footprint

- Detected fields: 8
- Field types: `Binary` x 1, `Float` x 3, `Integer` x 1, `Selection` x 2, `Text` x 1
- Relation fields: 0

## Sample fields

- `rating_avg`: `Float` (comodel `Average Rating`, compute `_compute_rating_stats`)
- `rating_avg_text`: `Selection` (compute `_compute_rating_avg_text`)
- `rating_count`: `Integer` (comodel `Rating count`, compute `_compute_rating_stats`)
- `rating_last_feedback`: `Text` (comodel `Rating Last Feedback`, related `rating_ids.feedback`)
- `rating_last_image`: `Binary` (comodel `Rating Last Image`, related `rating_ids.rating_image`)
- `rating_last_text`: `Selection` (related `rating_ids.rating_text`)
- `rating_last_value`: `Float` (comodel `Rating Last Value`, compute `_compute_rating_last_value`, store `True`)
- `rating_percentage_satisfaction`: `Float` (comodel `Rating Satisfaction`, compute `_compute_rating_satisfaction`)

## Method hints

- Detected methods: 13
- Action methods: none
- Compute methods: `_compute_rating_avg_text`, `_compute_rating_last_value`, `_compute_rating_satisfaction`, `_compute_rating_stats`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/rating/Models]]

<!-- GENERATED:MODEL -->
