<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# Website

- Module: [[docs/Community Addons/website/website|website]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `Home`
- Routes: 44

## Routes

### `index`
- Paths: `/`
- Auth: `public`
- Website route: `True`

### `website_force`
- Paths: `/website/force/<int:website_id>`
- Type: `http`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `client_action_redirect`
- Paths: `/@/`, `/@/<path:path>`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `web_login`
- Paths: `<dynamic>`
- Auth: `public`
- Website route: `True`

### `website_languages`
- Paths: `/website/get_languages`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `change_lang`
- Paths: `/website/lang/<lang>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `country_infos`
- Paths: `/website/country_infos/<model("res.country"):country>`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `robots`
- Paths: `/robots.txt`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `sitemap_xml_index`
- Paths: `/sitemap.xml`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `favicon`
- Paths: `/favicon.ico`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `website_info`
- Paths: `/website/info`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `website_configurator`
- Paths: `/website/configurator`, `/website/configurator/<int:step>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `social`
- Paths: `/website/social/<string:social>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `get_suggested_link`
- Paths: `/website/get_suggested_links`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `save_session_layout_mode`
- Paths: `/website/save_session_layout_mode`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `get_dynamic_filter`
- Paths: `/website/snippet/filters`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `get_dynamic_snippet_filters`
- Paths: `/website/snippet/options_filters`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `get_dynamic_snippet_templates`
- Paths: `/website/snippet/filter_templates`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `get_current_currency`
- Paths: `/website/get_current_currency`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `autocomplete`
- Paths: `/website/snippet/autocomplete`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `pages_list`
- Paths: `/pages`, `/pages/page/<int:page>`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `hybrid_list`
- Paths: `/website/search`, `/website/search/<string:search_type>`, `/website/search/<string:search_type>/page/<int:page>`, `/website/search/page/<int:page>`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `pagenew`
- Paths: `/website/add`, `/website/add/<path:path>`
- Type: `http`
- Auth: `user`
- Website route: `True`

### `get_new_page_templates`
- Paths: `/website/get_new_page_templates`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `save_xml`
- Paths: `/website/save_xml`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `get_switchable_related_views`
- Paths: `/website/get_switchable_related_views`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `reset_template`
- Paths: `/website/reset_template`
- Type: `jsonrpc`
- Auth: `user`

### `seo_suggest`
- Paths: `/website/seo_suggest`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `get_alt_images`
- Paths: `/website/get_alt_images`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `update_alt_images`
- Paths: `/website/update_alt_images`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `update_broken_links`
- Paths: `/website/update_broken_links`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `get_seo_data`
- Paths: `/website/get_seo_data`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `check_can_modify_any`
- Paths: `/website/check_can_modify_any`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `google_console_search`
- Paths: `/google<string(length=16):key>.html`
- Type: `http`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `google_maps_api_key`
- Paths: `/website/google_maps_api_key`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`
- Readonly: `True`

### `google_font_metadata`
- Paths: `/website/google_font_metadata`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `theme_customize_data_get`
- Paths: `/website/theme_customize_data_get`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `theme_customize_data`
- Paths: `/website/theme_customize_data`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `theme_customize_bundle_reload`
- Paths: `/website/theme_customize_bundle_reload`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`
- Readonly: `True`

### `update_footer_template`
- Paths: `/website/update_footer_template`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `theme_upload_font`
- Paths: `/website/theme_upload_font`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `actions_server`
- Paths: `/website/action/<path_or_xml_id_or_id>`, `/website/action/<path_or_xml_id_or_id>/<path:path>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `get_assets_editor_resources`
- Paths: `/website/get_assets_editor_resources`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `update_field_translation`
- Paths: `/website/field/translation/update`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/website/Controllers]]

<!-- GENERATED:CONTROLLER -->
