<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# UserInputSession

- Module: [[docs/Community Addons/survey/survey|survey]]
- Scope: Community Addons
- Source file: `controllers/survey_session_manage.py`
- Base classes: `http.Controller`
- Routes: 7

## Routes

### `survey_session_manage`
- Paths: `/survey/session/manage/<string:survey_token>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `survey_session_next_question`
- Paths: `/survey/session/next_question/<string:survey_token>`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `survey_session_results`
- Paths: `/survey/session/results/<string:survey_token>`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `survey_session_leaderboard`
- Paths: `/survey/session/leaderboard/<string:survey_token>`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `survey_session_code`
- Paths: `/s`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `survey_start_short`
- Paths: `/s/<string:session_code>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `survey_check_session_code`
- Paths: `/survey/check_session_code/<string:session_code>`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/survey/Controllers]]

<!-- GENERATED:CONTROLLER -->
