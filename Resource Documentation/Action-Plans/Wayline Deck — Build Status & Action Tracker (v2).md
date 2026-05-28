# Wayline Deck — Build Status & Action Tracker (v2)

**Loop:** Wednesday, May 20, 2026 · 1:30 PM PST · Virtual (Zoom)
**Panel:** Eric Rowell (CTO) + Jason Okra (CEO)
**Last updated:** Tuesday, May 19, 2026 (evening)
**Status:** Slide 18 pivoted from voice documentation to patient acuity. All other slide structure, assets, and design are unchanged. Final 24 hours.

---

## What changed since v1

| Change | Impact |
| --- | --- |
| Slide 18 swapped from *Voice is an input modality* → *Input isn't typed. It's inferred.* | New asset required: `symplify-patient-acuity.png`. Old voice assets retired. |
| Beat 4 speaker notes (18:30–20:30) rewritten | Acuity-as-input-inference argument replaces voice-as-input-modality argument. Script timing unchanged. |
| Synthesis Beat 2 surgical rewrite | Bidirectional *voice* → bidirectional *inference*. Framework preserved, noun changed. |
| Objection sheet S5 answer rewritten | Now points at acuity dashboard. Same slide number, new content. |
| Voice-doc assets retired | `symplify-voice-documentation.png` and `.mp4` no longer in build. |

---

## Asset status — all 27 slides

| # | Slide | Asset(s) | Status | Pri |
| --- | --- | --- | --- | --- |
| 1 | Cover | type only | ✅ | — |
| 2 | Stakes (three-column) | type only | ✅ | — |
| 3 | Stakes | type only | ✅ | — |
| 4 | Stakes | type only | ✅ | — |
| 5 | Stakes | type only | ✅ | — |
| 6 | From a percentage to a decision | `computis-classification-insights.png` | ✅ | P0 |
| 7 | Override is the failure mode | `computis-rule-engine.mp4` | ✅ | P0 |
| 8 | Anomaly route | `computis-anomaly-route.png` | ✅ | P0 |
| 9 | I shipped this. Then I audited myself | `computis-design-critique.png` | 🟡 | P1 |
| 10 | Outcomes | type only | ✅ | — |
| 11 | Outcomes | type only | ✅ | — |
| 12 | Outcomes | type only | ✅ | — |
| 13 | I write the React (Figma + code) | `figma-classification-insights.png` + `code-classification-insights.png` | 🟡 | P0 |
| 14 | Same primitive (through-line) | `computis-classification-insights.png` + `symplify-ai-assistant-popup.png` | ✅ | P0 |
| 15 | Stakes (06:45) | type only | ✅ | — |
| 16 | Section transition | type only | ✅ | — |
| 17 | The supervision primitive | `symplify-ai-assistant-popup-large.png` (+ 4 P2 peripherals) | 🟡 | P0 |
| 18 | **↻ Input isn't typed. It's inferred.** | **`symplify-patient-acuity.png`** | 🔴 | **P0** |
| 19 | Role isn't permissions | `symplify-sidebar-admin.png` + doctor + patient | 🟡 | P1 |
| 20 | Honest miss | `symplify-global-slider.png` + `symplify-per-feature-thresholds.png` | 🟡 | P1 |
| 21 | Symplify outcomes | type only | ✅ | — |
| 22 | Same primitive (second showing) | reuses slide 14 pair | ✅ | P1 |
| 23 | Wayline bridge (three-column) | reuses slide 14 pair + Wayline CSS sketch | ✅ | P0 |
| 24 | Wayline sketch | inline CSS | ✅ | P0 |
| 25 | Synthesis (three-column) | type only | ✅ | — |
| 26 | The ask | type only | ✅ | — |
| 27 | Close | type only | ✅ | — |

**Legend:** ✅ shipped · 🟡 placeholder rendering, asset pending · 🔴 NEW pending from slide 18 pivot · ↻ changed this update

---

## Remaining work — execution order

Single critical path. Each step blocks the next.

- [x]  **Capture the patient acuity dashboard screenshot**
    - Open running Symplify build, navigate to Patient Acuity Dashboard
    - Confirm all four acuity bands visible (critical / high / moderate / stable). If only three bands have patients in mock data, edit the mock array first.
    - Capture must show: distribution by unit at top, 6+ patient rows, sparklines, filter chips
    - Save as `symplify-patient-acuity.png`
    - Drop into `/Users/seansmith/Documents/GitHub/wayline-deck-hub/wayline-deck-bundle/assets/`
- [ ]  **Replace slide 18 in `wayline-deck.html`**
    - Drop in the replacement block from `slide-18-replacement.html`
    - Open the deck in Chrome — verify slide 18 renders with new heading + asset
- [ ]  **Update speaker notes**
    - Replace Beat 4 in Part 2 (18:30–20:30) with the acuity rewrite
    - Apply surgical rewrite to Synthesis Beat 2 (the bidirectional-voice paragraph becomes bidirectional-inference)
    - Grep Part 1 and Part 2 for stragglers: *voice*, *VoiceRecorder*, *TranscriptionEditor*, *MedicalTermsHighlighter*, *highlighter*, *transcription*
- [ ]  **Update objection-response sheet S5**
    - Replace the bidirectional-voice answer with the bidirectional-inference answer
    - One-line escape locked: *"Input inference and output inference are the same design problem at different temporal constraints."*
- [ ]  **Time the rewritten Beat 4 aloud**
    - Target: 90 seconds with 30 seconds of headroom inside the 2-minute slot
    - If long, tighten on second read
- [x]  **Optional retirement: remove voice assets**
    - Delete `symplify-voice-documentation.png` and `.mp4` from `/assets/` if present
    - Not required — they just won't be referenced anymore
- [ ]  **Rehearsal #3 (tonight, virtual config + kill-switch)**
    - Confirm slide 18 lands in the new shape during full run
    - Beat 2 kill-switch test proceeds as planned (independent of slide 18 work)
- [ ]  **Freeze**
    - No further script or slide edits after Rehearsal #3
    - Rehearsal #4 (Wed AM) is for rhythm only

---

## Dependency map

```
Acuity PNG captured
    └─> Slide 18 HTML swap
            └─> Beat 4 + Synthesis Beat 2 script rewrites
                    └─> S5 objection answer rewrite
                            └─> Rehearsal #3 (with kill-switch)
                                    └─> Freeze
                                            └─> Rehearsal #4 (Wed AM)
                                                    └─> The loop (Wed 1:30 PM PST)
```

**Single critical path.** Acuity PNG is the lone unblocked starting point. Everything else cascades from it.

---

## What "winning" looks like

A panel that, after thirty minutes, understands you've shipped a design system for trust across two products — and asks you to bring that same primitive to Wayline's communication surfaces.

---

## Reference paths

| Path | Purpose |
| --- | --- |
| `/Users/seansmith/Documents/GitHub/wayline-deck-hub/wayline-deck-bundle/` | Deck bundle root |
| `└─ wayline-deck.html` | Single-file presentation, open in Chrome fullscreen |
| `└─ assets/` | All PNG/MP4 assets, referenced via `./assets/filename` |
| `└─ speaker-notes-part-1.md` | Minutes 0:00–14:30 (cold open → transition) |
| `└─ speaker-notes-part-2.md` | Minutes 14:30–30:00 (Symplify → ask) |
| `└─ objection-response-sheet.md` | 13 Q&A entries for live use |
| `/Users/seansmith/Desktop/Symplify-1.7.4/` | Symplify codebase for asset capture |

---

## Keyboard reference — HTML deck

| Key | Action |
| --- | --- |
| `→` / `Space` | Next slide |
| `←` | Previous slide |
| `Home` | Slide 1 |
| `End` | Last slide |
| `?presenter=1` URL param | Presenter mode (notes visible) |
| `F` | Fullscreen toggle |