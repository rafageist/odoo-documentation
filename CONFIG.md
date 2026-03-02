---
tags: [odoo, config]
aliases: [Configuration, Sources]
---

# Source Configuration

This repository is wired for a single active Odoo version.

## Generator inputs
`[[tools/generate_from_sources.py|tools/generate_from_sources.py]]` reads these environment variables:

- `ODOO_PATH`
- `ODOO_COMMUNITY_ADDONS`
- `ODOO_ENTERPRISE_ADDONS`
- `OUTPUT_ROOT` (optional, defaults to this repository)

## Local source roots
- `ODOO_PATH = <workspace>/odoo19`
- `ODOO_COMMUNITY_ADDONS = <workspace>/odoo19/addons`
- `ODOO_ENTERPRISE_ADDONS = <workspace>/docker/odoo19-enterprise-sync/enterprise-cache/<snapshot>`
- Reference repo for examples and explanation patterns: `<workspace>/odoo-skills`

## PowerShell example

```powershell
$env:ODOO_PATH = 'C:\Users\RafaelRodríguez\sources\repos\odoo19'
$env:ODOO_COMMUNITY_ADDONS = 'C:\Users\RafaelRodríguez\sources\repos\odoo19\addons'
$env:ODOO_ENTERPRISE_ADDONS = 'C:\Users\RafaelRodríguez\sources\repos\docker\odoo19-enterprise-sync\enterprise-cache\3ff6ea5148ee9e3209f05e677ba8fff51fc44d0d'
python tools/generate_from_sources.py --scan
```

## Notes
- The generator refreshes addon notes and category indexes under `docs/`.
- Core notes are curated manually for now.
- Keep `OUTPUT_ROOT` unset unless you intentionally want a second export location.
