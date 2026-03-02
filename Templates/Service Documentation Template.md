---
tags: [template, service, documentation, v19]
status: draft
---

# Service `{{service_name}}`

- Module: `{{module_name}}`
- Entry point: `{{source_path}}`

## Purpose
- Trigger:
- Consumers:
- Expected outcome:

## Flow
1. Input arrives
2. Validation happens
3. Core logic executes
4. Side effects are emitted

```plantuml
@startuml
actor Caller
participant Service
participant Model
database External
Caller -> Service: request
Service -> Model: business logic
Model -> External: optional sync
External --> Model: response
Model --> Service: result
Service --> Caller: output
@enduml
```

## Dependencies
- Internal modules:
- External services:

## Risks
- Failure modes:
- Retries / idempotency:
- Security considerations:
