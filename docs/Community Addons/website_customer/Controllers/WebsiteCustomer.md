<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# WebsiteCustomer

- Module: [[docs/Community Addons/website_customer/website_customer|website_customer]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `GoogleMap`
- Routes: 2

## Routes

### `customers`
- Paths: `/customers`, `/customers/country/<model("res.country"):country>`, `/customers/country/<model("res.country"):country>/page/<int:page>`, `/customers/industry/<model("res.partner.industry"):industry>`, `/customers/industry/<model("res.partner.industry"):industry>/country/<model("res.country"):country>`, `/customers/industry/<model("res.partner.industry"):industry>/country/<model("res.country"):country>/page/<int:page>`, `/customers/industry/<model("res.partner.industry"):industry>/page/<int:page>`, `/customers/page/<int:page>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `customers_detail`
- Paths: `/customers/<partner_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/website_customer/Controllers]]

<!-- GENERATED:CONTROLLER -->
