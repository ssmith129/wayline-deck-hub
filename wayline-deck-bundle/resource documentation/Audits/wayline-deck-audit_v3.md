# Wayline Deck — UI/Visual-Density Audit

**Deck audited:** `wayline-deck.html` (the Wayline founding-product-designer pitch, with Computis + Symplify embedded as case studies)
**Scope:** This deck as-is · full-length 25–30 min version only
**Date:** May 2026

---

## Scope notes (read first)

Two framing corrections that change the recommendations:

1. **This is the Wayline pitch deck, not two standalone decks.** Computis (slides 3–13) and Symplify (slides 14–20) are *embedded case studies* inside a hiring pitch. "More UI assets" must serve the trust-surface thesis — not just prove the case studies. The panel's volume instinct is the screenshot-dump risk in disguise; the deck is closer to right than they think.

2. **Slide 19 is missing from the markup.** Section comments run 18 → 20. Runtime confirms **25 main `<section>` slides while numbering runs to 26.** Resolve before the interview loop — either restore a slide or renumber so the chrome counter is honest. *(Unresolved as of this writing.)*

**Asset reality:** The `/assets/` folder and the local GitHub path were not accessible during the audit. Every screenshot/MP4 referenced via `<img>`/`<video>` is therefore tagged `[CLAIMED]` (deck references it; existence unverified) rather than `[VERIFIED]`. This makes asset verification (T1) the single highest-leverage action — see playbook.

---

## 1. Evaluation Rubric

Each slide scored on four axes. Scales are explicit so the audit is reproducible.

**(a) Visual density — current state**
`T` text-only · `D` diagram / CSS-component · `H` hybrid (type + asset) · `A` asset-led (image/video is the argument)

**(b) UI-asset insertion opportunity — 0–3**
`0` none (asset would damage it) · `1` marginal · `2` real · `3` high-leverage (asset materially strengthens the staff signal)

**(c) Pacing / cognitive-load risk if an asset is added — severity**
`P0` critical (breaks narration rhythm or turns the slide into a dump) · `P1` moderate (manageable with constraints) · `P2` low

**(d) Staff-level signal of the proposed asset**
`★★★` evidence of decision-making / systems thinking · `★★` craft demonstration · `★` decoration (default-cut)

**Verdict vocabulary:** `ADD` (no asset now, insert one) · `ENHANCE` (asset exists, upgrade it) · `HOLD` (asset only as backup/appendix, not inline) · `LEAVE` (correct as-is; adding hurts).

**Asset-status tags:** `[CLAIMED]` deck references the file but existence is unverified · `[ASSET NEEDED]` would have to be created · `[DATA NEEDED]` a value is required and must not be fabricated.

---

## 2. Slide-by-Slide Audit

Density-budget context: the deck already carries ~7 asset-bearing slides (6, 7, 8, 9, 13, 17, 18) plus 4 live CSS-component slides (14, 21, 22, 23). That's a healthy asset load for a 26-slide narrated pitch. The gap is *asset presence on stakes/methodology slides*, not a wholesale shortage — so the dominant verdict is ENHANCE/LEAVE, not ADD.

| # | Title | Type | Opp (b) | Risk (c) | Signal (d) | Verdict | Note |
|---|-------|:----:|:-------:|:--------:|:----------:|:-------:|------|
| 1 | Title | T | 0 | P0 | — | **LEAVE** | Anchor slide. An asset cheapens the editorial open. |
| 2 | Agenda (3-col) | T | 1 | P1 | ★ | **LEAVE** | Thumbnails tempting but premature — screenshots not yet earned. |
| 3 | "11:00 PM April 14" | T | 0 | P0 | ★ | **LEAVE** | Stakes/setup. Silence is the point. |
| 4 | 32% conversion gap | T | 1 | P1 | ★★ | **HOLD** | Chart belongs in appendix, not on the line. → backup **B1**. |
| 5 | Three stakes | T | 0 | P0 | ★ | **LEAVE** | Setup. Type-only is correct. |
| 6 | From % to a decision (before/after) | H | 3 | P1 | ★★★ | **ENHANCE** | Load-bearing anchor. Callouts added — see §4. |
| 7 | Override is the failure mode | A (video) | 3 | P1 | ★★★ | **ENHANCE** | Already MP4. Highest live-failure risk — verify it plays/loops/rests on result. |
| 8 | Anomaly route | A | 2 | P2 | ★★ | **ENHANCE** | Static fine; one annotation callout available. |
| 9 | The honest miss (68/100) | H | 2 | P2 | ★★★ | **ENHANCE** | Highest-signal slide. Two-state (miss + fix) would close the loop. |
| 10 | 4 numbers overview | T | 1 | P1 | ★★ | **LEAVE** | Restraint *is* the argument. Don't asset it. |
| 11 | How we measured (40/45) | T | 1 | P2 | ★★ | **HOLD** | Methodology → backup **B2**, not inline. |
| 12 | How we measured (32/85) | T | 1 | P2 | ★★ | **HOLD** | 85% is objection bait — keep clean. → backup **B3**. |
| 13 | I write the React (Figma↔code) | H | 3 | P1 | ★★★ | **ENHANCE** | Craft proof. Code screenshot must be legible at projection scale. |
| 14 | Through-line #1 (CSS cards) | D | 1 | P1 | ★★ | **LEAVE** | Live CSS renders already. PNGs here are redundant. |
| 15 | "06:45" Symplify open | T | 0 | P0 | ★ | **LEAVE** | Stakes/setup. Protect. |
| 16 | Real vs. mocked | T | 2 | P1 | ★★★ | **ADD** | Strong honesty beat going naked. Small distribution diagram. `[ASSET NEEDED]` |
| 17 | Supervision primitive (constellation) | A | 3 | P1 | ★★★ | **ENHANCE** | 5 claimed PNGs. Invariant callout added — see §4. |
| 18 | Voice as input (acuity board) | A | 2 | P2 | ★★ | **ENHANCE** | Hero asset; detailed capture spec already in markup. |
| 19 | — | — | — | — | — | **[GAP]** | Missing from markup. Resolve first. |
| 20 | Three artifacts | T | 1 | P0 | ★ | **LEAVE** | Deliberate-breath slide. Asset kills the breath. |
| 21 | Through-line #2 (CSS cards) | D | 0 | P1 | ★ | **LEAVE** | Repeat of 14's components. Already dense. |
| 22 | The compound (3-col CSS) | D | 0 | P1 | ★★ | **LEAVE** | Three live renders + sketch. Maxed. |
| 23 | Legibly seamful (sketch) | D/H | 2 | P1 | ★★★ | **ENHANCE** | Thesis slide. Optional *one* motion moment — only if slide 7 is solid. |
| 24 | First 90 days | T | 0 | P1 | ★ | **LEAVE** | Operational. Type-only signals seriousness. |
| 25 | Spoken close | T | 0 | P0 | — | **LEAVE** | Never asset a close. |
| 26 | The ask | T | 0 | P0 | — | **LEAVE** | Same. |

**Verdict tally:** ADD 1 · ENHANCE 7 · HOLD 3 · LEAVE 14 (+1 GAP).
The deck does **not** need more asset slides. It needs the existing 7 verified, plus 1–2 strategic additions. Resisting the volume instinct is itself the staff-level move.

---

## 3. Compromise Playbook

Trade-off tactics that satisfy "more visuals" without degrading pacing. Effort: `LO` <30 min · `MD` 30 min–2 h · `HI` >2 h.

**T1 — Verify before you add. (LO · slides 6,7,8,9,13,17,18) — DO FIRST.**
~7 asset slides reference ~11 files that could not be verified. The bigger risk is *existing* visuals failing live, not a shortage. Open the deck from the real `/assets/` path on the actual presentation machine; confirm every `<img>`/`<video>` resolves. Each unresolved placeholder is worse than a text slide.

**T2 — Annotation over accumulation. (LO–MD · slides 6,8,17)**
Make existing screenshots do more, don't add new ones. One callout per asset, max two per slide. Annotated-static > raw-static > GIF for evidence slides. If a slide needs >2 callouts, it's doing too much — split it. *(Shipped on 6 and 17 — see §4.)*

**T3 — One motion moment, deck-wide. (policy · slides 7 + maybe 23)**
The deck has exactly one inline video (slide 7) — correct discipline. Permit a second loop only on slide 23 (thesis), and only if slide 7 verifies solid. Never three. For UI motion use MP4 + poster (as slide 7 does); never GIF (banding on the confidence colors).

**T4 — Backup-slide placement for deep-dives. (MD · slides 4,11,12)**
Methodology and the conversion-gap metric are where an interviewer presses for proof. Keep charts off the line; build them as appendix slides triggered only if asked. Protects pacing; arms Q&A; serves the objection-readiness signal. *(Shipped as B1–B3 — see §4.)*

**T5 — Breather protection. (policy · slides 3,5,10,15,20,25,26)**
These seven are load-bearing silence. "More visuals" must not touch them. At full length the silences are *more* affordable, not less — narration fills the air an asset would otherwise occupy. Converting a breather to an asset slide is the most common way this failure mode happens.

**T6 — Resolve the slide-19 gap + counter. (LO · slide 19) — DO FIRST (with T1).**
Restore the slide or renumber. Verify the chrome counter matches the true section count.

> **T7 (screening-variant density) — REMOVED.** Scope is full-length only. The screening-cut logic does not apply; cuttable tags below are full-deck cut-order only.

### Recommended sequencing (full-length, limited time before the loop)

1. **T1 + T6** — verify all claimed assets resolve; fix the slide-19 gap and counter. *Everything else is moot if assets fail.*
2. **T3 decision** on the slide-7 MP4 — confirm it plays/loops/rests-on-result, or fall back to its poster PNG.
3. **T2** — annotations on 6 and 17. *(Done.)*
4. **T4** — backup charts for 4/11/12. *(Done — B1–B3.)*
5. **Slide 9 two-state** and **slide 16 diagram** — only after 1–4. Both `[CUTTABLE]`.

---

## 4. Build Status — what's already shipped

Changes made to the deck since the audit, with verification notes:

| Change | Slides | Status | Verification |
|--------|--------|--------|--------------|
| **Annotation callouts** | 6, 17 | ✅ Shipped | Rendered + reviewed. Slide-6: "55% → accept in bulk" / "11% → escalate." Slide-17: invariant line "Same confidence primitive. Four surfaces." Accent-green; `--strike` red kept reserved. |
| **Backup charts B1–B3** | appendix (for 4/11/12) | ✅ Shipped | Off the linear sequence; counter stays 25; `B` cycles B1→B2→B3, `Esc` returns. Runtime-tested, no console errors. |
| **Font swap → Manrope** | deck-wide | ✅ Shipped | Manrope display + Inter body. Display weights 700/800, letter-spacing relaxed for Manrope's rounder set. Rendered on slides 1/6/10/23. |

### Callout detail (slides 6 & 17)
- **Slide 6** — two callouts on the after-panel. Connector arrows are positioned for the *real* PNG filling the frame; once the asset is in `/assets/`, nudge the `top`/`bottom` values so each arrow lands on the High row and Low row. (Inline comment marks the spot.)
- **Slide 17** — one callout, centered over the hero, naming the invariant rather than any single component. This is the line that lifts the slide from ★ (five screenshots) to ★★★ (one propagated primitive). Do **not** label peripherals individually.

### Backup-chart detail (B1–B3)
- **B1 (slide 4 · 32%)** — paired bar, pre/post, rate-only. Confound named in-slide ("sales also changed the onboarding script in the same window → directional, not isolated").
- **B2 (slide 11 · 40/45%)** — dot-distribution across the 6-firm cohort, medians marked. The direct answer to "n=6 is small." Strongest of the three.
- **B3 (slide 12 · 85%)** — leads with the exact definition of "reopened design-clarification ticket." Bars carry `n=?` placeholders. Fallback: present as definition-only if raw counts can't be sourced.

### Font-swap caveat
Dropping Fraunces costs one thing: the **slide-23 italic pull-quote** loses the expressive serif italic (now Manrope oblique at weight 500). It reads fine, but if that quote matters, keep one serif scoped to it (Option 2). The big numbers (slide 10) and title (slide 1) are arguably *stronger* in Manrope.

---

## 5. Fabrication Ledger

**Nothing fabricated.** All load-bearing metrics preserved and used once each, no cross-slide duplication:
- Computis: 40% accounting-time, 45% CPA-onboarding, 32% demo-to-customer, 85% engineering-dependency.
- Symplify: 14 shipped AI features, confidence-threshold slider, SBAR handoff, HIPAA context.

Every proposed asset is tagged `[CLAIMED]` or `[ASSET NEEDED]` — never assumed to exist.

### Open items requiring your input

| Item | Where | Action |
|------|-------|--------|
| `[GAP]` Slide 19 | markup | Intentional cut or missing? Restore or renumber + fix counter. |
| `[CLAIMED]` ~11 asset files | 6,7,8,9,13,17,18 | Verify each resolves from the real `/assets/` path (T1). |
| `[DATA NEEDED]` B2 dot positions + axis unit | backup B2 | Replace illustrative dots with real per-firm values; set days vs. hours. Flagged on-slide. |
| `[DATA NEEDED]` B3 raw pre/post counts | backup B3 | Source the counts, or present as the definition slide alone. Flagged on-slide. |
| Redundancy: slide-17 hero | 17 vs. 14/21/22 | Assistant card already renders live on 14/21/22. Confirm 17's hero shows something new (e.g., SBAR handoff). |
| `[ASSET NEEDED]` slide-9 "fix" half, slide-16 diagram, slide-23 motion loop | 9,16,23 | Build only after T1–T4. All `[CUTTABLE]`. |
| Style: red used twice | 9 (dot) + 23 (strike) | Deck's own rule says red "used once." Slide-9 dot weakens the slide-23 punch. |

### Cut-order (if time runs short)
1. Slide-23 motion loop — `[CUTTABLE]`, cut first.
2. Slide-9 two-state "fix" half.
3. Slide-13 Figma half (slide survives on the code panel alone).
4. Slide-16 distribution diagram (text version is defensible).
5. Backup B1 (verbal defense of 32% is nearly as good).

> Build B3 *first* among the backups despite its cut-order: it defends the metric your own deck flags as most attackable.
