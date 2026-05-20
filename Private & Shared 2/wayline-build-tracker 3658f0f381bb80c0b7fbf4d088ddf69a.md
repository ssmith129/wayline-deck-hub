# wayline-build-tracker

# Wayline Deck — Build Status & Action Tracker

**Loop**: Wednesday, May 20, 2026 · 1:30 PM PST · Virtual (Zoom)
**Panel**: Eric Rowell (CTO) + Jason Okra (CEO)
**Last updated**: Sunday, May 17, 2026

---

## Asset status at a glance

### ✅ Slides with real production-grade assets

| Slide | Asset | Type | Notes |
| --- | --- | --- | --- |
| 6 | `computis-classification-insights.png` | Static | Right-column hero. Also drives slides 14/22/23 thumbnails. |
| 7 | `computis-rule-engine.mp4` | Motion | 11.1s loop, 1920×1246. Re-encoded for inline playback. |
| 8 | `computis-anomaly-route.png` | Static | Full route screenshot, 8000×5000. |
| 14 | classification-insights + ai-assistant-popup | Static pair | Asymmetric landscape + portrait, bottom-aligned. |
| 22 | Same pair as slide 14 | Static pair | Second through-line showing. |
| 23 | Same pair + Wayline CSS sketch | Static + CSS | Three-column compound. |

## ⬜ Slides still needing asset extraction

Remove following SYMPLIFY AI FEATURES:

- Slide 19- voice documentation
- 
- [x]  **Slide 9** — `computis-design-critique.png`
    - Source: `computis-app/DESIGN_CRITIQUE_2026-03-29.md` rendered or shown in repo file tree
    - Target: screenshot of the markdown file showing the “Audit Score: 68/100” line, OR the filename visible in the repo’s file tree
    - Priority: **P1** — honest-miss beat needs the visual receipt
- [x]  **Slide 13** — `figma-classification-insights.png`
    - Source: your Figma file, classification-insights frame
    - Target: clean frame export, no Figma UI chrome
    - Priority: **P1** — repo-as-receipt beat, left side of split
- [x]  **Slide 13** — `code-classification-insights.png`
    - Source: `computis-app/client/components/transactions/classification-insights.tsx`
    - Target: syntax-highlighted screenshot, readable at projection scale (use VS Code or carbon.now.sh)
    - Priority: **P1** — repo-as-receipt beat, right side of split
- [x]  **Slide 17** — `symplify-ai-assistant-popup-large.png`
    - Source: `Symplify-1.7.4/src/feature-module/components/ai/` — AIAssistantPopup at full fidelity
    - Target: portrait crop, ConfidenceIndicator + HIPAABadge clearly visible at projection scale
    - Priority: **P0** — supervision primitive hero, load-bearing visual
    
    [](https://www.notion.so)
    
- [ ]  **Slide 17** — Four peripheral thumbnails (`symplify-triage-badge.png`, `symplify-severity-badge.png`, `symplify-urgency-indicator.png`, `symplify-confidence-indicator.png`)
    - Source: respective component renders from the Symplify build
    - Target: tight crops of each badge/indicator in context
    - Priority: **P2** — slide reads fine with hero alone if peripherals don’t ship; placeholders are acceptable fallback
- [ ]  **Slide 18** — `symplify-voice-documentation.png`
    - Source: VoiceRecorder + TranscriptionEditor + MedicalTermsHighlighter
    - Target: transcript with at least 3 high-risk terms visibly highlighted
    - Priority: **P0** — required as static fallback for the MP4 (and as primary asset if you don’t produce the MP4)
- [ ]  **Slide 18** — `symplify-voice-documentation.mp4` (optional but recommended)
    - Source: build in Figma with auto-animate, screen-capture, OR record from the Symplify build
    - Target: ~10s loop showing the highlighter activating in real-time
    - Priority: **P1** — motion artifact; if not produced by Tuesday afternoon, falls back to PNG cleanly
    - Encoding spec: `ffmpeg -i source -vf "scale=1920:-2,fps=30" -c:v libx264 -preset slow -crf 24 -profile:v high -pix_fmt yuv420p -movflags +faststart -an output.mp4`
- [ ]  **Slide 19** — Three role-aware sidebar screenshots
    - `symplify-sidebar-admin.png` — `src/core/common/` Sidebar (admin)
    - `symplify-sidebar-doctor.png` — SidebarTwo (doctor)
    - `symplify-sidebar-patient.png` — Sidebarthree (patient)
    - Priority: **P2** — slide is on the cut list (Cut #2); placeholders are acceptable if you don’t get to these
- [ ]  **Slide 20** — `symplify-global-slider.png`
    - Source: build in Figma — reconstruct the original buggy global slider
    - Target: single global confidence slider with strikethrough rule
    - Priority: **P1** — honest-miss beat
- [ ]  **Slide 20** — `symplify-per-feature-thresholds.png`
    - Source: build in Figma — the per-feature fix
    - Target: separate confidence sliders for triage / drug interactions / scheduling / handoff with “global default” toggle
    - Priority: **P1** — honest-miss beat
- [ ]  **Slide 7** — `computis-rule-engine.png` (poster fallback for the MP4)
    - Source: take a single frame from the existing MP4, or screenshot the rule-engine page in its resting state
    - Target: matches the MP4’s resting “end of loop” frame
    - Priority: **P2** — graceful degradation only; MP4 plays fine without it

---

## Production action items by day

## Tuesday

- [ ]  Copy Artifact 1 Part 1 (speaker-notes script: cold open through transition, minutes 0:00–14:30) into your Notion or Apple Notes
- [ ]  Read Part 1 aloud once to confirm voice register
- [ ]  Flag any line that doesn’t read in your mouth — send to me tonight or Monday AM for adjustment
- [ ]  Sleep early

#### **Production Block #2**

- [ ]  Copy Artifact 1 Part 2 (Symplify through ask, minutes 14:30–30:00) into your delivery tool
- [ ]  Copy Artifact 3 (objection-response sheet) into a second screen-friendly view
- [ ]  Read Part 2 aloud once

#### **Afternoon — Production Block #3 — Asset Extraction**

- [x]  Extract Slide 9 design-critique screenshot
- [x]  Extract Slide 13 Figma frame + code screenshot
- [ ]  Extract Slide 17 hero (P0 priority)
- [ ]  Extract Slide 18 voice documentation static (P0)
- [ ]  Build Slide 20 reconstructions in Figma (~30 min each)
- [ ]  Drop all extracted assets into `/Users/seansmith/Documents/GitHub/wayline-deck-hub/wayline-deck-bundle/assets/`
- [ ]  Open the deck in Chrome — verify each slot picks up its asset
- [ ]  Slide 17 peripheral thumbnails (P2)
- [ ]  Slide 19 sidebars (P2 — on cut list anyway)
- [ ]  Build Slide 18 voice MP4 if you can knock it out in <60 min

#### **Rehearsal #1: solo cold read, no slides**

- [ ]  Read entire script aloud, timed
- [ ]  Goal: 28:00–31:00 total runtime
- [ ]  Identify any beat >15s over target — flag for adjustment Monday night
- [ ]  Don’t tune delivery yet, just length

#### **Slide production cleanup**

- [ ]  Confirm all P0 + P1 assets are in `/assets/` and rendering
- [ ]  Walk every slide top to bottom in Chrome
- [ ]  Note any slide where the asset doesn’t fit/crop right
- [ ]  Address P2 assets only if morning runs short

#### **Direction 3 (optional but recommended)**

- [ ]  Activate hostile-panel pressure test by pinging me
- [ ]  45 min: I role-play Eric and Jason challenging the deck
- [ ]  Surface any objection answer that doesn’t land

#### **Rehearsal #2: solo full run with slides**

- [ ]  Full deck with all assets, screen-share configuration
- [ ]  Expect 32–34 min first try
- [ ]  Confirm pacing checkpoints land at minute 6, 14, 25
- [ ]  Note any visual that doesn’t read at projection scale

#### **Rehearsal #3: virtual config + kill-switch test**

- [ ]  Recruit one non-design listener (friend, partner — not someone in design)
- [ ]  Zoom call, share screen with deck in Chrome fullscreen
- [ ]  Deliver Beat 2 of synthesis (slide 24 — the seamful reframe)
- [ ]  **60 seconds after**: ask listener: *“What was the one phrase I used about the JD?”*
    - [ ]  If they say *“legibly seamful”* → ✅ ship Beat 2
    - [ ]  If they don’t → ❌ cut Beat 2 entirely Wednesday
- [ ]  Deliver remainder of deck for general rhythm check

### Wednesday May 20 — Loop day

**9–11am — Rehearsal #4: final solo run**

- [ ]  Full deck + script, virtual configuration as Wednesday afternoon
- [ ]  **DO NOT change a single word of the script today**
- [ ]  This run is for rhythm, not content tuning
- [ ]  Confirm beat timing one last time

---

## Dependency map — what blocks what

```
Speaker-notes script (Sun/Mon)
    └─> Rehearsal #1 (Mon eve) — pacing baseline
            └─> Script tuning (if needed)
                    └─> Rehearsal #2 (Tue PM) — integration

Asset extraction (Mon PM)
    └─> Slide visual completeness
            └─> Rehearsal #2 (Tue PM) — visual integrity check
                    └─> Rehearsal #3 (Tue eve) — virtual config test

Kill-switch test (Tue eve, inside Rehearsal #3)
    └─> Beat 2 decision: ship or cut
            └─> Rehearsal #4 (Wed AM) — final rhythm

Rehearsal #4 (Wed AM)
    └─> Buffer (11am–12:30pm)
            └─> The loop (1:30pm)
```

**Critical path**: speaker-notes script → asset extraction → rehearsal #2. If any one slips, the chain pushes back.

**Lowest-priority path**: P2 assets → slide 17 peripheral / slide 19 sidebars / slide 7 poster fallback. Acceptable to skip these entirely.

---

## Pre-Wednesday verification checklist

### Tech checks (do Sunday or Monday)

- [ ]  `symplify-v4.netlify.app` loads in browser (referenced in script Beat 7)
- [ ]  All three GitHub repos load from incognito (referenced in C5 objection answer)
- [ ]  HTML deck opens cleanly in Chrome from `/Users/seansmith/Documents/GitHub/wayline-deck-hub/wayline-deck-bundle/`
- [ ]  Slide 7 video plays inline (autoplay, no sound, loops)
- [ ]  All current real assets render (slides 6, 7, 8, 14, 22, 23)

### Camera + environment checks (do Tuesday or Wednesday morning)

- [ ]  Camera at eye level (stack books under laptop if needed)
- [ ]  Lighting in front (window or lamp facing you, not behind)
- [ ]  Background composed (nothing distracting in frame)
- [ ]  Test Zoom screen-share configuration once before Wednesday
- [ ]  Confirm second-screen layout for speaker notes + objection sheet
- [ ]  Headphones tested, no echo

### Material checks (do Tuesday evening)

- [ ]  Speaker-notes script accessible on second screen
- [ ]  Objection-response sheet accessible on second screen
- [ ]  Phone set to silent vibrate at 6:00, 14:00, 25:00 from start time
- [ ]  Water nearby
- [ ]  Notepad + pen for jotting questions during deck (no, not really — but on the desk for Q&A note-taking)

---

## Risk register — what could go wrong, what to do

| Risk | Likelihood | Mitigation |
| --- | --- | --- |
| Pacing slips during deck | Medium | Cut order discipline — see `02-cut-order-discipline.md`. Phone vibrates at checkpoints. |
| Kill-switch listener fails the test | Medium | Beat 2 cuts mechanically. Deck reflows cleanly. No agony. |
| An asset doesn’t render in Chrome | Low | Progressive enhancement falls back to labeled placeholder. Deck still works. |
| Founder interrupts mid-beat | High | Answer in 15s, reroute. Don’t shush a founder. Don’t redesign for them. |
| Zoom connection issue | Low | Backup: have phone hotspot ready. Test connection at 12:30pm. |
| Late-night Monday script anxiety | High | Resist edits. Trust the script. Re-reading isn’t tuning, it’s rehearsing. |
| Forgetting to silence Slack/notifications | Medium | macOS Do Not Disturb on, quit Slack at 1:00pm Wednesday |
| Showing wrong screen on share | Medium | Practice screen-share configuration once Tuesday evening |

---

## Anti-action list — what NOT to do between now and Wednesday

These would actively make the deck worse. Resist if tempted.

- ❌ Don’t add new slides
- ❌ Don’t rewrite the spoken close (slide 26)
- ❌ Don’t expand the deck’s scope to a third project
- ❌ Don’t memorize the script word-for-word — natural-read from notes is better
- ❌ Don’t send a thank-you note within 2 hours of the loop ending
- ❌ Don’t replay the conversation in detail in your head after — write down only questions and signal moments
- ❌ Don’t make edits to the deck after Wednesday 11am
- ❌ Don’t add motion to slides 8 or beyond — motion belongs only on slides 7 and (if produced) 18
- ❌ Don’t crop the AI Assistant popup to lose the HIPAA Compliant badge
- ❌ Don’t decline a work trial if offered, even if scheduling is hard

---

## What “winning” looks like Wednesday

The deck doesn’t have to close the offer. The deck has to **earn the trial slot with maximum momentum.**

✅ Win state: at 2:30pm Wednesday, you’ve been offered the two-day work trial and have a scheduled start date.

If that happens — Wednesday succeeded. Everything else is bonus.

---

## Quick reference paths

- **Working folder**: `/Users/seansmith/Documents/GitHub/wayline-deck-hub/wayline-deck-bundle/`
- **HTML deck**: `wayline-deck.html` (open in Chrome, press F for fullscreen)
- **Assets folder**: `./assets/` (drop new PNGs/MP4s here, deck progressively enhances)
- **Notion hub**: imported from `wayline-presentation-hub.zip` (decision log and reasoning)

## Keyboard reference (HTML deck)

| Key | Action |
| --- | --- |
| `→` `↓` `Space` `PageDown` | Next slide |
| `←` `↑` `PageUp` | Previous slide |
| `Home` / `End` | Jump to first/last |
| `F` | Toggle fullscreen |
| `H` | Hide/show bottom-right chrome (do this before screen-share) |
| `P` | Toggle presenter mode |

---

## When to ping me

✅ **Send a message if:**

- A script line doesn’t read in your mouth
- An asset lands in `/assets/` but doesn’t render correctly
- Rehearsal #1 lands outside 28–31 min
- Rehearsal #3’s kill-switch listener fails
- You want Direction 3 activated Tuesday afternoon
- A question surfaces from rehearsal that the objection sheet doesn’t cover

⛔ **Don’t send a message for:**

- Voice register adjustments at the paragraph level (calibrated; trust the dial)
- New objection questions (13 covers the realistic surface)
- New artifacts (anything requiring >50 lines of new content)
- Anything Tuesday after 9pm or Wednesday after 11am (buffer is non-negotiable)

---

*Direction 1 active. Direction 3 reserved Tuesday afternoon. Go execute.*