# Level, Fortschritt, Shop

Alle Daten stehen im Array `LEVELS` in `index.html`. Index = Level-Nummer.

| Nr | Name | Neue Tasten | Erz | Treffer | Belohnung |
|----|------|-------------|-----|---------|-----------|
| 0 | Hände auflegen | alle 8 Finger + Daumen | Erde | 9 (F J D S A K L Ö ␣) | Holzspitzhacke |
| 1 | A S D F | A S D F | Kohle | 16 | nur linke Hand |
| 2 | J K L Ö | J K L Ö | Kohle | 16 | nur rechte Hand |
| 3 | + G H | G H | Kohle | 16 | |
| 4 | Ganze Reihe | – | Kohle (zufällig ca. jeder dritte Block) | 32 | Steinspitzhacke |
| 5 | + E I | E I | Eisen | 16 | |
| 6 | + R U | R U | Kupfer | 16 | |
| 7 | + T Z | T Z | Lapislazuli | 16 | |
| 8 | + W O | W O | Eisen | 16 | |
| 9 | + Q P Ü | Q P Ü | Kupfer | 16 | |
| 10 | Obere Reihe | – | Erze der Tasten der oberen Reihe (je Taste wie oben) | 32 | Eisenspitzhacke |
| 11 | + C , | C , | Diamant | 16 | |
| 12 | + V M | V M | Gold | 16 | |
| 13 | + B N | B N | Redstone | 16 | |
| 14 | + X . | X . | Diamant | 16 | |
| 15 | + Y - | Y - | Gold | 16 | |
| 16 | Alle Reihen | – | Erze der Tasten der unteren Reihe (je Taste wie oben) | 48 | Diamantspitzhacke |
| 17 | + Ä ß | Ä ß | Redstone | 16 | |
| 18 | Zahlen | 1 2 3 4 5 6 7 8 9 0 (nur die Zahlen, sonst keine Taste aktiv) | Obsidian | 30 | |

**Ä** ist ab Level 18 dabei. **ß** liegt in einer zusätzlichen Reihe über Q–Ü (Zahlenreihe, `KEYPOS` = Reihe −1; in Level 18 steht dort nur ß, ab Level 19 alle Zahlen `NUMROW`: 1 beginnt in Spalte 1 über Q, ß in Spalte 41; die Reihe liegt eine halbe Taste weiter rechts als auf echten Tastaturen, damit sie ins Raster passt). Diese Reihe erscheint nur in Levels, deren `keys` ß enthalten; dann bekommt `.kb` die Klasse `num` und alles darunter rutscht per `--o` eine Reihe nach unten. Beide tippt der rechte kleine Finger. Level 19 führt die Zahlen ein (`FINGERS`: 1 kleiner Finger links, 2 Ring, 3 Mitte, 4 und 5 Zeigefinger links, 6 und 7 Zeigefinger rechts, 8 Mitte, 9 Ring, 0 kleiner Finger rechts). Der Spielstand ist `v:3`: die Werkbänke stehen jetzt bei Index 20–25.

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
- **Werkbänke:** Wort-Werkbänke haben 5 Herzen, Satz-Werkbänke 10 Herzen (`maxHearts(L)`). Die Genauigkeit für k Herzen steigt gleichmäßig von 70 % (1 Herz) bis 95 % (alle Herzen), siehe `heartAcc()`. Die Herz-Größe passt sich an (`heartSize()`). Ältere Spielstände mit 3 Herzen bleiben gültig.

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
Pro Nutzer ein Eintrag: `localStorage['typecraft-user-<name klein>']` (Namensliste in `typecraft-users`, letzter Nutzer in `typecraft-current`). Beim ersten Namen wird der alte Stand `typecraft-v1` übernommen. Inhalt: `{v:2, emeralds, stars:{levelIndex:sterne}, owned:{id:true}, biome}`. Alle Zugriffe sind in try/catch, das Spiel läuft auch ohne Speicher.

Spielstand `v:2`: Level 0 „Hände auflegen“ kam später dazu, `load()` verschiebt alte Herzen (ohne `v`) um eins nach hinten.

## Pfad, Werkbänke, Bauplätze und Bücher
**Menü:** ein Pfad (`renderPfad()`) in zwei Zeilen zu je 11 Spalten, darunter das Bücherregal (`shelfHTML()`). In der Mitte stehen die 19 Buchstaben-Level. Wer ein Level mit mindestens 1 Herz schafft, findet ein **Rezept** (Wörter) oder eine **Vorlage** (Sätze). Dann geht ein Zweig ab und das Zusatzlevel erscheint: Werkbänke nach unten, Bauplätze nach oben. Das Level, das etwas enthält, trägt oben rechts ein kleines Rezept- bzw. Vorlagen-Symbol. Ungefundenes ist nicht zu sehen, nur der nächste Bauplatz in der Kette steht als gestrichelter Umriss da. Die Zusatzlevel sind freiwillig, der Buchstabenpfad geht immer weiter.

Alle Zusatzlevel sind Einträge mit `chest:true` am Ende von `LEVELS` (Index 19–32, Herzen wie bei Leveln in `st.stars[i]`). Freigeschaltet (`unlocked(i)`): `ready:true` und das Level `need` hat mindestens 1 Herz. Das Abschluss-Fenster zeigt „Rezept gefunden!“ bzw. „Vorlage gefunden!“.

| Zusatzlevel | Tasten | `need` (Level mit dem Fund) |
|-------|--------|------------------------------|
| Werkbank 1 | A S D F + Umschalt | Level 2 (Index 1) |
| Werkbank 2 | A S D F J K L Ö + linke Umschalt | Level 3 (2) |
| Werkbank 3 | + G H | Level 4 (3) |
| Werkbank 4 | Grundreihe | Level 5 (4) |
| Werkbank 5 | + obere Reihe | Level 11 (10) |
| Werkbank 6 | alle Reihen | Level 17 (16) |
| Bauplatz 1 (3 Wörter) | bis X . (ohne Y, Bindestrich, Ä, ß) | Level 15 (14) |
| Bauplatz 2 (4 Wörter) | + Y - (ohne Ä, ß) | Level 16 (15) |
| Bauplatz 3 (5 Wörter) | wie Bauplatz 2 | Level 17 (16) |
| Bauplatz 4 (6 Wörter) | ganze Tastatur mit Ä, ß | Level 18 (17) |
| Bauplatz 5–8 (7 bis 10 Wörter) | ganze Tastatur | der vorige Bauplatz (Kette) |

Früher als Level 15 gibt es keine Sätze: Mit der Grundreihe und der oberen Reihe fehlen N, M, C, B, damit lassen sich keine Minecraft-Sätze schreiben. Die Sätze für Bauplatz 1–3 haben deshalb keine Ä und ß (Skript-Prüfung: alle Zeichen müssen in `keys` stehen).

**Bücherregal:** Jeder Bauplatz mit mindestens 1 Herz gibt einmal ein Buch (`st.books[k]`, k = Nummer des Bauplatzes 0–7; alte Spielstände bekommen die Bücher beim Laden nachträglich). Die Bücher haben die Farben der Bauwerke (`BOOK_COLORS`). Im Menü zeigt das Regal 8 Plätze, leer sind sie grau mit Buch-Umriss. Im Abschluss-Fenster erscheint ein Mini-Regal, das neue Buch fällt in seinen Platz (CSS `bookin`, Bling-Ton `xpPing()`). Bei 8 Büchern geht die Tür auf. Was dahinter liegt (Text-Level mit Fluss und Tempo), ist noch nicht gebaut: die Tür zeigt „Bald geöffnet“.

Bauplätze (`sentences:true`, früher Satz-Werkbänke): Der Satz steht als Text in der Werkbank-Leiste (getippte Zeichen werden grün). Es entstehen keine Gegenstände mehr, sondern ein **Bauwerk auf dem Bauplatz** unter der Leiste (`#bau`, `bauPlan()`): Jeder getippte Buchstabe setzt Blöcke von unten nach oben, am Level-Ende steht das fertige Bauwerk (auch im Abschluss-Fenster). Die acht Werkbänke bauen der Reihe nach `BAU_LEVEL`: Holzhaus, Steinhaus, Steinturm, Steinburg, Kupferhaus, Eisenturm, Goldburg, Diamantburg (Formen in `BAU_ART`, W = Wand, R = Dach, G = Glas, D = Tür). Ton: pro Buchstabe nur ein leiser Klick (`klick()`), das helle Bling (`xpPing()`) gibt es einmal am Satzende; die Pause zwischen zwei Buchstaben ist nur 50 ms, damit schnelles Tippen nicht verschluckt wird. Die Leertaste kommt als breiter Block (`.block.big.space`) über der Leertaste, beide Daumen leuchten. Satzzeichen nur Komma, Punkt und Bindestrich; weitere Zeichen und Enter stehen als Tickets in Notion.

Truhe 1: Beginn mit Einführung der Umschalt-Taste (Block „⇧“, Fenster „Neue Taste freigeschaltet“). Danach 9 Wörter (`CHEST1_WORDS`, je einmal, zufällig), Herzen und Smaragde wie bei Leveln. Alle Anfangsbuchstaben sind groß: Kohleblock = Großbuchstabe (Umschalt gedrückt halten), Steinblock = Kleinbuchstabe. Oben steht das Wort, der aktuelle Buchstabe ist gelb. Umschalt steht rechts neben dem rechten Arm (Zeile der Leertaste) und wird vom rechten kleinen Finger bedient.

Umschalt: Großbuchstaben tippt man mit der Umschalt der **anderen** Hand. Rechte Umschalt (`shift`, rechter kleiner Finger) für Buchstaben der linken Hand, linke Umschalt (`shiftl`, linker kleiner Finger, links neben Y) für Buchstaben der rechten Hand (`shiftFor(k)`). Akzeptiert wird jede Umschalt-Taste, hervorgehoben wird die passende. Truhe 2 führt die linke Umschalt ein (`newShift`), Truhe 3 hat keine Einführung und startet gleich mit den Wörtern. `rounds` = wie oft jedes Wort vorkommt.

**Umschalt-Einführung** (Phase `cshift`, Zustand `cs`, `introKeys` je Truhe: D F A bzw. J K L): 1. Umschalt-Block ⇧ mit Fingername „Kleiner Finger“, das Kind drückt Umschalt. 2. Danach steht ein kleiner Steinblock („d“) mit „⇧ halten“ über der Taste. Solange Umschalt gehalten wird, verwandelt er sich in einen Kohleblock „D“ (`csMorph`, loslassen = wieder klein). 3. Nur mit gehaltener Umschalt zählt der Anschlag, sonst wackeln Block und Umschalt-Taste, ohne Fehler. Nach drei Buchstaben beginnen die Wörter.

## Crafting an den Werkbänken und Inventar
Es gibt keine großen Blöcke mehr über den Fingern: die Buchstaben stehen nur oben. Bei Wort-Werkbänken steht in der Mitte das Wort groß (`#craft.words`, ein Block pro Buchstabe, Material des Gegenstands; der Block wird dort mit Rissen und Krümeln abgebaut und bleibt als Mulde): der aktuelle Block hat einen gelben Rahmen mit hüpfendem Dreieck, spätere sind etwas dunkler, erledigte werden zu leeren gestrichelten Mulden. Rechts steht eine Werkbank mit 3×3-Gitter (`.ctable`) und Ergebnis-Slot; ganz rechts daneben die kleine Truhe mit Zähler. Jeder abgebaute Block fliegt in den nächsten Gitter-Slot. Sind alle Buchstaben drin, entsteht im Ergebnis-Slot der Gegenstand (Name darunter) und wandert in die Truhe. Satz-Werkbänke (7–14) behalten die alte Leiste mit Text (`.csent`). Jedes Wort hat einen Gegenstand, seine Blöcke bestehen aus dem passenden Material (`CRAFT`, `chestSeq`). Welche Gegenstände vorkommen, hängt an der besten Spitzhacke (`pickTier()`); bessere Gegenstände sind häufiger (Gewicht 1 + 2 × Stufe).

Gecraftet werden nur Gegenstände der Kategorie Dekoration (https://de.minecraft.wiki/w/Handwerk/Dekoration). Lapislazuli und Redstone werden abgebaut, nicht gecraftet, und kommen deshalb nicht vor.

| Spitzhacke | Material → Gegenstand |
|---|---|
| Holz | Holz → Bett, Holztür, Leiter, Zaun; Stein → Ofen, Mauer, Hebel; Kohle → Fackel |
| Stein | Eisen → Laterne, Kessel, Amboss, Eisentür, Eisengitter, Trichter; Kupfer → Kupfergitter, Kupferlaterne, Kupfertruhe, Kupferfackel |
| Eisen | Gold → Feinwägeplatte; Redstone → Redstone-Fackel; Diamant → Zaubertisch, Plattenspieler |
| Diamant | Obsidian → Endertruhe |

Gecraftete Gegenstände zählt `st.items = {id: Anzahl}` im Spielstand. Im Menü zeigt der Bereich „Inventar“ gecraftete Gegenstände mit Namen und Anzahl; alles, was noch nicht gecraftet wurde, ist nur ein leerer grauer Inventar-Slot (ohne Namen). Das Abschluss-Fenster zeigt die Beute der Runde, neue Gegenstände mit „neu!“. Obsidian hat eine eigene Textur (`--obsidian`), aber es gibt noch keine Obsidian-Level mit Buchstaben, nur den Obsidian-Gegenstand in den Truhen.


**Stand v4 des Spielstands:** Die frühere Grundhaltung (F J + Leertaste, Holzblöcke) entfällt; die Holzspitzhacke gibt Level 0 „Hände auflegen“. F steht jetzt in Level 1 (linke Hand), J in Level 2 (rechte Hand). Alle Indizes ab dem alten Level 2 sind um eins nach vorn gerückt (Migration in `load()`). Der Code für die Grundhaltung (`grundAsk`, `GRUND_SEQ`) ist noch da, wird aber nicht mehr benutzt.
