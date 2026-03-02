---
tags: [odoo, core, masterdata, partner]
status: backlog
---

# res.partner

## Focus
- Shared partner model used by CRM, Sales, Accounting, Contacts, and Website flows in Odoo
- Important identity, company, address, and commercial fields that drive behavior across modules

## Source areas
- `odoo19/addons/base/models/res_partner.py`
- `odoo19/addons/contacts`

## Notes to develop
- Commercial partner logic
- Address and company-dependent behavior
- Downstream effects in sales, invoices, and portal access

## Navigation
- **Parent:** [[docs/Core/Master Data/Master Data]]
