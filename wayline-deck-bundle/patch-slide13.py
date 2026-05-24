#!/usr/bin/env python3
"""
patch-slide13.py — swaps slide 13 in wayline-deck.html for the new
content-hugging Figma/code-parity layout. Idempotent and safe: it matches the
exact old block and replaces it once. Makes a .bak first.

Run from the bundle root:
  cd /Users/seansmith/Documents/GitHub/wayline-deck-hub/wayline-deck-bundle
  python3 patch-slide13.py
"""
import os, sys, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
DECK = os.path.join(HERE, "wayline-deck.html")

OLD = '''  <section class="slide slide--top-anchor" data-slide="13">
    <div class="slide-inner">
      <div class="title-block">
        <h2 class="display-m">I write the React.</h2>
        <div class="body-l" style="max-width: 75%;">
          Computis component library — mine. 49 components on Radix primitives, design system documented alongside the code.
        </div>
      </div>
      <div class="spacer"></div>
      <div class="row" style="margin-bottom: 4%; align-items: stretch; min-height: 640px; gap: 3%;">
        <div class="stack-tight" style="display: flex; flex-direction: column;">
          <div class="label-overline">Figma — source of truth</div>
          <div class="asset-frame" style="flex: 1; margin-top: 10px;">
            <img src="./assets/figma-classification-insights.png" alt="Figma source for classification-insights" onload="this.nextElementSibling.classList.add('is-loaded')" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('is-loaded')" />
            <div class="placeholder">
              <div class="ph-label">Asset placeholder</div>
              <div class="ph-file">figma-classification-insights.png</div>
              <div class="ph-source">Source: your Figma file — the classification-insights frame</div>
            </div>
          </div>
        </div>
        <div class="stack-tight" style="display: flex; flex-direction: column;">
          <div class="label-overline">React — source of record</div>
          <div class="asset-frame" style="flex: 1; margin-top: 10px;">
            <img src="./assets/code-classification-insights.png" alt="React component code from the repo" onload="this.nextElementSibling.classList.add('is-loaded')" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('is-loaded')" />
            <div class="placeholder">
              <div class="ph-label">Asset placeholder</div>
              <div class="ph-file">code-classification-insights.png</div>
              <div class="ph-source">Source: computis-app/client/components/transactions/classification-insights.tsx — syntax-highlighted screenshot, readable at projection scale</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>'''

NEW = '''  <section class="slide slide--top-anchor" data-slide="13">
    <div class="slide-inner">
      <div class="title-block">
        <h2 class="display-m">I write the React.</h2>
        <div class="body-l" style="max-width: 78%;">
          49 components on Radix primitives — the design system and the code that renders it are both mine. Same source data, two representations.
        </div>
      </div>
      <div class="row" style="flex: 1; min-height: 0; margin-top: 64px; margin-bottom: 4%; align-items: center; display: grid; grid-template-columns: 1.32fr 1fr; gap: 54px;">

        <div style="display: flex; flex-direction: column;">
          <div class="label-overline" style="display: flex; align-items: center; gap: 14px; margin-bottom: 22px;">
            <span style="width: 14px; height: 14px; border-radius: 50%; background: var(--accent); display: inline-block;"></span>Figma — what the user sees
          </div>
          <div class="asset-frame" style="background: var(--panel); border: 1px solid var(--rule); box-shadow: var(--panel-shadow); border-radius: 14px; padding: 40px 44px; display: block;">
            <img src="./assets/figma-classification-insights-clean.png" alt="Figma render of the classification-insights confidence panel — High, Medium, Low bands with counts and Review actions" style="width: 100%; height: auto; object-fit: contain; display: block;" onload="this.nextElementSibling.classList.add('is-loaded')" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('is-loaded')" />
            <div class="placeholder" style="position: static; min-height: 360px;">
              <div class="ph-label">Asset placeholder</div>
              <div class="ph-file">figma-classification-insights-clean.png</div>
              <div class="ph-source">Run build-slide13-assets.py to generate this (border-cropped from figma-classification-insights.png).</div>
            </div>
          </div>
        </div>

        <div style="display: flex; flex-direction: column;">
          <div class="label-overline" style="color: var(--ink-muted); display: flex; align-items: center; gap: 14px; margin-bottom: 22px;">
            <span style="width: 14px; height: 14px; border-radius: 50%; background: var(--ink-muted); display: inline-block;"></span>React — the code I wrote
          </div>
          <div class="asset-frame asset-frame--motion" style="border-radius: 14px; display: block; overflow: visible;">
            <img src="./assets/code-classification-insights-dark.png" alt="classification-insights.tsx — the classificationData array and the render JSX that maps it to Progress bars and Review buttons" style="width: 100%; height: auto; object-fit: contain; display: block; border-radius: 14px; box-shadow: 0 14px 50px rgba(22,21,19,0.18);" onload="this.nextElementSibling.classList.add('is-loaded')" onerror="this.style.display='none'; this.nextElementSibling.classList.remove('is-loaded')" />
            <div class="placeholder" style="position: static; min-height: 360px;">
              <div class="ph-label">Asset placeholder</div>
              <div class="ph-file">code-classification-insights-dark.png</div>
              <div class="ph-source">Run build-slide13-assets.py to generate this dark-theme render of classification-insights.tsx.</div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>'''

def main():
    if not os.path.exists(DECK):
        print("! wayline-deck.html not found next to this script."); sys.exit(1)
    html = open(DECK, encoding="utf-8").read()
    if NEW in html:
        print("Already patched — slide 13 is up to date. Nothing to do."); return
    if OLD not in html:
        print("! Could not find the original slide-13 block to replace.")
        print("  The deck may already be modified. No changes made."); sys.exit(2)
    shutil.copy(DECK, DECK + ".bak")
    html = html.replace(OLD, NEW, 1)
    open(DECK, "w", encoding="utf-8").write(html)
    print("Patched slide 13. Backup saved as wayline-deck.html.bak")
    print("Next: run  python3 build-slide13-assets.py  to generate the two PNGs.")

if __name__ == "__main__":
    main()
