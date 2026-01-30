# System Fix: 2026-01-28

**Тип:** System Fix (мини-ревизия)  
**Автор:** LLM + человек

---

## Снимок состояния
### Обновления концепта и спецификаций
- уточнён контракт catalog items (signals/curated_sets)
- зафиксированы workbench’и Вовы v2

### Данные и ассеты
- `signals.jsonl` и `curated_sets.jsonl` как rows (без узлов)
- обновлён manifest exports
- флаги остаются ассетами (PNG)

### Viewer (dream-graph)
- UI остаётся read‑only consumer contracts
- Query Mode остаётся базовым режимом

### Инструменты
- HF control room: Graph + Telegram Content (две вкладки)

---

## GitHub экспорт
- [ ] commit
- [ ] push
- [ ] HF Space rebuild (push triggers)
- [ ] UI surfaces rebuild (if touched)
- [ ] dream-graph build + deploy (если менялся `dream-graph/`)

---

## Следующий System Fix
- собрать обратную связь по Vova workbenches + signals/curated_sets
- решить, нужен ли отдельный Control Room workbench
