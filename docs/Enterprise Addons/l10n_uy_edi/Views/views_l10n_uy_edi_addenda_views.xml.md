---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_uy_edi_addenda_views.xml

- Module: [[docs/Enterprise Addons/l10n_uy_edi/l10n_uy_edi|l10n_uy_edi]]
- Scope: Enterprise Addons
- Source file: `views/l10n_uy_edi_addenda_views.xml`
- Views: 4
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `l10n_uy_edi_addenda_view_search`
- Name: l10n_uy_edi.addenda.view.search
- Model: `l10n_uy_edi.addenda`
- Type: inferred from arch
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 0

### `l10n_uy_edi_addenda_view_tree`
- Name: l10n.uy.addenda.view.tree
- Model: `l10n_uy_edi.addenda`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `company_id`, `content`, `is_legend`, `name`, `type`
- XPath or positional patches: 0

### `l10n_uy_edi_addenda_view_form_only_item`
- Name: l10n.uy.addenda.view.form
- Model: `l10n_uy_edi.addenda`
- Type: inferred from arch
- Inherits: `l10n_uy_edi.l10n_uy_edi_addenda_view_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `company_id`, `type`
- XPath or positional patches: 0

### `l10n_uy_edi_addenda_view_form`
- Name: l10n.uy.addenda.view.form
- Model: `l10n_uy_edi.addenda`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `company_id`, `content`, `is_legend`, `name`, `type`
- XPath or positional patches: 0

## Actions

- `action_l10n_uy_edi_addenda`: `act_window` Addendas and Disclosures

## Menus

- `menu_l10n_uy_addenda`: unnamed
- `menu_dgi_config`: DGI

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_uy_edi/Views]]

