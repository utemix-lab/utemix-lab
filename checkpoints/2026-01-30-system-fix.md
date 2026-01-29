# System Fix: 2026-01-30

**Тип:** System Fix (мини-ревизия)  
**Автор:** LLM

---

## Снимок состояния
### Концепт и цели
- Введена система целей UG/LG/MG/SG и правило обязательной привязки к UG/LG
- Добавлены: `SYSTEM_INTENT`, `SYSTEM_GOALS`, `SYSTEM_FUNCTIONS`, `SYSTEM_GUARDRAILS`, `SYSTEM_CHECKS`
- Добавлен `DECISION_BACKBONE` и `MECHANISMS_TO_GOALS`

### Идеи и сверка
- `IDEAS_LOG.md` переведён на human‑first (RU) + machine tags
- Goal links оформлены как `[UG-*]`/`[LG-*]`/`[MG-*]`/`[SG-*]`
- `SYSTEM_CHECKS.md` обновлён под механизмы и goal links

### System Fix
- Добавлен шаблон и чеклист System Fix в `CHECKPOINT_GUIDE.md`
- Обновлён `SYSTEM_OVERVIEW.md` (текущее состояние)

---

## GitHub экспорт
- [x] commit
- [x] push

---

## Следующий System Fix
- Свести цели и механизмы к 5–7 опорным строкам (без бюрократии)
