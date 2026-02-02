# System Overview (Current)

Short, current-state reference. For concept/intent, see `PROJECT_OVERVIEW.md`.

## Core repositories (current)
- `extended-mind`: canon + specs (contracts, vocabularies, context rules)
- `contracts`: exported assets + registries + catalogs (JSON/JSONL)
- `dream-graph`: viewer UI (Visitor scene) consuming contracts

## Data flow (today)
1. `contracts/public/manifests/assets.manifest.json` lists exports.
2. `dream-graph` loads exports via `loadExports()`:
   - catalogs: `ai_catalog.jsonl`, `practice_participation.jsonl`
   - registries: `pointer_tags_registry.json`, `country_registry.json`
3. Query Mode filters catalog rows by `pointer_tags`.

## UI behavior (Visitor scene)
- Tag click => Query Mode (no route change).
- Service panel shows grouped results (Services / Models / Methods / Other).
- Selecting a catalog item adds a refine context (entity) in state, but not a canon node.
- Countries and flags are assets/contexts only (no nodes).

## Current state (Jan 2026)
- Exports manifest structured as `exports.catalogs` + `exports.registries`.
- `loadExports()` in `dream-graph` handles manifest + fallback.
- Flags stored as `contracts/public/assets/flags/*.png`.
- Workbench layer documented (Character/Workbench spec + v2 workbenches for Vova).
- Signals + curated sets introduced as JSONL rows (no canon nodes).
- HF control room: Graph + Telegram Content in Space (read-only graph from contracts).
- System docs established in `extended-mind/docs/system` (intent, goals, functions, guardrails, checks).
- Mechanisms-to-goals map added (`MECHANISMS_TO_GOALS.md`) with UG/LG/MG/SG tags.
- Ideas log now requires Goal links (UG/LG).
- Self‑description goals introduced (LG/MG) with narrative trace rule.
- Practices v1 expanded to 14 axial practices.
- Specs updated:
  - `PROJECTIONS_VOCABULARY.md`
  - `CATALOG_ITEM_CONTRACT.md`
  - `POINTER_TAGS_AND_QUERY_MODE.md`
  - `COUNTRY_CONTEXT.md`
- Living Book Interface goal added (UG‑5) with mechanism links.
- Coverage map reframed as a book‑map (`coverage-map-full.md`) with narrative anchor.
- Story‑nodes added for Living Book Interface and book‑map consolidation.

## Explicit non-goals (now)
- No facets/tag-ocean UI
- No multi-tag AND/OR UI
- No RAG integration
- No new large catalogs

## See also
- `PROJECT_OVERVIEW.md`
- `extended-mind/docs/system/*`
- `extended-mind/docs/ideas/IDEAS_LOG.md`
- `extended-mind/docs/system/INTERFACE_STAGE_CONTEXT.md`
