<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/ldap_installer_views.xml

- Module: [[docs/Community Addons/auth_ldap/auth_ldap|auth_ldap]]
- Scope: Community Addons
- Source file: `views/ldap_installer_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `res_company_ldap_view_tree`
- Name: res.company.ldap.list
- Model: `res.company.ldap`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `company`, `ldap_server`, `ldap_server_port`
- XPath or positional patches: 0

### `view_ldap_installer_form`
- Name: res.company.ldap.form
- Model: `res.company.ldap`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `company`, `create_user`, `ldap_base`, `ldap_binddn`, `ldap_filter`, `ldap_password`, `ldap_server`, `ldap_server_port`, `ldap_tls`, `sequence`, and 1 more
- Buttons: `test_ldap_connection`
- XPath or positional patches: 0

## Actions

- `action_ldap_installer`: `act_window` Setup your LDAP Server

## Navigation

- **Parent:** [[docs/Community Addons/auth_ldap/Views]]

<!-- GENERATED:VIEWFILE -->
