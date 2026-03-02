<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Onboarding Toolbox

- Scope: Community Addons
- Source: odoo/addons/onboarding
- Dependencies: [[docs/Community Addons/web/web|web]]

## XML Artifacts (detected)

- Views: 4
- Actions: 2
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 12

## Detected Models

- `onboarding.onboarding`
- `onboarding.onboarding.step`
- `onboarding.progress`
- `onboarding.progress.step`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Onboarding Toolbox - Models and Relations
class "onboarding.onboarding" as onboarding_onboarding
class "onboarding.onboarding.step" as onboarding_onboarding_step
class "onboarding.progress" as onboarding_progress
class "onboarding.progress.step" as onboarding_progress_step
onboarding_onboarding .. onboarding_onboarding_step : many2many
onboarding_onboarding --> onboarding_progress : many2one
onboarding_onboarding --|> onboarding_progress : one2many
onboarding_onboarding_step .. onboarding_onboarding : many2many
onboarding_onboarding_step --> onboarding_progress_step : many2one
onboarding_onboarding_step --|> onboarding_progress_step : one2many
class "res.company" as res_company
onboarding_progress --> res_company : many2one
onboarding_progress --> onboarding_onboarding : many2one
onboarding_progress .. onboarding_progress_step : many2many
onboarding_progress_step .. onboarding_progress : many2many
onboarding_progress_step --> onboarding_onboarding_step : many2one
onboarding_progress_step --> res_company : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





