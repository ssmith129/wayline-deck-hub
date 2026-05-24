#!/usr/bin/env python3
"""
build-slide13-assets.py
Generates the two treated visual assets for slide 13 of wayline-deck.html,
writing them into ./assets/ next to this script.

Outputs:
  assets/figma-classification-insights-clean.png   (border cropped, white preserved)
  assets/code-classification-insights-dark.png      (dark VS Code-style render)

Run from the bundle root:
  cd /Users/seansmith/Documents/GitHub/wayline-deck-hub/wayline-deck-bundle
  python3 build-slide13-assets.py

Requires: pillow  (pip install pillow)
Optional for the code panel: playwright (pip install playwright && playwright install chromium)
If playwright is unavailable, the script still writes code-panel.html so you can
screenshot it manually, or print it to PNG with any headless browser.
"""
import os
import sys
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

def crop_figma():
    from PIL import Image
    src = os.path.join(ASSETS, "figma-classification-insights.png")
    if not os.path.exists(src):
        print("  ! missing", src); return
    im = Image.open(src).convert("RGB")
    w, h = im.size
    # the asset carries a 1px hard border ring; crop 2px in on all sides
    out = im.crop((2, 2, w - 2, h - 2))
    dst = os.path.join(ASSETS, "figma-classification-insights-clean.png")
    out.save(dst)
    print("  +", os.path.relpath(dst, HERE), out.size)

CODE_HTML = r"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap');
*{margin:0;padding:0;box-sizing:border-box;}
body{background:transparent;}
.editor{width:760px;background:#1B1B1D;border-radius:10px;overflow:hidden;
  font-family:'JetBrains Mono',monospace;}
.titlebar{height:38px;background:#252528;display:flex;align-items:center;
  padding:0 16px;gap:8px;border-bottom:1px solid #303034;}
.dot{width:11px;height:11px;border-radius:50%;}
.fname{margin-left:12px;color:#9A9AA2;font-size:12.5px;}
.code{padding:16px 20px 18px;font-size:13px;line-height:1.65;}
.ln{display:flex;}
.num{color:#4A4A52;width:30px;flex-shrink:0;text-align:right;padding-right:16px;user-select:none;}
.txt{white-space:pre;}
.kw{color:#C586C0;}.fn{color:#DCDCAA;}.str{color:#CE9178;}
.num2{color:#B5CEA8;}.type{color:#4EC9B0;}.var{color:#9CDCFE;}
.prop{color:#9CDCFE;}.punct{color:#D4D4D4;}
</style></head><body>
<div class="editor">
  <div class="titlebar">
    <span class="dot" style="background:#FF5F57;"></span>
    <span class="dot" style="background:#FEBC2E;"></span>
    <span class="dot" style="background:#28C840;"></span>
    <span class="fname">classification-insights.tsx</span>
  </div>
  <div class="code">
__LINES__
  </div>
</div>
</body></html>"""

CODE_LINES = [
 ('5',  '<span class="kw">const</span> <span class="var">classificationData</span> <span class="punct">=</span> ['),
 ('6',  '  { <span class="prop">level</span>: <span class="str">"High Confidence"</span>,'),
 ('7',  '    <span class="prop">count</span>: <span class="num2">61</span>, <span class="prop">percentage</span>: <span class="num2">55</span>,'),
 ('8',  '    <span class="prop">color</span>: <span class="str">"text-success"</span>, <span class="prop">icon</span>: <span class="type">CheckCircle</span> },'),
 ('9',  '  { <span class="prop">level</span>: <span class="str">"Medium Confidence"</span>,'),
 ('10', '    <span class="prop">count</span>: <span class="num2">42</span>, <span class="prop">percentage</span>: <span class="num2">34</span>,'),
 ('11', '    <span class="prop">color</span>: <span class="str">"text-warning"</span>, <span class="prop">icon</span>: <span class="type">AlertCircle</span> },'),
 ('12', '  { <span class="prop">level</span>: <span class="str">"Low Confidence"</span>,'),
 ('13', '    <span class="prop">count</span>: <span class="num2">14</span>, <span class="prop">percentage</span>: <span class="num2">11</span>,'),
 ('14', '    <span class="prop">color</span>: <span class="str">"text-error"</span>, <span class="prop">icon</span>: <span class="type">XCircle</span> },'),
 ('15', '];'),
 ('',   '__GAP__'),
 ('41', '<span class="punct">{</span><span class="var">classificationData</span>.<span class="fn">map</span>((<span class="var">item</span>) <span class="kw">=&gt;</span> ('),
 ('44', '  <span class="punct">&lt;</span><span class="type">IconComponent</span> <span class="prop">className</span>=<span class="punct">{</span>`h-4 w-4 ${<span class="var">item</span>.color}`<span class="punct">}</span> <span class="punct">/&gt;</span>'),
 ('49', '  <span class="punct">&lt;</span><span class="type">Progress</span> <span class="prop">value</span>=<span class="punct">{</span><span class="var">item</span>.percentage<span class="punct">}</span> <span class="prop">className</span>=<span class="str">"h-2"</span> <span class="punct">/&gt;</span>'),
 ('58', '  <span class="punct">&lt;</span><span class="type">Button</span> <span class="prop">variant</span>=<span class="str">"link"</span><span class="punct">&gt;</span>Review<span class="punct">&lt;/</span><span class="type">Button</span><span class="punct">&gt;</span>'),
 ('63', '))<span class="punct">}</span>'),
]

def build_code_html():
    rows = []
    for num, txt in CODE_LINES:
        if txt == '__GAP__':
            rows.append('<div class="ln"><span class="num"></span><span class="txt" style="color:#4A4A52;">      \u22ee</span></div>')
        else:
            rows.append(f'<div class="ln"><span class="num">{num}</span><span class="txt">{txt}</span></div>')
    html = CODE_HTML.replace('__LINES__', "\n".join(rows))
    path = os.path.join(HERE, "code-panel.html")
    with open(path, "w") as f:
        f.write(html)
    return path

def render_code(html_path):
    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        print("  ! playwright not installed — wrote code-panel.html instead.")
        print("    Install with: pip install playwright && playwright install chromium")
        print("    Or screenshot code-panel.html manually (the .editor element).")
        return
    import pathlib
    uri = pathlib.Path(html_path).resolve().as_uri()
    dst = os.path.join(ASSETS, "code-classification-insights-dark.png")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(device_scale_factor=2)
        pg.goto(uri); pg.wait_for_timeout(1200)
        pg.query_selector(".editor").screenshot(path=dst, omit_background=True)
        b.close()
    print("  +", os.path.relpath(dst, HERE))

if __name__ == "__main__":
    print("Building slide-13 assets into", ASSETS)
    try:
        crop_figma()
    except ImportError:
        print("  ! Pillow not installed. Run: pip install pillow"); sys.exit(1)
    html_path = build_code_html()
    render_code(html_path)
    print("Done.")
