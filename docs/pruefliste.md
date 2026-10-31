# Prüfliste Typecraft

Stand: 31.10.2026, geprüft gegen `index.html` (letzter Commit `f77725f`).

**So benutzt du sie:** Vor jedem Commit auf `main` den Schnellcheck (Abschnitt A) machen. Vor einer Auslieferung an Kinder oder Testpersonen die ganze Liste durchgehen. Fehler kurz notieren: Abschnitt, Schritt, Gerät, Screenshot.

---

## 0. Vorbereitung

- [ ] Testgeräte festlegen: mindestens Mac mit Safari, Chrome, Firefox. Windows mit Chrome und Edge, wenn möglich.
- [ ] Tastatur auf **Deutsch (QWERTZ)** stellen. Ö, Ä, Ü und ß müssen über echte Tasten kommen.
- [ ] Vor jedem Durchlauf den Spielstand löschen (Browser-Entwicklerwerkzeuge → Anwendung → Lokaler Speicher → alle `typecraft-…`-Einträge entfernen). Dann ist alles frisch.
- [ ] Zusätzlich einen Durchlauf mit altem Spielstand machen (siehe Abschnitt K).
- [ ] Fenstergrößen vorbereiten: 1280×720, 1440×900, 1920×1080, 1024×768, 1000×600, 900×600.

---

## A. Schnellcheck vor jedem Commit (ca. 5 Minuten)

- [ ] `index.html` öffnet sich ohne Fehler in der Konsole.
- [ ] Menü erscheint, Level 1 lässt sich starten.
- [ ] Fünf Tastendrücke eines Level-1-Blocks funktionieren, falsche Taste zählt als Fehler.
- [ ] Ein Level bis zum Abschluss-Fenster durchspielen, Enter schließt es.
- [ ] Nach Neuladen bleibt der Fortschritt erhalten.
- [ ] `node --check` auf das Skript (JS aus `<script>`) ist grün.
- [ ] `python3 tests/spieltest.py` läuft durch, "Browserfehler: keine".
- [ ] Die Screenshots in `tests/ausgabe/` mit Blick auf Layoutfehler angesehen.

---

## B. Start und Namen

- [ ] Ein neuer Name lässt sich anlegen. Groß-/Kleinschreibung spielt keine Rolle (`Anna` und `anna` sind dieselbe Person).
- [ ] Zwei Namen lassen sich anlegen, jeder hat seinen eigenen Fortschritt, Sterne und Smaragde.
- [ ] Zwischen Namen wechseln funktioniert, der zuletzt gewählte Name bleibt nach Neuladen aktiv.
- [ ] Ein Name lässt sich löschen. Der Fortschritt dieses Namens ist danach weg, die anderen bleiben.
- [ ] Der Kopf-Avatar (Nummer je Name) bleibt nach Neuladen gleich.
- [ ] Ein Name mit Sonderzeichen oder Leerzeichen funktioniert (z. B. `Lena M.`).

---

## C. Level 0 „Hände auflegen“

- [ ] Zuerst nur die Hände, dann die Tastatur, dann Finger mit Namen über der Taste.
- [ ] Der passende Finger hebt sich, sein Name steht darüber, ein Erdblock mit dem Buchstaben erscheint.
- [ ] Neun Tastendrücke (F J D S A K L Ö ␣). Falsche Taste zählt nicht.
- [ ] Die Einblendung lässt sich überspringen.
- [ ] Am Ende gibt es die Holzspitzhacke, im Abschluss-Fenster zu sehen.
- [ ] Die Hände bewegen sich in dieser Zeit nicht (nur die Finger).

---

## D. Grundregeln (gelten für alle Level)

- [ ] **Kein Zeitdruck:** Ab Level 1 steht immer nur ein Block ruhig da. Er fällt nicht, er bleibt, bis er getippt ist.
- [ ] **Richtige Spalte:** Der Block steht in der Spalte der Taste auf der Bildschirmtastatur.
- [ ] **Falsche Taste:** Der Block wackelt, zählt als Fehler, nichts bricht ab, kein Game Over.
- [ ] **Abbau:** Ein richtiger Tastendruck baut den Block ab (Risse, Wackeln, Krümel), danach kommt der nächste.
- [ ] **Keine gleiche Taste zweimal hintereinander.**
- [ ] **Hände ruhig:** Während des Spiels bewegen sich nur die Finger. Die Arme wackeln nicht, sie stehen fest.
- [ ] **Daumen auf der Leertaste:** Die Leertaste ist eine breite Taste, beide Daumen liegen darauf.
- [ ] **Nur abbaubare Blöcke:** Es gibt keine grauen „gesperrt“-Blöcke.
- [ ] **Smaragde:** +1 pro Treffer, +3 bei mindestens einem Herz. Der Zähler oben rechts stimmt.
- [ ] **Hinweis-Knopf:** kostet 3 Smaragde, hebt den aktuellen Block 3 Sekunden hervor. Bei weniger als 3 Smaragden lässt er sich nicht auslösen.
- [ ] **Nur Desktop:** Auf Touch-Geräten ohne Tastatur erscheint der Hinweis „Typecraft braucht einen Computer mit Tastatur.“

---

## E. Einführung neuer Tasten

Gilt für jedes Level mit neuen Tasten (Level 1, 2, 3, 5 bis 9, 11 bis 15, 17, 18).

- [ ] Die neuen Tasten erscheinen als große Erzblöcke über ihrer Taste.
- [ ] Oben im schwarzen Bereich steht das Fenster „Neue Buchstaben freigeschaltet“.
- [ ] Jede neue Taste wird genau einmal getippt.
- [ ] Danach erscheinen die Blöcke einzeln, die Einführung startet nicht erneut.
- [ ] Die Erzart stimmt mit der Tabelle in `docs/level-und-fortschritt.md` überein (Kohle, Eisen, Kupfer, Lapislazuli, Gold, Redstone, Diamant, Obsidian).

---

## F. Abschluss-Fenster

- [ ] Erscheint **1 Sekunde** nach dem letzten Treffer, nicht früher.
- [ ] In dieser Sekunde lösen Tastendrücke nichts aus (sie zählen nicht).
- [ ] Wächst sichtbar aus der Mitte.
- [ ] Enter schließt es und führt weiter.
- [ ] Text stimmt: „N Blöcke, M Fehler“, und es steht, was für den nächsten Herzen nötig ist. Keine Prozentzahl.
- [ ] Die angezeigten Herzen stimmen mit der Fehlerzahl überein (siehe G).
- [ ] Bei Leveln mit Belohnung erscheint die Spitzhacke (Level 0 Holz, 4 Stein, 10 Eisen, 16 Diamant).
- [ ] Die Beute zeigt neue Gegenstände mit „neu!“ (nur bei Werkbänken).
- [ ] Das nächste Level bleibt gesperrt, bis das vorige mindestens 1 Herz hat.

---

## G. Herzen und Sterne

Die Herzen hängen an der Fehlerzahl. Das Budget steht in `starBudget()`.

| Länge | ❤❤❤ | ❤❤ | ❤ |
|---|---|---|---|
| 16 Tasten | 0 Fehler | bis 2 | bis 6 |
| 32 Tasten | bis 1 | bis 5 | bis 13 |
| 48 Tasten | bis 2 | bis 8 | bis 20 |

- [ ] Grenzfälle durchprobieren: bei 16 Tasten 0, 1, 2, 3 und 6, 7 Fehler (ab 7 kein Herz mehr).
- [ ] Die Grundhaltung und alle Einführungen geben immer 3 Herzen.
- [ ] Die Live-Leiste (oben, „Treffer / Ziel“) zählt richtig mit.
- [ ] „Noch N Fehler für ❤❤“ stimmt, sobald ein Fehler passiert.
- [ ] Ein erloschenes Herz kommt nicht zurück.
- [ ] Werkbänke: 5 Herzen (Wort-Werkbänke), 10 Herzen (Satz-Werkbänke). Die Herzgröße passt sich an.

---

## H. Level-Durchlauf

Für jedes Level prüfen: Trefferzahl, neue Tasten, Erzart, Belohnung, Freischaltung des nächsten Levels.

| Level | Name | Treffer | Belohnung | Besonderheit prüfen |
|---|---|---|---|---|
| 1 | A S D F | 16 | – | nur linke Hand, Einführung |
| 2 | J K L Ö | 16 | – | nur rechte Hand, Ö über echter Taste |
| 3 | + G H | 16 | – | |
| 4 | Ganze Reihe | 32 | Steinspitzhacke | ca. jeder dritte Block ist Kohle |
| 5 | + E I | 16 | – | Eisen |
| 6 | + R U | 16 | – | Kupfer |
| 7 | + T Z | 16 | – | Lapislazuli |
| 8 | + W O | 16 | – | Eisen |
| 9 | + Q P Ü | 16 | – | Kupfer, Ü |
| 10 | Obere Reihe | 32 | Eisenspitzhacke | Erze je nach Taste |
| 11 | + C , | 16 | – | Diamant, Komma |
| 12 | + V M | 16 | – | Gold |
| 13 | + B N | 16 | – | Redstone |
| 14 | + X . | 16 | – | Diamant, Punkt |
| 15 | + Y - | 16 | – | Gold, Minus |
| 16 | Alle Reihen | 48 | Diamantspitzhacke | Erze je nach Taste |
| 17 | + Ä ß | 16 | – | Ä und ß, ß-Reihe über Q–Ü |
| 18 | Zahlen (1–0) | 30 | – | Obsidian, Zahlenreihe, Ziffern |

- [ ] Jedes Level startet mit Einführung (wenn neue Tasten dabei sind) und endet mit Abschluss-Fenster.
- [ ] Nach Level 17 erscheint die Zahlenreihe, bis ß und die Zahlen korrekt angeschlagen werden.
- [ ] Level 18: der ß-Block liegt nicht auf dem Ä-Block (Commit `cfe4e30`).
- [ ] Level 19 (Zahlen einführen, `FINGERS`): Finger-Zuordnung je Ziffer stimmt.
- [ ] Die Erze in Übungslevels stimmen mit der Tabelle überein (je Taste das Erz ihres Einführungslevels, `ORE_OF`).

---

## I. Werkbänke (Craften)

### Wort-Werkbänke (1–6)

- [ ] Freischaltung: Werkbank 1 ab Level 2, Werkbank 2 ab Level 3, Werkbank 3 ab Level 4, Werkbank 4 ab Level 6, Werkbank 5 ab Level 12, Werkbank 6 ab Level 18.
- [ ] Gesperrte Werkbänke sind kleiner, grau, mit Vorhängeschloss.
- [ ] Werkbank 1: Einführung der Umschalt-Taste (⇧), Fenster „Neue Taste freigeschaltet“.
- [ ] Umschalt-Einführung: kleiner Block „d“ wird beim Halten von Umschalt zu „D“ (Kohle). Loslassen macht ihn wieder klein. Ohne Umschalt zählt der Anschlag nicht.
- [ ] Das Wort steht groß in der Mitte, der aktuelle Buchstabe hat den gelben Rahmen mit Dreieck.
- [ ] Erledigte Buchstaben werden zu leeren gestrichelten Mulden.
- [ ] Jeder abgebaute Block fliegt in den nächsten Gitter-Slot (3×3).
- [ ] Am Ende entsteht der Gegenstand im Ergebnis-Slot, Name darunter, und wandert in die Truhe.
- [ ] Gegenstand hängt an der besten Spitzhacke: mit Holzspitzhacke keine Eisengegenstände, mit Eisen keine Diamantgegenstände.
- [ ] Großbuchstaben: Kohleblock = Großbuchstabe (Umschalt halten), Steinblock = klein.
- [ ] Die Umschalt-Taste der **anderen** Hand wird hervorgehoben (rechte Umschalt für linke Hand, linke Umschalt für rechte Hand).
- [ ] Truhen-Fenster mit 3×3 Slots nach dem Durchlauf, Zähler stimmt.

### Satz-Werkbänke (7–14)

- [ ] Freischaltung ab Level 19 (laut Tabelle, im Code prüfen: `need`).
- [ ] Der Satz steht als Text in der Leiste. Getippte Zeichen werden grün.
- [ ] Der Bauplatz liegt unten über die ganze Breite. Das Bauwerk steht erst durchsichtig da und füllt sich mit jedem Buchstaben.
- [ ] Bauwerke in der richtigen Reihenfolge (Holzhaus, Steinhaus, Steinturm, Steinburg, Kupferhaus, Eisenturm, Goldburg, Diamantburg).
- [ ] Jeder Buchstabe gibt einen leisen Klick, das helle Bling kommt nur einmal am Satzende.
- [ ] Die Pause zwischen zwei Buchstaben ist kurz. Schnelles Tippen verschluckt nichts.
- [ ] Leertaste erscheint als breiter Block über der Leertaste, beide Daumen leuchten.
- [ ] Satzzeichen: nur Komma, Punkt und Bindestrich. Andere Zeichen werden nicht angenommen.
- [ ] Am Ende das fertige Bauwerk auch im Abschluss-Fenster.

### Gegenstände

- [ ] Gecraftet werden nur Dekorationsgegenstände (Liste in `level-und-fortschritt.md`). Lapislazuli und Redstone kommen nicht vor.
- [ ] Neue Gegenstände werden mit Namen im Inventar gezeigt. Nicht gecraftete Plätze sind grau und leer.
- [ ] Obsidian (Endertruhe) erscheint nur mit Diamantspitzhacke.

---

## J. Inventar und Shop

- [ ] Haustier Wolf (🐺) kostet 5 Smaragde, Katze (🐱) kostet 10.
- [ ] Höhle (Biom) kostet 8 und ist erst mit Level 4 mit mindestens einem Herz freigeschaltet.
- [ ] Kauf zieht Smaragde ab. Zu wenig Smaragde: Kauf nicht möglich, klare Rückmeldung.
- [ ] Gekaufte Haustiere stehen zwischen den Armen und hüpfen bei Treffern.
- [ ] Biome wechseln sichtbar (Wald, Höhle).
- [ ] Gekaufte Gegenstände bleiben nach Neuladen.

---

## K. Spielstand und Speicher

- [ ] Fortschritt bleibt nach Neuladen erhalten (Sterne, Smaragde, Gegenstände, Shop).
- [ ] Alter Spielstand `typecraft-v1` wird beim ersten angelegten Namen übernommen.
- [ ] Ein alter Spielstand ohne Versionsnummer (vor v2) verschiebt die Herzen korrekt (`load()`).
- [ ] Ein Spielstand aus v4 (Indizes nach Level 0 verschoben) wird richtig gelesen, Level 1 bleibt Level 1.
- [ ] Privates Fenster / gesperrter Speicher: Spiel läuft trotzdem, Fehlermeldungen erscheinen keine.
- [ ] Nutzer löschen: nur der eine Nutzer verschwindet.

---

## L. Layout und Darstellung

Fenstergrößen: 1280×720, 1440×900, 1920×1080, 1024×768, 1000×600, 900×600, 800×500 und sehr hoch (z. B. 1000×1200).

- [ ] Die Arme sind genau 4 Tasten breit.
- [ ] Die Finger bleiben am Arm, sie lösen sich nicht ab.
- [ ] Beschriftungen (Fingernamen, Erzblock-Namen) werden nicht verdeckt.
- [ ] Blöcke berühren sich nicht und überlappen keinen Text.
- [ ] Das Fenster „Neue Buchstaben“ und das Abschluss-Fenster liegen über allem, nie unter den Händen.
- [ ] Die Tastatur ist vollständig sichtbar, nichts wird abgeschnitten.
- [ ] Ab 1000×600 kein Hinweis. Bei 900×600 und 800×500 erscheint der Hinweis „Typecraft braucht einen Computer mit Tastatur.“ (Ab Breite < 1000 oder Höhe < 600 gilt der Hinweis laut Code, siehe Abschnitt O.)
- [ ] Fenster verkleinern und vergrößern: Hinweis erscheint und verschwindet wieder.
- [ ] Mobil-Emulation (390×844, Touch): Hinweis erscheint, Spiel bleibt gesperrt oder weiter spielbar mit „Trotzdem spielen“.
- [ ] Die Herz-Größe passt sich an, auch bei 48 Tasten.

---

## M. Ton

- [ ] Der Tipp-Klick kommt bei jedem richtigen Anschlag.
- [ ] Erfolgston beim Abschluss.
- [ ] Der erste Tastendruck schaltet den Ton frei. Vorher gibt es keinen Fehler in der Konsole (wichtig in **Safari**).
- [ ] Ton ist nicht zu laut und nicht zu leise.

---

## N. Texte und Sprache

- [ ] Alle Texte sind Deutsch, kurz, ohne Fachbegriffe.
- [ ] Keine Texte mit Rechtschreibfehlern (Ö, Ä, Ü, ß).
- [ ] Der Name im Spiel ist „Typecraft“ (Titel, Menü, Abschluss-Fenster).

---

## O. Technik und Konsole

- [ ] Keine Fehler in der Browser-Konsole während eines ganzen Durchlaufs.
- [ ] Keine Mojang-Dateien, alle Texturen sind eigene Pixelgrafik.
- [ ] Vorschaubild und Open-Graph-Tags sind korrekt (geteilte Links).
- [ ] Bildschirm-Lesbarkeit: Kontraste auf Hell- und Dunkelbildschirm prüfen.

---

## P. Offene Widersprüche in der Dokumentation

Diese Punkte sind vor dem Test zu klären, sonst prüft man gegen falsche Vorgaben.

1. **Level-Nummern:** `CLAUDE.md` sagt „Anzeige = Index + 1“ (Level 1 = Hände auflegen). `docs/level-und-fortschritt.md` nennt Level 0 = Hände auflegen. Im Spiel nachsehen, welche Nummer angezeigt wird.
2. **Grundhaltung:** `CLAUDE.md` (Regel 6) sagt, die Holzspitzhacke kommt aus der Grundhaltung (Level 1). Laut Tabelle kommt sie aus Level 0. `docs/tests.md` und der Spieltest beschreiben noch die alte Grundhaltung (F J ␣).
3. **Umfang:** `CLAUDE.md` nennt „18 Level (0–17)“ und „noch nicht umgesetzt: Zahlenreihe, Umschalttaste, Ä“. Die Tabelle hat Level 0–18 und Werkbänke mit Umschalt und Ä, sowie Zahlen in Level 18/19.
4. **Trefferzahl Level 17:** `docs/tests.md` sagt „Level 17 (48 Treffer)“. Laut Tabelle hat Level 16 48 Treffer und Level 17 nur 16.
5. **Spielstand-Version:** `docs/level-und-fortschritt.md` nennt `v:2`, `v:3` und `v4`. Im Code nachsehen, welche Version aktuell gespeichert wird.

---

## Q. Lücken in der automatischen Prüfung

Der Spieltest (`tests/spieltest.py`) deckt standardmäßig nur die Level 0, 1, 5 und 13 ab. Diese Bereiche sind nicht automatisch geprüft:

- Werkbänke (Wort und Satz), Umschalt-Einführung, Bauwerke
- Shop, Haustiere, Biome
- Namen, mehrere Nutzer, alter Spielstand
- Abschluss-Fenster-Sekunde (1 s Sperre)
- Herzen an den Grenzfällen (Abschnitt G)
- Ton
- Level 16, 17, 18 und 19 (Zahlen, Ä, ß)
- Geräte-Hinweis bei verkleinertem Fenster

Vorschlag: Den Bot um diese Fälle erweitern, bevor die Liste auf Testpersonen angewendet wird.

---

## R. Test mit echten Kindern oder Testpersonen

Beobachtungsbogen pro Sitzung:

- [ ] Alter, Tippvorerfahrung, wie viele Finger benutzt die Person
- [ ] Hält sie die Hände ruhig? Wann schaut sie auf die Tastatur?
- [ ] Wo bleibt sie stecken (Level, Taste, Text)?
- [ ] Versteht sie den Abschluss und die Herzen ohne Erklärung?
- [ ] Wirkt der Anfang (Level 0 und 1) leicht genug?
- [ ] Gibt es Frust-Momente (falsche Taste ohne klare Rückmeldung)?
- [ ] Was würde sie als Nächstes gern haben (Skins, Tiere, Biome)?
