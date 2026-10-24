# MineTyper – Projektkontext für Agenten

Browser-Spiel im Minecraft-Look, mit dem Kinder das 10-Finger-Schreiben lernen. Sprache des Projekts, der Oberfläche und aller Dokumente: **Deutsch** (deutsches QWERTZ-Layout). Arbeitstitel früher „FlotteFinger“, Dateinamen früher „tipp-mine“. Der Name im Spiel ist noch „Tipp-Mine“ und soll auf **MineTyper** umgestellt werden (noch nicht gemacht).

## Stand
- Lauffähiger Prototyp: `index.html` (Stand v9, eine einzige Datei mit HTML, CSS und JS, keine Abhängigkeiten, keine Build-Schritte). Einfach im Browser öffnen.
- 17 Level (Grundhaltung + Level 1–16): Grundreihe, obere Reihe, untere Reihe, mit Spitzhacken-Belohnungen Holz, Stein, Eisen, Diamant.
- Noch nicht umgesetzt: Skins, weitere Haustiere und Biome, Zahlenreihe, Umschalttaste, Ä (siehe `docs/roadmap.md`).
- Lokal getestet nur mit Chromium/Playwright (siehe `docs/tests.md`). Ein Test auf echten Geräten und Fenstergrößen steht aus.

## Wichtigste Regeln (vom Auftraggeber so entschieden)
1. **Kein Zeit- oder Tempodruck.** Wichtig sind das Einprägen der Positionen durch Wiederholung und das schrittweise Erweitern der Tasten. Blöcke fallen langsam, ein Block erreicht nie „Game Over“, er startet einfach wieder oben.
2. **Nur Desktop** (dort schreibt man mit 10 Fingern). Kein Touch, kein Mobil-Layout.
3. **Hände liegen ruhig auf der Tastatur, nur die Finger bewegen sich.** Das ist der Sinn des Systems und darf nicht durch Animationen verletzt werden. Die Daumen liegen auf der Leertaste, die Hände sind Minecraft-Arme (genau so breit wie vier Tasten), die Finger sind Teil des Arms.
4. **Blöcke fallen in der Spalte der passenden Taste** auf der Bildschirmtastatur.
5. **Nur Blöcke, die man mit der aktuellen Spitzhacke abbauen kann, kommen ins Spiel.** Keine grauen „noch gesperrt“-Blöcke.
6. **Schneller sichtbarer Erfolg** zu Beginn: Die Grundhaltung ist kurz (6 Tastendrücke) und gibt sofort die Holzspitzhacke.
7. **Jedes Level mit neuen Tasten beginnt mit einer Einführung** wie die Grundhaltung: die neuen Tasten erscheinen als große Erzblöcke über ihrer Taste, das Kind tippt sie mehrmals (6 Tastendrücke), danach fallen die Blöcke.
8. Nicht kommerziell. Eigene Pixelgrafik für alles (Texturen, Spitzhacken, Smaragd), **keine Mojang-Dateien** verwenden. Minecraft ist eine Marke von Mojang.
9. Das Abschluss-Fenster (Modal) liegt immer über allem, erscheint 1 Sekunde nach dem letzten Treffer und wächst aus der Mitte. Mit Enter geht es weiter. In dieser Sekunde zählen keine Anschläge mehr.

## Dateien
- `index.html` – das Spiel
- `docs/konzept.md` – Spielidee, Entscheidungen, Wünsche des Auftraggebers
- `docs/architektur.md` – Aufbau des Codes (Datenmodell, Phasen, Layout-Mathematik, Animationen)
- `docs/level-und-fortschritt.md` – Level-Tabelle, Sterne, Smaragde, Spitzhacken, Shop
- `docs/design.md` – Pixel-Texturen, Farben, Tastatur- und Hand-Layout
- `docs/tests.md` – wie man das Spiel ohne Mensch prüft (Playwright)
- `docs/roadmap.md` – offene Punkte und Ideen
- `docs/vorschau-tastatur-drei-reihen.html` – Layout-Vorschau, aus der das Tastatur-Layout entstand (nur Referenz)
- `tests/spieltest.py` – Bot, der Level durchspielt und Screenshots macht
- `.claude/skills/` – Arbeitsanleitungen für wiederkehrende Aufgaben (neues Level, Spieltest im Browser)

## Arbeitsweise mit dem Auftraggeber
- Antworten und Texte auf Deutsch, kurz, ohne Fachjargon. Der Auftraggeber prüft meist mit Screenshots und gibt konkretes Feedback zum Aussehen.
- Änderungen werden als neue Datei geliefert (früher `tipp-mine-vN.html`, fortlaufend; v9 ist die letzte). Behalte das bei oder nutze Git, aber nenne immer, was sich geändert hat.
- Vor dem Ausliefern immer im Browser prüfen (Playwright, siehe `docs/tests.md`), nicht nur auf Syntax. Früher wurde nur `node --check` benutzt, das reicht nicht für Layout.
- Frage zuerst, wenn eine Änderung die Spielregeln oben berührt.

## Stolperfallen
- Der Speicherschlüssel im localStorage heißt weiterhin `tipp-mine-v6`. Nicht ändern, sonst verlieren Testspieler den Fortschritt. Wenn nötig, Migration einbauen.
- Level-Nummern stehen im Spielstand als Index (`st.stars[i]`). Neue Level nur **am Ende** anhängen oder alle Verweise (`reward`, Shop `need`) prüfen.
- Die Taste Ö lässt sich in Playwright nicht per `keyboard.press` senden. Nutze `dispatchEvent(new KeyboardEvent('keydown', {key:'ö'}))`.
- Alle Positionen der Tastatur hängen an einem 45-Spalten-Raster (Viertel-Tasten). Wer Reihen oder Tasten ändert, muss `ROWSTART`, die CSS-Spalten der Arme und Daumen und `cxOf()` gemeinsam anpassen (siehe `docs/architektur.md`).
