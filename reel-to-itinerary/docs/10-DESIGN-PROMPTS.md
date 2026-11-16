# Prompts to fill the design gaps (2026-11-16)

How to use: paste **S0 (shared brief)** into Claude Design once per chat, then paste one prompt at a time. Each prompt is self-contained apart from S0. Art prompts (section C) are for OpenArt or any text-to-image tool. Gap list source: `docs/08-CHANGE-PLAN.md`; directions and scorecard: `docs/09-DESIGN-DIRECTION.md`.

| Gap | Prompt | Canvas artboard(s) |
|---|---|---|
| Import preview | P1 | rework `Review` |
| Instagram and sample variants, positive reframe | P2, P3 | `Main` variants, new Sample |
| Reality-check states | P4 | `Day`, `Trip` |
| Error and permission states | P5 | new |
| Read-only day view, per-stop chips | P6 | `Day` |
| Evidence sheet fixes | P7 | `Evidence` |
| Settings additions, "What we send" | P8 | `Settings`, new |
| Onboarding cut-down | P9 | `Onb1-4`, `Taste` |
| Paywall and free limit | P10 | new |
| Trip tabs, Notes, export sheet | P11 | `Trip`, new |
| Dark mode | P12 | all key screens |
| Motion spec | P13 | new |
| Variant sprint (3 hero screens x 3 directions) | P14 | new |
| Art kit | C1 to C9 | assets |

---

## A. Shared brief (paste first)

### S0
```
You are designing screens for an iPhone app that will be rebuilt 1:1 in SwiftUI by Claude Code.

PRODUCT: Reel to Itinerary. The user shares a travel reel (TikTok, Instagram, YouTube) or pastes text/screenshots; the app reads caption, on-screen text, voiceover and comments, finds places, verifies each on the map, and builds an editable day-by-day trip with travel times, meals and budget. Positioning: "Every place from the reel, checked and mapped." Our edge is accuracy and trust: a Verified label with its source on every place, reality checks, a calm paywall, and privacy claims we can prove.

WORK IN the existing canvas "Reel to Itinerary Screens" (40 artboards). Keep every existing artboard unless I say to replace it. Name new artboards "<number> <Title>" and state variants "<Screen>: <state>". Frame 390x844. 1 CSS px = 1 pt. Use flex/grid with gaps, no absolute positioning except map pins, the map top bar and bottom sheets. Safe areas: do not fake a status bar. Do not add a fake home indicator.

TOKENS (use only these; add a token before using a new value). Light: bg #F4F6F8, surface #FFFFFF, line #E1E6EB, lineStrong #C9D2DA, ink #0F1E2E, muted #5B6B7B, accent #0B6E6E, accentPressed #084F4F, onAccent #FFFFFF, okBg #DDF3E4, okFg #1B6B3A, warnBg #FFF1D6, warnFg #8A5A00, warnText #6B4500, warnBorder #E8B64A, neutralBg #E8ECF0, neutralFg #44525F, day1 #5B3FD1, day2 #C2410C, day3 #0B6E6E. Dark (provisional, you may refine and must check contrast): bg #0E1620, surface #16222F, line #263544, lineStrong #3A4B5C, ink #F2F5F8, muted #9AA9B8, accent #3FB8B0, onAccent #06201F, okBg #12331F, okFg #7AD39A, warnBg #3A2A0A, warnFg #F2C46B, neutralBg #223140, neutralFg #B7C3CF, day1 #8F7BFF, day2 #FF8A5B, day3 #3FB8B0.
TYPE: Space Grotesk 700 for titles (30, 28, 20, 17); Inter 400/500/600 for body (16, 15, 14, 13, 12). Eyebrow 13/600 uppercase tracking 0.06em.
SHAPE: radius chip 999, control 12, button 14, card 16, sheet 24. Primary button 52 high, secondary 48, small 44. Screen padding 20. Minimum touch target 44.

COMPONENT NAMES (reuse, do not invent near-duplicates): PrimaryButton, SecondaryButton, IconButton, StatusDot, CaptureChecklistRow, PlaceChip, StatusPill (verified / pickOne / unverified), CandidateCard, SourceTypeLabel, FilterChip, DayChip, MapPin, StopRow, TravelConnector, RealityCheckBanner, AttributionCard, LinkOutButton, BottomSheet.

HARD RULES
- Never show creator videos, thumbnails or frames, or photos of real people. Placeholders are labelled boxes.
- Every stop shows its source type (caption / on-screen text / voiceover / pasted comment) and, where known, a timestamp. Show a short quote only as transient text on the Import preview, never as saved data.
- Every stop credits the creator with a link back ("Credit: @handle · View original").
- Unverified places are never added automatically.
- Prices are always labelled "Est.", "Creator said" or "You entered", with the source.
- Never show third-party ratings or reviews. Link out instead ("Opens the other service. We don't copy their reviews.").
- Privacy wording, exact: "Your videos never leave your phone. Only the text we read from them is sent, to find the places." Never say saved reels never leave the phone. No ad or social-login logos.
- Copy: plain, active, specific, no hype, no emoji as UI, no em-dash asides. Use real sample content (Lisbon, 3 days, creator @sunnyroutes). No lorem ipsum.
- Accessibility: text 4.5:1 contrast, real buttons and links, labels on icon-only buttons, readable at Dynamic Type XXL.
- Each artboard: also write a short "Notes for build" block in the artboard's source comments listing component names used, states, and tap targets.
```

---

## B. Claude Design prompts

### P1. Import preview (rework Review)
```
Rework the artboard "2 Review places" into the IMPORT PREVIEW. Keep the existing Verified / Pick one / Unverified card styling and timestamps.
Top to bottom:
1) Header: platform chip ("TikTok"), post summary in one line ("3 days in Lisbon"), creator handle with a "View original" link.
2) Row: "Select all" / "Select none" and a count ("5 of 8 selected").
3) Place list. Each CandidateCard: checkbox, name, category and area, StatusPill, SourceTypeLabel + timestamp ("On-screen text · 0:14"). For the selected card in the example, also show a one-line transient quote under the label, visually lighter and marked "from the reel, not saved". Pick-one cards show 2 radio options. Photo slot: show a labelled 56x56 placeholder "Map photo" (we may get photos from the map provider only).
4) A "Not verified" collapsed section at the end (off by default, count shown, expand to see).
5) A map strip (160 high) above the list or pinned under the header with numbered pins for the selected places, tapping a pin scrolls to its card.
6) Footer: day/section picker ("Add to: Day 1 ▾") + PrimaryButton "Add 5 places to trip".
Also design these states as separate artboards: "Import preview: after add" (Undo toast, 5 seconds, "Added 5 places · Undo"), "Import preview: feedback" (bottom sheet "How was this import?" thumbs up/down, optional reason field, Send / Skip), "Import preview: all verified", "Import preview: nothing selected" (button disabled with reason).
```

### P2. Import card variants (Instagram capture-first, positive reframe)
```
Update "1 Import card" and add variants. Problem: today it opens with three amber "Not captured" rows, which feels like failure.
Reframe the header as progress: eyebrow "Reading your reel", title "Found 4 places", subtitle "Add a recording to find more." Make the checklist a "What we read" list where read items are green and the others are neutral "Add" rows (tap to add) instead of warnings. Keep the three actions (Add a screen recording, Add screenshots, Paste caption) and the privacy line (exact wording from S0, shortened to fit).
New artboards:
- "Import card: Instagram" - captions cannot be read automatically, so lead with the capture helper: "Instagram needs a recording or screenshots." Steps shown as 3 small cards (Paste caption, Screenshots, Screen recording) with the recommended one highlighted. No "Caption: Read" row.
- "Import card: YouTube" - description read via official route; comments available.
- "Import card: pasted text" - source label "Pasted text", creator unknown (no handle).
```

### P3. Sample reel (first run)
```
Design the first-run sample reel. It must show a new user the whole value in under 20 seconds without finding a reel.
Artboards: "Sample: entry" (card on the Trips empty state: "Try it with a sample reel", clear "Sample" badge, one line "A made-up reel so you can see how it works"), "Sample: reading" (the import card in reading state with a SAMPLE ribbon), "Sample: result" (Import preview with SAMPLE ribbon, 4 verified places), "Sample: done" (explains what to do next: "Share a real reel from TikTok, Instagram or YouTube", with a 3-step how-to).
Content is synthetic: a made-up creator "@sample.trips", Lisbon, 3 days. Use a labelled placeholder for the reel frame, never a real video still. Every screen carries a visible "Sample" marker so no one mistakes it for real data.
```

### P4. Reality-check states
```
Add reality checks to "6 Day plan" and "3 Trip map". Design these states, each as its own artboard, using RealityCheckBanner (warnBg/warnText, radius 12) and a marker on TravelConnector:
1) "Day: closed" - a stop is closed on this day ("Closed on Mondays"), banner with two actions: "Move to another day" / "Keep anyway".
2) "Day: long leg" - leg over 45 minutes ("52 min by tram") flagged with a warn marker on the connector and a banner "This leg is long. Consider moving a stop closer."
3) "Day: not doable" - day too full ("Not enough time: about 11 h of travel and visits between 09:00 and 20:00"), banner with "See why" and "Fix day" actions, and a "Why" sheet listing the numbers (travel time, time at stops, hours available).
4) "Day: no hours" - opening hours unknown, show "Hours unknown" as neutral text, never a guess.
Banner wording must say what is wrong, why, and what to do. No red full-screen alarms.
```

### P5. Error and permission states
```
Design error and permission states, one artboard each, calm and specific (what happened, what to do, one primary action):
1) "Error: photos denied" (cannot read the recording; Open Settings / Paste caption instead)
2) "Error: recording failed" (could not read this video; Try again / Add screenshots)
3) "Error: speech unavailable" (voiceover can't be read on this device; continue with on-screen text)
4) "Error: no network" (we need a connection to find places; your trips are still available offline)
5) "Error: limit reached" (3 of 3 reels used this month; shows plan summary, links to the paywall; does NOT block viewing existing trips)
6) "Error: extraction failed" (we couldn't read this one; Try again / Paste caption; never show technical codes)
Each has an illustration slot (labelled placeholder 160x160) and uses existing buttons.
```

### P6. Day plan: read-only variant and per-stop chips
```
Update "6 Day plan".
- Remove the steps ring from the default design (steps goal mode is a later feature); keep it only as a separate artboard "Day: steps (later)".
- Add a READ-ONLY variant "Day: read-only" that opens without edit mode: big stop list, large tap targets, no drag handles, a single "Edit" in the header, designed to be glanced at while walking. Two taps or fewer from the Trips list.
- Every stop shows a SourceTypeLabel chip (Caption / On-screen / Voiceover / Comment), the credit, and an opening-hours line ("Open until 23:00", or "Hours unknown").
- Budget chips under the header must read "Est. €15", "Est. €25", "You entered €40" and show their source on tap.
- Meals the app adds are visibly separate: a dashed card labelled "Suggested by us".
```

### P7. Evidence sheet fixes
```
Update "25 Why is this here".
- Add the short transient quote beside each timestamp (lighter text, small "from the reel" note).
- Remove the line "No paid-partnership label found in the caption". Replace with a neutral "Sponsored? We only check visible text, so we can't confirm either way." with an info icon.
- Define confidence: High = seen in 2 or more different sources, Medium = 1 source and verified, Low = 1 source and unclear. Show the level with a small legend row ("How we decide").
- Keep: credit link, "Mentioned in 2 reels", "Creator said €1.50 · 0:14".
```

### P8. Settings additions and "What we send"
```
Update "17 Settings and privacy" and add a detail artboard.
Settings additions: Plan card (Free: "2 of 3 reels this month" / Pro), Restore purchases, Appearance (Light / Dark / System), Currency, Units, Notifications, Send feedback, About and legal. Keep Privacy group and Delete all data. Account: show only what we truly have; if we keep Sign in with Apple, label it and explain what is stored where (I will decide).
New artboard "What we send": a plain table - What we read on your phone (video frames, audio: deleted after reading) / What we send (extracted text only, no usernames, to find places) / What we do not send or keep (videos, audio, creator text) / Who receives it (our server and our AI provider for text only; the map service for place names). Use the exact privacy sentence from S0 as the lead.
```

### P9. Onboarding cut-down
```
Replace the current 4 carousel + 4 taste screens with a short flow. Rules: at most 3 questions (trip type, who with, budget feel), every step has Skip, no paywall inside onboarding, one notification prompt with its reason shown BEFORE the system dialog, never ask for location "Always".
Artboards: "Onb: welcome" (value in one line + one illustration slot + "Try a sample reel" / "Share a reel"), "Onb: trip type", "Onb: who with", "Onb: budget feel", "Onb: notifications" (reason: "Tell me when a reel has finished reading"), "Onb: done" (goes to the sample reel). Progress shown as a thin bar, back button on every step. Keep the app palette; do not copy any competitor's look.
```

### P10. Paywall and free limit
```
Design the paywall. Rules: appears only at a natural limit (fourth reel in a month, offline, export), only after the user has already seen their first plan, at most once per session. Calm, honest, always dismissible.
Artboards: "Paywall: limit" (headline "You've used your 3 free reels this month", what Pro adds as 5 specific benefits, annual plan with trial highlighted, monthly below, price in local currency, "Restore purchases", "Not now" always visible, small print: renews, cancel any time), "Paywall: offline" and "Paywall: export" (same layout, headline changes), "Paywall: counter" (the Trips list with "2 of 3 reels this month"), "Pro locks" (lock icons on gated rows). Use placeholders: $5.99 per month, $34.99 per year (UK price: [£ to be set]). No fake urgency, no countdown timers, no dark patterns.
```

### P11. Trip tabs, Notes, Google Maps export
```
Update "3 Trip map": add trip tabs Itinerary / Map / Budget / Notes (native-style segmented tabs under the header). Add "Trip: notes" (free text per trip, empty state and filled). Add "Export sheet" (Pro): options Apple Maps, Google Maps link (note: "Long days are split into parts"), Calendar, Share link; Pro lock on Google Maps link. Keep the bottom sheet as a native-style sheet with detents (peek, medium, large) and show all three detents as artboards.
```

### P12. Dark mode
```
Create dark-mode variants of: Import card, Import preview, Review states, Trip map, Day plan, Place card, Budget, Evidence, Settings, Paywall. Name them "<Screen> (dark)". Use the provisional dark tokens in S0; adjust any that fail 4.5:1 text contrast and list the changes. The map must have a dark treatment (muted land, deeper water, lighter route lines). Do not simply invert colours.
```

### P13. Motion spec
```
Make a MOTION SPEC page (one wide artboard, 800 wide) for three signature moments, each as a storyboard of 5 frames with timings, easing names and notes for SwiftUI:
1) "Reel becomes places": places appear in the checklist one by one (stagger 80 ms), each pin drops onto the mini map (spring, short), count updates.
2) "Route draws": the day route line draws from stop 1 to the last (1.2 s ease-in-out), pins pop (scale 0.8 to 1, spring) as the line reaches them.
3) "Verified": the Verified pill fills with a subtle stamp motion (scale 1.15 to 1, 220 ms) and a light haptic.
Also list global rules: durations (fast 150 ms, base 250 ms, slow 400 ms), easing (standard, decelerate, spring), Reduce Motion fallback (cross-fade only, no movement), haptic types. Output the numbers as a table so they can become tokens.
```

### P14. Variant sprint (3 hero screens x 3 directions)
```
Create 9 artboards exploring 3 directions for 3 hero screens. Use only our tokens unless a direction says otherwise, and note any new token you add.
Directions:
A "Refined utility": the current system, polished. Fix hierarchy (one hero element per screen, fewer identical cards), bigger type on the trip header.
B "Cartographic editorial": the map and route lines are the hero; large type; an illustrated destination cover (labelled placeholder 390x220, we will generate art); evidence and Verified as an ownable motif; flat sections with dividers instead of bordered cards. Keep the palette cool; do NOT use cream and terracotta.
C "Immersive": gradient hero with a large destination card (placeholder, no real photos), bold white type. This is a counter-example, expect it to be rejected for legal and effort reasons.
Screens: (1) Import: reel becomes places, (2) Trip home (header, day chips, itinerary list), (3) Place card.
Name artboards "Explore <screen> - A/B/C". After the artboards, add a one-artboard scorecard (1 to 5) for: legal fit, build effort in SwiftUI, difference from a photo-heavy competitor, text contrast, emotional impact in a 15-second screen recording, dark-mode viability, ownability.
```

---

## C. OpenArt (or any text-to-image) prompts

Rules for all art: text prompts only (never upload creator thumbnails or frames); no real brand logos, no readable text, no faces; keep the same style reference and seed across a set if the tool supports them; save prompt, model, seed and date in `art/prompts/`; check the tool's commercial-use terms before shipping; human review each image for artefacts (hands, signage, odd text).

**Style anchor (add to every prompt):**
`flat editorial travel illustration, soft geometric shapes, limited palette of deep teal #0B6E6E, ink navy #0F1E2E, violet #5B3FD1, burnt orange #C2410C and pale grey paper #F4F6F8, subtle paper grain, clean vector look, generous negative space, no text, no letters, no logos, no faces`

**Negative prompt (all):** `text, letters, words, watermark, logo, brand, photo, photorealistic, 3d render, faces, people close-up, UI, screenshot, blurry, noisy, busy background`

### C1. Style test (generate first, approve before the rest)
```
[style anchor] a narrow hillside street in a sunny coastal European city, a small yellow tram, tiled facades, a viewpoint with a river beyond, long shadows, vertical 4:5
```

### C2. Destination covers (one per city; 4:5 and a 16:9 crop-safe version)
Template:
```
[style anchor] [CITY] skyline and street scene with [3 generic landmarks or features], warm late-afternoon light, a thin route line in violet looping through the scene with small numbered circles (no digits visible), vertical 4:5, calm composition with open sky at the top for a title
```
Fill with: Lisbon (trams, tiled facades, hills, river), Tokyo (narrow lantern-lit lane, tall towers, a train), Paris (rooftops, a river, a tower silhouette), London (red bus, bridge, rooftops), Rome (domes, a plaza, stone steps), Barcelona (curved facades, a beach, a cathedral silhouette), Kyoto (wooden gate, pagoda silhouette, maple), New York (brownstones, water towers, a bridge), Bali (rice terraces, a temple gate, palms), Iceland (black beach, waterfall, a small red house).

### C3. Onboarding illustrations (4:5, minimal)
```
[style anchor] 1) a hand holding a phone whose screen shows abstract hills and a play triangle, a small share arrow floating above
2) [style anchor] a map pin being stamped onto a folded map, a tick mark floating nearby
3) [style anchor] a route line connecting three pins across a folded map, small clock icons
4) [style anchor] a phone on a bench in a city square, a dotted walking path leaving it
```

### C4. Empty and error states (square, 1:1, lots of space)
```
[style anchor] an empty suitcase open on a bench, nothing inside   (no trips yet)
[style anchor] a magnifying glass over a blank folded map   (no places found)
[style anchor] a paper plane circling above a cloud with a small broken line   (offline)
[style anchor] a tangled route line being gently straightened   (error, try again)
```

### C5. Paywall art
```
[style anchor] a travel map unfolding into a path of pins across hills, a small flag at the end, warm light, vertical 4:5
```

### C6. Sample reel frame (synthetic placeholder, not a real reel)
```
[style anchor] vertical 9:16 illustrated video frame of a sunny viewpoint over a hillside city at golden hour, a low wall in the foreground, no people, no text
```

### C7. App icon concepts (generate 6, pick 1, then redraw as clean vector)
```
flat app icon concept, a location pin whose tail turns into a route line, deep teal background #0B6E6E, off-white pin, one violet dot, rounded-square composition, centred, no text, no gradients beyond a subtle one, 1:1
flat app icon concept, a circular verified stamp with a small pin in the middle, teal and navy, bold simple shapes, 1:1
flat app icon concept, a folded map forming the letter-free shape of a pin, teal and orange, 1:1
```
Notes: Apple icons are square (1024x1024), no transparency, no text; keep a simple silhouette that survives small sizes.

### C8. Share-back poster backgrounds (one per day colour)
```
[style anchor] abstract topographic contour lines and a looping route in [violet | orange | teal], pale paper background, large quiet area in the lower third for text, vertical 4:5
```

### C9. App Store screenshot backgrounds
```
[style anchor] soft gradient from teal to navy with faint route lines and pin shapes, large empty centre for a phone frame, vertical 9:19
```

---

## D. After you generate
1. Drop approved images into the Claude Design canvas as assets and tell Claude Design the file name and where it is used.
2. Record each prompt, model, seed and date in `art/prompts/` (see `docs/05-ART-PIPELINE.md`).
3. Export reference PNGs of each approved screen at 3x into `design/reference/` for the snapshot tests.
4. Ask me to sync `06-DESIGN-HANDOVER.md` and `design-tokens.json` with the approved designs.
