# Wayline Deck — UI-Density Audit & Render Verification

> Portfolio case-study deck audit for a Senior→Staff product-design interview loop. Panel feedback: *“more UI assets throughout.”* This document audits where that’s right, where it’s wrong, and what’s actually broken.

**Deck:** `wayline-deck.html` · 25 slides (numbered 1–26, no 19) · 16:9 · custom keyboard-driven HTML (**not Remark.js**) · full-length version only
**Audited:** 2026-05-22
**Method:** Static parse of every slide + **headless render verification** of all asset slides (Playwright/Chromium at 1920×1080)

-----

## TL;DR

- The deck is **not** under-assetted. It already has **7 image/video slides + 4 live-HTML-component slides** out of 25.
- **6 of 7 image slides render correctly** (verified). Five real Symplify captures on slide 17 and the patient-acuity dashboard on slide 18 are strong.
- **One environment-independent defect:** slide 7’s video declares a poster/fallback file (`computis-rule-engine.png`) that **does not exist on disk**. No safety net if the MP4 fails to load while presenting.
- **Two cheap, high-value upgrades:** rewire slide 8 to its existing-but-unused MP4 (done — see `slide-08-replacement.html`); build one confidence-slider GIF for slide 20.
- **Protect the Wayline section (21–26).** Its asset-lightness is deliberate — the product doesn’t exist yet; that *is* the pitch. Do not “fix” it with mocked UI.
- If the panel saw placeholders during a screen-share, “add more UI” may have meant **“your assets didn’t load.”** Verify renders before adding anything.

-----

## 1 — Evaluation Rubric

|Axis                 |Scale                                  |Measures                                                                                                                              |
|---------------------|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
|**Density**          |0–3                                    |Current visual/information load                                                                                                       |
|**Asset opportunity**|None / Low / Med / High                |Room for a UI artifact that earns its place                                                                                           |
|**Pacing risk**      |P0 / P1 / P2                           |Damage if an asset is added. P0 = breaks a deliberate breather/climax; P1 = noticeable drag; P2 = cosmetic                            |
|**Staff signal**     |Decoration / Craft / Decision / Systems|What the asset proves. *Decision* = a judgment call; *Systems* = cross-feature/cross-vertical thinking. Decoration is the failure mode|
|**Verdict**          |Add / Enhance / Hold / Leave           |Action                                                                                                                                |

**Motion-vs-static rule:** Motion (GIF/MP4) only when *change over time* is the point (slider moving, route resolving, state transition). Otherwise static.
**Annotation rule:** Annotate when the artifact proves a *decision* the narration claims. Raw screenshots prove craft; annotated screenshots prove judgment — the staff signal.

> ⚠️ **Pacing caveat:** the deck file contains **no speaker notes**. Pacing roles below are inferred from on-slide content + sequence `[ASSUMED-PACING]`. If a narration script exists elsewhere, share it to tighten the Pacing-Risk column.

-----

## 2 — Slide-by-Slide Audit

Sections: **Computis** (1–13) → **Symplify** (14–20) → **Wayline synthesis/pitch** (21–26).

### Computis (slides 1–13)

|# |Title                                         |Type          |D|Asset opp.|Verdict         |Note                                                                                                                                            |
|--|----------------------------------------------|--------------|-|----------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
|1 |The trust surface… (title)                    |text          |0|None      |**Leave**       |Cold open. A screenshot would undercut it.                                                                                                      |
|2 |The next 30 minutes (roadmap)                 |text          |1|Low       |**Hold**        |Thumbnails would spoil the three reveals. `[CUTTABLE]` if added.                                                                                |
|3 |11:00 PM April 14th                           |text          |1|None      |**Leave**       |Deliberate tension beat. P0.                                                                                                                    |
|4 |32% conversion gap                            |text          |1|Low       |**Hold**        |The number is the asset.                                                                                                                        |
|5 |Three stakes                                  |text          |2|None      |**Leave**       |Rhetorical triad; UI breaks it.                                                                                                                 |
|6 |From a percentage to a decision               |hybrid        |3|**High**  |**Enhance · P1**|**Climax of Computis arc.** Before/after; “after” image wired. Annotate the 3 decision bands + $-risk reframe. Static is correct. → **Decision**|
|7 |Override is the failure mode                  |MP4           |2|High      |**Fix · P1**    |Pattern is right (motion). **Poster/fallback PNG missing — fix it.** See §3. → **Decision**                                                     |
|8 |If it recurs, it needs a noun in the URL      |static→**MP4**|2|High      |**Enhance · P2**|**DONE.** MP4 existed unused; rewired. See `slide-08-replacement.html`. → **Decision**                                                          |
|9 |I shipped this. Then I audited myself (68/100)|hybrid        |3|Med       |**Hold**        |**Honest-miss = load-bearing staff signal.** Don’t crowd. Light annotation on worst offender only. → **Systems**                                |
|10|Measured, not asserted (4 metrics)            |numerals      |2|None      |**Leave**       |Load-bearing verified metrics. A dashboard here would *weaken* them. P0.                                                                        |
|11|How we measured                               |text          |2|None      |**Leave**       |Methodology = rigor; text is the medium.                                                                                                        |
|12|How we measured (cont.)                       |text          |2|None      |**Leave**       |Objection-readiness signal (“happiest to be pressed on”). Protect. Screening-cut candidate, not asset candidate.                                |
|13|I write the React (Figma + code)              |hybrid        |3|High      |**Enhance · P2**|Both images verified rendering. Optional: annotate one token→code line. → **Systems**                                                           |

### Symplify (slides 14–20)

|# |Title                                            |Type      |D|Asset opp.|Verdict           |Note                                                                                                                                                              |
|--|-------------------------------------------------|----------|-|----------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|14|Same primitive. New vertical                     |live HTML |3|High      |**Leave**         |Live dual-panel render. Live > screenshot. → **Systems**                                                                                                          |
|15|06:45 (Symplify cold open)                       |text      |1|None      |**Leave**         |Mirror of slide 3. P0.                                                                                                                                            |
|16|What was real / mocked                           |text      |2|Low       |**Hold**          |Intellectual-honesty signal. Don’t dilute with an asset. P1.                                                                                                      |
|17|Same primitive — across fourteen features        |5 PNGs    |3|High      |**Leave (verify)**|**Best systems artifact in Symplify arc. All 5 verified rendering.** → **Systems**                                                                                |
|18|Input isn’t typed. It’s inferred (patient acuity)|static PNG|2|High      |**Enhance · P1**  |**Verified: meets capture spec.** Optional annotation on one pre-filled→confirmed field → converts craft to **Decision**. Minor: framing leaves wide dead margins.|
|20|Three artifacts                                  |text      |1|Med       |**Add · P2**      |Real text-gap. **Confidence-threshold slider GIF** belongs here (temporal). `[ASSET NEEDED]` `[CUTTABLE]`. SBAR handoff also `[ASSET NEEDED]`.                    |

### Wayline synthesis / pitch (slides 21–26) — protect deliberate asset-lightness

|# |Title                                                     |Type     |D|Asset opp.|Verdict  |Note                                                                            |
|--|----------------------------------------------------------|---------|-|----------|---------|--------------------------------------------------------------------------------|
|21|Same primitive. Two regulated verticals                   |live HTML|3|covered   |**Leave**|Live dual-panel.                                                                |
|22|One primitive. Three regulated verticals                  |live HTML|3|High      |**Leave**|Thesis slide; densest live artifact. P0.                                        |
|23|Legibly seamful (live Wayline surface)                    |live HTML|3|covered   |**Leave**|Most elaborate in-DOM mock; carries the design philosophy. P0 — do not touch.   |
|24|First 90 days                                             |text     |2|None      |**Leave**|Roadmap-as-product-UI would be fabrication. Wayline isn’t built. Honest as text.|
|25|I design the surface where a professional supervises an AI|text     |1|None      |**Leave**|Thesis restatement. P0.                                                         |
|26|The ask: two-day work trial                               |text     |0|None      |**Leave**|CTA.                                                                            |

### Verdict roll-up

|Verdict    |Slides                                                 |
|-----------|-------------------------------------------------------|
|**Fix**    |7 (missing poster/fallback)                            |
|**Enhance**|6, 8 *(done)*, 13, 18                                  |
|**Add**    |20 *(both assets `[ASSET NEEDED]`, `[CUTTABLE]`)*      |
|**Hold**   |2, 4, 9, 16                                            |
|**Leave**  |1, 3, 5, 10, 11, 12, 14, 15, 17, 21, 22, 23, 24, 25, 26|

-----

## 3 — Render Verification Results

All asset slides rendered headless at 1920×1080. Per-frame check: image `complete && naturalWidth>0`, placeholder `display !== none`.

|Slide|Asset                                                                   |Result                                                                                                                      |
|-----|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
|6    |computis-classification-insights.png                                    |✅ Renders                                                                                                                   |
|7    |computis-rule-engine.mp4                                                |⚠️ Could not verify in audit container (no H.264 codec). **Plays in Chrome/Safari/Edge on macOS.** `[VERIFY IN YOUR BROWSER]`|
|8    |computis-anomaly-route.png → **.mp4**                                   |✅ Static verified; MP4 rewired (same codec caveat as 7, but **has working poster fallback**)                                |
|9    |computis-design-critique.png                                            |✅ Renders                                                                                                                   |
|13   |figma-classification-insights.png + code-classification-insights.png    |✅ Both render                                                                                                               |
|17   |triage / ai-assistant-popup-large / severity / urgency / confidence (×5)|✅ All 5 render                                                                                                              |
|18   |symplify-patient-acuity.png                                             |✅ Renders + **meets capture spec** (4 acuity bands, 10 rows, sparklines, filter chips, legible Dx)                          |

### 🔧 The one real defect (environment-independent)

**Slide 7 has no working fallback.** Its `<video>` declares:

```
poster="./assets/computis-rule-engine.png"
onerror="...nextElementSibling.classList.remove('is-loaded')"
```

…but **`computis-rule-engine.png` does not exist on disk.** If the MP4 fails to load on the presenting machine, the slide falls back to the diagonal-hatch placeholder — on your highest-signal Computis evidence slide.

**Fix (≤5 min):** export one poster frame from the MP4 (rest/result state) and save as `assets/computis-rule-engine.png`:

```
ffmpeg -i assets/computis-rule-engine.mp4 -vf "select=eq(n\,0)" -frames:v 1 assets/computis-rule-engine.png
# or grab the final/result frame:
ffmpeg -sseof -0.5 -i assets/computis-rule-engine.mp4 -frames:v 1 assets/computis-rule-engine.png
```

Slide 8 (rewired) already avoids this — its poster points at the real `computis-anomaly-route.png`.

### ℹ️ Codec note (why the audit couldn’t play the MP4s)

Both MP4s are standard **H.264 High / yuv420p** — valid, web-safe, decodable by all major desktop browsers. The audit’s headless Chromium ships **without proprietary H.264** (`canPlayType('avc1')` → empty), so it can’t play *any* H.264 file. This is a sandbox limitation, **not** a defect in your files. Still: do one live playback pass in your actual presenting browser before the loop.

-----

## 4 — Compromise Playbook

Effort: **S** <30min · **M** hours · **L** day+

|#|Tactic                                                                                                                                                                             |Effort|Slides          |Why it protects pacing                                                                       |
|-|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|----------------|---------------------------------------------------------------------------------------------|
|1|**Render-verify pass** (done here; redo in your browser for the 2 MP4s)                                                                                                            |S     |6,7,8,9,13,17,18|Zero pacing cost. Likely the real fix for the panel complaint.                               |
|2|**Generate slide 7 poster PNG**                                                                                                                                                    |S     |7               |Closes the only real defect. Working fallback on top-signal slide.                           |
|3|**Rewire slide 8 to existing MP4** ✅ done                                                                                                                                          |S     |8               |Asset existed unused; motion where motion is the point.                                      |
|4|**Annotate, don’t add** — callouts on slide 6 “after” + slide 18                                                                                                                   |M     |6,18,(13)       |Same slide count, higher signal. Craft → Decision.                                           |
|5|**Progressive reveal** for dense slides (6 before/after, 17’s 5 badges)                                                                                                            |M     |6,17            |Lets narration pace the visual; controls cognitive load.                                     |
|6|**Backup-slide deep-dives** after slide 26 (full dashboards, more badges, SBAR)                                                                                                    |M     |appendix        |Absorbs “more UI” appetite without bloating the linear narrative. Best for a Q&A-heavy panel.|
|7|**Build confidence-slider GIF** for slide 20                                                                                                                                       |M–L   |20              |The one missing temporal artifact. `[ASSET NEEDED]` `[CUTTABLE]`.                            |
|8|**Asset standards**: loops ≤6s, ≤1MB, muted, autoplay-on-enter/pause-on-exit (JS already does this); statics `object-fit:contain` (already set); PNG-optimize the 5 slide-17 badges|S     |all asset       |Consistency prevents the “screenshot dump” feel.                                             |
|9|**Tag no-asset zones** in build notes: slides 3,5,10,15,16,24,25                                                                                                                   |S     |those           |Explicit guardrail against over-correcting on the feedback.                                  |

### Recommended sequencing before the loop

1. **Tactic 1 + 2** — *today, <1 hr.* Verify the 2 MP4s play in your browser; generate the slide-7 poster. Resolves the most likely real complaint.
1. **Tactic 3** — ✅ already done (`slide-08-replacement.html`).
1. **Tactic 4** — *next session.* Highest staff-signal gain per hour (annotate slides 6 + 18).
1. **Tactic 6** — *if panel is Q&A-heavy.* Safe appetite-absorber.
1. **Tactic 7** — *only if time remains.* `[CUTTABLE]`.

-----

## 5 — Gaps & Assumptions

- `[ASSUMED-PACING]` — no speaker notes in file; pacing roles inferred. Share a script to tighten.
- `[VERIFY]` — slide 7 & 8 MP4 playback unconfirmed in this environment (H.264). Confirm in your presenting browser.
- `[DEFECT]` — `computis-rule-engine.png` (slide 7 poster/fallback) missing on disk.
- `[ASSET NEEDED]` — slide 20 confidence-slider GIF and SBAR handoff do not exist.
- `[GAP]` — screening variant out of scope. If revisited, the right move there is the **opposite**: cut slides 11/12, don’t add assets.

-----

## Deliverables produced

- `wayline-deck-ui-density-audit.md` — this document
- `slide-08-replacement.html` — drop-in: static PNG → looped MP4, with working poster fallback