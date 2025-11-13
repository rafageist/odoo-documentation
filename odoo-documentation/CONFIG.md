---
tags: [odoo, config]
aliases: [Configuración, Fuentes]
---

# Configuración de Fuentes (Odoo 18/19)

Define rutas locales a los código fuente para habilitar la generación automática de notas.

Variables de entorno esperadas por [[tools/generate_from_sources.py|el generador]]:

- `ODOO18_PATH`: ruta al core de Odoo 18 CE (por ejemplo, carpeta con `odoo/__init__.py`).
- `ODOO19_PATH`: ruta al core de Odoo 19 CE.
- `ODOO18_COMMUNITY_ADDONS`: carpeta con addons community para Odoo 18.
- `ODOO18_ENTERPRISE_ADDONS`: carpeta con addons enterprise para Odoo 18.
- `ODOO19_COMMUNITY_ADDONS`: carpeta con addons community para Odoo 19.
- `ODOO19_ENTERPRISE_ADDONS`: carpeta con addons enterprise para Odoo 19.

Opcional:

- `OUTPUT_ROOT`: carpeta destino para notas (por defecto, este vault).

Alternativamente, puedes pasar rutas mediante flags del script: `--o18`, `--o19`, `--o18c`, `--o18e`, `--o19c`, `--o19e`.

Ejemplo (PowerShell):

```powershell
$env:ODOO18_PATH = 'D:\sources\odoo-18'
$env:ODOO19_PATH = 'D:\sources\odoo-19'
$env:ODOO18_COMMUNITY_ADDONS = 'D:\sources\odoo-18\addons'
$env:ODOO18_ENTERPRISE_ADDONS = 'D:\sources\enterprise18'
$env:ODOO19_COMMUNITY_ADDONS = 'D:\sources\odoo-19\addons'
$env:ODOO19_ENTERPRISE_ADDONS = 'D:\sources\enterprise19'
python odoo-documentation/tools/generate_from_sources.py --scan
```

Valores por defecto (si no defines nada) según tu estructura:

- `odoo` se usa como Odoo 18 CE root; sus addons en `odoo/addons`.
- `odoo19` se usa como Odoo 19 CE root; sus addons en `odoo19/addons`.
- `enterprise18` se usa como raíz de addons Enterprise 18.
- `enterprise19` se usa como raíz de addons Enterprise 19.

Comparativas básicas (nuevos/deprecados) pueden generarse con:

```powershell
python odoo-documentation/tools/generate_from_sources.py --scan --compare
```
