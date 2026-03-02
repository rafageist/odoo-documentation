<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# wizard/base_module_install_request_views.xml

- Module: [[docs/Community Addons/base_install_request/base_install_request|base_install_request]]
- Scope: Community Addons
- Source file: `wizard/base_module_install_request_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `base_module_install_review_view_form`
- Name: base.module.install.review.view.form
- Model: `base.module.install.review`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `module_id`, `module_ids`, `modules_description`
- Buttons: `action_install_module`
- XPath or positional patches: 0

### `base_module_install_request_view_form`
- Name: base.module.install.request.view.form
- Model: `base.module.install.request`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `body_html`, `module_id`, `user_ids`
- Buttons: `action_send_request`
- XPath or positional patches: 0

## Actions

- `action_base_module_install_review`: `act_window` You are about to install an extra application

## Navigation

- **Parent:** [[docs/Community Addons/base_install_request/Views]]

<!-- GENERATED:VIEWFILE -->
