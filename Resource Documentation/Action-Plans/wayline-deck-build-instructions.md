# Wayline Deck — Slide Resize Build Instructions

> **Owner:** Sean Smith
> **Canvas migration:** 1600×900 → **1920×1080** (already applied)
> **Status:** Slide 8 complete (Option B). This document tracks per-slide work remaining.
> **Scope rule:** Verified metrics, hierarchy, and typography are **locked**. Slide 18 copy was rewritten (voice-modality video → patient-acuity dashboard); all other slide copy is locked. **Edits redistribute spatial allocation only.**

---

## Priority Legend

| Tag | Meaning |
|-----|---------|
| **P0** | Materially improves asset showcase |
| **P1** | Polish — consistency, hierarchy |
| **P2** | Optional refinement |

---

## Summary — Remaining Slides

Eleven asset-bearing slides remain: **eight discrete spatial reallocations, one consistency sweep, one batch verification pass.**

| # | Slide | Priority | Action Type |
|---|-------|----------|-------------|
| 6 | From a percentage to a decision (before/after table vs. insights panel) | **P0** | Reallocate |
| 7 | Override is the failure mode (rule engine video) | **P0** | Enlarge video |
| 9 | I shipped this. Then I audited myself (critique screen) | **P1** | Enlarge artifact |
| 13 | I write the React (Figma + code two-up) | **P0** | Enlarge both |
| 14 | Same primitive. New vertical (first compare) | **P1** | Match slide 22 |
| 17 | Same primitive across fourteen features (5-asset grid) | **P0** | Re-grid |
| 18 | Input isn't typed. It's inferred. (patient acuity dashboard) | **P0** | Frame static asset |
| 19 | Role isn't permissions (3-up sidebars) | **P1** | Enlarge each |
| 20 | I shipped the wrong knob (before/after fix) | **P1** | Enlarge both |
| 22 | Same primitive. Two regulated verticals (compare) | **P1** | Enlarge both |
| 23 | One primitive. Three regulated verticals (3-up + Wayline) | **P0** | Enlarge first two |

### Pattern-Lock Dependency
Slides **14, 22, and 23** share one asset pair (Computis classification + Symplify popup). Apply consistent treatment across all three to reinforce the "same primitive" argument. **Decide grid dimensions once, apply across all three** — if slide 14 lands at 720px grid height, slide 22 does too.

---

# Project 1 · Classification + Rule Engine + Self-Audit
### Computis — Slides 6, 7, 9

## Slide 6 — From a Percentage to a Decision · **P0** · Reallocate
**Asset:** Before/after — raw confidence table vs. banded insights panel.
Two-column layout. Left is a hand-built mock-table. Right is the real `classification-insights.png`. Min-height currently 480px on a 1080 canvas (~44%). Underutilized.

- [ ] Raise `.row` min-height from **480px → 620px**
- [ ] Confirm the mock-table left column scales proportionally — may need a font-size bump on `.row-tab` rows for parity with the larger right panel
- [ ] Verify the bottom caption ("Same data…") doesn't collide with the enlarged row
- [ ] Consider shifting column ratio from `1:1` → `1fr 1.15fr` so the real screenshot dominates the comparison

## Slide 7 — Override Is the Failure Mode · **P0** · Enlarge video
**Asset:** Rule engine MP4 — currently capped at 70% canvas height.
Pattern lock with slide 8 (bumped to 85%). Slide 7 needs the same treatment for consistency — and because the video has fine UI detail in the rule-authoring flow.

- [ ] Change `max-height: 70%` → **`85%`**
- [ ] Change `margin: 32px auto 0` → **`20px auto 0`**
- [ ] Add `margin-top: -8px` to the `h2` to match slide 8's tightened header
- [ ] Verify the video's native aspect-ratio `1920 / 1246` still fits — it should, video is wider than 8:5

## Slide 9 — I Shipped This. Then I Audited Myself. · **P1** · Enlarge artifact
**Asset:** 68/100 audit screen — fixed 440×611 sidecar (design-critique markdown).
Currently locked at `flex: 0 0 440px; height: 611px`. The text column keeps dominance (correct for this slide), but the markdown should be readable enough to verify the 68/100 line.

- [ ] Bump `flex: 0 0 440px` → **`flex: 0 0 540px`**
- [ ] Bump `height: 611px` → **`height: 740px`**
- [ ] Confirm the asset still sits at `align-self: flex-start` — top-aligned with the heading is intentional
- [ ] Hold the row gap at **7%** — the asymmetry gives the text column its weight

---

# Project 1 Close + Transition
### Computis → Symplify — Slides 13, 14

## Slide 13 — I Write the React · **P0** · Enlarge both
**Asset:** Figma source + React code — two-up at 460px min-height.
The "I write the React" claim only lands if the code is legible. Code screenshots need vertical room. **One of the highest-leverage resize opportunities in the deck.**

- [ ] Raise `.row` min-height from **460px → 640px**
- [ ] Tighten `.row` gap from **4% → 3%** to claim more horizontal pixels
- [ ] Both `.asset-frame` elements use `flex: 1` — confirm they expand to fill the new height
- [ ] Code screenshot legibility — at 640px frame height, verify React syntax is readable at projection distance. If still tight, push min-height to **680px** and trim the `body-l` max-width to **70%**

## Slide 14 — Same Primitive. New Vertical. (first showing) · **P1** · Match slide 22
**Asset:** Two-up — Computis insights (wide) + Symplify popup (tall) — 560px min-height.
Transition slide. Sets up the visual rhyme that repeats on slides 22 and 23. **Whatever change applies here must also apply to slide 22.**

- [ ] Raise grid min-height from **560px → 720px**
- [ ] Remove the `max-height: 560px` cap on the Symplify popup — let it scale to the new grid height
- [ ] Hold the grid columns at **`1.45fr 0.75fr`** — wide-screen vs. tall-popup ratio is correct
- [ ] **Apply the identical change to slide 22** to preserve the pattern lock

> **Transition pattern:** Slides 14, 22, 23 share asset DNA. The "one primitive, multiple verticals" argument only works if the assets feel like the same family across all three appearances.

---

# Project 2 · Primitive Proliferation + Inferred Input
### Symplify — Slides 17, 18

## Slide 17 — The Same Primitive Across Fourteen Features · **P0** · Re-grid
**Asset:** Five-asset grid — hero in center, four peripherals at 85% opacity.
Densest asset slide in the deck. Grid is `1fr 2fr 1fr × 2 rows`; the hero spans both rows. The 14-features claim depends on the hero being unambiguously the canonical instance.

- [ ] Raise grid min-height from **620px → 800px**
- [ ] Widen grid gap from **24px → 32px** to let each peripheral breathe
- [ ] Verify peripherals at `opacity: 0.85` still read as present, not faded — at the larger size, **0.9** may be more honest
- [ ] Hero column is currently `2fr` — consider **`2.2fr`** on a 1920 canvas to give it more dominance

## Slide 18 — Input Isn't Typed. It's Inferred. · **P0** · Frame static asset
**Asset:** Symplify patient acuity dashboard — **static PNG** (slide rewritten; previously held the voice-documentation MP4). Parity-with-slide-7 logic no longer applies — it's a single still image, not motion.

**Current state per `slide-18-replacement.html`:**
- Heading: "Input isn't typed. It's inferred."
- Sub: "The clinician's job is to confirm what the system already extracted."
- Frame: Single `.asset-frame` at `height: 72%` with `margin-bottom: 4%`
- Source: `Symplify-1.7.4/src/feature-module/components/pages/ai-modules/patient-acuity/patientAcuity.tsx`
- Asset file: `symplify-patient-acuity.png` *(still under capture — placeholder block live)*

**Actions:**
- [ ] Verify the rendered asset has **all four acuity bands visible** — if any band is missing in the capture, the proof point weakens

> **Wayline signal:** Slide 18 is the slide Wayline's panel lingers on — the "confirm what the system extracted" frame is exactly the Wayline argument. The patient acuity dashboard makes the case more concretely than the voice video did (specific diagnoses, clinical bands, sparklines = trend, not just a single moment).

---

# Project 2 · Role Calibration + Honest Miss
### Symplify — Slides 19, 20

## Slide 19 — Role Isn't Permissions. It's Calibration. · **P1** · Enlarge each
**Asset:** Three sidebar variants — admin / doctor / patient. Three asset-frames in a `row-3` grid at 600px min-height.
Tagged "**first to cut if pacing slips**" in the script comment — make it strong if it survives, don't overinvest.

**Capture the asset first.** Placeholder is live with explicit capture requirements:
- (a) acuity distribution by unit visible at top
- (b) at least 6 patient rows showing all four acuity bands (critical / high / moderate / stable)
- (c) at least one trend sparkline visible per row
- (d) filter chips at top with acuity color dots
- Do **not** desaturate — `ACUITY_COLORS` tokens carry the chromatic work
- Patient names, room numbers, and diagnoses (Septic Shock, ARDS — Ventilated, STEMI — Post PCI) must remain legible at projection scale

**Size for legibility, not parity.** Slide 7's 85%-to-match-the-video logic does **not** apply — a still dashboard with 6+ rows of small text needs different treatment than a wide-frame video. Test at `height: 72%` first; only raise if patient rows are illegible.

- [ ] Raise `.row-3` min-height from **600px → 760px**
- [ ] Each frame uses `flex: 1` — will scale automatically with the grid
- [ ] If raising height, also reduce `margin-bottom: 4% → 2%` to absorb the change
- [ ] Verify the `body-m` sub-headline at `max-width: 70%` doesn't crowd the asset top edge once the image loads
- [ ] Caption text (`.body-s` under each frame) — verify it doesn't break alignment when frames get taller
- [ ] Confirm the placeholder block's `onerror` fallback renders cleanly during dev — should disappear once the PNG is in `./assets/`
- [ ] Cross-check against slide 17: patient acuity must read as **one of those fourteen** — slide 17's hero shouldn't look like a different visual family from slide 18's dashboard

## Slide 20 — I Shipped the Wrong Knob · **P1** · Enlarge both
**Asset:** Strikethrough global slider + per-feature thresholds (the fix). Symplify's honest-miss beat; visual rhyme with slide 9. Two asset-frames side by side, with an 11° rotated strikethrough rule overlaid on the left.

- [ ] Raise `.row` min-height from **520px → 680px**
- [ ] Strikethrough rule is positioned via `transform: rotate(11deg) translateY(50%)` — verify it still spans the asset at the new height
- [ ] Footer caption ("Caught in clinician testing…") — confirm it sits flush at the canvas bottom with the enlarged row above
- [ ] **P2** — consider increasing `.row` gap from **6% → 7%** to separate the "wrong" and "right" panels more decisively

---

# Synthesis — Slides 22, 23
### Compound Argument

## Slide 22 — Same Primitive. Two Regulated Verticals. · **P1** · Enlarge both
**Asset:** Second appearance of the Computis + Symplify compare. Identical structure to slide 14 — **mirror whatever change was made there.**

- [ ] Apply the exact change made to slide 14 — **min-height match**
- [ ] Remove the `max-height: 560px` cap on the Symplify popup (identical to slide 14)
- [ ] Verify the heading "Same primitive. Two regulated verticals." sits in the same vertical position as slide 14's heading
- [ ] Hold the column ratio **`1.45fr 0.75fr`** consistent

## Slide 23 — One Primitive. Three Regulated Verticals. · **P0** · Enlarge first two
**Asset:** Three-up — Computis + Symplify + Wayline sketch. The compound payoff; third appearance of the pattern. The Wayline column is a hand-drawn sketch component, not a screenshot. **The first two columns can grow; the sketch must remain visually balanced with them.**

- [ ] Raise `.row-3` min-height from **480px → 600px**
- [ ] Bump Computis frame max-height from **380px → 500px**
- [ ] Bump Symplify frame max-height from **460px → 580px**
- [ ] Wayline sketch column — increase inner pane padding and font-sizes proportionally so the three columns feel parity-balanced
- [ ] Widen `.row-3` gap from **48px → 56px**
- [ ] If the three sidebar screens have noticeably different native aspect ratios, consider letterboxing to a uniform frame ratio so the three-up reads as a deliberate set

---

# Closing Batch Pass — Non-Asset Slides
### ★ Slides 1–5, 10–12, 15, 16, 21, 24–27 (16 total) · **P2**

Text-only and diagram-only slides inherit the new canvas via percentage padding. Walk through once at the end to flag anything sparse, overflowing, or out of balance.

- [ ] Open the deck post-resize and walk every text-only slide
- [ ] Flag any slide where the new 1920×1080 ratio leaves text feeling stranded
- [ ] **Slide 10** — Computis outcomes overview, four large numbers — verify the numeric scale still feels confident, not lost
- [ ] **Slide 21** — Symplify outcomes — same check
- [ ] **Slide 26** (centered "one thing they remember") — confirm the centering still feels intentional, not accidental
- [ ] **Slide 24** (the seamful reframe) — **kill-switch slide.** If anything looks worse at the new size, this is the most worth fixing

---

## Execution Summary

| Metric | Count |
|--------|-------|
| P0 actions | 8 |
| P1 actions | 4 |
| P2 batch pass | 1 |
| Est. per-slide work | ~90 min |
| Est. closing batch | ~30 min |

**Final step:** After all changes ship, do one full deck walkthrough at projection scale (full-screen) before locking the file.

> ⚠️ **Open dependency:** Slide 18 asset (`symplify-patient-acuity.png`) is still under capture. Placeholder block ships in dev but **must be replaced before lockup.**
