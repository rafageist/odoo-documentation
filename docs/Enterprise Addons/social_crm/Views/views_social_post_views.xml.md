---
tags: [odoo, enterprise, generated, views]
---

# views/social_post_views.xml

- Module: [[docs/Enterprise Addons/social_crm/social_crm|social_crm]]
- Scope: Enterprise Addons
- Source file: `views/social_post_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `social_post_view_kanban`
- Name: social.post.view.kanban.inherit.social.crm
- Model: `social.post`
- Type: inferred from arch
- Inherits: `social.social_post_view_kanban`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `leads_opportunities_count`, `use_leads`
- XPath or positional patches: 2

### `social_post_view_form`
- Name: social.post.view.form.inherit.social.crm
- Model: `social.post`
- Type: inferred from arch
- Inherits: `social.social_post_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `leads_opportunities_count`, `use_leads`
- Buttons: `action_redirect_to_leads_opportunities`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/social_crm/Views]]

