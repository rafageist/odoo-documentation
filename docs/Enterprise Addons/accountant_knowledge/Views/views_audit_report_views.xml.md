<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/audit_report_views.xml

- Module: [[docs/Enterprise Addons/accountant_knowledge/accountant_knowledge|accountant_knowledge]]
- Scope: Enterprise Addons
- Source file: `views/audit_report_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `audit_report_view_search`
- Name: audit.report.view.search
- Model: `audit.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `title`
- XPath or positional patches: 0

### `audit_report_view_kanban`
- Name: audit.report.view.kanban
- Model: `audit.report`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `color`, `company_id`, `end_date`, `knowledge_article_id`, `responsible_user_ids`, `start_date`, `status`, `title`
- Buttons: `action_audit_report_pdf`
- XPath or positional patches: 0

### `audit_report_view_form`
- Name: audit.report.view.form
- Model: `audit.report`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `end_date`, `knowledge_template_article_id`, `responsible_user_ids`, `start_date`, `title`
- XPath or positional patches: 0

## Actions

- `action_audit_report`: `act_window` Audit Reports
- `action_audit_report_quick_create`: `act_window` Create an Audit Report

## Navigation

- **Parent:** [[docs/Enterprise Addons/accountant_knowledge/Views]]

<!-- GENERATED:VIEWFILE -->
