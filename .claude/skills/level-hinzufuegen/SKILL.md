---
name: level-hinzufuegen
description: Ein neues Level oder neue Tasten im Typecraft-Spiel hinzufügen oder ändern (Level-Daten, Erzart, Belohnung, Tests). Nutzen, wenn Level, Tastenreihenfolge, Trefferzahlen oder Spitzhacken-Belohnungen geändert werden.
---

# Level hinzufügen oder ändern

Alle Level stehen im Array `LEVELS` in `index.html`. Lies zuerst `docs/level-und-fortschritt.md`.

## Schritte
1. **Regeln beachten** (`CLAUDE.md`): kein Tempodruck, neue Tasten paarweise und von starken zu schwachen Fingern, jedes Level mit neuen Tasten bekommt automatisch eine Einführung (Feld `neu` nicht leer).
2. **Neues Level ans Ende anhängen.** Der Spielstand speichert Sterne pro Level-Index, ein Einfügen in der Mitte verschiebt den Fortschritt. Wenn es doch nötig ist: Spielstand migrieren und `SHOP[].need` sowie alle `reward`-Verweise prüfen.
3. Level-Objekt anlegen:
   ```js
   {name:'Level 17: + Ä', keys:UPPER([...alle bisherigen Tasten, 'ä']), neu:['ä'], ore:'diamond',
    hint:'Neu: Ä (rechter kleiner Finger).', target:16}
   ```
   - `keys` muss alle aktiven Tasten enthalten (sonst sind sie abgedunkelt und werden nicht gewertet).
   - `ore`: `'coal'` (Stein-Stufe), `'iron'` (obere Reihe), `'diamond'` (untere Reihe). Eine neue Erzart braucht eine Textur (`--<name>` in `tex()`, CSS-Klassen `.block.<name>` und `.nk.<name>`).
   - Übungslevel ohne neue Tasten: `neu:[]`, optional `oreRow` (0 oben, 2 unten).
   - Belohnung: `reward:'<spitzhacke>'`. Die Spitzhacke muss in `PICKS` und `HOTBAR` stehen. `hasPick` findet sie über das Level mit diesem `reward`.
4. **Neue Taste?** Sie muss in `KEYROWS` stehen, einem Finger in `FINGERS` zugeordnet sein (`fingerOf`), und das 45-Spalten-Raster muss passen (`docs/architektur.md`). Ä ist schon in `KEYROWS` und `FINGERS`.
5. **Prüfen** mit der Anleitung `spieltest-browser`: Einführung, Spiel, Abschluss-Fenster, Screenshot ansehen.
6. `docs/level-und-fortschritt.md` aktualisieren (Tabelle) und kurz im Antworttext nennen, was neu ist und wie lang es ist.
