<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, community, generated, controller]
---

# WebsiteHrRecruitment

- Module: [[docs/Community Addons/website_hr_recruitment/website_hr_recruitment|website_hr_recruitment]]
- Scope: Community Addons
- Source file: `controllers/main.py`
- Base classes: `WebsiteForm`
- Routes: 6

## Routes

### `jobs`
- Paths: `/jobs`, `/jobs/page/<int:page>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `jobs_add`
- Paths: `/jobs/add`
- Type: `jsonrpc`
- Auth: `user`
- Website route: `True`

### `jobs_detail`
- Paths: `/jobs/detail/<model("hr.job"):job>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `job`
- Paths: `/jobs/<model("hr.job"):job>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `jobs_apply`
- Paths: `/jobs/apply/<model("hr.job"):job>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `check_recent_application`
- Paths: `/website_hr_recruitment/check_recent_application`
- Type: `jsonrpc`
- Auth: `public`
- Website route: `True`

## Navigation

- **Parent:** [[docs/Community Addons/website_hr_recruitment/Controllers]]

<!-- GENERATED:CONTROLLER -->
