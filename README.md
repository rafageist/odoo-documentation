# Odoo Documentation 19

Documentation workspace focused on the current Odoo release in use, with every note anchored to local source code.

## What lives here
- `docs/` contains the canonical documentation tree for core topics, community addons, and enterprise addons.
- `templates/` contains reusable authoring templates and diagram snippets for modules, models, services, and business processes.
- `tools/` contains generators and maintenance scripts for refreshing documentation from code.
- `CONFIG.md`, `Documentation Playbook.md`, `Index.md`, and `TAGS.md` define the working rules for the repo.

## Source of truth
- Community core: `<workspace>/odoo19`
- Enterprise addons: `<workspace>/docker/odoo19-enterprise-sync/enterprise-cache/<snapshot>`
- Reference material for richer examples: `<workspace>/odoo-skills`

## Repository rules
- One canonical note per module, stored at `docs/<scope>/<technical_name>/<technical_name>.md`.
- Category folders such as `Finance`, `Sales`, or `Operations` are indexes only; they do not hold duplicate module notes.
- Odoo 18, migration-only content, and 18-to-19 comparison notes are intentionally out of scope.
- The repository tracks a single active Odoo version at a time; when the next major release becomes the focus, the tree evolves in place and Git history preserves the previous state.
- Generated module sections can be refreshed, but curated analysis must remain outside the generated markers.
