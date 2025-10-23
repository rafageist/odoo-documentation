---
tags: [v18, examples, sales, subscriptions]
status: draft
---
# Service Subscription Example (Odoo 18)

> **Goal:** Demonstrate how to build a custom module that plugs into subscriptions, projects, and the web client. This walkthrough highlights models, views, assets, security, and tests so the reader sees how the framework pieces combine.

## 1. Scenario
- We ship an add-on named `awesome_subscription`.
- Purpose: extend sale subscriptions with an onboarding checklist, customer health score, and a small Owl dashboard widget.
- Touchpoints: ORM, mail chatter, QWeb inheritance, Owl component, security ACLs, scheduled jobs, tests.

## 2. File tree
```text
awesome_subscription/
+-- __manifest__.py
+-- __init__.py
+-- security/
¦   +-- ir.model.access.csv
¦   +-- subscription_security.xml
+-- models/
¦   +-- __init__.py
¦   +-- sale_subscription.py
¦   +-- subscription_health.py
+-- data/
¦   +-- subscription_stage.xml
¦   +-- ir_cron.xml
+-- views/
¦   +-- sale_subscription_views.xml
¦   +-- subscription_health_views.xml
¦   +-- templates.xml
+-- static/
¦   +-- src/
¦       +-- js/
¦       ¦   +-- subscription_dashboard.js
¦       +-- scss/
¦       ¦   +-- subscription_dashboard.scss
¦       +-- xml/
¦           +-- subscription_dashboard.xml
+-- tests/
    +-- test_subscription_health.py
```

## 3. Manifest highlights (`__manifest__.py`)
```python
{
    'name': 'Awesome Subscription',
    'version': '18.0.1.0.0',
    'depends': ['sale_subscription', 'project'],
    'assets': {
        'web.assets_backend': [
            'awesome_subscription/static/src/js/subscription_dashboard.js',
            'awesome_subscription/static/src/scss/subscription_dashboard.scss',
        ],
        'web.assets_qweb': [
            'awesome_subscription/static/src/xml/subscription_dashboard.xml',
        ],
    },
    'data': [
        'security/subscription_security.xml',
        'security/ir.model.access.csv',
        'data/subscription_stage.xml',
        'data/ir_cron.xml',
        'views/sale_subscription_views.xml',
        'views/subscription_health_views.xml',
        'views/templates.xml',
    ],
}
```
- Demonstrates asset bundling explained in `[[Odoo 18/Core/Framework/Web.md]]`.

## 4. Server-side logic
### Models (`models/sale_subscription.py`)
```python
from odoo import api, fields, models, _

class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'

    onboarding_checklist = fields.Text()
    health_score = fields.Integer(default=50)
    health_state = fields.Selection([
        ('good', 'On Track'),
        ('risk', 'At Risk'),
        ('churn', 'Churned'),
    ], compute='_compute_health_state', store=True)

    @api.depends('recurring_monthly', 'health_score')
    def _compute_health_state(self):
        for sub in self:
            if sub.health_score >= 70:
                sub.health_state = 'good'
            elif sub.health_score >= 40:
                sub.health_state = 'risk'
            else:
                sub.health_state = 'churn'

    def action_generate_project(self):
        """Illustrates integration with project module."""
        Project = self.env['project.project']
        for sub in self:
            if not sub.project_id:
                project = Project.create({
                    'name': _('[Onboarding] %s') % sub.name,
                    'partner_id': sub.partner_id.id,
                    'allow_timesheets': True,
                })
                sub.project_id = project.id
```
- Uses ORM patterns described in `[[Odoo 18/Core/Infrastructure/ORM.md]]`.

### Helper model (`subscription_health.py`)
```python
class SubscriptionHealth(models.Model):
    _name = 'subscription.health'
    _description = 'Subscription Health Snapshot'
    _order = 'date desc'

    subscription_id = fields.Many2one('sale.subscription', required=True)
    date = fields.Date(default=fields.Date.context_today)
    mrr = fields.Float()
    health_score = fields.Integer()

    @api.model
    def cron_compute_health(self):
        subs = self.env['sale.subscription'].search([('stage_category', '=', 'progress')])
        for sub in subs:
            score = sub._compute_health_metric()  # Custom method (not shown)
            self.create({
                'subscription_id': sub.id,
                'mrr': sub.recurring_monthly,
                'health_score': score,
            })
```
- `cron_compute_health` connected to `ir_cron` data entry.

## 5. Security
- `subscription_security.xml` grants manager/users groups.
- `ir.model.access.csv` includes read/write for `subscription.health` only to managers.

## 6. Views
### Form inheritance (`sale_subscription_views.xml`)
```xml
<odoo>
  <record id="view_subscription_form_inherit_health" model="ir.ui.view">
    <field name="name">sale.subscription.health.form</field>
    <field name="model">sale.subscription</field>
    <field name="inherit_id" ref="sale_subscription.sale_subscription_view_form"/>
    <field name="arch" type="xml">
      <xpath expr="//sheet/notebook/page[@name='general']" position="after">
        <page string="Health">
          <group>
            <field name="health_score" widget="progressbar"/>
            <field name="health_state" widget="statusbar"/>
            <field name="onboarding_checklist" nolabel="1" widget="html"/>
          </group>
          <field name="project_id"/>
          <button name="action_generate_project" type="object" string="Generate Project" class="oe_highlight"/>
        </page>
      </xpath>
    </field>
  </record>
</odoo>
```
- Shows QWeb inheritance, aligning with `[[Odoo 18/Core/Framework/Web.md]]` templating rules.

### Tree/pivot view for health snapshots (`subscription_health_views.xml`)
- Provide list/pivot to analyze scores over time.

## 7. Owl widget (dashboard)
### Template (`static/src/xml/subscription_dashboard.xml`)
```xml
<t t-name="awesome_subscription.SubscriptionDashboard">
  <div class="o_subscription_dashboard">
    <h3 t-esc="props.title"/>
    <div class="metrics">
      <div class="metric">
        <span class="label">MRR</span>
        <span class="value" t-esc="props.mrr"/>
      </div>
      <div class="metric">
        <span class="label">Health</span>
        <span class="value" t-att-class="props.healthClass" t-esc="props.healthScore"/>
      </div>
    </div>
  </div>
</t>
```

### Component (`static/src/js/subscription_dashboard.js`)
```javascript
/** @odoo-module */
import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import rpc from "web.rpc";

export class SubscriptionDashboard extends Component {
    setup() {
        this.state = useState({ mrr: 0, healthScore: 0, title: 'Loading...' });
        onWillStart(async () => {
            const data = await rpc.query({
                model: 'sale.subscription',
                method: 'get_dashboard_stats',
                args: [],
            });
            this.state.mrr = data.mrr;
            this.state.healthScore = data.health_score;
            this.state.title = data.title;
        });
    }

    get healthClass() {
        return this.state.healthScore >= 70 ? 'o_good' : 'o_warning';
    }
}

registry.category('actions').add('awesome_subscription.subscriptions_dashboard', {
    component: SubscriptionDashboard,
    props: {},
});
```
- Demonstrates Owl usage with `registry`, referencing JS details from the web framework note.

### Template injection (`views/templates.xml`)
```xml
<template id="assets_backend" inherit_id="web.assets_backend">
  <xpath expr="." position="inside">
    <script type="module" src="/awesome_subscription/static/src/js/subscription_dashboard.js"/>
    <link rel="stylesheet" href="/awesome_subscription/static/src/scss/subscription_dashboard.scss"/>
  </xpath>
</template>
```

## 8. Actions & menus
- Add menu for `subscription.health` reporting.
- Client action to open Owl dashboard (`ir.actions.client` with tag `awesome_subscription.subscriptions_dashboard`).

## 9. Tests (`tests/test_subscription_health.py`)
```python
from odoo.tests import TransactionCase

class TestSubscriptionHealth(TransactionCase):
    def test_health_snapshot(self):
        sub = self.env['sale.subscription'].create({
            'name': 'Test Sub',
            'partner_id': self.env.ref('base.partner_admin').id,
        })
        cron = self.env['subscription.health'].cron_compute_health()
        self.assertTrue(self.env['subscription.health'].search([('subscription_id', '=', sub.id)]))
```

## 10. Walkthrough
1. Install module; new stage “Nurturing” added via data file.
2. Confirm sale order with recurring product ? subscription created.
3. Health tab displays score; button generates project automatically.
4. Dashboard action shows Owl widget with aggregated metrics.
5. Cron runs nightly to log health snapshots; managers review pivot report.

## 11. Links to core docs
- ORM usage: `[[Odoo 18/Core/Infrastructure/ORM.md]]`
- Web assets & Owl: `[[Odoo 18/Core/Framework/Web.md]]`
- Subscription process: `[[Odoo 18/Community Addons/Sales/sale_subscription.md]]`
- Projects integration: `[[Odoo 18/Core/Processes/Projects/Index]]`

## 12. To-do
- [ ] Provide downloadable code snippet repository.
- [ ] Add example of unit tests for Owl component (QUnit).
- [ ] Document translation/i18n extraction for JS strings.

## Navigation
- **Parent:** `[[Odoo 18/Examples/Index]]`
- **Related:** `[[Odoo 18/Core/Framework/Web.md]]`, `[[Odoo 18/Core/Processes/Sales/Index]]`, `[[Odoo 18/Community Addons/Sales/sale_subscription.md]]`
