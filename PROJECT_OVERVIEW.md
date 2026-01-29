# PROJECT OVERVIEW (Concept)

## 1) What this project is (short)
A graph-oriented navigation system for knowledge, practices, and tools that:
- does not try to become a second internet,
- does not build a full ontology of everything,
- provides a minimal canon + powerful navigation over external data.

It is designed for:
- orientation in complex technological and cultural domains,
- exploration of tools, practices, and capabilities,
- demonstrating paths of thought and work (via characters and practices),
- future RAG/LLM integration without rewriting the architecture.

## 2) Core principle
Minimal canon — maximal coverage.

We deliberately separate:
- meaning structure (canon),
- data mass (catalogs),
- reading contexts (projections),
- interaction modes (modes).

## 3) What the system does NOT do (by design)
- Does not store “everything about everything”.
- Does not create a page for every service/model/tool.
- Does not turn tags, countries, or capabilities into graph nodes.
- Does not force a single “correct” route for the user.

## 4) Main layers
### 4.1 Canon
Minimal ontology fixed in `universe.json`:
- Domains (continents of knowledge)
- Practices (ways of applying/moving)
- Characters (guides/perspectives)
- System nodes (the system and its principles)

Canon is small, stable, and edited deliberately. It is the single source of truth for structure.

### 4.2 Catalogs
External data stored as JSONL rows (services, models, methods, etc).

**Catalog items are not nodes. They are rows.**

Catalogs:
- do not enter the canon,
- can be large and mutable,
- can be removed without breaking structure.

### 4.3 Projections (contexts)
Axes for reading the world, not entities.

Examples:
- `cap:lipsync` — capability
- `provider:krea` — provider
- `country:jp` — country context
- `domain:ai` — domain context

Projections:
- are not nodes,
- are not pages,
- are not ontology,
- exist only as context keys for filtering and focus.

All projections are carried via `pointer_tags`.

### 4.4 Pointer Tags
Pointer tags are key-strings attached to catalog rows.

They:
- have no standalone ontology meaning,
- are used for filtering,
- may map to external sources (HF, PWC, etc).

### 4.5 Modes
Modes are interaction states (UI + logic), not canon nodes.

Current core mode:
**Query Mode**
- activated by clicking a tag,
- does not change the route or graph geometry,
- filters catalogs by active context.

## 5) User logic (examples)
Example: capability
- user clicks `cap:lipsync`
- system activates Query Mode
- system shows all catalog rows with this tag
- groups results (services / models / methods)
- offers external links

Example: country (conceptual)
- user applies `country:jp` context
- system filters catalogs by country
- no “country page”, no graph node

## 6) Role of the graph
The graph is a map, not the territory.

It provides:
- orientation,
- meaning links,
- routes and perspectives.

Data oceans remain outside the graph, but are reachable through it.

## 7) Where the system lives (repos)
- `extended-mind`: canon + architecture specs + vocabularies
- `contracts`: assets, flags, registries, catalogs, manifests
- `dream-graph`: viewer UI (Visitor scene), Query Mode, contracts loading

## 8) Data flow (as-is)
- `assets.manifest.json` lists exports
- `dream-graph` loads exports via `loadExports()`
- Query Mode filters catalog rows by `pointer_tags`

## 9) Current boundaries (Jan 2026)
- Canon is minimal and stable
- Catalogs are connected as exports
- Query Mode works
- Projections are formalized in specs
- Flags are context assets, not entities
- RAG/LLM not connected yet

## 10) Explicit non-goals (now)
- no tag-ocean / facets UI
- no multi-tag AND/OR logic
- no auto-generated knowledge
- no attempt to cover “the whole world”

## 11) Where it can evolve
Later the system can:
- add RAG on top of catalogs,
- generate summaries on demand,
- build personalized routes,
- turn Practices and Characters into guides,
- record system history as narratives.

Architecture already anticipates this.

## 12) Short LLM context (copy as-is)
“We keep the canon minimal (universe.json). External data lives in JSONL catalogs. Navigation is done via projection tags (cap:, provider:, country:) that activate Query Mode. Tags, countries, and catalog items are not nodes. The graph is a map, catalogs are the territory.”

## See also
- `SYSTEM_OVERVIEW.md`
