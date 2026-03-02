<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# Survey

- Module: [[docs/Community Addons/survey/survey|survey]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 15

## Routes

### `survey_test`
- Paths: `/survey/test/<string:survey_token>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `survey_retry`
- Paths: `/survey/retry/<string:survey_token>/<string:answer_token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `survey_start`
- Paths: `/survey/start/<string:survey_token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `survey_display_page`
- Paths: `/survey/<string:survey_token>/<string:answer_token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `survey_get_background`
- Paths: `/survey/<string:survey_token>/get_background_image`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `survey_section_get_background`
- Paths: `/survey/<string:survey_token>/<int:section_id>/get_background_image`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `survey_get_question_image`
- Paths: `/survey/get_question_image/<string:survey_token>/<string:answer_token>/<int:question_id>/<int:suggested_answer_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `survey_begin`
- Paths: `/survey/begin/<string:survey_token>/<string:answer_token>`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `survey_next_question`
- Paths: `/survey/next_question/<string:survey_token>/<string:answer_token>`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `survey_submit`
- Paths: `/survey/submit/<string:survey_token>/<string:answer_token>`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `survey_print`
- Paths: `/survey/print/<string:survey_token>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `show_certification_pdf`
- Paths: `/survey/<model("survey.survey"):survey>/certification_preview`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `survey_get_certification_preview`
- Paths: `/survey/<model("survey.survey"):survey>/get_certification_preview`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `survey_get_certification`
- Paths: `/survey/<int:survey_id>/get_certification`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `survey_report`
- Paths: `/survey/results/<model("survey.survey"):survey>`
- Type: `http`
- Auth: `user`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/survey/Controllers]]

<!-- GENERATED:CONTROLLER -->
