# Level, Fortschritt, Shop

Alle Daten stehen im Array `LEVELS` in `index.html`. Index = Level-Nummer.

| Nr | Name | Neue Tasten | Erz | Treffer | Belohnung |
|----|------|-------------|-----|---------|-----------|
| 0 | Grundhaltung | F J + Leertaste | Holz | 6 (F J Leertaste, zweimal) | Holzspitzhacke |
| 1 | A S D | A S D | Kohle | 16 | nur linke Hand (A S D F) |
| 2 | K L Ö | K L Ö | Kohle | 16 | nur rechte Hand (J K L Ö) |
| 3 | + G H | G H | Kohle | 16 | |
| 4 | Ganze Reihe | – | Kohle (zufällig ca. jeder dritte Block) | 32 | Steinspitzhacke |
| 5 | + E I | E I | Eisen | 16 | |
| 6 | + R U | R U | Eisen | 16 | |
| 7 | + T Z | T Z | Eisen | 16 | |
| 8 | + W O | W O | Eisen | 16 | |
| 9 | + Q P Ü | Q P Ü | Eisen | 16 | |
| 10 | Obere Reihe | – | Eisen = Tasten der oberen Reihe | 32 | Eisenspitzhacke |
| 11 | + C , | C , | Diamant | 16 | |
| 12 | + V M | V M | Diamant | 16 | |
| 13 | + B N | B N | Diamant | 16 | |
| 14 | + X . | X . | Diamant | 16 | |
| 15 | + Y - | Y - | Diamant | 16 | |
| 16 | Alle Reihen | – | Diamant = Tasten der unteren Reihe | 48 | Diamantspitzhacke |

Die Taste **Ä** ist auf der Bildschirmtastatur sichtbar, aber in keinem Level enthalten.

## Level-Felder
```js
{name, keys:[...aktive Tasten], neu:[...neue Tasten], hint:'Text', target:Trefferzahl,
 ore:'coal'|'iron'|'diamond',   // Erzart der neuen Tasten (Standard: coal)
 oreRow:0|2,                    // nur in Übungslevels: Tasten dieser Reihe sind Erz (0 oben, 2 unten)
 intro:true,                    // nur Grundhaltung
 reward:'holz'|'stein'|'eisen'|'diamant'}   // Spitzhacke im Abschluss-Fenster
```
- Bekannte Tasten erscheinen als **Stein**, neue Tasten des Levels als **Erz** (immer nur ein Block, nie zweimal dieselbe Taste hintereinander). Neue Tasten werden doppelt gewichtet.
- Ein Level ist freigeschaltet, wenn das vorige mindestens 1 Stern hat.

## Sterne und Smaragde
- Die Sterne hängen an der Zahl der Fehler (`starBudget(target)`, `starsFor()`), nicht an einer sichtbaren Prozentzahl. Intern gilt weiter: Genauigkeit ≥ 95 % → 3 Sterne, ≥ 85 % → 2, ≥ 70 % → 1, sonst 0 (nochmal, ohne Druck). Die Grundhaltung und alle Einführungen geben immer 3 Sterne.

  | Level-Länge | ★★★ | ★★ | ★ |
  |---|---|---|---|
  | 16 Tasten | 0 Fehler | bis 2 | bis 6 |
  | 32 Tasten | bis 1 | bis 5 | bis 13 |
  | 48 Tasten | bis 2 | bis 8 | bis 20 |
- Live-Leiste im Spiel (`#goal` in der Kopfzeile, `updateGoal()`): „Treffer / Ziel“, Fortschrittsbalken, drei Sterne und „Noch N Fehler für ★★“. Jeder Fehler über dem Budget lässt einen Stern erlöschen (er kommt nicht zurück). Nur in der Spielphase sichtbar.
- Abschluss-Fenster zeigt „16 Blöcke, 2 Fehler“ und was für den nächsten Stern nötig ist, keine Prozent.
- +1 Smaragd pro Treffer, +3 bei mindestens 1 Stern. Hinweis-Knopf kostet 3 Smaragde (hebt den aktuellen Block 3 Sekunden hervor).
- Eine Spitzhacke gehört dem Kind, sobald das Level mit ihrer `reward` mindestens 1 Stern hat (`hasPick`).

## Shop (Array `SHOP`)
| Id | Art | Preis | Bedingung |
|----|-----|-------|-----------|
| wolf | Haustier (Emoji 🐺) | 5 | – |
| katze | Haustier (Emoji 🐱) | 10 | – |
| hoehle | Biom Höhle | 8 | Level 3 mit Stern |

Haustiere stehen zwischen den Armen und hüpfen bei Treffern. Biome sind CSS-Verläufe (`wald`, `hoehle`). Skins gibt es noch nicht.

## Spielstand
`localStorage['typecraft-v1']` = `{emeralds, stars:{levelIndex:sterne}, owned:{id:true}, biome}`. Alle Zugriffe sind in try/catch, das Spiel läuft auch ohne Speicher.
