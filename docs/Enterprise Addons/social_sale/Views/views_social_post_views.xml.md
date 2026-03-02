<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/social_post_views.xml

- Module: [[docs/Enterprise Addons/social_sale/social_sale|social_sale]]
- Scope: Enterprise Addons
- Source file: `views/social_post_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `social_post_view_kanban`
- Name: social.post.view.kanban.inherit.social.sale
- Model: `social.post`
- Type: inferred from arch
- Inherits: `social.social_post_view_kanban`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `sale_invoiced_amount`, `sale_quotation_count`
- XPath or positional patches: 2

### `social_post_view_form`
- Name: social.post.view.form.inherit.social.sale
- Model: `social.post`
- Type: inferred from arch
- Inherits: `social.social_post_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `sale_invoiced_amount`, `sale_quotation_count`
- Buttons: `action_redirect_to_invoiced`, `action_redirect_to_quotations`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_sale/Views]]

<!-- GENERATED:VIEWFILE -->
