<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/dte_caf_view.xml

- Module: [[docs/Enterprise Addons/l10n_cl_edi/l10n_cl_edi|l10n_cl_edi]]
- Scope: Enterprise Addons
- Source file: `views/dte_caf_view.xml`
- Views: 2
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `view_dte_caf_tree`
- Name: CAF
- Model: `l10n_cl.dte.caf`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `company_id`, `filename`, `final_nb`, `l10n_latam_document_type_id`, `start_nb`, `status`
- XPath or positional patches: 0

### `view_dte_caf_form`
- Name: l10n_cl.dte.caf.form
- Model: `l10n_cl.dte.caf`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `caf_file`, `company_id`, `final_nb`, `issued_date`, `l10n_latam_document_type_id`, `start_nb`, `status`
- Buttons: `action_spend`
- XPath or positional patches: 0

## Actions

- `action_l10n_cl_dte_caf`: `act_window` CAFs

## Menus

- `menu_l10n_cl_dte_caf`: unnamed
- `menu_sii_chile`: Chilean SII

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_cl_edi/Views]]

<!-- GENERATED:VIEWFILE -->
