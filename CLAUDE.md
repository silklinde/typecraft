# Typecraft – Projektkontext für Agenten

Browser-Spiel im Minecraft-Look, mit dem Kinder das 10-Finger-Schreiben lernen. Sprache des Projekts, der Oberfläche und aller Dokumente: **Deutsch** (deutsches QWERTZ-Layout). Der Name im Spiel ist **Typecraft**.

## Stand
- Lauffähiger Prototyp: `index.html` (Stand v10, eine einzige Datei mit HTML, CSS und JS, keine Abhängigkeiten, keine Build-Schritte). Einfach im Browser öffnen.
- 18 Level (Level 0 Hände auflegen, Level 1 Grundhaltung, Level 2–17): Grundreihe, obere Reihe, untere Reihe, mit Spitzhacken-Belohnungen Holz, Stein, Eisen, Diamant.
- Menü: ein Pfad mit den 19 Buchstaben-Leveln, Zweige für Rezepte (Werkbänke, unten) und Vorlagen (Bauplätze, oben), darunter das Bücherregal mit 8 Plätzen. Die Tür zu den Text-Leveln ist ein Platzhalter („Bald geöffnet“). Siehe `docs/level-und-fortschritt.md`.
- Noch nicht umgesetzt: Skins, weitere Haustiere und Biome, Zahlenreihe, Umschalttaste, Ä. Die Roadmap wird nicht im Repo gepflegt, sondern im Projekt.
- Lokal getestet nur mit Chromium/Playwright (siehe `docs/tests.md`). Ein Test auf echten Geräten und Fenstergrößen steht aus.
- Geräteprüfung: Bei reinen Touch-Geräten (ohne erkannte Taste) oder Fenstern kleiner als 1000×600 deckt ein Hinweis das Spiel ab (`geraetPruefen()`, `MIN_W`/`MIN_H` in `index.html`). Der Spielstand bleibt unberührt.

## Wichtigste Regeln (vom Auftraggeber so entschieden)
1. **Kein Zeit- oder Tempodruck.** Wichtig sind das Einprägen der Positionen durch Wiederholung und das schrittweise Erweitern der Tasten. Ab Level 1 steht immer nur **ein** Block ruhig da (er fällt nicht), er bleibt stehen, bis die Taste getippt ist.
2. **Nur Desktop** (dort schreibt man mit 10 Fingern). Kein Touch, kein Mobil-Layout.
3. **Hände liegen ruhig auf der Tastatur, nur die Finger bewegen sich.** Das ist der Sinn des Systems und darf nicht durch Animationen verletzt werden. Die Daumen liegen auf der Leertaste, die Hände sind Minecraft-Arme (genau so breit wie vier Tasten), die Finger sind Teil des Arms.
4. **Der Block steht in der Spalte der passenden Taste** auf der Bildschirmtastatur. Ein Tastendruck baut ihn mit einer Minecraft-Animation ab (Risse, Wackeln, Krümel), danach kommt der nächste.
   **Ausnahme Craft-Level (Werkbänke):** Dort stehen keine Blöcke über den Fingern. Die Buchstaben erscheinen nur oben in der Werkbank-Leiste (Wort groß in der Mitte, 3×3-Gitter und Truhe rechts), der aktuelle Block hat den gelben Rahmen mit Dreieck und wird dort abgebaut. Die Tastatur zeigt weiter die richtige Taste. **Satz-Werkbänke** bauen zusätzlich mit jedem Buchstaben ein Haus, einen Turm oder eine Burg (eigener Bauplatz-Bereich unten über die ganze Breite, das Bauwerk steht erst durchsichtig da und füllt sich), mit leisem Klick statt Bling pro Buchstabe.
5. **Nur Blöcke, die man mit der aktuellen Spitzhacke abbauen kann, kommen ins Spiel.** Keine grauen „noch gesperrt“-Blöcke.
6. **Schneller sichtbarer Erfolg** zu Beginn: Level 0 ist „Hände auflegen“ (kein Zuschauen, kaum Text: der passende Finger hebt sich, sein Name steht darüber, ein Erdblock mit dem Buchstaben erscheint, das Kind tippt ihn ab; 9 Tastendrücke, überspringbar), danach ist die Grundhaltung (Level 1, Holzblöcke mit Abbau-Animation) kurz (6 Tastendrücke) und gibt die Holzspitzhacke.
7. **Jedes Level mit neuen Tasten beginnt mit einer Einführung** wie die Grundhaltung: die neuen Tasten erscheinen als große Erzblöcke über ihrer Taste, das Kind tippt jede neue Taste genau einmal, oben im schwarzen Bereich steht dabei das Fenster „Neue Buchstaben freigeschaltet“ (wie das Rezept-Fenster in Minecraft), danach erscheinen die Blöcke einzeln.
8. Nicht kommerziell. Eigene Pixelgrafik für alles (Texturen, Spitzhacken, Smaragd), **keine Mojang-Dateien** verwenden. Minecraft ist eine Marke von Mojang.
9. Das Abschluss-Fenster (Modal) liegt immer über allem, erscheint 1 Sekunde nach dem letzten Treffer und wächst aus der Mitte. Mit Enter geht es weiter. In dieser Sekunde zählen keine Anschläge mehr.

## Dateien
- `index.html` – das Spiel
- `docs/konzept.md` – Spielidee, Entscheidungen, Wünsche des Auftraggebers
- `docs/architektur.md` – Aufbau des Codes (Datenmodell, Phasen, Layout-Mathematik, Animationen)
- `docs/level-und-fortschritt.md` – Level-Tabelle, Sterne, Smaragde, Spitzhacken, Shop
- `docs/design.md` – Pixel-Texturen, Farben, Tastatur- und Hand-Layout
- `docs/tests.md` – wie man das Spiel ohne Mensch prüft (Playwright)
- `docs/vorschau-tastatur-drei-reihen.html` – Layout-Vorschau, aus der das Tastatur-Layout entstand (nur Referenz)
- `tests/spieltest.py` – Bot, der Level durchspielt und Screenshots macht
- `.claude/skills/` – Arbeitsanleitungen für wiederkehrende Aufgaben (neues Level, Spieltest im Browser)

## Arbeitsweise mit dem Auftraggeber
- Antworten und Texte auf Deutsch, kurz, ohne Fachjargon. Der Auftraggeber prüft meist mit Screenshots und gibt konkretes Feedback zum Aussehen.
- Änderungen werden per Git versioniert; nenne immer, was sich geändert hat.
- **Nach jeder Änderung sofort committen und pushen**, auch bevor getestet wurde. Der Auftraggeber sagt nach einem erfolgreichen Test nicht extra, dass gepusht werden soll. Gearbeitet wird direkt auf `main`. Schlägt ein Test danach fehl, wird der Fehler in einem Folge-Commit behoben.
- Vor dem Ausliefern immer im Browser prüfen (Playwright, siehe `docs/tests.md`), nicht nur auf Syntax. Früher wurde nur `node --check` benutzt, das reicht nicht für Layout.
- Frage zuerst, wenn eine Änderung die Spielregeln oben berührt.

## Stolperfallen
- Anzeige-Nummern der Level sind Index + 1 (Level 1 = „Hände auflegen“ = Index 0). Diese Datei und `docs/` nennen teils noch die alten Nummern (Level 0 = „Hände auflegen“).
- Level-Nummern stehen im Spielstand als Index (`st.stars[i]`). Neue Level nur **am Ende** anhängen oder alle Verweise (`reward`, Shop `need`) prüfen.
- Die Taste Ö lässt sich in Playwright nicht per `keyboard.press` senden. Nutze `dispatchEvent(new KeyboardEvent('keydown', {key:'ö'}))`.
- Alle Positionen der Tastatur hängen an einem 45-Spalten-Raster (Viertel-Tasten). Wer Reihen oder Tasten ändert, muss `ROWSTART`, die CSS-Spalten der Arme und Daumen und `cxOf()` gemeinsam anpassen (siehe `docs/architektur.md`).
