# Wayline Deck — Enhancement Plan to Panel-Ready

**Deck:** `wayline-deck.html` · full-length 25–30 min · Senior-to-Staff product designer pitch
**Basis:** Audit findings established in this conversation (rubric, slide-by-slide verdicts, playbook T1–T6, fabrication ledger). No new critique introduced.
**Mode:** Forward-only. Steps cover work remaining from the current audited state.

-----

## Completed baseline (not re-stepped)

Three enhancements already shipped and verified. They are the starting state for this plan, not steps within it:

- **Annotation callouts** — slides 6, 17 (audit §4; tactic T2). Rendered + reviewed.
- **Backup charts B1–B3** — appendix for slides 4/11/12 (T4). Off-sequence, counter stays 25, `B`/`Esc` nav, runtime-tested.
- **Font swap → Manrope** — deck-wide, display 700/800 + relaxed tracking. Rendered on 1/6/10/23.

Two of these carry **open data flags** that are *not* design work but content the candidate must supply — tracked in Phase 4 (P4-S1, P4-S2) because the slides ship incomplete until filled.

-----

# 1. Enhancement Plan

Phases sequenced by dependency: **Phase 0 (integrity) → 1 (asset verification) → 2 (narrative/objection adds) → 3 (visual polish) → 4 (content gaps the candidate must close)**. Earlier phases are prerequisites — verifying an asset (P1) before annotating a new one (P3) prevents annotating a file that doesn’t resolve.

-----

## Phase 0 — Structural integrity

*Must precede everything. A broken counter or missing slide undermines every downstream change.*

### P0-S1 — Resolve the slide-19 gap

- **What:** The missing slide-19 in the markup (audit Scope note 2; ledger open-item).
- **Why:** Runtime shows 25 main sections while numbering runs to 26. A gap or off-by-one counter reads as carelessness to a panel evaluating attention to detail.
- **How:** Decide intentional cut vs. accidental omission.
  - If cut → renumber sections and comments 20→19, 21→20 … 26→25 so `data-slide` is contiguous.
  - If missing → restore the intended slide.
- **Severity:** P0
- **Done:** `data-slide` attributes are contiguous 1…N; the chrome counter total matches the true section count with no gap.
- **Signal:** Narrative clarity, attention to craft.

### P0-S2 — Reconcile the chrome counter

- **What:** The nav-chrome total vs. actual main-slide count.
- **Why:** Ledger + audit; a counter that disagrees with the deck is a visible defect on screen-share.
- **How:** Confirm the script’s computed `total` (currently 25, appendix correctly excluded) matches what the chrome displays after P0-S1. If P0-S1 renumbers, re-verify in-browser that the counter reads the new total and `B`/`Esc` appendix nav still returns to the correct main slide.
- **Severity:** P0
- **Done:** Counter reads the correct total on load; appendix excluded; `Esc` returns to the originating slide.
- **Signal:** Narrative clarity.

### P0-S3 — Single-use red audit

- **What:** `--strike` red appears twice — slide 9 dot + slide 23 strikethrough (ledger open-item).
- **Why:** The deck’s own system comment states red is “used once.” The slide-23 seamless→seamful strike is the intended single dramatic use; the slide-9 dot dilutes it.
- **How:** Recolor the slide-9 “What I found” dot to a neutral token (`--ink-faint` or `--ink-muted`). Leave slide 23 as the sole red.
- **Severity:** P2
- **Done:** Red (`--strike`) appears exactly once in the deck, on slide 23.
- **Signal:** Systems thinking (honoring your own design-system rule is itself the signal).

-----

## Phase 1 — Asset verification (tactic T1)

*The single highest-leverage phase. ~11 referenced files are `[CLAIMED]`, not verified. A placeholder rendering live is worse than a text slide. Must precede any visual polish in Phase 3.*

### P1-S1 — Verify every claimed asset resolves

- **What:** All `<img>`/`<video>` sources on slides 6, 7, 8, 9, 13, 17, 18.
- **Why:** Audit T1; assets unverifiable during audit. Live failure mid-narration is the top risk in the deck.
- **How:** Open the deck from the real `/assets/` path on the **actual presentation machine** (not a dev environment). Walk all asset slides. For each, confirm the image/video renders and the placeholder fallback does *not* show. Log any that fail.
- **Severity:** P0
- **Done:** Every asset slide renders its real asset; zero placeholders visible on the presentation machine.
- **Signal:** Objection-readiness (you can screen-share without surprises).

### P1-S2 — Slide-7 MP4 live check (tactic T3)

- **What:** `computis-rule-engine.mp4` autoplay/loop/rest behavior — the deck’s one inline video.
- **Why:** Audit flags this as the highest live-failure-risk asset; an MP4 that won’t autoplay degrades to a dead poster mid-narration.
- **How:** On the presentation machine/browser: confirm it autoplays muted, loops, is <10s, H.264, and rests on the result state (per the spec comment in markup). If it fails to autoplay, confirm the poster PNG (`computis-rule-engine.png`) is self-sufficient as a static fallback.
- **Severity:** P0
- **Done:** Video autoplays + loops on the target machine, OR the poster is confirmed self-sufficient and you’ve decided which is presenting.
- **Signal:** Objection-readiness; narration pacing (slide 7 timing depends on this).

### P1-S3 — Slide-13 code legibility

- **What:** `code-classification-insights.png` (the React panel).
- **Why:** Audit ENHANCE verdict — the “I write the React” craft claim is only as strong as the code screenshot’s legibility; a blurry panel actively undercuts the claim.
- **How:** Confirm the `.tsx` screenshot is syntax-highlighted and readable at projection scale (~14px min effective). If not, recapture at higher resolution.
- **Severity:** P1
- **Done:** Code is legible from the back of a room at projection scale.
- **Signal:** Craft demonstration (staff-level: design + implementation).

### P1-S4 — Slide-17 hero non-redundancy

- **What:** `symplify-ai-assistant-popup-large.png` hero vs. the live CSS assistant card on slides 14/21/22 (ledger open-item).
- **Why:** Audit — the assistant card already renders three times live; if the slide-17 hero repeats it, the constellation adds no new information.
- **How:** Confirm the hero shows a surface the audience has *not* seen (audit suggests the SBAR handoff). If it duplicates the assistant card, swap the hero asset for the unseen surface. `[GAP]` whether an SBAR-handoff capture exists — confirm availability before swapping.
- **Severity:** P1
- **Done:** Slide-17 hero shows a distinct surface, not a repeat of the live assistant card.
- **Signal:** Systems thinking (one primitive, *distinct* surfaces — the whole point of the slide).

-----

## Phase 2 — Narrative & objection-readiness adds

*Depends on Phase 1 (don’t build new annotated assets before verifying the base assets exist). These are the audit’s ADD/ENHANCE items that strengthen staff-level signal.*

### P2-S1 — Slide-9 two-state (miss + fix)

- **What:** Add an “after/fix” half to the honest-miss slide (audit ENHANCE; cut-order 2).
- **Why:** Audit calls slide 9 the highest-signal slide. Current state admits the 68/100 miss; pairing it with the commit/file that fixed one item (e.g., the duplicated `Button` consolidation) shows the loop *closed*, not just the miss confessed.
- **How:** Add a second image beside the critique screenshot showing the resolved state — the consolidated component or the diff. Keep static, side-by-side. `[ASSET NEEDED]` — the “after” capture must be created.
- **Severity:** P1
- **Done:** Slide 9 shows miss → fix as a two-state pair; narration can say “I found it, here’s the fix.”
- **Signal:** Honest-miss inclusion **and** iteration evidence (the two strongest staff signals, compounded).

### P2-S2 — Slide-16 distribution diagram

- **What:** Add a small diagram to the real-vs-mocked honesty beat (audit ADD; cut-order 4).
- **Why:** Audit’s only ADD verdict. The “model inference was mocked” admission currently runs as pure text; a seeded-distribution → High/Med/Low diagram *shows* the integrity of the decision rather than asserting it. Low risk (diagram, not screenshot).
- **How:** Build a CSS/SVG diagram: seeded confidence distribution feeding the three bands. Pairs visually with the slide-17 constellation. `[ASSET NEEDED]`. Do not use a screenshot.
- **Severity:** P1
- **Done:** Slide 16 shows the mocked-inference pipeline as a diagram; the honesty claim is visual.
- **Signal:** Honest-miss/integrity; narrative clarity (preempts “was any of this real?”).

### P2-S3 — Slide-8 anomaly annotation (tactic T2)

- **What:** One callout on the anomaly-route screenshot (audit ENHANCE, P2).
- **Why:** Audit notes a single annotation upgrade is available; the routed-triage-queue point is stronger shown than stated.
- **How:** Add one callout (reuse the shipped `.callout` component from slides 6/17) pointing to the priority/status/affected-transactions column, labeled with the routing decision it enables. One callout only — P2 risk if more.
- **Severity:** P2
- **Done:** Anomaly slide carries exactly one callout naming the routing decision.
- **Signal:** Decision-making (anomaly → routed queue, not toast).

-----

## Phase 3 — Visual polish

*Depends on Phases 1–2. These tune already-present or just-added assets. The motion item is gated on P1-S2.*

### P3-S1 — Slide-6 callout connector alignment

- **What:** The two shipped slide-6 callouts’ connector-arrow positions.
- **Why:** Audit §4 — connectors are positioned for the *real* PNG filling the frame; against the CSS fallback they point slightly off. Once the real asset is in (P1-S1), they must be aligned.
- **How:** With the verified PNG in place, nudge the inline `top`/`bottom` on the two `.callout-line` elements so the top arrow lands on the High row and the bottom arrow on the Low row. (Inline comment in markup marks the spot.)
- **Severity:** P2
- **Done:** Each connector arrow visually touches its target band on the real screenshot.
- **Signal:** Craft (polish reads as senior).
- **Depends on:** P1-S1.

### P3-S2 — Slide-23 motion moment (tactic T3) — CONDITIONAL

- **What:** Optional second motion loop on the thesis slide (audit ENHANCE; cut-order 1).
- **Why:** Audit permits a *second* loop only here, only if slide 7 verifies solid. A 6–8s loop of the confidence pill shifting HI→MD→LO with the Confirm/Override affordance appearing reinforces “legibly seamful.”
- **How:** **Gate:** proceed only if P1-S2 confirms slide 7’s video is reliable. If yes, build the loop as MP4 + poster (never GIF). If slide-7 is on poster-fallback, **do not** add this — keep slide 23 static. `[ASSET NEEDED]`.
- **Severity:** P2
- **Done:** Either a verified second loop on slide 23, or an explicit decision to keep it static. Never three motion moments deck-wide.
- **Signal:** Narrative clarity (motion serves the thesis, not decoration).
- **Depends on:** P1-S2. **First to cut if time-constrained.**

-----

## Phase 4 — Content gaps the candidate must close

*Not design work — content the candidate alone can supply. The B2/B3 backups ship incomplete until these are filled, so they belong on the critical path to panel-ready even though no layout changes.*

### P4-S1 — Fill B2 cohort data

- **What:** Backup B2 dot positions + axis unit (ledger `[DATA NEEDED]`).
- **Why:** Dots are illustrative-only; presenting them as real would be fabrication. The slide carries a visible `[DATA NEEDED]` band until filled.
- **How:** Replace each `.dist-dot` `left:%` with the real per-firm value across the 6-firm cohort; set the axis unit (days vs. hours). Remove the `[DATA NEEDED]` band once real. `[GAP]` — the actual per-firm values are not in the audit; candidate must supply.
- **Severity:** P1 (if B2 will be shown in Q&A)
- **Done:** B2 shows real cohort spread; no `[DATA NEEDED]` band remains.
- **Signal:** Objection-readiness (answers “n=6 is small” with real variance).

### P4-S2 — Fill or convert B3

- **What:** Backup B3 raw pre/post ticket counts (ledger `[DATA NEEDED]`).
- **Why:** The 85% is verified but the numerator/denominator aren’t in hand; bars carry `n=?` placeholders.
- **How:** Either supply the real pre/post counts (replace both `n=?`), **or** convert B3 to definition-only per the audit fallback (a precise definition defends an attackable metric better than a vague bar) and pair with the v2 component-spec artifact. `[GAP]` — counts not in audit.
- **Severity:** P1 (B3 backs the most-attackable metric)
- **Done:** B3 shows real counts, or is a clean definition slide with the v2-spec artifact. No `n=?` shown to a panel.
- **Signal:** Objection-readiness (this is the metric your own deck flags as most attackable).

-----

# 2. Sequencing & Dependency Map

```
PHASE 0  (integrity — do first, blocks nothing technically but must land before polish)
  P0-S1 ──> P0-S2        (renumber before re-checking counter)
  P0-S3                  (independent; can run anytime)

PHASE 1  (asset verification — CRITICAL PATH ROOT)
  P1-S1 ──┬──> P3-S1     (must verify slide-6 PNG before aligning its connectors)
          └──> P2-S1/S2/S3 indirectly (don't build new assets on unverified base)
  P1-S2 ──────> P3-S2    (slide-7 video gates the slide-23 motion loop)
  P1-S3                  (independent legibility check)
  P1-S4                  (independent; needs [GAP] SBAR availability)

PHASE 2  (narrative adds — after P1)
  P2-S1   P2-S2   P2-S3  (mutually independent; parallelizable)

PHASE 3  (polish — after P1/P2)
  P3-S1   (needs P1-S1)
  P3-S2   (needs P1-S2; conditional)

PHASE 4  (content gaps — parallel to all design phases; candidate-supplied)
  P4-S1   P4-S2  (independent of design work; blocked only by data availability)
```

**Parallelizable:** P0-S3 · all of Phase 2 · P4-S1/S2 (can proceed the moment data exists, independent of design phases).

**Blocking edges:**

- P1-S1 → P3-S1 (align connectors only on the verified asset)
- P1-S2 → P3-S2 (slide-7 reliability gates the slide-23 loop)
- P0-S1 → P0-S2 (renumber before counter re-check)

**Critical path to panel-ready:**
`P0-S1 → P0-S2 → P1-S1 → P1-S2 → P4-S2`
Integrity intact → assets verified → the one video confirmed → the most-attackable metric defensible. Everything else (P2 adds, P3 polish, P1-S3/S4, P4-S1) strengthens the deck but is not on the minimum path to “won’t break and can survive the hard question.”

-----

# 3. Prioritization Summary

### P0 — Non-negotiable. Skip → the deck visibly breaks or embarrasses on screen-share.

- **P0-S1 / P0-S2** — slide-19 gap + counter. *Skip impact:* a visible off-by-one counter signals carelessness on the exact axis (attention to detail) a Staff panel scrutinizes.
- **P1-S1** — verify all claimed assets. *Skip impact:* a placeholder rendering live mid-narration is the worst single failure available; it makes the candidate look like they didn’t open their own deck.
- **P1-S2** — slide-7 MP4 check. *Skip impact:* dead video mid-story; pacing collapses at the slide built around motion.

### P1 — High. Skip → measurable loss of staff-level signal or objection-readiness.

- **P1-S3** — code legibility. *Skip:* the “I write the React” claim lands weaker than the candidate’s actual ability.
- **P1-S4** — slide-17 hero non-redundancy. *Skip:* the constellation reads as “five screenshots” (★) instead of “one propagated primitive” (★★★) — the slide’s entire thesis.
- **P2-S1** — slide-9 two-state. *Skip:* keeps the strongest staff slide at “honest miss” without the “and I fixed it” — leaves iteration evidence on the table.
- **P2-S2** — slide-16 diagram. *Skip:* “was any of this real?” goes unanswered visually; the mocked-inference admission floats.
- **P4-S1 / P4-S2** — B2/B3 data. *Skip:* the backups can’t be shown; the “n=6” and “85% measured how?” objections lose their prepared answers. (Note: B3 can be salvaged as definition-only — see P4-S2.)

### P2 — Polish. Skip → deck is fully panel-ready; these add finish.

- **P0-S3** — single-use red. *Skip:* the slide-23 strike loses a little punch; minor.
- **P2-S3** — anomaly annotation. *Skip:* the routing decision is narrated rather than shown; acceptable.
- **P3-S1** — connector alignment. *Skip:* arrows slightly off on slide 6; noticeable only to a designer’s eye.
- **P3-S2** — slide-23 motion. *Skip:* none — this is *intended* to be cut first; static thesis slide is the safe default.

### Cut-order if time-constrained (most-deferrable first)

1. **P3-S2** — slide-23 motion loop (audit cut-order 1; conditional anyway).
1. **P2-S3** — anomaly annotation.
1. **P3-S1** — connector micro-alignment.
1. **P2-S2** — slide-16 diagram (text version is defensible).
1. **P0-S3** — single-use red.

**Never cut:** P0-S1, P0-S2, P1-S1, P1-S2 (the critical path), plus P4-S2 in at-least-definition form. P2-S1 (slide-9 two-state) is the last *value* add to drop — it touches the two strongest staff signals at once.

-----

## Open `[GAP]` flags carried from the audit

- **P1-S4** — existence of an SBAR-handoff (or other unseen) capture for the slide-17 hero swap.
- **P4-S1** — real per-firm cohort values + axis unit for B2.
- **P4-S2** — raw pre/post ticket counts for B3.
- **P2-S1 / P2-S2 / P3-S2** — `[ASSET NEEDED]`: slide-9 fix capture, slide-16 diagram, slide-23 loop must be created; none exist per the audit.