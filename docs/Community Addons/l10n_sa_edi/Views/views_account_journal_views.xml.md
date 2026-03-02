<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/account_journal_views.xml

- Module: [[docs/Community Addons/l10n_sa_edi/l10n_sa_edi|l10n_sa_edi]]
- Scope: Community Addons
- Source file: `views/account_journal_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_form_inherit`
- Name: account.move.form.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_show_chain_head`
- XPath or positional patches: 2

### `view_account_journal_form`
- Name: account.journal.form.l10n_sa_edi
- Model: `account.journal`
- Type: inferred from arch
- Inherits: `account.view_account_journal_form`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `l10n_sa_compliance_checks_passed`, `l10n_sa_compliance_csid_json`, `l10n_sa_csr`, `l10n_sa_csr_errors`, `l10n_sa_production_csid_json`, `l10n_sa_production_csid_validity`
- Buttons: `%(l10n_sa_edi_otp_wizard_act_window)d`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/l10n_sa_edi/Views]]

<!-- GENERATED:VIEWFILE -->
