# Architecture

```
[IG/TikTok share] ─URL/media─▶ Share Extension ─App Group─▶ Host App
                                                          │
         ┌────────────────────────────────────────────────┤
         ▼                      ▼                         ▼
   oEmbed fetch           Vision OCR (frames)      Speech (audio)    ← on-device, media deleted after
   (caption, author)      sample 1–2 fps, dedupe   timestamps
         └───────────────┬──────────┴───────────────┬─────┘
                         ▼ text only
                  Backend LLM proxy ──▶ Claude (structured JSON, schema-validated)
                         ▼
                  ItineraryCore: normalise, dedupe, drop low-confidence
                         ▼
                  MapKit MKLocalSearch verify (city-scoped)
                         ▼
                  Review Inbox ─▶ Trip (SwiftData) ─▶ Day clustering ─▶ Map/Export
```

## Modules
- **ItineraryCore (Swift Package, Foundation-only)**: `Candidate`, `Place`, `Trip`, `Day`; schema decoding;
  `PlaceDeduper`, `DayClusterer` (explicit "Day N" wins, else geo + time-of-day), `ConfidenceRanker`.
  Protocols: `OEmbedClient`, `TextRecognizer`, `Transcriber`, `PlaceResolver`, `ExtractionService`.
- **App (SwiftUI)**: adapters implementing the protocols with Vision, Speech, MapKit, PhotosUI; views; SwiftData store.
- **ShareExtension**: validates payload, writes to App Group container, opens host app. No heavy work.
- **Backend (TypeScript)**: `POST /extract` (text in → schema JSON out; auth via App Attest/DeviceCheck token;
  rate limit; no body logging), `POST /art/generate` (internal/dev only, Kie.ai proxy).

## Data model (persisted)
`Trip(id,title,startDate?)` → `Day(index)` → `Stop(placeRef, type, timeOfDay, note, confidence, verified)`
`PlaceRef(mapkitID|placesID, name, lat, lon, city)` · `Source(url, platform, creatorHandle, addedAt)`
No media blobs. Transient processing files live in `tmp/` and are deleted in a `defer`/on failure.

## Privacy
On-device OCR/ASR; only text sent out; backend does not log payloads; delete-all-data in Settings;
privacy manifest + App Store nutrition labels reflect text-only transfer.

## Failure handling
oEmbed unavailable → fall back to paste/recording prompt. Zero places found → show how-to, never fabricate.
LLM schema violation → one repair retry, then show "couldn't read this one".
