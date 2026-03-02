---
tags: [odoo, core, framework, views]
status: active
---

# views

## Focus
- Server-side XML view architecture, inheritance, and supported attributes.
- Safe extension patterns for list, form, pivot, activity, and related views.

## Canonical sources
- `odoo19/odoo/addons/base/rng`
- `odoo19/odoo/addons/base/models/ir_ui_view.py`
- `odoo19/addons/web/static/src/views`

## Odoo 19 facts worth keeping in mind
- The RNG files under `addons/base/rng` are the most reliable way to confirm what a view root or attribute actually supports.
- New list architectures use `<list>` as the root tag. The grammar explicitly allows attributes such as `editable`, `multi_edit`, `default_order`, `create`, `delete`, `edit`, and `open_form_view`.
- Pivot views explicitly support `disable_linking`, which is useful when the pivot should stay analytical and not drill into source records.
- Activity views have their own grammar in `activity_view.rng`; treat them as a distinct view contract, not just a form/list variation.

## Inheritance guidance
- Do not patch base XML in place. Use inherited views so upgrades and downstream modules keep a mergeable architecture.
- Prefer semantic selectors over positional selectors. Matching by `name` is usually more stable than relying on numeric indexes or deep positional paths.
- Prefer `position="attributes"` over `position="replace"` when the goal is to change behavior rather than remove structure. Replacing a node can break later inherited views that still target the original node.
- Remember that inherited XML files only matter if they are loaded in module data from `__manifest__.py`.

## Safe patterns
```xml
<field name="partner_id" position="attributes">
    <attribute name="readonly">1</attribute>
    <attribute name="invisible">1</attribute>
</field>
```

```xml
<xpath expr="//page[@name='sales']" position="inside">
    <group>
        <field name="sale_order_count"/>
    </group>
</xpath>
```

```xml
<list editable="bottom" multi_edit="1" default_order="name desc">
    <field name="name"/>
    <field name="state"/>
</list>
```

```xml
<pivot disable_linking="1">
    <field name="amount_total" type="measure"/>
    <field name="country_id" type="row"/>
</pivot>
```

## Related notes
- `[[docs/Core/Framework/web]]` for the client-side view registry and rendering runtime.
- `[[docs/Core/Framework/http]]` for controller surfaces that feed actions and view payloads.

## Navigation
- **Parent:** [[docs/Core/Framework/Framework]]
