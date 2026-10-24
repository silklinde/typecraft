# Tests

Es gibt keine automatisierten Unit-Tests. Geprüft wird im echten Browser mit Playwright (in der Cloud-Umgebung ist Chromium vorinstalliert, `from playwright.sync_api import sync_playwright`, nicht neu installieren).

1. `node --check` für eine schnelle Syntaxprüfung des Skripts (JS aus `<script>` in eine Datei schreiben).
2. `python3 tests/spieltest.py` – öffnet `index.html` (1280×720), schaltet alle Level frei, spielt eine Auswahl per Bot und speichert Screenshots nach `tests/ausgabe/`. Fehler im Browser (`pageerror`) werden ausgegeben.
3. Screenshots ansehen (Read-Werkzeug) und auf Layoutfehler achten: Finger lösen sich vom Arm, Beschriftungen verdeckt, Blöcke berühren sich, Fenster liegt unter den Händen, Texte überlappen Blöcke.

Hinweise:
- Tasten per `window.dispatchEvent(new KeyboardEvent('keydown',{key:k}))` senden. Ö, Ü, Ä gehen mit `keyboard.press` nicht (US-Layout).
- Zustand kann über `page.evaluate` gesetzt werden: `st.stars={0:3,...}; save(); renderMenu(); start(13)`.
- Der Bot liest `lowestBlock().key` und drückt die Taste. Level 16 (48 Treffer) braucht länger, die Schleife braucht mehr Durchläufe.
- Netz im Container ist eingeschränkt, `npm install` externer Pakete (z. B. jsdom) kann scheitern. Playwright reicht.
- Level 0 beginnt mit „Hände auflegen“: Der Bot wartet die Demo ab oder sendet `Enter` (überspringt die Demo), tippt dann A S D F ␣ J K L Ö und danach F J ␣ F J ␣. Playwright ggf. mit `pip3 install playwright && python3 -m playwright install chromium` einrichten.
