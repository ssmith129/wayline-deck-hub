# Speaker Notes Script

# Computis

### Artifact 1, Part 1 — Speaker-Notes Script: Cold Open Through Transition (Minutes 0:00–14:30)

---

## Cold Open + Thesis — 0:00 to 1:30

【slide 1: title — *"The trust surface between a professional and an AI"* — your name, the date, nothing else】

`[Camera on. Two-second pause before speaking. Let them see you settled before you start. Do not smile-on-arrival. Neutral, composed, ready.]`

Thanks for the hour. Quick housekeeping first — I'm going to take the full 30 minutes for the case study, and then we'll open it up for questions. So save them up. If something jumps out, write it down — I want to give you proper answers, not rushed ones, and the deck is built to hold together as one arc.

`[Pause 1 sec.]`

Here's the frame for the next 30 minutes.

`[Eye contact at camera. This is the thesis line. Deliver it deliberately, one beat between clauses.]`

I design the trust surface between a professional and an AI. The screen where a CPA, a clinician, a property manager — somebody whose license is on the line — decides whether to trust what the model just told them. I've shipped that surface twice, in two regulated verticals. Today I'm going to walk you through both, and then I'm going to tell you what I'd do at Wayline.

▸ PACING CHECK: should be exiting slide 1 by 1:15. If past 1:30, skip the housekeeping recap and go straight to the next slide.

【slide 2: agenda — three columns, *Computis / Symplify / Wayline*, no body copy】

Two projects, in order. Computis first — crypto tax automation, regulated finance, CPAs as the user. Then Symplify — AI-enhanced hospital operations, clinicians as the user. Then three and a half minutes on Wayline — what the through-line is and what I'd do in the first 90 days.

Let's go.

---

## Computis — Beat 1: The Room — 1:30 to 2:30

【slide 3: visual — a single composed image suggesting a CPA's desk at night, or a stylized "11:00 PM April 14" timestamp. No product UI yet. Stakes only.】

`[High-stakes beat #1 of 4. Slow down here. The opening frame is doing work — let it land.]`

Picture a CPA. It's 11pm on April 14th. She has 47 client wallets in front of her, over 200,000 transactions, and a filing deadline that does not move. The tool she's been told to use gives her a CSV — every transaction, with an AI classification next to it, and a confidence percentage. 0.82. 0.67. 0.91. 0.43.

She reads four rows. She doesn't know what 0.67 means in dollars at risk. She doesn't know what threshold separates "I can sign this" from "I need to look at this." So she does what every CPA in that position does. She closes the tool and opens her spreadsheet.

`[One-second pause.]`

The AI was technically correct. And operationally useless.

---

## Computis — Beat 2: The Problem as the Business Felt It — 2:30 to 4:00

【slide 4: the business problem — *32% demo-to-customer conversion gap*, simple type-driven layout, no chart yet】

That CPA's experience showed up in the business numbers as a 32% demo-to-customer conversion gap. Prospects loved the demo — every time. Signed paperwork at half the rate. And the CPAs who did onboard ghosted in week two.

The team's read of the problem when I came on was that the model needed to be more accurate. So they were rebuilding the classification engine every two months, chasing precision gains that weren't moving adoption. The model wasn't the problem. The surface was the problem. Design wasn't the obvious culprit, which is exactly why design was the actual culprit.

【slide 5: stakes at a glance — three lines, *regulatory / commercial / engineering rhythm*】

Three stakes worth naming, because they shaped every decision that came after.

Regulatory — a wrong crypto classification on a tax return is an IRS audit. And the CPA's PTIN is on the return, not Computis's. So the design has to surface enough confidence and enough audit trail that the CPA can sign and defend.

Commercial — every churned CPA represented a firm-sized account, not a seat-sized one. Logo churn was firm churn squared.

Engineering — the team's two-month model-rebuild cadence was eating velocity. If design could close the adoption gap, engineering could stop chasing precision and start building features. That's what was actually at stake.

▸ PACING CHECK: at minute 4, you should be advancing to the confidence-band slide. If you're behind, compress the next intro sentence and get there.

---

## Computis — Beat 3: The Load-Bearing Decision — 4:00 to 6:00

【slide 6: the load-bearing decision — `classification-insights` panel screenshot, High/Medium/Low confidence bands with counts and review actions visible. Display heading: *"From a percentage to a decision."*】

`[High-stakes beat #2 of 4. This is the slide that plants the trust-surface frame for the entire deck. Slow tempo. Allow eye contact at the camera between sentences.]`

Here's the call I made — and this is the one I want you to remember.

The model output a confidence percentage between zero and one. That's honest, and it's unusable. A CPA looking at 0.82 has to invent her own threshold for what she reviews and what she accepts. And she invents a different threshold on Tuesday than on Monday.

So we don't show her the percentage. We show her three bands. High confidence. Medium confidence. Low confidence. Three buckets, mapped to three decisions. Accept in bulk. Review individually. Escalate to investigation.

`[Pause one beat.]`

The math doesn't change. The model still computes the percentage. The audit trail still preserves it down to four decimal places. What changes is that the surface turns one continuous number into three pre-decided thresholds — calibrated once, defended in the audit trail.

I'll give you the principle, because every decision in this project follows from it: **trust surfaces translate model output into human decisions, not human numbers.** A trust surface's job is to compress what the model knows into what the user can act on, without losing the path back to what the model actually said.

`[Beat.]`

And yes — somebody is going to ask me in the next 30 minutes whether I threw information away. The answer is yes, deliberately, on the action surface. And no, never, in the audit trail. The information's preserved. The decision-load is reduced. That's the trade. That's what makes the band design defensible.

▸ PACING CHECK: at minute 6, you should be advancing to the next slide. If still here at 6:30, deploy CUT #1.

---

## Computis — Beat 4: Two More Decisions, Fast — 6:00 to 8:00

【slide 7: decision #2 — rule engine over bulk-edit. Show the rule-engine UI from the repo. Heading: *"Override is the failure mode."*】

Two more decisions, fast — same principle, different applications.

First: rule engine over bulk-edit. The obvious feature request from every demo was "let me select 200 rows and reclassify them." The non-obvious read of that request was "I don't trust your AI and I want to override it manually forever." So bulk-edit would have entrenched distrust as the dominant workflow. A rule engine — "any transaction from wallet X over $Y, classify as Z" — let the CPA encode her judgment into the model. Every override became permanent training signal she could see and audit.

The principle: **override is a design failure mode; rule-authoring is the design success state.** When a user overrides, that's the system failing. When a user authors a rule, that's the system learning at the user's pace, not the engineer's.

`[Brief pause, advance.]`

【slide 8: decision #3 — anomaly flags as first-class objects. Show the anomaly route screenshot with priority/status/affected-transactions columns. Heading: *"If it recurs, it needs a noun in the URL."*】

Second: anomaly flags as first-class objects. Anomalies — volume spikes, duplicate ingestion, wallet inconsistencies — initially lived as toast notifications and inline icons. They were invisible by Tuesday. So we promoted them to a dedicated route with priority, status, and assigned reviewer. They went from interruptions to a triage queue. And the audit trail emerged for free, because the route is the audit trail.

The principle: **if a class of issue recurs, it deserves a noun in the URL.** Toasts are for transient events. Routes are for ongoing concerns.

▸ CUT GUIDANCE: if running long here, you can collapse decision #3 into one sentence — "anomalies got promoted from toasts to a routed triage queue" — and save 30 seconds.

---

## Computis — Beat 5: The Honest Miss — 8:00 to 9:30

【slide 9: the honest miss — screenshot of `DESIGN_CRITIQUE_2026-03-29.md` filename and excerpt. Display heading: *"I shipped this. Then I audited myself."* Score: **68/100**】

I want to spend 90 seconds on something most case studies skip.

I shipped this product. It hit its metrics. And then I audited my own work and scored it 68 out of 100. That audit is in the repo, dated, public, alongside the production code.

What did I find? 40% of feature components were bypassing the design token system — they were using hardcoded Tailwind color classes and arbitrary pixel values instead of the semantic tokens I'd built. I had a duplicate Button component — one called `button`, one called `enhanced-button` — and a duplicate Input pattern, both forks shipping working features. Two toast systems running simultaneously. Sidebar muted text written as `#a3a3a3` in nine separate files instead of as a token.

The honest part isn't the bugs. Every shipping product has bugs. The honest part is publishing the audit alongside the product, dated, before anyone asked.

`[Beat.]`

The principle: **a design system you don't audit isn't a system. It's a wish.**

And if anyone wants to ask me about the 68 — I'll say it now: shipping at 100 means you over-engineered. Shipping at 68 with a dated public audit means the next iteration has a starting line. I'd rather work somewhere that ships at 68 and audits in week six than somewhere that ships at 95 and never audits at all.

---

## Computis — Beat 6: The Outcomes — 9:30 to 11:30

【slide 10: outcomes overview — four numbers, *40% / 45% / 32% / 85%*, big and quiet. No chart. Heading: *"Measured, not asserted."*】

Now the metrics. Four numbers, each tied to what it actually measured.

【slide 11: outcomes detail — 40% / 45% panel】

40% reduction in accounting processing time. That's the median time from wallet-ingest to filed-classification, sampled across 6 onboarded firms over a 6-week post-launch window. Real behavioral measurement, not a survey.

45% reduction in CPA onboarding time. Time from credential-issue to first-completed-classification task. Same 6-firm cohort.

【slide 12: outcomes detail — 32% / 85% panel】

32% increase in demo-to-customer conversion. Sales pipeline data, quarter-over-quarter post-redesign. That's the gap I described at the start, closed.

And 85% engineering dependency reduction. This is the one I'm happiest to be pressed on, because it's the most attackable. It's measured against design clarification tickets reopened post-handoff, before versus after the v2 component spec. So the claim is: components shipped tight enough that engineering didn't have to come back and ask what I meant. Falsifiable, measured, and the ticket data is real.

`[Beat.]`

▸ PACING CHECK: at minute 11:30, you should be advancing to slide 13. If past 12:00, deploy CUT #5 — skip the repo-as-receipt beat — but only as a last resort.

---

## Computis — Beat 7: The Repo-as-Receipt — 11:30 to 13:30

【slide 13: split layout — left side, Figma source for `classification-insights.tsx`. Right side, the actual React component code from the repo. Heading: *"I write the React."*】

One more thing before we transition to Symplify, because the job description says this role is not Figma-only — and I want to address that directly.

Everything you've seen so far is in the repo. The Computis app is a React 18 / TypeScript / Tailwind / Radix application, 49 UI components, 14 feature directories. The component library is mine. The `classification-insights` panel you saw two slides ago — that's me. The anomaly route. The rule engine forms. The design system documentation. Mine.

Where's the line? I write the surfaces. I don't write the data layer. Transaction table virtualization, chart rendering, server endpoints — that's engineering. But the surface where the CPA decides whether to trust the AI — that one ships from me, in production code, with Figma as the upstream source of truth and the React as the source of record.

I'm telling you this now because if I'm the founding designer at Wayline, this is the rhythm I bring. Figma to React, owned end-to-end on the surfaces I'm responsible for. No handoff theater. If it ships visual drift, that's on me.

【slide 14: Computis recap — six principles in a single composed list, no embellishment】

To close Computis quickly: six principles, one project.

Trust surfaces translate model output into human decisions, not human numbers. Override is a failure mode; rule-authoring is the success state. If a class of issue recurs, it deserves a noun in the URL. Visual density is a respect signal to power users. In regulated verticals, the audit trail is the product. And a design system you don't audit isn't a system; it's a wish.

Hold those for a minute. We're going to see most of them again in a different vertical.

▸ PACING CHECK: at minute 13:30, you should be on the transition slide. If past 14:00, skip the transition slide and go directly to the Symplify opening.

---

## Transition — 13:30 to 14:30

【slide 15: the through-line — split composition. Left: Computis `classification-insights` panel. Right: Symplify `AIAssistantPopup` with `ConfidenceIndicator` + `HIPAABadge`. Heading: *"Same primitive. New vertical."*】

Quick transition before Symplify.

Hold the Computis primitive in your head — three-band confidence on the AI output, decision routing, audit trail behind every call. Here it is on the left.

On the right, the same primitive, in a different product, in a different industry, for a different professional user. Confidence indicator on every AI output. Compliance badge in-line. A panel where the human supervises an agent.

I designed both of these. Computis is a crypto tax product. The one on the right is from a hospital operations platform. Two regulated verticals. Same primitive. Same staff-level instinct underneath — that the design problem with AI products isn't "show the user what the AI said." It's "design the screen where the user decides whether to trust what the AI said."

`[Brief pause. Advance to Symplify opening.]`

Let me show you the second project.

---

▸ END OF PART 1 — MINUTE 14:30 ▸ HANDOFF TO PART 2 (SYMPLIFY OPENING THROUGH SPOKEN CLOSE + ASK)

---

## Part 1 — Production notes for your review

A few things to flag before you read Part 2:

**P0 — The voice is your voice, but compressed.** Read the cold open and Beat 3 aloud once. If anything in those two beats sounds like *not how you'd actually say it*, flag the sentences and I'll rework them in Part 2 with the corrections applied. Voice consistency between Part 1 and Part 2 is the highest risk of the split-output approach — the easiest way to manage it is to lock the voice in Part 1 before Part 2 is produced.

**P1 — Stage directions are minimal, as you requested.** They appear only at the four high-stakes moments. The cold open has the heaviest cue load — *"Camera on. Two-second pause."* — because the opening seconds set the panel's read of you for the whole hour. Beat 3 (the load-bearing decision) has one cue. The other beats in Part 1 have none. Beat 6 (outcomes) deliberately has no cues despite being a high-density slide — the density is the cue.

**P2 — The repo-as-receipt beat is heavier than Step 3's outline suggested.** Step 3 specified one sentence and a move-on. The script gives it ~75 seconds because the JD's *"not a Figma-only role"* language is loud enough that I want this beat doing more work than I originally scoped. If you feel it's overweighted relative to the metrics beat, flag it and I'll trim by 30 seconds.

**P3 — Word count for Part 1: approximately 1,650 words of script + pacing infrastructure.** That maps to 14:30 of speaking time at ~115 words per minute, which is a measured-but-not-slow rate for a virtual delivery to two listeners. If your natural rate is faster, expect to land closer to 13:00 in Rehearsal #1 — which is *fine*, gives margin into the transition.

**P4 — The Computis recap slide (slide 14) is new.** Step 3 didn't explicitly call for it. I added it because the six principles need to land as a group before the transition asks the panel to carry them into Symplify. If it feels like over-architecture, we can cut it — but I'd argue strongly for keeping it, because it makes the transition slide do less work.

---

## Decisions needed before Part 2

Three:

1. **Voice consistency check.** Read the cold open and Beat 3 aloud. Does this sound like you, or like a version of you that's been polished too much? If polished too much, point me at one or two specific lines and I'll calibrate Part 2's voice accordingly.
2. **The repo-as-receipt weight (P2 above).** Keep at ~75 seconds, or trim to ~45 seconds?
3. **Computis recap slide (slide 14).** Keep, or cut?

Confirm and I'll produce Part 2 — Symplify opening through the spoken close and the ask.