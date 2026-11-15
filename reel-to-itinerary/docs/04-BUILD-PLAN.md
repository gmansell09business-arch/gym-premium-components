# Build plan (milestones for Claude Code) — aligned to PRD v2

Do one milestone per session. Each ends with passing tests + a rules check against `CLAUDE.md` and `docs/03-LEGAL-GUARDRAILS.md`.
Tags: **[MVP]** and **[v1.0]** are PRD v2 phases. The eight weeks below cover all of MVP plus the v1.0 items that fit. Anything that does not fit is listed under "Moved to v1.1" at the end.

## M0 — Scaffold (day 1)
**Prompt:** "Read CLAUDE.md and docs/02-ARCHITECTURE.md. Scaffold `ItineraryCore` (Swift Package, Foundation-only),
`Backend` (TypeScript, Hono, vitest), and `App/project.yml` for XcodeGen with an app target and a Share Extension
sharing an App Group. Generate `Theme.swift` from `spec/design-tokens.json` (light + dark). Add CI (GitHub Actions: `swift test` on macOS, `npm test` on Linux). No feature code yet."
**Done when:** both test suites run green (empty), `xcodegen generate` produces a project that builds on a Mac, token test passes.

## M1 — Extraction core (week 1)
**Prompt:** "Implement Codable models from `spec/extraction.schema.json`, a validator, `PlaceDeduper`, and
`ConfidenceRanker` in ItineraryCore with tests using hand-written fixtures in `spec/fixtures/`. Add `source type` (caption / on-screen / voiceover / pasted comment) and a quote or timestamp to each candidate. Then build
Backend `POST /extract` that calls the Claude API with `spec/extraction.prompt.md`, validates against the schema,
retries once on violation, and never logs request bodies. Use the claude-api skill for current model IDs."
**Done when:** fixture tests pass; schema-invalid LLM output is rejected; every candidate carries a source type; a contract test mocks the LLM.

## M2 — Share → Import preview, text paths (weeks 2–3) [MVP]
**Prompt:** "Implement the Share Extension handoff via App Group and the host-app flow: shared link / pasted text → `OEmbedClient`
(TikTok public oEmbed; YouTube via official API; **Instagram oEmbed only behind a feature flag, off by default**) → /extract →
MapKit verify → **Import preview**: post summary, creator handle + link back, place checklist with select all/none, Verified / Needs check label,
source type + quote/timestamp, map with numbered pins, 'Add N places to trip' with day/section picker, Undo toast, thumbs up/down with optional reason (stored locally + sent as text-only feedback).
Ambiguous places ask to pick; unverified are off by default. Fallback paste-caption sheet. Instagram default = capture helper prompt. Add the first-run **sample reel** using a synthetic fixture (no real creator content)."
**Done when:** sharing a TikTok/YouTube link or pasting text shows verified candidates; unverified ones are flagged, not added; attribution shown; Undo works; sample reel produces a result with no network call to a platform.

## M3 — User-supplied media (weeks 3–4) [MVP]
**Prompt:** "Add image/video acceptance in the Share Extension and a PhotosUI picker. Implement `TextRecognizer`
(Vision, 1–2 fps frame sampling, near-duplicate frame dedupe) and `Transcriber` (Speech/SpeechAnalyzer,
on-device only, `requiresOnDeviceRecognition = true`). Merge timestamped text, send text only to /extract.
Strip comment usernames before anything leaves the device. Delete all temp media in `defer` and on error.
Add the capture helper (3 steps), 'Import latest recording' and screenshots paths. Reddit and other text arrives only as pasted text or screenshots."
**Done when:** a sample screen recording yields places with timestamps; a test asserts temp dir is empty afterwards; no network call carries media; no server-side Reddit fetch exists (grep audit).

## M4 — Trips, day plan, reality checks, budget (weeks 5–6) [MVP]
**Prompt:** "Implement SwiftData Trip/Day/Stop, `DayClusterer` (explicit day wins; else geo clustering + time of day) with **auto-build days from picks**,
multi-reel merge into a trip, map view with travel time and distance between stops (MKDirections), opening hours per stop **from the chosen hours source (see conflicts log: decide before starting)**,
drag-reorder, **reality checks** (closed day, leg over 45 min, 'this day is not doable'), **budget per meal and trip total** (creator-stated and user-entered prices, estimate bands; label every price as an estimate and its source),
meals the app adds marked 'suggested by us' and visually separate, evidence + Verified label on every stop, and export (Apple Maps guide, Calendar, share link)."
**Done when:** two reels merge into one 3-day trip with no duplicate stops; edits persist; no unflagged leg over 45 minutes in a day; at least 90% of accepted stops carry a source-type label (test with fixtures).

## M5 — v1.0 experience and polish (weeks 6–7)
**Prompt:** "Build, in this order and stopping when time runs out (see cut order below): **[v1.0] Onboarding** (max three questions: trip type, who with, budget feel; one notification prompt with a clear reason; never request location 'Always');
**[v1.0] Trip tabs** (Itinerary, Map, Budget, Notes); **[v1.0] fast read-only day view** (two taps or fewer);
**[v1.0] Dark mode** (free) from the dark tokens; **[v1.0] Paywall** with StoreKit 2 (free: 3 reels/month, one trip; shown only at a natural limit after the user has seen a plan; at most once per session; annual plan with trial; UK price in pounds);
**[v1.0] Google Maps export link** (Pro; respect waypoint limits by splitting the day). Then art per docs/05-ART-PIPELINE.md (icon set, onboarding and empty-state art from text prompts only, prompts/seeds in `art/prompts/`)."
**Done when:** a new user reaches their first plan before any paywall; paywall never appears before the first plan; dark mode passes the layout and contrast checks; assets committed, no API key in repo.

## M6 — Compliance & launch (weeks 7–8)
**Prompt:** "Run the release checklist in docs/03-LEGAL-GUARDRAILS.md: grep audit for scraping libs/CDN fetches/secrets and **for ad and social-login SDKs** (inspect `Package.resolved`/dependencies),
privacy manifest and nutrition labels matching the PRD privacy wording, delete-all-data flow, App Attest on /extract, rate limits, App Review notes explaining the
user-supplied-media flow, and run the four-type benchmark (about 10 reels per type) comparing recall and precision against Wanderlog. Produce a short compliance report."
**Done when:** checklist all ticked except items needing humans (lawyer, Meta review); TestFlight build; benchmark report written.

## Cut order if the eight weeks slip
1. Google Maps export link  2. Read-only day view polish  3. Dark mode  4. Budget tab beyond per-meal totals.
Never cut: attribution, verified-only, text-only upload, delete-my-data, the paywall rules (first plan before paywall).

## Moved to v1.1 (does not fit in eight weeks)
- **Route optimisation** (best order for a day with total time and distance): needs a travel-time matrix and a solver; does not fit alongside M4–M5.
- **Offline read-only trips (Pro):** trip data is stored locally in SwiftData and readable offline anyway, but map tiles cannot be cached with MapKit, and the Pro gating and download UX do not fit. Ship "trip text works offline" in M4 and sell true offline in v1.1 (map solution to be decided).
- **Share link then tripmates**, booking prompts with affiliate disclosure, files import (PDF, Word, text), lists copied from Maps, text pasted from a chatbot (all already v1.1 in the PRD).
- Later (unscheduled): steps / walking goal mode, expense splitting, group voting, journal, creator-permissioned trips, Android.

## Human-only tasks
Apple Developer + App Group IDs, Meta app review (oEmbed Read, only if the lawyer signs off on reading captions with it),
lawyer review, Kie.ai & Anthropic keys in backend secrets, App Store listing/privacy labels, App Store Connect subscription products and UK/US prices,
agreeing a sample reel (we use a synthetic fixture until a creator agrees), choosing the opening-hours data source.
