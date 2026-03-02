<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# WebsiteTest

- Module: [[docs/Community Addons/test_website/test_website|test_website]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `Home`
- Routes: 37

## Routes

### `test_view`
- Paths: `/test_view`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_view_access_error`
- Paths: `/test_view_access_error`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_ignore_args_converter_only`
- Paths: `/ignore_args/converteronly/<string:a>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_ignore_args_none`
- Paths: `/ignore_args/none`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_ignore_args_a`
- Paths: `/ignore_args/a`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_ignore_args_kw`
- Paths: `/ignore_args/kw`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_ignore_args_converter`
- Paths: `/ignore_args/converter/<string:a>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_ignore_args_converter_nokw`
- Paths: `/ignore_args/converter/<string:a>/nokw`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_company_context`
- Paths: `/multi_company_website`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_lang_url`
- Paths: `/test_lang_url/<model("res.country"):country>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_get_dbname`
- Paths: `/test_get_dbname`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `test_error_view`
- Paths: `/test_error_view`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_user_error_http`
- Paths: `/test_user_error_http`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_user_error_json`
- Paths: `/test_user_error_json`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `test_validation_error_http`
- Paths: `/test_validation_error_http`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_validation_error_json`
- Paths: `/test_validation_error_json`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `test_access_error_json`
- Paths: `/test_access_error_json`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `test_access_error_http`
- Paths: `/test_access_error_http`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_missing_error_json`
- Paths: `/test_missing_error_json`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `test_missing_error_http`
- Paths: `/test_missing_error_http`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_internal_error_json`
- Paths: `/test_internal_error_json`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `test_internal_error_http`
- Paths: `/test_internal_error_http`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_denied_error_json`
- Paths: `/test_access_denied_json`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

### `test_denied_error_http`
- Paths: `/test_access_denied_http`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `get_method`
- Paths: `/get`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `post_method`
- Paths: `/post`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `get_post_method`
- Paths: `/get_post`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `get_post_method_no_multilang`
- Paths: `/get_post_nomultilang`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `empty_controller_test`
- Paths: `/empty_controller_test`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_model_converter_country`
- Paths: `/test_website/country/<model("res.country"):country>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_model_converter_seoname`
- Paths: `/test_website/200/<model("test.model"):rec>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_model_item`
- Paths: `/test_website/model_item/<int:record_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_model_item_sudo`
- Paths: `/test_website/model_item_sudo/<int:record_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_redirect_view_qs`
- Paths: `/test_website/test_redirect_view_qs`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_countries_308`
- Paths: `/test_countries_308`, `/test_countries_308/<model("test.model"):rec>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_sitemap`
- Paths: `/test_website_sitemap`, `/test_website_sitemap/something/<model("test.model"):rec>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `test_model`
- Paths: `/test_model/<model("test.model"):test_model>`
- Type: `http`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/test_website/Controllers]]

<!-- GENERATED:CONTROLLER -->
