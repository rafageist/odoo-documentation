<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/l10n_it_edi_doi_declaration_of_intent_views.xml

- Module: [[docs/Community Addons/l10n_it_edi_doi/l10n_it_edi_doi|l10n_it_edi_doi]]
- Scope: Community Addons
- Source file: `views/l10n_it_edi_doi_declaration_of_intent_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_l10n_it_edi_doi_declaration_of_intent_search`
- Name: l10n_it_edi_doi.declaration_of_intent.search
- Model: `l10n_it_edi_doi.declaration_of_intent`
- Type: `search`
- Root tag: `search`
- Field references: 2
- Sample fields: `protocol_number_part1`, `protocol_number_part2`
- XPath or positional patches: 0

### `view_l10n_it_edi_doi_form`
- Name: l10n_it_edi_doi.declaration_of_intent.form
- Model: `l10n_it_edi_doi.declaration_of_intent`
- Type: inferred from arch
- Root tag: `form`
- Field references: 15
- Sample fields: `company_id`, `currency_id`, `end_date`, `invoice_ids`, `invoiced`, `issue_date`, `not_yet_invoiced`, `partner_id`, `protocol_number_part1`, `protocol_number_part2`, and 5 more
- Buttons: `action_open_invoice_ids`, `action_open_sale_order_ids`, `action_reactivate`, `action_reset_to_draft`, `action_revoke`, `action_terminate`, `action_validate`
- XPath or positional patches: 0

### `view_l10n_it_edi_doi_tree`
- Name: l10n_it_edi_doi.declaration_of_intent.list
- Model: `l10n_it_edi_doi.declaration_of_intent`
- Type: inferred from arch
- Root tag: `list`
- Field references: 13
- Sample fields: `company_id`, `currency_id`, `end_date`, `invoiced`, `issue_date`, `not_yet_invoiced`, `partner_id`, `protocol_number_part1`, `protocol_number_part2`, `remaining`, and 3 more
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/l10n_it_edi_doi/Views]]

<!-- GENERATED:VIEWFILE -->
