---
tags: [odoo, config, v19]
aliases: [Configuration, Sources]
---

# Source Configuration

This repository is wired for Odoo 19 only.

## Generator inputs
`[[tools/generate_from_sources.py|tools/generate_from_sources.py]]` reads these environment variables:

- `ODOO19_PATH`
- `ODOO19_COMMUNITY_ADDONS`
- `ODOO19_ENTERPRISE_ADDONS`
- `OUTPUT_ROOT` (optional, defaults to this repository)

## Local paths in this workspace
- `ODOO19_PATH = C:\Users\RafaelRodríguez\sources\repos\odoo19`
- `ODOO19_COMMUNITY_ADDONS = C:\Users\RafaelRodríguez\sources\repos\odoo19\addons`
- `ODOO19_ENTERPRISE_ADDONS = C:\Users\RafaelRodríguez\sources\repos\docker\odoo19-enterprise-sync\enterprise-cache\3ff6ea5148ee9e3209f05e677ba8fff51fc44d0d`
- Reference repo for examples and explanation patterns: `C:\Users\RafaelRodríguez\sources\repos\odoo-skills`

## PowerShell example

```powershell
$env:ODOO19_PATH = 'C:\Users\RafaelRodríguez\sources\repos\odoo19'
$env:ODOO19_COMMUNITY_ADDONS = 'C:\Users\RafaelRodríguez\sources\repos\odoo19\addons'
$env:ODOO19_ENTERPRISE_ADDONS = 'C:\Users\RafaelRodríguez\sources\repos\docker\odoo19-enterprise-sync\enterprise-cache\3ff6ea5148ee9e3209f05e677ba8fff51fc44d0d'
python tools/generate_from_sources.py --scan
```

## Notes
- The generator refreshes addon notes and category indexes for Odoo 19.
- Core notes are curated manually for now.
- Keep `OUTPUT_ROOT` unset unless you intentionally want a second export location.
