"""Spieltest für Typecraft: öffnet index.html in Chromium, spielt Level per Bot und macht Screenshots.
Aufruf:  python3 tests/spieltest.py [Level ...]     (Standard: 0 5 13)
Ausgabe: tests/ausgabe/*.png, Browserfehler auf der Konsole.
"""
import os, sys
from playwright.sync_api import sync_playwright

HIER = os.path.dirname(os.path.abspath(__file__))
SEITE = 'file://' + os.path.join(HIER, '..', 'index.html')
AUS = os.path.join(HIER, 'ausgabe'); os.makedirs(AUS, exist_ok=True)
level = [int(x) for x in sys.argv[1:]] or [0, 5, 13]

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1280, 'height': 720})
    fehler = []
    pg.on('pageerror', lambda e: fehler.append(str(e)))
    pg.on('console', lambda m: fehler.append(m.text) if m.type == 'error' else None)
    # Tasten per Ereignis senden, weil Ö/Ü/Ä mit keyboard.press nicht gehen
    def taste(k): pg.evaluate('k=>window.dispatchEvent(new KeyboardEvent("keydown",{key:k}))', k)

    pg.goto(SEITE); pg.wait_for_timeout(300)
    pg.evaluate("st.stars={}; for(let i=0;i<16;i++) st.stars[i]=3; st.emeralds=20; save(); renderMenu()")
    pg.screenshot(path=f'{AUS}/menue.png')

    for lv in level:
        pg.evaluate(f'start({lv})'); pg.wait_for_timeout(300)
        pg.screenshot(path=f'{AUS}/level{lv}_start.png')
        if lv == 0:
            # Hände auflegen: nur Hände, Tastatur, Demo, selbst tippen, dann Grundhaltung
            pg.wait_for_timeout(1200); pg.screenshot(path=f'{AUS}/level0_haende1_nur_haende.png')
            pg.wait_for_timeout(3500); pg.screenshot(path=f'{AUS}/level0_haende2_tastatur.png')
            pg.wait_for_timeout(7000); pg.screenshot(path=f'{AUS}/level0_haende3_demo.png')
            taste('Enter'); pg.wait_for_timeout(300)   # Demo überspringen
            assert pg.evaluate('hz.step') == 'tippen'
            for k in ['f', 'j', 'd', 's', 'a']: taste(k); pg.wait_for_timeout(150)
            taste('x'); pg.wait_for_timeout(150)       # falsche Taste zählt nicht
            pg.screenshot(path=f'{AUS}/level0_haende4_tippen.png')
            for k in ['k', 'l', 'ö', ' ']: taste(k); pg.wait_for_timeout(150)
            pg.wait_for_timeout(2300)
            assert pg.evaluate('phase') == 'grund'
            pg.screenshot(path=f'{AUS}/level0_grund.png')
            for k in ['f', 'j', ' ', 'f', 'j', ' ']: taste(k); pg.wait_for_timeout(120)
        else:
            if pg.evaluate('phase') == 'learn':
                for k in pg.evaluate('learn.seq'): taste(k); pg.wait_for_timeout(100)
                pg.wait_for_timeout(1500)
            pg.wait_for_timeout(3500)
            pg.screenshot(path=f'{AUS}/level{lv}_spiel.png')
            for _ in range(1500):
                low = pg.evaluate('(()=>{const b=lowestBlock();return b?b.key:null})()')
                if low: taste(low)
                pg.wait_for_timeout(50)
                if pg.evaluate('!active'): break
        pg.wait_for_timeout(1500)
        pg.screenshot(path=f'{AUS}/level{lv}_ende.png')
        print(f'Level {lv}: Sterne =', pg.evaluate(f'st.stars[{lv}]'))
        pg.evaluate('hideOverlay()')
    print('Browserfehler:', fehler or 'keine')
    b.close()
