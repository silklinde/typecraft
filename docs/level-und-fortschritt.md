# Level, Fortschritt, Shop

Alle Daten stehen im Array `LEVELS` in `index.html`. Index = Level-Nummer.

| Nr | Name | Neue Tasten | Erz | Treffer | Belohnung |
|----|------|-------------|-----|---------|-----------|
| 0 | Hände auflegen | alle 8 Finger + Daumen | Erde | 9 (F J D S A K L Ö ␣) | – |
| 1 | Grundhaltung | F J + Leertaste | Holz | 6 (F J Leertaste, zweimal) | Holzspitzhacke |
| 2 | A S D | A S D | Kohle | 16 | nur linke Hand (A S D F) |
| 3 | K L Ö | K L Ö | Kohle | 16 | nur rechte Hand (J K L Ö) |
| 4 | + G H | G H | Kohle | 16 | |
| 5 | Ganze Reihe | – | Kohle (zufällig ca. jeder dritte Block) | 32 | Steinspitzhacke |
| 6 | + E I | E I | Eisen | 16 | |
| 7 | + R U | R U | Kupfer | 16 | |
| 8 | + T Z | T Z | Lapislazuli | 16 | |
| 9 | + W O | W O | Eisen | 16 | |
| 10 | + Q P Ü | Q P Ü | Kupfer | 16 | |
| 11 | Obere Reihe | – | Erze der Tasten der oberen Reihe (je Taste wie oben) | 32 | Eisenspitzhacke |
| 12 | + C , | C , | Diamant | 16 | |
| 13 | + V M | V M | Gold | 16 | |
| 14 | + B N | B N | Redstone | 16 | |
| 15 | + X . | X . | Diamant | 16 | |
| 16 | + Y - | Y - | Gold | 16 | |
| 17 | Alle Reihen | – | Erze der Tasten der unteren Reihe (je Taste wie oben) | 48 | Diamantspitzhacke |
| 18 | + Ä ß | Ä ß | Redstone | 16 | |

**Ä** ist ab Level 18 dabei. **ß** liegt in einer zusätzlichen Reihe über Q–Ü (Zahlenreihe nur mit ß, `KEYPOS['ß']` = Reihe −1, Spalte 39). Diese Reihe erscheint nur in Levels, deren `keys` ß enthalten; dann bekommt `.kb` die Klasse `num` und alles darunter rutscht per `--o` eine Reihe nach unten. Beide tippt der rechte kleine Finger.

## Level-Felder
```js
{name, keys:[...aktive Tasten], neu:[...neue Tasten], hint:'Text', target:Trefferzahl,
 ore:'coal'|'iron'|'copper'|'lapis'|'diamond'|'gold'|'redstone',   // Erzart der neuen Tasten (Standard: coal); in Übungslevels gilt je Taste das Erz aus ihrem Einführungslevel (`ORE_OF`)
 oreRow:0|2,                    // nur in Übungslevels: Tasten dieser Reihe sind Erz (0 oben, 2 unten)
 intro:true, haende:true,        // Level 0 (Hände auflegen); intro allein = Grundhaltung
 reward:'holz'|'stein'|'eisen'|'diamant'}   // Spitzhacke im Abschluss-Fenster
```
- Bekannte Tasten erscheinen als **Stein**, neue Tasten des Levels als **Erz** (immer nur ein Block, nie zweimal dieselbe Taste hintereinander). Neue Tasten werden doppelt gewichtet.
- Ein Level ist freigeschaltet, wenn das vorige mindestens 1 Herz hat.

## Herzen und Smaragde
- Die Herzen hängen an der Zahl der Fehler (`starBudget(target)`, `starsFor()`), nicht an einer sichtbaren Prozentzahl. Intern gilt weiter: Genauigkeit ≥ 95 % → 3 Herzen, ≥ 85 % → 2, ≥ 70 % → 1, sonst 0 (nochmal, ohne Druck). Die Grundhaltung und alle Einführungen geben immer 3 Herzen.

  | Level-Länge | ❤❤❤ | ❤❤ | ❤ |
  |---|---|---|---|
  | 16 Tasten | 0 Fehler | bis 2 | bis 6 |
  | 32 Tasten | bis 1 | bis 5 | bis 13 |
  | 48 Tasten | bis 2 | bis 8 | bis 20 |
- Live-Leiste im Spiel (`#goal` in der Kopfzeile, `updateGoal()`): „Treffer / Ziel“, Fortschrittsbalken, drei Herzen und „Noch N Fehler für ❤❤“. Jeder Fehler über dem Budget lässt ein Herz erlöschen (er kommt nicht zurück). Nur in der Spielphase sichtbar.
- Abschluss-Fenster zeigt „16 Blöcke, 2 Fehler“ und was für den nächsten Herz nötig ist, keine Prozent.
- +1 Smaragd pro Treffer, +3 bei mindestens 1 Herz. Hinweis-Knopf kostet 3 Smaragde (hebt den aktuellen Block 3 Sekunden hervor).
- Eine Spitzhacke gehört dem Kind, sobald das Level mit ihrer `reward` mindestens 1 Herz hat (`hasPick`).

## Shop (Array `SHOP`)
| Id | Art | Preis | Bedingung |
|----|-----|-------|-----------|
| wolf | Haustier (Emoji 🐺) | 5 | – |
| katze | Haustier (Emoji 🐱) | 10 | – |
| hoehle | Biom Höhle | 8 | Level 4 mit Herz |

Haustiere stehen zwischen den Armen und hüpfen bei Treffern. Biome sind CSS-Verläufe (`wald`, `hoehle`). Skins gibt es noch nicht.

## Spielstand
`localStorage['typecraft-v1']` = `{v:2, emeralds, stars:{levelIndex:sterne}, owned:{id:true}, biome}`. Alle Zugriffe sind in try/catch, das Spiel läuft auch ohne Speicher.

Spielstand `v:2`: Level 0 „Hände auflegen“ kam später dazu, `load()` verschiebt alte Herzen (ohne `v`) um eins nach hinten.

## Werkbänke (Wörter-Level, früher „Truhen“)
Menü-Bereiche: „Minen“ (die Level), „Craften“ (6 Werkbänke mit Wörtern), „Inventar“ (gecraftete Gegenstände), „Shop“. Am Ende einer Werkbank wird eine offene Truhe gezeigt, aus der die erhaltenen Gegenstände ragen (Zahl = Anzahl; Vorderwand liegt davor). Im Menü steht unter der Werkbank nur ein freier Platz für die Herzen, keine Buchstaben. Sie stehen als Einträge mit `chest:true` am Ende von `LEVELS` (Index 19–24, Sterne wie bei Leveln in `st.stars[i]`) und erscheinen nicht in der Level-Liste. Freigeschaltet (`unlocked(i)`): `ready:true` und das Level `need` hat mindestens 1 Herz. Gesperrte Truhen sind kleiner, grau und haben ein Vorhängeschloss.

| Werkbank | Tasten | Freigeschaltet durch | Stand |
|-------|--------|----------------------|-------|
| 1 | A S D F + Umschalt | Level 2 | spielbar |
| 2 | A S D F J K L Ö + linke Umschalt | Level 3 | spielbar (kurz: 5–6 Wörter einmal, ca. 20 Buchstaben) |
| 3 | + G H | Level 4 | spielbar (kurz: 5–6 Wörter einmal, ca. 20 Buchstaben) |
| 4–6 | offen | – | noch gesperrt |

Truhe 1: Beginn mit Einführung der Umschalt-Taste (Block „⇧“, Fenster „Neue Taste freigeschaltet“). Danach 6 Wörter (`CHEST1_WORDS`, je einmal, zufällig), 19 Buchstaben, Herzen und Smaragde wie bei Leveln. Alle Anfangsbuchstaben sind groß: Kohleblock = Großbuchstabe (Umschalt gedrückt halten), Steinblock = Kleinbuchstabe. Oben steht das Wort, der aktuelle Buchstabe ist gelb. Umschalt steht rechts neben dem rechten Arm (Zeile der Leertaste) und wird vom rechten kleinen Finger bedient.

Umschalt: Großbuchstaben tippt man mit der Umschalt der **anderen** Hand. Rechte Umschalt (`shift`, rechter kleiner Finger) für Buchstaben der linken Hand, linke Umschalt (`shiftl`, linker kleiner Finger, links neben Y) für Buchstaben der rechten Hand (`shiftFor(k)`). Akzeptiert wird jede Umschalt-Taste, hervorgehoben wird die passende. Truhe 2 führt die linke Umschalt ein (`newShift`), Truhe 3 hat keine Einführung und startet gleich mit den Wörtern. `rounds` = wie oft jedes Wort vorkommt.

**Umschalt-Einführung** (Phase `cshift`, Zustand `cs`, `introKeys` je Truhe: D F A bzw. J K L): 1. Umschalt-Block ⇧ mit Fingername „Kleiner Finger“, das Kind drückt Umschalt. 2. Danach steht ein kleiner Steinblock („d“) mit „⇧ halten“ über der Taste. Solange Umschalt gehalten wird, verwandelt er sich in einen Kohleblock „D“ (`csMorph`, loslassen = wieder klein). 3. Nur mit gehaltener Umschalt zählt der Anschlag, sonst wackeln Block und Umschalt-Taste, ohne Fehler. Nach drei Buchstaben beginnen die Wörter.

## Crafting an den Werkbänken und Inventar
Oben in der Mitte steht eine Werkbank-Leiste (`#craft`): ein Slot pro Buchstabe, Pfeil, Ergebnis-Slot; rechts eine kleine Truhe mit Zähler. Jeder abgebaute Block fliegt als kleiner Block in seinen Slot. Ist das Wort fertig, entsteht im Ergebnis-Slot ein Gegenstand (mit Namen) und wandert in die Truhe. Jedes Wort hat einen Gegenstand, seine Blöcke bestehen aus dem passenden Material (`CRAFT`, `chestSeq`). Welche Gegenstände vorkommen, hängt an der besten Spitzhacke (`pickTier()`); bessere Gegenstände sind häufiger (Gewicht 1 + 2 × Stufe).

Gecraftet werden nur Gegenstände der Kategorie Dekoration (https://de.minecraft.wiki/w/Handwerk/Dekoration). Lapislazuli und Redstone werden abgebaut, nicht gecraftet, und kommen deshalb nicht vor.

| Spitzhacke | Material → Gegenstand |
|---|---|
| Holz | Holz → Bett, Holztür, Leiter, Zaun; Stein → Ofen, Bruchsteinmauer, Hebel; Kohle → Fackel |
| Stein | Eisen → Laterne, Kessel, Amboss, Eisentür, Eisengitter, Trichter |
| Eisen | Diamant → Zaubertisch, Plattenspieler |
| Diamant | Obsidian → Endertruhe |

Gecraftete Gegenstände zählt `st.items = {id: Anzahl}` im Spielstand. Im Menü zeigt der Bereich „Inventar“ gecraftete Gegenstände mit Namen und Anzahl; alles, was noch nicht gecraftet wurde, ist nur ein leerer grauer Inventar-Slot (ohne Namen). Das Abschluss-Fenster zeigt die Beute der Runde, neue Gegenstände mit „neu!“. Obsidian hat eine eigene Textur (`--obsidian`), aber es gibt noch keine Obsidian-Level mit Buchstaben, nur den Obsidian-Gegenstand in den Truhen.
