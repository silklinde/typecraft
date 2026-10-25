# Architektur von index.html

Eine Datei: `<style>` (CSS), HTML-Gerüst (Menü `#menu`, Spiel `#game`, Modal `#overlay`) und ein `<script>` ohne Bibliotheken. Zeichnen per DOM und CSS, Spielschleife per `requestAnimationFrame` (`tick`).

## Zustände (`phase`)
- `haende` – Level 0 „Hände auflegen“: `hz.step` = `show` (nur Hände, Tastatur blendet ein) → `tippen` (für jede Taste aus `HAENDE_SEQ` = F J D S A K L Ö ␣: der Finger hebt sich, darüber steht groß sein Name (`HNAME`), über der Taste ein Erdblock mit dem Buchstaben; richtige Taste → `layFinger(k)` und `mineBlock()`, falsche → Block wackelt) → `done` → `finish()` (Abschluss-Fenster, ohne Belohnung). Finger sind per Klasse `.away` angehoben, `layFinger(k)` legt sie ab. Schritte laufen als Kette über `pendingTimer` (`later()`). Es gibt keine Zuschau-Demo; Button „Überspringen“ überspringt den ganzen Teil.
- `grund` – Grundhaltung (Level 1): ein Holzblock nach dem anderen über F, J bzw. Leertaste (`grundAsk()`, `bigBlock()`), Reihenfolge `GRUND_SEQ` = F J ␣ F J ␣, Abbau per `mineBlock()` wie in den Spiellevels. Gibt die Holzspitzhacke.
- `learn` – Einführung in Levels mit neuen Tasten: große Erzblöcke `#big-<taste>`, `learn.seq` (jede neue Taste einmal, nur neue Tasten werden gewertet; das Fenster `#toast` steht oben im Kopfbereich, bis die Einführung vorbei ist).
- `wait` – 1 Sekunde Pause nach der Einführung (`pendingTimer`), dann `beginPlay`.
- `play` – ein einzelner großer Block (`run.cur = {key, el, kind}`) steht über seiner Taste (`showBlock()`). Richtige Taste → `mineBlock()` (10 Rissstufen als Canvas-Pixelbild, Wackeln, Krümel per `burst()`), `run.busy` sperrt Anschläge während des Abbaus, nach 450 ms kommt der nächste Block. Falsche Taste → Block wackelt (`.shake`), Hinweistext.
`finish()` setzt `active=false`, berechnet Sterne, speichert und zeigt das Modal nach 1 s. `pendingTimer` wird in `start()` und `renderMenu()` mit `clearTimeout` geleert, damit nichts nachläuft.

## Tastatur-Raster (wichtigste Mathematik)
- Die Tastatur ist ein CSS-Grid mit **45 Spalten**. Eine Taste = 4 Spalten (Viertel-Tasten), damit die Reihen wie bei QWERTZ versetzt liegen: Q beginnt in Spalte 1, A in Spalte 2, Y in Spalte 4 (`ROWSTART = [1,2,4]`).
- `KEYROWS` (Tasten pro Reihe), `KEYPOS[k] = {r, c}` (Reihe, Startspalte), `cxOf(k)` = Mitte der Taste als Anteil der Breite → für die Blöcke (`left: %`) und Einführungsblöcke.
- Zeilen: 3 Tastenreihen (`--kh`) + Leertaste (`--sp`), Zeilenabstand 8 px. `#biome` definiert `--kh`, `--sp`, `--kbh`.
- Leertaste: Spalten 10–34 in Zeile 4. Arme: links Spalten 2–17, rechts 26–41 (je 4 Tasten breit), beginnen unter der unteren Reihe (Zeile 4, `margin-top:-8px`). Daumen: links Spalten 18–21, rechts 22–25 (kommen von der Innenseite der Arme).
- Blockbereich `#lanes` endet an der Oberkante der oberen Tastenreihe.

## Hände und Finger
- 8 Finger (`.fing[data-k=a,s,d,f,j,k,l,ö]`) liegen auf der Grundreihe und reichen bis zum Arm (Zeilen 2–3). Die Zuordnung steht in `FINGERS` (jeder Finger → Tasten), `fingerOf(k)`.
- `fingerFor(wrap,k)` berechnet `--dx`/`--dy` (Abstand zur Grundtaste per `offsetLeft/offsetTop`); CSS verschiebt den Finger entsprechend. Die Höhe `calc(100% - var(--dy))` hält das untere Ende am Arm.
- `setExpected(k)`: der nächste Finger hebt sich (`.hover`), Taste und Beschriftung leuchten gelb. `pressKey(k)`: `.press` (160 ms), Taste dunkler.
- Beschriftungen (`.lbl`) liegen in eigener Ebene über den Händen (z-index 6), damit Buchstaben unter den Fingern lesbar bleiben.
- Leertaste: der rechte Daumen (`.thumb.r`) drückt.
- Tasten außerhalb von `L.keys` sind abgedunkelt (`.off`).

## Wichtige Funktionen
`start(i)` · `buildBoard(field,L,mode)` · `beginPlay(L)` · `showBlock()` · `mineBlock()` · `tick()` (nur noch Rest) · `onKey(e)` (Enter im Modal, Grundhaltung, Einführung, Spiel) · `finish()` · `renderMenu()` · `rewardHtml(type)` · `renderHotbar()`.

## Eingabe
`keydown` auf `window`; `e.key.toLowerCase()`. Strg/Meta/Alt werden ignoriert. Leertaste: `preventDefault`, Fokus wird beim Levelstart von Buttons genommen.
