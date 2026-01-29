# System Fix: 2026-01-29

**Тип:** System Fix (мини-ревизия)  
**Автор:** LLM

---

## Снимок состояния
### Обновления концепта и спецификаций
- Добавлены `PROJECT_OVERVIEW.md` и обновлён `SYSTEM_OVERVIEW.md`
- Введены спеки: `PROJECTIONS_VOCABULARY.md`, `CATALOG_ITEM_CONTRACT.md`
- Обновлены `POINTER_TAGS_AND_QUERY_MODE.md`, `COUNTRY_CONTEXT.md`

### Данные и ассеты
- Флаги приведены к `assets/flags/*.png` (ISO2, lowercase)
- `assets.manifest.json` переключён на `exports.catalogs/registries`

### Viewer (dream-graph)
- `loadExports()` читает manifest + fallback
- Добавлен `activeContext` (projection/entity)
- Улучшена видимость Query Mode (status / hint)

### Инструменты
- `scripts/check-exports.mjs` проверяет наличие экспортов
- Добавлена схема `schemas/assets-manifest.schema.json` (минимальная)

---

## GitHub экспорт
Не выполнен в этом фиксе (нет commit/push).

---

## Следующий System Fix
- Синхронизировать коммиты и выгрузить на GitHub
- Добавить короткий UI‑гайд (2–3 шага) в `SYSTEM_OVERVIEW.md` (если нужно)
