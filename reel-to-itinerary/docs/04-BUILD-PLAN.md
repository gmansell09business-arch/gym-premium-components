# Build plan (milestones for Claude Code)

Do one milestone per session. Each ends with passing tests + a rules check against `CLAUDE.md`.

## M0 — Scaffold (day 1)
**Prompt:** "Read CLAUDE.md and docs/02-ARCHITECTURE.md. Scaffold `ItineraryCore` (Swift Package, Foundation-only),
`Backend` (TypeScript, Hono, vitest), and `App/project.yml` for XcodeGen with an app target and a Share Extension
sharing an App Group. Add CI (GitHub Actions: `swift test` on macOS, `npm test` on Linux). No feature code yet."
**Done when:** both test suites run green (empty), `xcodegen generate` produces a project that builds on a Mac.

## M1 — Extraction core (week 1)
**Prompt:** "Implement Codable models from `spec/extraction.schema.json`, a validator, `PlaceDeduper`, and
`ConfidenceRanker` in ItineraryCore with tests using hand-written fixtures in `spec/fixtures/`. Then build
Backend `POST /extract` that calls the Claude API with `spec/extraction.prompt.md`, validates against the schema,
retries once on violation, and never logs request bodies. Use the claude-api skill for current model IDs."
**Done when:** fixture tests pass; schema-invalid LLM output is rejected; a contract test mocks the LLM.

## M2 — Caption path end-to-end (week 2)
**Prompt:** "Implement `OEmbedClient` (TikTok public oEmbed; Instagram oEmbed behind a feature flag + token),
the Share Extension payload handoff via App Group, and a host-app flow: share URL → oEmbed → /extract →
MapKit verify → Review Inbox. Graceful fallback to a paste-caption sheet."
**Done when:** sharing a link shows verified candidates; unverified ones are flagged, not added; attribution shown.

## M3 — User-supplied media (week 3–4)
**Prompt:** "Add image/video acceptance in the Share Extension and a PhotosUI picker. Implement `TextRecognizer`
(Vision, 1–2 fps frame sampling, near-duplicate frame dedupe) and `Transcriber` (Speech/SpeechAnalyzer,
on-device only, `requiresOnDeviceRecognition = true`). Merge timestamped text, send text only to /extract.
Delete all temp media in `defer` and on error. Add a recording how-to sheet and 'Import latest recording' prompt."
**Done when:** a sample screen recording yields places; a test asserts temp dir is empty afterwards; no network
call carries media.

## M4 — Trips & itinerary (week 5–6)
**Prompt:** "Implement SwiftData Trip/Day/Stop, `DayClusterer` (explicit day wins; else geo clustering + time of day;
opening-hours aware if available), multi-reel merge into a trip, map view with routes/travel times (MKDirections),
drag-reorder, and export (Apple Maps guide, Calendar, share link)."
**Done when:** two reels merge into one 3-day trip with no duplicate stops; edits persist.

## M5 — Art & polish (week 6–7)
**Prompt:** "Follow docs/05-ART-PIPELINE.md: write `Backend/scripts/generate-art.ts` for Kie.ai, generate icon set,
onboarding and empty-state art from text prompts only, record prompts/seeds in `art/prompts/`. Wire into
Assets.xcassets with dark-mode variants."
**Done when:** assets committed, no API key in repo, prompts reproducible.

## M6 — Compliance & launch (week 7–8)
**Prompt:** "Run the release checklist in docs/03-LEGAL-GUARDRAILS.md: grep audit for scraping libs/CDN fetches/secrets,
privacy manifest, delete-all-data flow, App Attest on /extract, rate limits, App Review notes explaining the
user-supplied-media flow. Produce a short compliance report."
**Done when:** checklist all ticked except items needing humans (lawyer, Meta review); TestFlight build.

## Human-only tasks
Apple Developer + App Group IDs, Meta app review (oEmbed Read), lawyer review, Kie.ai & Anthropic keys in
backend secrets, App Store listing/privacy labels.
