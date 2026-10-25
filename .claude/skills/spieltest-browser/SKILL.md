---
name: spieltest-browser
description: Das Typecraft-Spiel mit Playwright in Chromium testen, Level per Bot durchspielen und Screenshots auf Layoutfehler prüfen. Immer vor dem Ausliefern einer Änderung nutzen.
---

# Spieltest im Browser

Reine Syntaxprüfung reicht nicht, weil fast alle Fehler im Layout und im Zusammenspiel liegen.

## Ablauf
1. Syntax: JS aus `index.html` (`<script>…</script>`) in eine temporäre Datei schreiben und `node --check <datei>` ausführen.
2. Bot: `python3 tests/spieltest.py` (Standard Level 0, 1, 6, 14) oder mit Level-Nummern, z. B. `python3 tests/spieltest.py 5 11 17`. Playwright ist in der Cloud-Umgebung vorinstalliert. Nicht neu installieren.
3. Die Screenshots in `tests/ausgabe/` mit dem Read-Werkzeug ansehen. Prüfen:
   - Finger hängen am Arm, auch beim Greifen in die obere oder untere Reihe und beim Ö-Finger zu `-`.
   - Buchstaben sind lesbar (auch unter den Fingern), Texte überlappen keine Blöcke.
   - Das Abschluss-Fenster liegt über allem und zeigt die Spitzhacke.
   - Dunkle Tasten = noch nicht freigeschaltet, gelbe Markierung = nächste Taste.
4. `Browserfehler:` in der Ausgabe muss `keine` sein.
5. Bei Layoutänderungen zusätzlich ein größeres Fenster testen (z. B. 1920×1080), den Viewport in `spieltest.py` anpassen.

## Tricks
- Zustand setzen: `pg.evaluate("st.stars={0:3}; save(); renderMenu(); start(5)")`.
- Tasten immer per `dispatchEvent(new KeyboardEvent('keydown',{key:k}))` senden (Ö, Ü, Ä gehen mit `keyboard.press` nicht).
- Wenn der Bot ein Level in der Zeit nicht schafft, die Schleife in `spieltest.py` verlängern. Pro Block dauern Abbau und Pause ca. 0,8 s.
