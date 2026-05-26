# Wayline Deck — Build Status & Action Tracker (v3)

**Loop:** Wednesday, May 20, 2026 · 1:30 PM PST · Virtual (Zoom)
**Panel:** Eric Rowell (CTO) + Jason Okra (CEO)
**Last updated:** Tuesday, May 26, 2026
**Status:** Reconciled against the live files on disk. The deck has advanced well past the v2 snapshot — Manrope font swap, slide 6/17 callouts, and B1–B3 backup charts are all shipped. Several **net-new issues** surfaced during verification that v2 did not capture. See "What changed since v2" and "Remaining work."

> **How this version was produced:** every claim below was checked against the actual repository — `wayline-deck.html` as it currently sits on disk and the real contents of `/wayline-deck-bundle/` and its subfolders — not against the v2 tracker's assumptions. Where the live state contradicts v2 or the older planning docs, the live state wins and the discrepancy is flagged.

---

## ⚠️ Read first — three issues that will show on screen

These are new since v2 and are the highest-leverage fixes before the loop:

1. **`computis-classification-insights.png` is a 0-byte file.** It exists in `/assets/` but contains no data, so slide 6's "after" panel (the load-bearing trust-surface anchor) **will fail to render and fall back to the striped placeholder.** A `computis-classification-insights.svg` (79 KB, valid) sits right next to it — almost certainly the intended replacement. Either re-export the PNG or point slide 6 at the `.svg`.
2. **`computis-rule-engine.png` (the slide-7 video poster) is missing from `/assets/`.** The MP4 itself is present and fine, so if autoplay works this is invisible — but on any machine that blocks autoplay, the poster fallback won't load either. Low-probability, high-embarrassment. Export the poster frame.
3. **The slide-19 gap is still open in the numbering.** `data-slide` jumps **18 → 20** (no slide 19 in the markup). The runtime counter is now honest — it reads "N / 25" because the nav script counts actual main slides and excludes the appendix — but the internal numbering still has a hole. Cosmetic for the audience, but decide consciously: renumber 20→26 down by one, or leave it. (v3 audit flagged this; it's the one item from that audit still unresolved.)

---

## What changed since v2

The deck moved further than the v2 tracker recorded. v2's headline ("Slide 18 pivoted, all else unchanged, slide-18 asset 🔴 pending") is now stale on almost every point.

| Change | Status vs. v2 | Detail |
| --- | --- | --- |
| **Slide-18 pivot asset landed** | v2 had it 🔴 NEW/pending | `symplify-patient-acuity.png` (1.17 MB) is now in `/assets/` and referenced by slide 18. The pivot is structurally complete. |
| **Font swapped Fraunces → Manrope** | not in v2 | `--serif` token now resolves to Manrope; Google Fonts link loads Manrope 400–800. Affects every display heading + the slide-10 numbers + slide-23 pull-quote. |
| **Slide 6 & 17 annotation callouts shipped** | not in v2 | Slide 6: "55% → accept in bulk" / "11% → escalate." Slide 17: invariant line "Same confidence primitive. Four surfaces." |
| **Backup charts B1–B3 shipped** | not in v2 | Three `.appendix-slide` sections (for slides 4, 11, 12). Reached on demand via **B** to cycle, **Esc** to return. Excluded from the linear counter and arrow nav. |
| **Slide 9 redesigned to CSS hero** | not in v2 | No longer embeds `computis-design-critique.png`. The 68/100 score is now a large Manrope typographic hero in accent green. That PNG is now **orphaned** (see asset table). |
| **`slide--top-anchor` layout modifier added** | not in v2 | New class applied to ~15 slides for consistent top-alignment. Purely structural. |
| **Counter logic rewritten** | v2 hardcoded 27 | Total is now computed at runtime (`slides.length`, appendix excluded). The hardcoded `27` in the markup is overwritten on load and is harmless, but should be corrected to avoid confusing future editors. |
| **`code-…-dark.png` + `figma-…-clean.png` adopted** | v2 referenced non-suffixed names | Slide 13 now points at the **dark** code screenshot and the **clean** Figma frame. The original `figma-classification-insights.png` is superseded. |

---

## Asset status — live reconciliation

Checked file-by-file: what the HTML references vs. what is actually on disk in `/assets/`.

### Referenced by the live deck

| Slide | File | On disk | Status |
| --- | --- | --- | --- |
| 6 | `computis-classification-insights.png` | **0 bytes** | 🔴 **Broken — will not render.** Use the `.svg` beside it or re-export. |
| 7 | `computis-rule-engine.mp4` | 690 KB | ✅ Plays. Verify loop + rest-on-result live. |
| 7 | `computis-rule-engine.png` (poster) | **missing** | 🟠 Poster fallback absent. Export frame. |
| 8 | `computis-anomaly-route.png` | 1.01 MB | ✅ |
| 13 | `figma-classification-insights-clean.png` | 25.9 KB | ✅ |
| 13 | `code-classification-insights-dark.png` | 113 KB | ✅ Confirm legibility at projection scale. |
| 17 | `symplify-triage-badge.png` | 23.9 KB | ✅ peripheral |
| 17 | `symplify-ai-assistant-popup-large.png` | 541 KB | ✅ hero |
| 17 | `symplify-severity-badge.png` | 744 KB | ✅ peripheral |
| 17 | `symplify-urgency-indicator.png` | 782 KB | ✅ peripheral |
| 17 | `symplify-confidence-indicator.png` | 1.02 MB | ✅ peripheral |
| 18 | `symplify-patient-acuity.png` | 1.17 MB | ✅ **Pivot asset landed.** Confirm all four acuity bands populated. |

### Present in `/assets/` but NOT referenced (orphans)

Not errors, but dead weight and a source of confusion. Decide keep-or-cull before freeze.

| File | Size | Likely reason |
| --- | --- | --- |
| `computis-classification-insights.svg` | 79 KB | Probable valid replacement for the 0-byte PNG — promote it. |
| `computis-design-critique.png` | 2.40 MB | Orphaned by the slide-9 CSS-hero redesign. |
| `computis-anomaly-route.mp4` | 342 KB | Motion version of slide 8; slide uses the PNG. Backup only. |
| `figma-classification-insights.png` | 25.9 KB | Superseded by the `-clean` variant. |
| `symplify-ai-assistant-popup.png` | 81 KB | Small popup; deck uses the `-large` asset + live CSS card. |
| `symplify-ai-assistant-popup-large.mp4` | 1.89 MB | Motion popup; unused (slide 17 uses the static PNG). |
| `Predictive Clinical Alerts.png` | 995 KB | Not referenced anywhere. |
| `Smart Insights.png` | 1005 KB | Not referenced anywhere. |

### Duplicated at the bundle root (outside `/assets/`)

`computis-anomaly-route.mp4`, `computis-rule-engine.mp4`, and `symplify-ai-assistant-popup-large.mp4` also sit loose in `/wayline-deck-bundle/`. The deck loads everything via `./assets/…`, so these root copies are unused duplicates. Safe to remove; harmless if left.

**Legend:** ✅ present & wired · 🟠 fallback/secondary missing · 🔴 broken, fix before loop

---

## Slide inventory — as it actually renders

25 main slides. `data-slide` runs 1–26 but **skips 19.** Plus 3 appendix backup slides (B1–B3), not in the linear count.

| data-slide | Heading | Asset / treatment |
| --- | --- | --- |
| 1 | The trust surface between a professional and an AI. | type only |
| 2 | The next 30 minutes. | type only (3-col agenda) |
| 3 | 11:00 PM. April 14th. | type only |
| 4 | 32% demo-to-customer conversion gap. | type only · backup **B1** |
| 5 | Three stakes. | type only |
| 6 | From a percentage to a decision. | before table + **after asset (🔴 0-byte)** + callouts |
| 7 | Override is the failure mode. | `computis-rule-engine.mp4` (poster 🟠 missing) |
| 8 | If it recurs, it needs a noun in the URL. | `computis-anomaly-route.png` |
| 9 | I shipped this. Then I audited myself. | CSS hero "68/100" (no image) |
| 10 | Measured, not asserted. | type only (4 numbers) |
| 11 | How we measured. | type only · backup **B2** |
| 12 | How we measured (continued). | type only · backup **B3** |
| 13 | I write the React. | Figma `-clean` + code `-dark` two-up |
| 14 | Same primitive. New vertical. | live CSS cards (Computis + Symplify) |
| 15 | 06:45. | type only |
| 16 | What was real. What was mocked… | type only |
| 17 | The same primitive — across fourteen features. | hero popup + 4 peripherals + invariant callout |
| 18 | Input isn't typed. It's inferred. | `symplify-patient-acuity.png` ✅ |
| *19* | *— absent from markup —* | **[GAP]** |
| 20 | Three artifacts. | type only |
| 21 | Same primitive. Two regulated verticals. | live CSS cards |
| 22 | One primitive. Three regulated verticals. | live CSS (3-up + Wayline sketch) |
| 23 | Legibly seamful. | Wayline CSS sketch + reframe |
| 24 | First 90 days. | type only (30/60/90) |
| 25 | I design the surface where a professional supervises an AI. | spoken close |
| 26 | The ask: a two-day work trial. | type only |
| B1 | Backup · for slide 4 (32%) | paired-bar appendix chart |
| B2 | Backup · for slide 11 (40/45%) | dot-distribution appendix chart |
| B3 | Backup · for slide 12 (85%) | paired-bar appendix chart |

> **Note on v2's inventory:** v2 listed 27 slides and named a slide 19 "Role isn't permissions" and a slide 20 "Honest miss / slider." **Neither exists in the live HTML.** Those came from the older `wayline-deck-build-instructions.md` planning doc, which describes a structure that was cut/renumbered and never built. v3's inventory above is what actually renders.

---

## Remaining work — execution order

Single critical path, re-derived from the live state. Top items are new since v2.

- [ ] **Fix the slide-6 broken asset (🔴 P0 — do first)**
    - `computis-classification-insights.png` is 0 bytes. Either:
      - re-export a valid PNG to `/assets/`, **or**
      - repoint slide 6's `<img src>` to `computis-classification-insights.svg` (already present, 79 KB).
    - Open the deck in Chrome and confirm the "after" panel renders the real insights component, not the striped placeholder.
- [ ] **Export the slide-7 video poster (🟠 P1)**
    - Save a single frame as `computis-rule-engine.png` into `/assets/` so the poster fallback resolves if autoplay is blocked.
- [ ] **Resolve the slide-19 numbering gap (P1)**
    - Decide: renumber slides 20–26 down by one (closing the hole), or leave it. Counter is already honest at runtime either way.
    - If renumbering, also correct the hardcoded `<span id="totSlides">27</span>` to the true count for editor sanity (runtime already overrides it).
- [ ] **Stale "voice" stragglers in comments (P2)**
    - Section comment at the slide-18 block still reads "SLIDE 18 — SYMPLIFY: VOICE AS INPUT MODALITY"; the CSS `--motion` modifier comment still references "slide 18 symplify voice MP4." Body content is correct — only the comments lie. Grep and clean: *voice, VoiceRecorder, transcription, highlighter.*
- [ ] **Decide the red-usage conflict (P2 — style integrity)**
    - The deck's own rule is "red used once" (the slide-23 strikethrough). Slide 9 now also uses `--strike` red for a bullet dot. Pick one; the v3 audit notes the slide-9 dot dilutes the slide-23 punch.
- [ ] **Cull or keep orphaned assets (P2)**
    - 8 unreferenced files in `/assets/` (incl. two ~1 MB clinical PNGs and a 2.4 MB critique screenshot) + 3 duplicate MP4s at bundle root. Removing them trims ~8 MB and removes ambiguity. None are load-bearing.
- [ ] **Rehearsal #3 (tonight, virtual config + kill-switch)**
    - Confirm slide 18 lands in the acuity shape during a full run.
    - Confirm slide 6 renders post-fix. Confirm the **B / Esc** backup-chart flow works mid-narration.
- [ ] **Freeze**
    - No further script or slide edits after Rehearsal #3. Rehearsal #4 (Wed AM) is rhythm only.

---

## Dependency map

```
Slide-6 asset fix (0-byte PNG → valid PNG or .svg)   ← lone P0 blocker
    └─> Slide-7 poster export (P1, parallel-safe)
            └─> Slide-19 gap + counter decision (P1)
                    └─> Comment/red-usage/orphan cleanup (P2, parallel-safe)
                            └─> Rehearsal #3 (with kill-switch)
                                    └─> Freeze
                                            └─> Rehearsal #4 (Wed AM)
                                                    └─> The loop (Wed 1:30 PM PST)
```

**Changed from v2:** the critical path no longer starts at "capture the acuity PNG" (done). It now starts at **the slide-6 0-byte asset** — the one thing guaranteed to render visibly broken on screen.

---

## What "winning" looks like

A panel that, after thirty minutes, understands you've shipped a design system for trust across two regulated products — and asks you to bring that same primitive to Wayline's communication surfaces. (Unchanged from v2 — still the right target.)

---

## Reference paths — corrected

v2's reference table pointed at speaker-notes and objection-sheet files **at the bundle root. Those files are not there.** The bundle root actually contains the files below. The notes/objection docs may live elsewhere (not in any accessible directory checked) — locate and relink them, or update wherever they're tracked.

| Path | Status | Purpose |
| --- | --- | --- |
| `…/wayline-deck-hub/` | ✅ | Repo root — also holds this tracker + `netlify.toml` |
| `└─ wayline-deck-bundle/` | ✅ | Deck bundle root |
| `   └─ wayline-deck.html` | ✅ | The live single-file presentation (2,572 lines) |
| `   └─ wayline-deck-tester.html` | ✅ present | Secondary/QA copy — confirm which is canonical before edits |
| `   └─ assets/` | ✅ | All PNG/MP4/SVG, referenced via `./assets/filename` |
| `   └─ resource documentation/Action-Plans/` | ✅ | `wayline-deck-build-instructions.md` (older structure — see note), `wayline-actions-plan.pdf` |
| `   └─ resource documentation/Audits/` | ✅ | `wayline-deck-audit_v3.md`, `wayline-deck-ui-density-audit-v2.md`, `Computis v2.0.4 Design System Audit.md`, + UI-Density Audit_v2 subfolder |
| `   └─ Computis v2.0.4 Design System Audit.pdf` | ✅ | PDF at bundle root |
| `   └─ wayline-actions.pdf` | ✅ | PDF at bundle root |
| `…/GitHub/Symplify-1.7.4/` | ✅ (allowed) | Symplify codebase for asset capture |
| `…/GitHub/computis-app/` | ✅ (allowed) | Computis codebase for asset capture |
| `speaker-notes-part-1.md` / `-part-2.md` | ❓ **not found** | Claimed at bundle root in v2; absent there. Relocate/relink. |
| `objection-response-sheet.md` | ❓ **not found** | Same — verify location. |

---

## Keyboard reference — HTML deck

| Key | Action |
| --- | --- |
| `→` / `Space` | Next slide |
| `←` | Previous slide |
| `Home` | Slide 1 |
| `End` | Last slide |
| `B` | Enter / cycle backup charts (B1 → B2 → B3) |
| `Esc` | Return from backup to the main deck |
| `F` | Fullscreen toggle |
| `H` | Hide / show nav chrome |
| `P` or `?presenter=1` | Presenter mode (timeline bar) |

> New since v2: **B** (backup charts) and **Esc** (return) — added with the B1–B3 appendix. The chrome hint line in the deck reflects these.
