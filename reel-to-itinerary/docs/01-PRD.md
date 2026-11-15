# PRD — Reel→Itinerary (v2, 2026-11-15)

v2 aligns the PRD with the business plan ("Integrate and beat plan") and the Wanderlog onboarding and import recording. Changes since v1 are marked **[NEW]** or **[CHANGED]**. Phases: **MVP** = the eight-week build, **v1.0** = public launch, **v1.1** = after launch, **Later** = unscheduled.

## Problem
People save travel reels/posts and never turn them into a plan. Places are scattered across captions, on-screen text, voiceover and comments.

## Users
Travellers who save creator content on Instagram/TikTok/YouTube and want a usable trip plan.

## Positioning [NEW]
"Every place from the reel, checked and mapped." Share-sheet import is table stakes: Wanderlog accepts links, screenshots, pasted text, files, and Maps/chatbot lists, shows timestamped quotes, and credits creators. Our edge is accuracy and trust: a Verified label on every place with its source type, reality checks, a calm paywall, and privacy claims we can prove.

## Core flow [CHANGED]
1. User taps Share on a reel (or pastes a link / screenshots / text) → picks our app. A first-run sample reel is offered so a new user sees a result without having to find one. **[NEW, MVP]**
2. App reads what it legitimately can:
   - TikTok / YouTube: caption or description via the official oEmbed / API route.
   - Instagram: default is the capture helper (paste caption, screenshots or a screen recording). Caption via Meta oEmbed only if and when Meta App Review is approved and legal signs off on that use.
3. If coverage is thin, offer "Add a screen recording or screenshots for more" (3-step helper).
4. On-device OCR + speech-to-text run on the user's media. Text only goes to the extraction service.
5. Candidates are verified with MapKit and shown in the Import preview (below). Unverified places are never auto-added.
6. Confirmed places merge into a Trip (multiple reels can feed one trip) and are grouped into days.
7. User edits, views map + travel times, runs reality checks, sees budget, and exports.

## Import preview [NEW, MVP]
Replaces the plain Inbox. For each import show:
- A short summary of the post, the creator's handle with a link back, and the platform.
- A checklist of places with select all / deselect all.
- Per place: name, photo if licensed, a Verified or Needs check label, the source type (caption / on-screen / voiceover / pasted comment) and the quote or timestamp ("seen on screen at 0:14").
- A map with numbered pins for the selected places.
- "Add N places to trip" with a day or section picker, and an Undo toast after adding.
- A thumbs up/down "How was this import?" with an optional reason; used to improve extraction.
- Ambiguous places ask the user to pick; places we could not verify are listed separately and are off by default.

## Input types
- **MVP:** shared link, pasted caption/text, screenshots, screen recording. Reddit threads and other text come in as pasted text or screenshots (user-supplied, on-device); no server-side Reddit fetch.
- **v1.1:** files (PDF, Word, text), lists copied from Maps, text pasted from a chatbot.

## MVP scope [CHANGED]
- Share extension (URL, image, video, text)
- oEmbed (TikTok/YouTube) + paste + user-supplied media
- On-device OCR and transcription
- LLM extraction → MapKit verification → Import preview
- Trip with day plan: day clustering, reorder/edit, auto-build days from picks **[NEW]**
- Map with travel time and distance between stops, opening hours per stop **[NEW]**
- Evidence per stop and Verified label **[NEW]**
- Reality checks: closed days, long legs, "this day is not doable" **[NEW]**
- Budget per meal and trip total; meals marked "suggested by us" **[NEW]**
- Sample reel; delete-my-data; attribution on every stop

## v1.0 (public launch) [NEW]
- Optimise route for a day, showing total time and distance.
- Offline read-only trips (Pro) and Google Maps export link (Pro), alongside Apple Maps guide, Calendar and share link.
- Dark mode (free; Wanderlog gates it as Pro).
- Trip tabs: Itinerary, Map, Budget, Notes.
- Fast read-only day view that opens without entering edit mode.
- Onboarding: at most three questions (trip type, who with, budget feel), one notification prompt with a clear reason, no location "Always" request.
- Paywall: shown only at a natural limit (the fourth reel in a month, offline, export), after the user has seen their first plan. Annual plan with a trial; UK price in pounds.

## v1.1 [NEW]
Share link then tripmates; booking prompts (for example a "need a place to stay?" banner) with clear affiliate disclosure; files, Maps lists and chatbot text import.

## Later [NEW]
Steps / walking goal mode (HealthKit, on-device only), expense splitting, group voting or collaboration, journal, creator-permissioned trips with a link-in-bio programme, Android.

## Out of scope (by design — legal and positioning)
Profile/account import, background crawling, downloading platform media, logging in to IG/TikTok, storing creator media, republishing creator text. Scraping or bot-capturing creator content, server-side Reddit scraping. Reservations and Gmail scanning, flight deals, always-on trip tracking, a guides marketplace (Wanderlog's ground, not our edge).

## Privacy wording [CHANGED]
Do not claim "your saved reels never leave your phone". Extracted text is sent to our backend and an LLM provider. Use: **"Your videos never leave your phone. Only the text we read from them is sent, to find the places."** No ad or social-login SDKs; claim "no ad tracking" only if the build has none. Keep the privacy policy and App Store labels consistent with this.

## Success metrics
- ≥70% of shared reels yield ≥1 verified place (caption + recording)
- Median time share→reviewed list < 60s
- ≥40% of users who see the recording prompt complete it
- <5% of accepted places later deleted as wrong
- **[NEW]** ≥90% of accepted stops carry a source-type label
- **[NEW]** Benchmark: on ~10 reels in each of four types (caption-rich, on-screen-text-only, voiceover-only, carousel), recall and precision beat Wanderlog on at least 3 of the 4 types before wide launch.
- **[NEW]** No unflagged leg over 45 minutes inside a single day.
- **[NEW]** First plan visible before any paywall; paywall prompt at most once per session.
- **[NEW]** Read-only day view opens in 2 taps or fewer.
- **[NEW]** Budget used on ≥30% of trips (hypothesis).

## Monetisation
Free: 3 reels/month, one trip. Pro: unlimited reels, multi-trip, offline, Google Maps export, route optimisation, budget tools. Prices to test: about $5.99/month or $34.99/year in the US and a pound price in the UK (Wanderlog UK shows £30.99/year, £2.57/month with a 7-day trial). Affiliate booking links only with clear disclosure.

## Open questions
- Does Meta allow reading an Instagram caption from oEmbed for place extraction? (lawyer + Meta)
- Android: when, and React Native or native?
- Whether to add Google Places (ratings) in v1, given licence and attribution rules.
- Whose sample reel can we use? (our own, or a creator who has agreed)
- Which of the v1.0 items fit the eight-week build, and which move to v1.1? *(answered in `04-BUILD-PLAN.md`)*
