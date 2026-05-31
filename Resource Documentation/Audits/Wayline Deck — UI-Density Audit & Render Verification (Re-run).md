# Wayline Deck — UI-Density Audit & Render Verification (Re-run)  
Second-pass audit of the portfolio case-study deck for a Senior→Staff product-design interview loop. This re-run re-verifies the deck **against the files actually on disk today**, not the version captured in the first audit. The deck has been revised since — slides 9 and 13 were rebuilt, a deck-wide title-anchor system was added, and the asset folder has changed. Two asset references are now broken.  
**Deck:** wayline-deck.html · 25 slides (numbered 1–26, no 19) · 16:9 · custom keyboard-driven HTML · full-length version only **Path:** wayline-deck-hub/wayline-deck-bundle/wayline-deck.html (2,055 lines · modified 2026-05-24) **Audited:** 2026-05-24 **Method:** Static parse of every slide on disk + asset-reference cross-check against the real assets/ directory + visual inspection of changed/critical image assets.  
  
## TL;DR  
* **The headline finding has changed since the first audit: there are now TWO broken asset references, not one — and both sit on your highest-signal Computis evidence slides.**  
* **Slide 6 (computis-classification-insights.png) is missing on disk.** The folder now contains computis-classification-insights.svg instead. The HTML still points at .png, so the Computis climax slide (“From a percentage to a decision”) falls back to its placeholder. This is **new** — this asset rendered fine in the first audit. The fix is a one-character-class edit (.png → .svg); the SVG is a clean, projection-ready render.  
* **Slide 7’s poster defect from the first audit is STILL unfixed.** computis-rule-engine.png does not exist; the <video poster="…"> still references it. If the MP4 fails to load while presenting, slide 7 falls to the hatch placeholder. Recommended ffmpeg one-liner is unchanged from the first audit.  
* **The deck improved in two real ways.** Slide 9 was rebuilt from a screenshot into a native two-column “what broke / what held” scorecard with a 68/100 hero — stronger staff signal, no asset dependency. Slide 13 was rebuilt into a clean Figma-render-vs-dark-code split using two new, verified assets.  
* **The first audit’s slide-8 MP4 rewire was NOT applied.** Slide 8 is back to (or never left) the static computis-anomaly-route.png. The .mp4 exists in assets/ but is orphaned. This is fine — static is defensible here — but if you intended the rewire, it’s not in this file.  
* **Still genuinely missing:** slide 20’s confidence-slider GIF and SBAR handoff artifact. Unchanged from the first audit.  
* **Protect the Wayline section (21–26).** Its asset-lightness is still deliberate and still correct. The product doesn’t exist; that is the pitch.  
* **Net:** the deck is not under-assetted. The real work before the loop is fixing two broken references — both ≤5-minute edits — and doing one live playback pass in your presenting browser.  
  
## 1. What changed since the first audit  

| Area | First audit | Now | Implication |
| --------------------- | ----------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------- |
| Slide 6 “after” asset | …insights.png present, ✅ renders | .png gone; .svg present; HTML still says .png | New defect — placeholder on climax slide |
| Slide 7 poster | …rule-engine.png missing (the one defect) | Still missing | Unfixed carry-over |
| Slide 8 | Recommended rewire to .mp4 | Static .png (rewire not applied); .mp4 orphaned | Cosmetic; static is fine |
| Slide 9 | Screenshot computis-design-critique.png | Rebuilt as native HTML scorecard (68/100, two-column) | Improvement; screenshot now orphaned |
| Slide 13 | figma-…png + code-…png | Rebuilt: figma-…-clean.png + code-…-dark.png (both new, verified) | Improvement |
| Layout system | Per-slide nudges | New .slide--top-anchor + .title-block uniform anchor | Cleaner vertical rhythm |
  
## 2. Evaluation Rubric  

| Axis | Scale | Measures |
| ----------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Density | 0–3 | Current visual / information load |
| Asset opportunity | None / Low / Med / High | Room for a UI artifact that earns its place |
| Pacing risk | P0 / P1 / P2 | Damage if an asset is added. P0 = breaks a deliberate breather/climax; P1 = noticeable drag; P2 = cosmetic |
| Staff signal | Decoration / Craft / Decision / Systems | What the asset proves. Decision = a judgment call; Systems = cross-feature/cross-vertical thinking. Decoration is the failure mode |
| Verdict | Fix / Enhance / Hold / Leave | Action |
  
**Motion-vs-static rule:** Motion (GIF/MP4) only when change over time is the point. Otherwise static. **Annotation rule:** Annotate when the artifact proves a decision the narration claims. Raw screenshots prove craft; annotated screenshots prove judgment — the staff signal.  
⚠️ **Pacing caveat:** the deck file still contains no speaker notes. Pacing roles are inferred from on-slide content + sequence [ASSUMED-PACING]. Comment markers in the HTML give script-time pairings (e.g. slide 6 = 4:00–6:00), which I’ve used to sharpen the inference.  
  
## 3. Slide-by-Slide Audit  
Sections: **Computis (1–13)** → **Symplify (14–20)** → **Wayline synthesis/pitch (21–26)**.  
**Computis (slides 1–13)**  

| # | Title | Type | D | Asset opp. | Verdict | Note |
| -- | ---------------------------------------------- | ----------- | - | ---------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | The trust surface… (title) | text | 0 | None | Leave | Cold open. A screenshot would undercut it. |
| 2 | The next 30 minutes | text | 1 | Low | Hold | Thumbnails would spoil the three reveals. |
| 3 | 11:00 PM April 14th | text | 1 | None | Leave | Deliberate tension beat. P0. |
| 4 | 32% conversion gap | text | 1 | Low | Hold | The number is the asset. |
| 5 | Three stakes | text | 2 | None | Leave | Rhetorical triad; UI breaks it. |
| 6 | From a percentage to a decision | hybrid | 3 | High | Fix · P0 | Climax of Computis arc. img src points at …insights.png, which is GONE from disk — .svg is there instead. Renders as placeholder. Repoint to .svg (or export .svg→.png). → Decision |
| 7 | Override is the failure mode | MP4 | 2 | High | Fix · P1 | Poster/fallback computis-rule-engine.png STILL missing (carry-over from first audit). Generate it. → Decision |
| 8 | If it recurs, it needs a noun in the URL | static PNG | 2 | High | Hold | computis-anomaly-route.png ✅ renders. First audit’s .mp4 rewire not applied; .mp4 orphaned in assets. Static is defensible. → Decision |
| 9 | I shipped this. Then I audited myself (68/100) | native HTML | 3 | covered | Leave | Rebuilt since first audit — now a two-column “what broke / what held” scorecard, no screenshot. Stronger honest-miss signal, zero asset risk. Don’t touch. → Systems |
| 10 | Measured, not asserted (4 numerals) | numerals | 2 | None | Leave | Load-bearing verified metrics. A dashboard here would weaken them. P0. |
| 11 | How we measured | text | 2 | None | Leave | Methodology = rigor; text is the medium. |
| 12 | How we measured (cont.) | text | 2 | None | Leave | Objection-readiness signal (“happiest to be pressed on”). Protect. |
| 13 | I write the React (Figma + code) | hybrid | 3 | covered | Leave (verify) | Rebuilt: figma-classification-insights-clean.png + code-classification-insights-dark.png. Both verified rendering. Figma-vs-code framing is a clean Systems beat. → Systems |
  
**Symplify (slides 14–20)**  

| # | Title | Type | D | Asset opp. | Verdict | Note |
| -- | ------------------------------------------------- | ---------- | - | ---------- | -------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 14 | Same primitive. New vertical | live HTML | 3 | High | Leave | Live dual-panel render. Live > screenshot. → Systems |
| 15 | 06:45 (Symplify cold open) | text | 1 | None | Leave | Mirror of slide 3. P0. |
| 16 | What was real / mocked | text | 2 | Low | Hold | Intellectual-honesty signal. Don’t dilute with an asset. P1. |
| 17 | Same primitive — across fourteen features | 5 PNGs | 3 | High | Leave (verify) | Best systems artifact in Symplify arc. All 5 referenced assets present. → Systems |
| 18 | Input isn’t typed. It’s inferred (patient acuity) | static PNG | 2 | High | Enhance · P1 | symplify-patient-acuity.png ✅ present. Optional annotation on one prefilled→confirmed field converts craft to Decision. |
| 20 | Three artifacts | text | 1 | Med | Add · P2 | Real text-gap. Confidence-slider GIF belongs here (temporal). [ASSET NEEDED] [CUTTABLE]. SBAR handoff also [ASSET NEEDED]. |
  
**Wayline synthesis / pitch (slides 21–26) — protect deliberate asset-lightness**  

| # | Title | Type | D | Asset opp. | Verdict | Note |
| -- | ---------------------------------------------------------- | --------- | - | ---------- | ------- | -------------------------------------------------------------------------------- |
| 21 | Same primitive. Two regulated verticals | live HTML | 3 | covered | Leave | Live dual-panel. |
| 22 | One primitive. Three regulated verticals | live HTML | 3 | High | Leave | Thesis slide; densest live artifact. P0. |
| 23 | Legibly seamful (live Wayline surface) | live HTML | 3 | covered | Leave | Most elaborate in-DOM mock; carries the design philosophy. P0 — do not touch. |
| 24 | First 90 days | text | 2 | None | Leave | Roadmap-as-product-UI would be fabrication. Wayline isn’t built. Honest as text. |
| 25 | I design the surface where a professional supervises an AI | text | 1 | None | Leave | Thesis restatement. P0. |
| 26 | The ask: two-day work trial | text | 0 | None | Leave | CTA. |
  
**Verdict roll-up**  

| Verdict | Slides                                                         |
| ------- | -------------------------------------------------------------- |
| Fix     | 6 (missing .png, has .svg), 7 (missing poster)                 |
| Enhance | 18                                                             |
| Hold    | 2, 4, 8, 16                                                    |
| Leave   | 1, 3, 5, 9, 10, 11, 12, 13, 14, 15, 17, 21, 22, 23, 24, 25, 26 |
| Add     | 20 (both assets [ASSET NEEDED] / [CUTTABLE])                   |
  
## 4. Render Verification Results  
Cross-checked every src=/poster= reference in the HTML against the real assets/ directory, and visually inspected the changed and load-bearing image assets.  

| Slide | Asset referenced | On disk? | Result |
| ----- | ------------------------------------------ | ------------------- | --------------------------------------------------------------------- |
| 6 | computis-classification-insights.png | ❌ NO (.svg present) | BROKEN — renders placeholder. Highest-priority fix. |
| 7 | computis-rule-engine.mp4 | ✅ Yes (691 KB) | MP4 present. H.264 — do a live playback pass [VERIFY IN YOUR BROWSER] |
| 7 | computis-rule-engine.png (poster/fallback) | ❌ NO | BROKEN — no safety net if MP4 fails. |
| 8 | computis-anomaly-route.png | ✅ Yes (1.0 MB) | ✅ Renders |
| 13 | figma-classification-insights-clean.png | ✅ Yes | ✅ Renders (verified — clean confidence panel) |
| 13 | code-classification-insights-dark.png | ✅ Yes | ✅ Renders (verified — dark-theme .tsx) |
| 17 | symplify-triage-badge.png | ✅ Yes | ✅ Present |
| 17 | symplify-ai-assistant-popup-large.png | ✅ Yes (542 KB) | ✅ Present (hero) |
| 17 | symplify-severity-badge.png | ✅ Yes | ✅ Present |
| 17 | symplify-urgency-indicator.png | ✅ Yes | ✅ Present |
| 17 | symplify-confidence-indicator.png | ✅ Yes | ✅ Present |
| 18 | symplify-patient-acuity.png | ✅ Yes (1.2 MB) | ✅ Renders (meets first-audit capture spec) |
  
**🔧 Defect #1 (NEW, highest priority) — Slide 6 broken image reference**  
Slide 6’s “after” image declares:  
```
<img src="./assets/computis-classification-insights.png"…/>

```
…but computis-classification-insights.png **does not exist on disk.** The folder contains computis-classification-insights.svg (81 KB, modified 2026-05-23) — a clean, projection-ready confidence-band panel that was clearly regenerated as SVG without updating the HTML reference. Result: the Computis climax slide falls back to its placeholder block.  
**Fix A (≤1 min, recommended): repoint the reference.** Inline-SVG renders crisply at projection scale.  
```
<img src="./assets/computis-classification-insights.svg"…/>

```
**Fix B (if you’d rather keep a raster):** export the SVG to PNG and keep the HTML unchanged.  
```
# requires librsvg (rsvg-convert) or Inkscape
rsvg-convert -w 3352 -h 2004 assets/computis-classification-insights.svg \\
  -o assets/computis-classification-insights.png

```
**🔧 Defect #2 (CARRY-OVER, unfixed) — Slide 7 missing poster/fallback**  
Unchanged from the first audit. The <video> declares:  
```
poster="./assets/computis-rule-engine.png"
onerror="…nextElementSibling.classList.remove('is-loaded')"

```
…but computis-rule-engine.png does not exist. If the MP4 fails to load on the presenting machine, the slide falls to the hatch placeholder.  
**Fix (≤5 min):** export one poster frame from the MP4 and save as assets/computis-rule-engine.png.  
```
# first frame:
ffmpeg -i assets/computis-rule-engine.mp4 -vf "select=eq(n\\,0)" -frames:v 1 assets/computis-rule-engine.png
# or the final/result frame:
ffmpeg -sseof -0.5 -i assets/computis-rule-engine.mp4 -frames:v 1 assets/computis-rule-engine.png

```
**ℹ️ Codec note**  
computis-rule-engine.mp4 is the only remaining playing MP4 in the deck (slide 8 uses a static PNG). Standard H.264 plays in all major desktop browsers, but headless/sandboxed Chromium often ships without proprietary H.264. Confirm playback in your **actual presenting browser** before the loop. [VERIFY]  
**🧹 Orphaned assets (present but unreferenced)**  
Not defects — just housekeeping. These files exist in assets/ but no current slide uses them:  
* computis-anomaly-route.mp4 — the first audit’s proposed slide-8 rewire; not wired in.  
* symplify-ai-assistant-popup-large.mp4 — unused motion variant.  
* computis-design-critique.png — superseded by the rebuilt native slide 9.  
* figma-classification-insights.png — superseded by the clean variant on slide 13.  
* symplify-ai-assistant-popup.png, Predictive Clinical Alerts.png, Smart Insights.png — never referenced.  
If you want slide 8 in motion (the first audit’s recommendation), the asset is sitting right there; otherwise leave it.  
  
## 5. Compromise Playbook  
Effort: **S** <30 min · **M** hours · **L** day+  

| # | Tactic | Effort | Slides | Why it protects pacing |
| - | --------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | --------------------------------------------------------------------------------------------- |
| 1 | Repoint slide 6 to the .svg (or export .svg→.png) | S | 6 | Closes the new, highest-priority defect on your Computis climax. Zero pacing cost. |
| 2 | Generate slide 7 poster PNG | S | 7 | Closes the carry-over defect. Working fallback on a top-signal slide. |
| 3 | Live playback pass for the slide-7 MP4 in your presenting browser | S | 7 | Confirms the one remaining motion asset actually plays. |
| 4 | Annotate, don’t add — one callout on slide 18 (prefilled→confirmed field) | M | 18 | Same slide count, higher signal. Craft → Decision. |
| 5 | (Optional) wire slide 8 to its orphaned .mp4 if motion is wanted | S | 8 | Asset already exists; motion where motion is the point. Skip if static reads better. |
| 6 | Backup-slide deep-dives after slide 26 (full dashboards, SBAR) | M | appendix | Absorbs “more UI” appetite without bloating the linear narrative. Best for a Q&A-heavy panel. |
| 7 | Build confidence-slider GIF for slide 20 | M–L | 20 | The one missing temporal artifact. [ASSET NEEDED] [CUTTABLE]. |
| 8 | Asset standards: loops ≤6 s, ≤1 MB, muted, autoplay-on-enter/pause-on-exit (JS already does this); statics object-fit: contain (already set). | S | all asset | Consistency prevents the “screenshot dump” feel. |
| 9 | Tag no-asset zones in build notes: 1, 3, 5, 10, 11, 12, 15, 16, 24, 25 | S | those | Explicit guardrail against over-correcting on the panel’s “more UI” feedback. |
  
**Recommended sequencing before the loop**  
1. **Tactics 1 + 2 + 3 — today, <1 hr.** Repoint slide 6, generate the slide-7 poster, verify the MP4 plays. This resolves both broken references and the only playback risk. **Do this first.**  
2. **Tactic 4 — next session.** Highest staff-signal gain per hour (annotate slide 18).  
3. **Tactic 6 — if the panel is Q&A-heavy.** Safe appetite-absorber.  
4. **Tactic 7 — only if time remains.** [CUTTABLE].  
  
## 6. Gaps & Assumptions  
* [ASSUMED-PACING] — no speaker notes in file; pacing roles inferred from on-slide content and the script-time comment markers in the HTML.  
* [VERIFY] — slide 7 MP4 playback unconfirmed in this audit environment (H.264 in a sandbox). Confirm in your presenting browser.  
* [DEFECT — NEW] — computis-classification-insights.png (slide 6) missing on disk; .svg present, HTML not repointed.  
* [DEFECT — CARRY-OVER] — computis-rule-engine.png (slide 7 poster/fallback) still missing on disk.  
* [ASSET NEEDED] — slide 20 confidence-slider GIF and SBAR handoff still do not exist.  
* [GAP] — screening/short variant out of scope. If revisited, the right move there is the opposite: cut slides 11/12, don’t add assets.  
* The first audit’s slide-08-replacement.html deliverable does not appear to be wired into this wayline-deck.html. If you intended that rewire, it isn’t in the live file.  
**Bottom line**  
The deck got better since the first audit — slides 9 and 13 are stronger, and the layout system is cleaner. But two image references are broken, both on your strongest Computis evidence, and both are sub-five-minute fixes. Fix those two references and do one live playback pass; that is the real pre-loop work, and almost certainly what the panel’s “more UI” comment was actually reacting to.  
