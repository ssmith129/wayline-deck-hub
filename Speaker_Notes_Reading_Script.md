# Speaker Notes — Reading Script

**Loop:** Wednesday, May 20, 2026 · 1:30 PM PST
**Format:** Reading-mode. Production scaffolding stripped. Prose flows as continuous speech.

Slide cues `【slide N】` are silent — advance when you reach them. Stage directions in `[brackets]` appear only at the four high-stakes moments. Two pacing checks at the load-bearing transitions. Everything else is read.

**Authorship status — read before locking.** Part 1 (Computis) is your original locked prose, lightly reflowed for live reading. Patient Acuity (Beat 4) and the bidirectional paragraph in Synthesis 2 are the locked rewrites from the slide-18 pivot. The remaining Part 2 beats — Supervision Primitive, Role-Aware UI, Outcomes, second Transition, Synthesis 1, Synthesis 3, Spoken Close, and the Ask — are **first-draft prose written tonight from the verified Symplify codebase + past-session principle maps**. They are voice-matched to Part 1 and free of fabricated metrics or unverifiable claims, but they have not been through your rehearsal cycle. Read each one aloud once tonight before Rehearsal #3. If a sentence sounds like a version of you that's been polished too much, edit in place.

**Late edit — Symplify honest miss cut.** The Symplify-side honest-miss slide (previously slide 20) was removed for time. Computis honest miss (slide 9) still carries the *"I audit my own work"* signal for the deck. Symplify arc is now: supervision → acuity → role-aware → outcomes. One minute of margin recovered — total runtime is 29:00, not 30:00.

---

# Part 1 — Computis

## Cold Open + Thesis · 0:00–1:30

【slide 1】

`[Camera on. Two-second pause. Neutral. Composed.]`

Thanks for the hour. Quick housekeeping first — I'm going to take the full 30 minutes for the case study, and then we'll open it up for questions. So save them up. If something jumps out, write it down. I want to give you proper answers, not rushed ones, and the deck is built to hold together as one arc.

`[Pause. Then deliver the thesis deliberately, one beat between clauses.]`

Here's the frame for the next 30 minutes. I design the trust surface between a professional and an AI. The screen where a CPA, a clinician, a property manager — somebody whose license is on the line — decides whether to trust what the model just told them. I've shipped that surface twice, in two regulated verticals. Today I'm going to walk you through both, and then I'm going to tell you what I'd do at Wayline.

【slide 2】

Two projects, in order. Computis first — crypto tax automation, regulated finance, CPAs as the user. Then Symplify — AI-enhanced hospital operations, clinicians as the user. Then three and a half minutes on Wayline — what the through-line is and what I'd do in the first 90 days.

Let's go.

---

## The Room · 1:30–2:30

【slide 3】

Picture a CPA. It's 11pm on April 14th. She has 47 client wallets in front of her, over 200,000 transactions, and a filing deadline that does not move. The tool she's been told to use gives her a CSV — every transaction, with an AI classification next to it, and a confidence percentage. 0.82. 0.67. 0.91. 0.43.

She reads four rows. She doesn't know what 0.67 means in dollars at risk. She doesn't know what threshold separates "I can sign this" from "I need to look at this." So she does what every CPA in that position does. She closes the tool and opens her spreadsheet. The AI was technically correct. And operationally useless.

---

## The Business Problem · 2:30–4:00

【slide 4】

That CPA's experience showed up in the business numbers as a 32% demo-to-customer conversion gap. Prospects loved the demo — every time. Signed paperwork at half the rate. And the CPAs who did onboard ghosted in week two.

The team's read of the problem when I came on was that the model needed to be more accurate. So they were rebuilding the classification engine every two months, chasing precision gains that weren't moving adoption. The model wasn't the problem. The surface was the problem. Design wasn't the obvious culprit, which is exactly why design was the actual culprit.

【slide 5】

Three stakes worth naming, because they shaped every decision that came after. Regulatory — a wrong crypto classification on a tax return is an IRS audit, and the CPA's PTIN is on the return, not Computis's, so the design has to surface enough confidence and enough audit trail that the CPA can sign and defend. Commercial — every churned CPA represented a firm-sized account, not a seat-sized one; logo churn was firm churn squared. Engineering — the team's two-month model-rebuild cadence was eating velocity; if design could close the adoption gap, engineering could stop chasing precision and start building features. That's what was actually at stake.

---

## The Load-Bearing Decision · 4:00–6:00

【slide 6】

`[Slow tempo. Eye contact at the camera between sentences.]`

Here's the call I made — and this is the one I want you to remember. The model output a confidence percentage between zero and one. That's honest, and it's unusable. A CPA looking at 0.82 has to invent her own threshold for what she reviews and what she accepts. And she invents a different threshold on Tuesday than on Monday.

So we don't show her the percentage. We show her three bands. High confidence. Medium confidence. Low confidence. Three buckets, mapped to three decisions. Accept in bulk. Review individually. Escalate to investigation.

The math doesn't change. The model still computes the percentage. The audit trail still preserves it down to four decimal places. What changes is that the surface turns one continuous number into three pre-decided thresholds — calibrated once, defended in the audit trail.

I'll give you the principle, because every decision in this project follows from it. Trust surfaces translate model output into human decisions, not human numbers. A trust surface's job is to compress what the model knows into what the user can act on, without losing the path back to what the model actually said.

And yes — somebody is going to ask me in the next 30 minutes whether I threw information away. The answer is yes, deliberately, on the action surface. And no, never, in the audit trail. The information's preserved. The decision-load is reduced. That's the trade. That's what makes the band design defensible.

▸ PACING — out by 6:00.

---

## Two More Decisions, Fast · 6:00–8:00

【slide 7】

Two more decisions, fast — same principle, different applications.

First: rule engine over bulk-edit. The obvious feature request from every demo was "let me select 200 rows and reclassify them." The non-obvious read of that request was "I don't trust your AI and I want to override it manually forever." So bulk-edit would have entrenched distrust as the dominant workflow. A rule engine — "any transaction from wallet X over $Y, classify as Z" — let the CPA encode her judgment into the model. Every override became permanent training signal she could see and audit. The principle: override is a design failure mode; rule-authoring is the design success state. When a user overrides, that's the system failing. When a user authors a rule, that's the system learning at the user's pace, not the engineer's.

【slide 8】

Second: anomaly flags as first-class objects. Anomalies — volume spikes, duplicate ingestion, wallet inconsistencies — initially lived as toast notifications and inline icons. They were invisible by Tuesday. So we promoted them to a dedicated route with priority, status, and assigned reviewer. They went from interruptions to a triage queue. And the audit trail emerged for free, because the route is the audit trail. The principle: if a class of issue recurs, it deserves a noun in the URL. Toasts are for transient events. Routes are for ongoing concerns.

---

## The Honest Miss · 8:00–9:30

【slide 9】

I want to spend 90 seconds on something most case studies skip. I shipped this product. It hit its metrics. And then I audited my own work and scored it 68 out of 100. That audit is in the repo, dated, public, alongside the production code.

What did I find? 40% of feature components were bypassing the design token system — they were using hardcoded Tailwind color classes and arbitrary pixel values instead of the semantic tokens I'd built. I had a duplicate Button component — one called `button`, one called `enhanced-button` — and a duplicate Input pattern, both forks shipping working features. Two toast systems running simultaneously. Sidebar muted text written as `#a3a3a3` in nine separate files instead of as a token.

The honest part isn't the bugs. Every shipping product has bugs. The honest part is publishing the audit alongside the product, dated, before anyone asked. The principle: a design system you don't audit isn't a system. It's a wish.

And if anyone wants to ask me about the 68 — I'll say it now: shipping at 100 means you over-engineered. Shipping at 68 with a dated public audit means the next iteration has a starting line. I'd rather work somewhere that ships at 68 and audits in week six than somewhere that ships at 95 and never audits at all.

---

## The Outcomes · 9:30–11:30

【slide 10】

Now the metrics. Four numbers, each tied to what it actually measured.

【slide 11】

40% reduction in accounting processing time. That's the median time from wallet-ingest to filed-classification, sampled across 6 onboarded firms over a 6-week post-launch window. Real behavioral measurement, not a survey. 45% reduction in CPA onboarding time. Time from credential-issue to first-completed-classification task. Same 6-firm cohort.

【slide 12】

32% increase in demo-to-customer conversion. Sales pipeline data, quarter-over-quarter post-redesign. That's the gap I described at the start, closed. And 85% engineering dependency reduction. This is the one I'm happiest to be pressed on, because it's the most attackable. It's measured against design clarification tickets reopened post-handoff, before versus after the v2 component spec. So the claim is: components shipped tight enough that engineering didn't have to come back and ask what I meant. Falsifiable, measured, and the ticket data is real.

▸ PACING — out by 11:30.

---

## The Repo-as-Receipt · 11:30–13:30

【slide 13】

One more thing before we transition to Symplify, because the job description says this role is not Figma-only — and I want to address that directly.

Everything you've seen so far is in the repo. The Computis app is a React 18 / TypeScript / Tailwind / Radix application, 49 UI components, 14 feature directories. The component library is mine. The `classification-insights` panel you saw two slides ago — that's me. The anomaly route. The rule engine forms. The design system documentation. Mine.

Where's the line? I write the surfaces. I don't write the data layer. Transaction table virtualization, chart rendering, server endpoints — that's engineering. But the surface where the CPA decides whether to trust the AI — that one ships from me, in production code, with Figma as the upstream source of truth and the React as the source of record.

I'm telling you this now because if I'm the founding designer at Wayline, this is the rhythm I bring. Figma to React, owned end-to-end on the surfaces I'm responsible for. No handoff theater. If it ships visual drift, that's on me.

To close Computis quickly: six principles, one project. Trust surfaces translate model output into human decisions, not human numbers. Override is a failure mode; rule-authoring is the success state. If a class of issue recurs, it deserves a noun in the URL. Visual density is a respect signal to power users. In regulated verticals, the audit trail is the product. And a design system you don't audit isn't a system; it's a wish.

Hold those for a minute. We're going to see most of them again in a different vertical.

---

## Transition · 13:30–14:30

【slide 14】

Quick transition before Symplify.

Hold the Computis primitive in your head — three-band confidence on the AI output, decision routing, audit trail behind every call. Here it is on the left. On the right, the same primitive, in a different product, in a different industry, for a different professional user. Confidence indicator on every AI output. Compliance badge in-line. A panel where the human supervises an agent.

I designed both of these. Computis is a crypto tax product. The one on the right is from a hospital operations platform. Two regulated verticals. Same primitive. Same staff-level instinct underneath — that the design problem with AI products isn't "show the user what the AI said." It's "design the screen where the user decides whether to trust what the AI said."

Let me show you the second project.

---

# Part 2 — Symplify

## The One-Liner Cold Open · 14:30–15:30

【slide 15】

`[One beat between long clauses. Let the stakes line settle.]`

Okay, project two. Symplify was the AI layer I designed for a hospital operations platform at CDP — fourteen agent-assisted features running underneath nurses on a twelve-hour shift, where the design bar wasn't "delightful," it was "don't kill anyone."

Quick framing note before I go further. Symplify is a CDP client engagement — meaning it's a client product I led design on, not my company. I'm the founding product designer on it. Clinical users. HIPAA. Fourteen AI features in production. Now — the interesting part.

Picture a nurse at 6:45 in the morning. She's fifteen minutes from the end of her shift, with eight patients to hand off to the incoming team. The legacy workflow is a verbal walk-and-talk plus a Word doc. Information loss during handoffs is one of the largest single sources of in-hospital incident reports. And the AI tooling that exists to fix it generates summaries that clinicians either ignore or — worse — half-trust. That's what we were designing into.

---

## What Was Real, What Was Mocked · 15:30–16:30

【slide 16】

I want to get one thing out of the way in the first sixty seconds of Symplify, because somebody in the panel is going to ask about it later and I'd rather just tell you upfront.

The model inference layer was mocked. Simulated latency, seeded confidence distributions across High, Medium, and Low bands. Real-model integration was scoped for post-handoff. That's on the right side of the slide.

What was real — and this is the important part — was the design problem. What does the trust surface look like when the model is wrong twelve percent of the time? That question is identical whether the inference is live or mocked. The thresholds would move with a real model. The surface wouldn't. That's the whole point of confidence-banded UX — it's resilient to model swaps. The reason I'm naming this now: it's the exact problem you're solving with a real voice model at Wayline.

---

## The Supervision Primitive · 16:30–18:30

【slide 17】

`[Slow tempo. Eye contact at the camera. This is the Symplify-side load-bearing slide — the one the panel locks onto.]`

Here's the same call I made at Computis, in a different vertical. On screen is the AI Assistant Popup — the surface that sits over every AI-generated output in Symplify. Three things on it. The output itself — a draft handoff summary, a triage recommendation, a drug-interaction flag, whatever the model produced. A confidence indicator next to it, three bands again — High, Medium, Low. And a compliance badge in-line, indicating the HIPAA posture of that specific output.

The principle is the one I planted at Computis, and I want to name it again because it's the through-line of the whole deck. Trust surfaces translate model output into human decisions, not human numbers. The clinician doesn't see 0.87. She sees High, with the model's reasoning one click away and the audit trail one click further. Three bands, three decisions. Accept. Review. Escalate. Same shape as Computis.

What's different here is the failure cost. A wrong crypto classification is an audit. A wrong drug-interaction flag is a patient. So the supervision design has to do more work — the badge in-line on every output isn't decoration, it's the surface saying *this is the regulatory posture of this specific decision, right now, not the platform in general.* Compliance signaling lives at the output, not in the footer.

And the same primitive shows up across fourteen features. Triage. Drug interaction. Shift handoff. Discharge instructions. Operational insights. Predictive alerts. The supervision pattern is the design system. That's the staff-level move — when you ship one trust primitive across fourteen surfaces, you're not designing features anymore. You're designing the company's relationship with its model.

---

## Patient Acuity · 18:30–20:30

【slide 18】

Patient acuity. This is the one where the design instinct most candidates have — and where I'd argue the wrong instinct is the obvious one.

The obvious instinct with clinical AI is to ship dictation. Build a microphone. Transcribe speech. Let the clinician edit the output. Voice in, free text out. Every clinical AI product on the market works that way.

The clinical instinct is the opposite. The clinician doesn't need a faster way to type. She needs the system to surface what she should already be looking at. Acuity isn't something a doctor writes down — it's something the model infers from vitals, lab trends, nursing notes, length of stay. The job of the surface is to render that inference legibly and let her confirm or override.

`[Gesture at the screenshot.]`

So what you're looking at is the acuity dashboard. Four bands — critical, high, moderate, stable. Color-coded against the same token system the rest of the AI surfaces use. Sparklines on every row, because a patient trending from an 8 down to a 7 is a very different clinical situation than a patient trending from a 6 up to a 7. The current score is the same. The trajectory is what tells you what to do.

The principle: the clinician's job isn't to write. It's to confirm. Open-ended typing puts the burden of structure on the human. Inference with a confirm-or-override surface puts the burden of structure on the system. That's the whole game in clinical AI. It's the same shape underneath triage, underneath drug interaction, underneath every AI feature Symplify ships.

And just so the through-line is unambiguous — the same banded primitive shows up in operational insights and in predictive alerts. One visual language for risk, across three different surfaces.

---

## Role-Aware UI · 20:30–22:00

【slide 19】

Quick decision worth surfacing — sixty seconds.

Symplify has three roles. Admin, doctor, patient. The obvious read is that role-aware UI is a permission system — who gets to see what. That's the half of it that doesn't matter. The half that matters is that each role sees a different calibration of the same AI confidence.

The admin sees numeric values — 0.87, 0.62 — because the admin is auditing model behavior across the platform and needs the underlying signal. The doctor sees three bands — High, Medium, Low — same as Computis, because she's making decisions at the patient level and three buckets map to three actions. The patient sees no AI surface at all. Not because the AI isn't running underneath — it is — but because the patient isn't supervising the model. The clinician is. Showing an AI confidence band to a patient would invite trust calibration from someone who shouldn't be doing it.

The principle: role isn't a permission system. It's a trust calibration. Permissions decide who can see what. Calibration decides how much of the model's uncertainty each viewer is qualified to act on.

---

## Outcomes · 22:00–23:30

【slide 20】

Three artifacts. No metric numbers on this slide, and I want to name that directly because the absence is intentional.

Fourteen shipped AI features across clinical, operational, and communication workflows. That's the count of surfaces I designed and that engineering deployed — countable, defensible, in the codebase. The confidence threshold slider became a primitive — the same banded review affordance shows up underneath fourteen features instead of fourteen different review surfaces. And the shift handoff feature ships as SBAR — Situation, Background, Assessment, Recommendation — the framework clinicians have used for twenty years. The AI didn't invent a new structure. It adopted the one the user already trusts.

Now — the metric question. Computis had four numbers because the launch window let us measure them. Symplify launched into a clinical setting where adoption telemetry takes six to twelve months to read cleanly, and I don't have that data yet. So rather than fabricate softer numbers, the slide reads as artifacts. If you press me on what shipped, that's the answer — these three. I'd rather show three artifacts honestly than four numbers I can't defend.

---

## Through-Line, Second Showing · 23:30–24:30

【slide 21】

We're at the close.

Same composition you saw at the Computis-to-Symplify transition, second showing. On the left, the Computis classification-insights panel. On the right, the Symplify AI Assistant Popup. Two regulated verticals. Two professional user bases. One trust primitive — confidence-banded inference with an audit trail behind every call.

Hold that frame for a minute, because the next three slides are about what it means for Wayline.

---

# Part 3 — Synthesis, Close, Ask

## Compound the Two Projects · 24:30–25:30

【slide 22】

Compounding the two projects into one argument.

Computis taught me to design trust surfaces for finance. Symplify taught me to design them for healthcare. Two regulated verticals, two professional user bases, two different failure costs — and the same primitive underneath both. That's the staff-level signal I want to plant here. It's not that I've shipped two AI products. It's that I've shipped the same trust primitive into two industries where the failure cost is high enough that the surface had to earn its way past skeptical users with licenses on the line.

Property management is the third regulated vertical. A property manager handling a tenant complaint isn't a CPA filing a return or a clinician on a twelve-hour shift, but the design problem is the same shape. Confidence-banded inference. Compliance posture surfaced at the output. Audit trail behind every call. Same primitive. Third vertical.

---

## Bidirectional Inference · 25:30–26:30

【slide 23】

One friendly amendment to the job description, and then the bridge to Wayline. The JD says *seamless human-agent interaction.* In regulated AI surfaces — finance, healthcare, property management — the design goal is the opposite. Legibly seamful. The user needs to see the seams precisely because the stakes punish over-trust.

The argument I want to leave you with is this. Input inference and output inference are the same design problem at different temporal constraints.

What I've shown you in acuity — a model inferring something the clinician would otherwise have to extract by hand, rendered as a banded surface with a confirm-or-override path — that's the input half. Wayline's product is the output half. A model inferring what to say next, rendered as a draft, with a human review path before send.

Same primitive. Same trust surface. Same supervision design.

The thing that's genuinely different on the output side is the temporal constraint. Acuity gets re-scored every few minutes; the clinician has time to scan a band before acting. Voice happens in real time; the override window collapses. That's the design problem — confidence-banded inference with a real-time human override path. I've shipped the input half of it. The output half is the same primitive applied to a different temporal constraint.

`[Gesture back at the deck.]`

That's the through-line. Now let me tell you what I'd do about it in the first 90 days.

---

## 30/60/90 · 26:30–27:30

【slide 24】

Three things, one per period. Concrete, defensible, the kind of plan you'd want a founding designer to have on day one.

First 30 days — ship a baseline supervision surface for one intent class. Lease inquiries. The simplest, highest-volume call type — perfect for instrumenting trust. Confidence band on what the model is about to say. The seam where the property manager decides whether to confirm, edit, or override. Behind a feature flag, in front of one customer, with measurement infrastructure shipping alongside. Not a pilot. A measurable trust surface from day one.

By day 60 — extend the primitive to maintenance requests and payment disputes. Two more intent classes, same review affordance, same override path. The point of doing three intent classes inside 60 days isn't volume. It's calibration validation. If the confidence bands hold up across lease inquiries, maintenance, and payment disputes — three very different conversation shapes — the primitive is real, not a one-off.

By day 90 — versioned component library, and the first round of property-manager-co-authored iteration. Half-days sitting with two PMs on real calls. Same move as Computis's clinician testing on the Symplify side, ported to a different vertical. The design system bet is that one trust primitive ships across intent classes. The co-authoring bet is that the primitive only earns its way past skeptical PMs if the PMs helped shape it.

Three intent classes. One versioned component library. Two PMs co-authoring. None of it requires me to invent a new pattern — it requires me to apply the one I've shipped twice already to a third vertical.

---

## Spoken Close · 27:30–28:00

【slide 25】

`[High-stakes beat #4. Deliberate. Camera contact. One beat between sentences.]`

Here's the one sentence I want you to remember.

I design the surface where a professional decides whether to trust an AI. I've shipped that surface twice, in two regulated verticals, and audited my own work publicly in the repo. Wayline is the third vertical, and the design problem is the same shape.

---

## The Ask · 28:00–29:00

【slide 26】

The ask.

I want the founding designer role at Wayline. Not because I'm looking for my next thing — I'd be telling you a different story if that were the move. Because the problem you're solving — confidence-banded inference with a real-time human override path, in a third regulated vertical — is the problem I've been preparing to solve for the last four years across the first two.

If you decide to move forward, what I'd want from the next conversation is one hour with the product surface as it exists today. Not a portfolio review of mine. A working session on yours. I'd rather show you how I think by reading your actual product than by walking you through more of mine.

Whatever you decide, thanks for the hour. I'm going to stop here and open it up for questions.

---

**End — 29:00**
