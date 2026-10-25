# Design

## Pixel-Grafik (alles selbst gezeichnet, keine Mojang-Dateien)
- Texturen sind kleine SVGs, die als `data:`-URI in CSS-Variablen stehen (Funktion `tex()` am Anfang des Skripts): `--askin` (Arm), `--fskin` (Finger), `--sleeve` (Ärmel, Cyan wie Minecraft-Steve), `--wood`, `--stone`, `--coal`, `--iron`, `--copper`, `--lapis`, `--diamond`, `--gold`, `--redstone`. Alle mit `image-rendering:pixelated`.
- Neue Erze: Stein-Grundfarbe `#8a8a8a` mit farbigen Pixelflecken (Kohle dunkel, Eisen pfirsich `#d8af93`, Diamant türkis `#33ebcb`, Kupfer orange `#c8774a`, Lapislazuli blau `#2a52be`, Gold `#f5d33b`, Redstone rot `#d02020`).
- Spitzhacken: `pickaxeSVG(type,size)` zeichnet 16×16 Pixel. Farben pro Stufe im Objekt `PICKS` (b = Grundfarbe, l = hell, d = dunkel). Holz `#a8793a`, Stein `#9a9a9a`, Eisen `#d8d8d8`, Diamant `#33ebcb`.
- Smaragd: `emeraldSVG(size)`, ovaler Edelstein mit Facetten, angelehnt an Vorbild des Auftraggebers.
- Schnellzugriffsleiste: grauer Rahmen mit 3D-Kanten wie das Minecraft-Inventar, ausgewählter Slot mit weißem Rahmen, neue Spitzhacke „poppt“.

## Layout
- Desktop, volle Fensterbreite. Spielfeld `#biome` ist `clamp(520px, 80vh, 760px)` hoch.
- Hände: Arme genau 4 Tasten breit, Finger als Teil des Arms (gleiche Hautfarbe), Daumen kommen von innen auf die Leertaste. Referenz für das Aussehen war ein Minecraft-Arm (Steve), vom Auftraggeber gezeigt.
- Fingerfarben (`FCOL`) werden nicht mehr in der Oberfläche gezeigt (die Buchstabenleiste unten wurde entfernt), die Zuordnung ist nur noch im Code für Hinweise.
- Das Abschluss-Fenster ist `z-index:1000`, damit es über den Händen liegt.
- Hinweiszeile unter dem Menü-Knopf nennt immer Taste und Finger.

## Noch offen im Design
- Test auf kleineren Fenstern (unter 1100 px Breite) und sehr hohen Fenstern.
- Haustiere sind noch Emojis, sollen Pixelgrafiken werden.
