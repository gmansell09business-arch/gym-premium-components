# CLAUDE.md — Reel→Itinerary (iOS)

Read this first, every session. Then read `docs/03-LEGAL-GUARDRAILS.md` before touching any ingestion code.

## What we're building
An iOS app. User shares an Instagram/TikTok reel or post to the app (share sheet). We extract places
(restaurants, hotels, activities, areas) and the creator's day-by-day structure from **caption text,
on-screen text and spoken audio**, verify each place with MapKit, and build an editable itinerary.

## Non-negotiable rules (legal/safety)
1. **No scraping.** Never write code that downloads video/media from instagram.com / tiktok.com
   (or their CDNs), logs in to those platforms, automates their apps/webviews, or crawls profiles.
   Do not add yt-dlp, instaloader, youtube-dl, gallery-dl, Apify/BrightData-style actors, headless
   browsers aimed at those sites, or reverse-engineered/private endpoints. (`.claude/settings.json` denies them.)
2. **Only three input paths:** (a) the shared URL + official **oEmbed** (caption/author/thumbnail),
   (b) text the user pastes, (c) screenshots / screen recordings **the user supplies** via share sheet or photo picker.
3. **OCR + speech run on-device** (Vision, Speech/SpeechAnalyzer). Frames and audio are deleted after extraction.
   Only extracted *text* may leave the device (to our LLM proxy).
4. **Store facts, not content.** Persist: place name, type, city, day, note (our paraphrase), confidence,
   MapKit/Places ID, source URL, creator handle (for attribution). Never persist video, audio, frames,
   thumbnails, or verbatim captions beyond the processing session.
5. **Every stop shows attribution + link back** to the source post.
6. **No bulk/profile features** ("import whole account", "follow creator"). One item at a time, user-initiated.
7. Secrets (LLM key, Kie.ai key, Meta token) live on the backend only. Never in the app bundle or repo.
8. Verified-only output: a place that doesn't resolve via MapKit is shown as "unverified" and never auto-added.

If a task seems to require breaking a rule above, stop and ask the user.

## Environment note
Cloud Claude Code runs on Linux: it **cannot build iOS**. Split the code so most logic is testable anywhere:
- `ItineraryCore/` — Swift Package, **no Apple-only imports** (Foundation only). Models, extraction-schema
  decoding, day clustering, dedupe, ranking. `swift test` works on Linux and macOS.
- `App/` — SwiftUI app + Share Extension + adapters (Vision, Speech, MapKit, PhotosUI). Built on a Mac
  (`xcodegen generate && xcodebuild ...`). Adapters sit behind protocols defined in `ItineraryCore`.
- `Backend/` — small TypeScript (Hono/Cloudflare Workers or Node) LLM proxy + Kie.ai proxy. `npm test` works anywhere.

## Tech decisions
- iOS 17+ (SpeechAnalyzer path if iOS 26 available), SwiftUI, SwiftData, App Group for extension handoff.
- Share Extension is thin (≈120 MB limit): save payload to App Group, open host app, process there.
- LLM: Claude API via backend, structured output matching `spec/extraction.schema.json`.
  Use the `claude-api` skill for model IDs/params; don't hardcode from memory.
- Project generated with XcodeGen (`project.yml`) so it's diffable text.
- Style: Swift concurrency (async/await), no force unwraps, `os.Logger` (never log captions or transcripts).

## Workflow
- Work through `docs/04-BUILD-PLAN.md` one milestone at a time; each has acceptance criteria. Don't skip ahead.
- TDD for `ItineraryCore` and `Backend`. Golden-file tests use only synthetic fixtures in `spec/fixtures/`
  (hand-written text, never real scraped captions).
- Commit small, conventional messages. Do not open PRs unless asked.
- Before finishing a milestone: run tests, then re-check the rules above against the diff.

## Connectors available
- GitHub MCP (repo, PRs, CI), Google Drive (specs/notes), Claude Docs (shared docs).
- **Kie.ai** for art generation — see `docs/05-ART-PIPELINE.md`. Design-time/brand assets only.

## UI work
Building any screen or component? Read `docs/06-DESIGN-HANDOVER.md` first. Tokens come only from
`spec/design-tokens.json` (generate `Theme.swift`; never hard-code colours, sizes or fonts). View, component
and string-key names must match the handover. Snapshot-test against `design/reference/` before wiring real data.
