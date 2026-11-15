# Design → Code handover (Claude Design ⇄ Claude Code)

Purpose: Claude Design builds the interface once; Claude Code rebuilds it in SwiftUI **1:1** with no
guessing. Every screen, component, token, string and state has one name that is the same in the canvas and in code.

- **Canvas (current, 40 artboards):** https://claude.ai/artifact/M45SQBUpsEHoCUdMcGnieP (private to the owner). Read artboard sources with the Artifact tool: `action: "read"`, that `url`, `path: "project/<Artboard>.dc.html"` or `project/canvas.json`.
  An earlier 4-screen canvas (https://claude.ai/artifact/QgrULd5i1DGQD69NZ2EaKN) is superseded. **Sections 1 to 11 below were written for those first four screens (Main, Review, Trip, Place); section 12 maps PRD v2 to the 40-artboard canvas.** Artboard contents beyond the first four have not been reviewed against this document.
- **Tokens:** `spec/design-tokens.json` is the only source of colours, type, spacing, radii, sizes, shadows.
- **Rules that apply to all UI:** `CLAUDE.md` (attribution on every stop, verified-only, no media stored, on-device OCR).

## 1. The contract

| Claude Design must | Claude Code must |
|---|---|
| Use only tokens from `spec/design-tokens.json`. No literal hex, px or font in artboards. A new value means adding a token first. | Generate `Theme.swift` from the tokens file and never hard-code a value in a view. |
| Name every artboard and component with the names in §3 and §4. | Use the same names for Swift files and types. |
| Draw every state listed in §5 for each screen, not only the happy path. | Implement each state as an enum case on the view model and snapshot-test it. |
| Keep the layout flexible (stacks, grids, gaps), fixed 390×844 is only the artboard frame. | Use SwiftUI stacks, safe areas and Dynamic Type. Verify at 375, 390 and 430 pt wide. |
| Put all copy in the artboard as literal text and keep the string table in §6 in sync. | Move copy to `Localizable.xcstrings` using the keys in §6. |
| Export reference PNGs at 3x after each approved change (§8). | Snapshot-test against those PNGs (§7). |

Unit mapping: 1 CSS px in the canvas = 1 pt in SwiftUI.

## 2. Pixel-to-SwiftUI translation rules
- `padding: 56px 20px 28px` on a root = **safe area + 20 pt sides**. The 56 px top only simulates the status bar and notch. Do not reproduce it.
- `display:flex` column or row with `gap` = `VStack` / `HStack(spacing:)`. `flex-wrap` chip rows = a wrapping flow layout (custom `Layout`).
- `flex:1` spacer = `Spacer(minLength: 0)`. `grid-template-columns: repeat(2, 1fr)` = `LazyVGrid` with two flexible columns.
- Absolute positions appear only for map pins, the map top bar and the bottom sheet. Pins use map coordinates in the app, not pixel offsets.
- Bottom sheet on the Trip screen = `.presentationDetents` sheet or a custom draggable sheet over `Map` (peek 372 pt, expand to full). Corner radius `sheet`.
- Text sizes use the `textStyle` hint in `design-tokens.json` so Dynamic Type works, while default size matches the canvas.
- Fonts: bundle Space Grotesk (500, 700) and Inter (400, 500, 600), register in `UIAppFonts`, fall back to the system font.
- Borders, radii and shadows come from tokens. 1 px borders are 1 pt (`lineWidth: 1`), the "needs you" card border is 2 pt.

## 3. Screens (artboard file → SwiftUI view)

| Artboard | Canvas title | SwiftUI view | Purpose |
|---|---|---|---|
| `Main.dc.html` | 1 Import card | `ImportCardView` | After share: shows what was read and what is missing |
| `Review.dc.html` | 2 Review places | `ReviewPlacesView` | Confirm or fix candidates before adding to a trip |
| `Trip.dc.html` | 3 Trip map | `TripMapView` | Days, pins, route, stops with travel times |
| `Place.dc.html` | 4 Place card | `PlaceDetailView` | Attribution, link-outs, reality check, add to day |

Navigation: Share extension → `ImportCardView` → (after capture) `ReviewPlacesView` → "Add N verified places to trip" → `TripMapView` → tap stop → `PlaceDetailView` (push). Close (✕) on the import card dismisses to the Inbox.

### 3.1 ImportCardView
Layout top to bottom, 20 pt side padding, 20 pt gaps:
1. Top bar: close icon button 44×44 circle (surface, 1 pt line), centred source label "Shared from {platform}" (small, muted, weight 500), 44 pt spacer.
2. Heading block, 6 pt gap: eyebrow "Reading your reel" (accent), title1 destination text ("3 days in Lisbon", `text-wrap: balance` = allow 2 lines), caption "Destination detected from the caption · by @{creator}" (muted).
3. `CaptureChecklistCard`: surface card, radius card, 1 pt line, 16 pt horizontal padding, rows separated by 1 pt line. Row = 28 pt status dot + title (bodyStrong) + detail (small, muted). Rows in order: Caption, On-screen text, Voiceover, Comments.
4. "Found so far" label (small, muted, weight 600) + wrapping `PlaceChip`s.
5. Spacer, then actions: primary "Add a screen recording" (52 pt), a row of two secondary buttons "Add screenshots" and "Paste caption" (48 pt, equal width), footnote centred (micro, muted).

### 3.2 ReviewPlacesView
1. Title2 "Review {n} places", caption "{city} · from {k} reel(s) · checked against the map".
2. Filter chips: All, Verified, Needs you (selected chip = ink fill, white text).
3. Scrolling list of `CandidateCard`s (10 pt gap). Spacer. Pinned primary button "Add {n} verified places to trip".

### 3.3 TripMapView
1. Full-bleed map. Map pins: numbered 30 pt circles in the day colour with 3 pt white border and `float` shadow for the selected day, 24 pt plain dots for other days (85% opacity). Route = 5 pt line in day colour, round caps and joins.
2. Floating top: trip summary pill (surface, radius 14, float shadow: title4 "{city}, {n} days", micro muted "{stops} stops · {reels} reels") and a small button "Open in Maps". Under it, `DayChip`s (selected = day colour fill, white text, others surface).
3. Bottom sheet, 372 pt peek: grabber, header row (title3 "Day {n} · {from} to {to}", micro muted duration), then `StopRow`s joined by `TravelConnector`s, then a `RealityCheckBanner` pinned to the bottom of the sheet.
4. Map attribution: show Apple's own, never hide it.

### 3.4 PlaceDetailView
1. Photo header 210 pt (photo from the map provider with its attribution chip "Photo from Apple Maps" bottom-left, back button 44 pt top-left). When no photo: the striped placeholder.
2. Title2 name, caption "{category} · {neighbourhood}", `StatusPill`.
3. `AttributionCard`: eyebrow "Why it's here", body text (our paraphrase), small "Credit: @{creator} · View original" (link, accent, weight 600).
4. "See more": 2×2 grid of `LinkOutButton`s: Google Maps, Apple Maps, Reviews, Menu and website. Footnote "Opens the other service. We don't copy their reviews."
5. `RealityCheckBanner`. Spacer. Primary "Add to Day {n}" + 52 pt square "more" button.

## 4. Component inventory

| Component | SwiftUI type | Variants and rules |
|---|---|---|
| `PrimaryButton` | `Button` + `PrimaryButtonStyle` | 52 pt, accent fill, onAccent text, radius button. Pressed = accentPressed. Disabled = 40% opacity. |
| `SecondaryButton` | `SecondaryButtonStyle` | 48 pt (44 pt in sheets/cards), surface fill, 1 pt lineStrong border, ink text. |
| `IconButton` | `Button` | 44×44 circle, surface, 1 pt line. Needs `accessibilityLabel`. |
| `StatusDot` | `View` | 28 pt circle. `.ok` (okBg/okFg "✓"), `.attention` (warnBg/warnFg "!"). Use SF Symbols `checkmark` and `exclamationmark`. |
| `CaptureChecklistRow` | `View` | Inputs: `CaptureSource` (caption, onScreenText, voiceover, comments), `CaptureStatus`. |
| `PlaceChip` | `View` | Pill, surface, 1 pt line, body size 14, 8×12 pt padding. |
| `StatusPill` | `View` | `.verified` (okBg/okFg), `.pickOne` (warnBg/warnFg), `.unverified` (neutralBg/neutralFg). 12 pt, weight 600, 4×10 pt padding. |
| `CandidateCard` | `View` | Variants: `.verified`, `.ambiguous(options)`, `.unverified`. Verified/ambiguous differ by border: verified = 1 pt line, ambiguous = 2 pt warnBorder, unverified = 1 pt dashed lineStrong. |
| `SourceBadgeText` | `Text` | Evidence line: "From the caption", "On-screen text · {m:ss}", "Heard in voiceover · {m:ss}", "From a pinned comment". |
| `FilterChip` | `View` | Selected = ink fill, white text. Others surface + 1 pt line. |
| `DayChip` | `View` | Selected = day colour fill, white text. 9×16 pt padding, 13 pt weight 600. |
| `MapPin` | `MapAnnotation` content | `.selectedDay(number, day)` 30 pt, `.otherDay(day)` 24 pt dot. |
| `RouteLine` | `MapPolyline` | 5 pt, day colour, round cap and join. |
| `StopRow` | `View` | 28 pt numbered badge in day colour, bodyStrong name, micro muted "{slot} · {source}". |
| `TravelConnector` | `View` | 2 pt dashed lineStrong rule, 14 pt from badge centre, 24 pt left text inset, micro muted "{n} min by tram/walk". |
| `RealityCheckBanner` | `View` | warnBg, warnText, radius control (12), 12 pt padding, small text. |
| `AttributionCard` | `View` | surface, 1 pt line, radius 14, 14 pt padding. |
| `LinkOutButton` | `Button` | 48 pt secondary, opens `Link` destination, label never says "reviews from X" unless attributed. |
| `BottomSheet` | `View` | radius 24 top corners, `sheet` shadow, grabber 40×5 lineStrong. |

Each component gets a SwiftUI `#Preview` per variant and a snapshot test.

## 5. States to design (artboards still to add)

| Screen | States |
|---|---|
| ImportCardView | `reading` (spinner on rows), `partial` (shown), `allRead`, `noPlacesFound` (how-to + paste), `oEmbedUnavailable` (paste/record prompt), `offline` |
| ReviewPlacesView | `loading`, `list` (shown), `allVerified`, `empty`, `verifyFailed` (map lookup error, retry) |
| TripMapView | `noRoute` (single stop), `routeLoading`, `mapUnavailable`, `dayEmpty`, `warning` (shown), `offline` |
| PlaceDetailView | `noPhoto`, `hoursUnknown`, `alreadyInTrip`, `linkOutsUnavailable` |
| All | Dynamic Type XXL, VoiceOver order, Reduce Motion, dark mode (tokens `dark` values to be designed), landscape optional |

## 6. Screens still missing (priority order for Claude Design)
1. **Capture helper** (3 steps: record, play with sound, scroll comments) + "Import latest recording" + progress and "deleting recording" confirmation.
2. **Trips list / Inbox** with processing items.
3. **Settings and privacy** (what we send, delete all data, source rules).
4. **Budget per meal and steps target** overlays on the day sheet (see ideas doc).
5. **Meals per route** (breakfast/lunch/dinner slots, "suggested by us" labelled separately from creator picks).
6. **Share-back poster** (Kie.ai art).

## 7. String table (keys → copy)
Use `screen.element` keys, e.g. `import.title.reading` = "Reading your reel". Initial set (copy exactly from the artboards):

| Key | Copy |
|---|---|
| `import.eyebrow` | Reading your reel |
| `import.source` | Shared from %@ |
| `import.destination.caption` | Destination detected from the caption · by %@ |
| `import.row.caption.title` / `.read` | Caption / Read · %d places found |
| `import.row.onscreen.title` / `.missing` | On-screen text / Not captured. Needs a recording. |
| `import.row.voice.title` / `.missing` | Voiceover / Not captured. Record with sound on. |
| `import.row.comments.title` / `.missing` | Comments / Not captured. Pinned comments often list every stop. |
| `import.foundSoFar` | Found so far |
| `import.cta.record` / `.screenshots` / `.paste` | Add a screen recording / Add screenshots / Paste caption |
| `import.privacy` | Text is read on your phone. Recordings are deleted afterwards. |
| `review.title` | Review %d places |
| `review.subtitle` | %@ · from %d reel(s) · checked against the map |
| `review.filter.all` / `.verified` / `.needsYou` | All %d / Verified %d / Needs you %d |
| `review.pill.verified` / `.pickOne` / `.unverified` | Verified / Pick one / Unverified |
| `review.unverified.note` | Not added until you confirm a match |
| `review.cta.add` | Add %d verified places to trip |
| `trip.title` / `.meta` | %@, %d days / %d stops · %d reels |
| `trip.openMaps` | Open in Maps |
| `trip.day` | Day %d |
| `trip.travel.tram` / `.walk` | %d min by tram / %d min walk |
| `trip.warning.closedDay` | Check: the creator visits %@ on a Monday. Some museums nearby are closed that day. |
| `place.why` | Why it's here |
| `place.credit` | Credit: @%@ · View original |
| `place.seeMore` | See more |
| `place.link.google` / `.apple` / `.reviews` / `.menu` | Google Maps / Apple Maps / Reviews / Menu and website |
| `place.linkoutNote` | Opens the other service. We don't copy their reviews. |
| `place.reality` | Reality check: popular spots like this get busy around midday. Opening hours come from the map and may change. |
| `place.cta.add` | Add to Day %d |

Rules: copy is paraphrased by us, never the creator's verbatim text. Never show a rating or review text without the provider's required attribution.

## 8. View-model contract (from `ItineraryCore`, Foundation-only)
Views bind to plain structs so they can be previewed with fixtures.

```swift
enum CaptureSource { case caption, onScreenText, voiceover, comments }
enum CaptureStatus { case reading, read(placeCount: Int), missing, unavailable }

struct ImportCardModel {
  var platform: String            // "TikTok" | "Instagram" | "YouTube"
  var creatorHandle: String?
  var destinationTitle: String?   // "3 days in Lisbon"
  var rows: [CaptureSource: CaptureStatus]
  var foundNames: [String]
}

enum CandidateStatus { case verified, ambiguous([PlaceOption]), unverified }
enum EvidenceSource { case caption, onScreenText(t: TimeInterval), voiceover(t: TimeInterval), comment }
struct CandidateModel: Identifiable {
  let id: UUID; var name: String; var category: String; var area: String?
  var status: CandidateStatus; var evidence: EvidenceSource; var dayHint: Int?
}

struct StopModel: Identifiable { let id: UUID; var number: Int; var name: String
  var slot: String; var source: EvidenceSource; var legToNext: TravelLeg? }
struct TravelLeg { enum Mode { case walk, tram, drive }; var mode: Mode; var minutes: Int }
struct DayModel: Identifiable { let id: UUID; var index: Int; var title: String
  var duration: TimeInterval; var stops: [StopModel]; var warning: String? }
```

Fixtures for previews live in `spec/fixtures/` (synthetic, never real captions). The Lisbon names in the canvas are sample content only.

## 9. Parity tests (Claude Code)
1. **Snapshot tests** (`swift-snapshot-testing` or Xcode image comparisons) of each view in each state at 390 pt wide, against `design/reference/<Screen>-<state>@3x.png` exported from the canvas. Tolerance: perceptual 98% (fonts and map tiles excluded: mask the map and photo regions).
2. **Token test:** a unit test loads `spec/design-tokens.json` and asserts `Theme` values equal it (colour hex, type size, radius, space).
3. **Layout checks** at 375 and 430 pt wide and Dynamic Type XXL: no clipped text, no horizontal scroll, touch targets at least 44 pt.
4. **Accessibility audit:** every `IconButton` has a label, VoiceOver reads each `CaptureChecklistRow` as "{title}, {status}", contrast at least 4.5:1 for text.
5. **Rules audit:** no view renders third-party ratings or reviews without attribution, and every stop shows credit and a link back.

## 10. Build order for Claude Code
1. Generate `Theme.swift` and bundle fonts. Token test green.
2. Components (§4) with previews and snapshots, no screens yet.
3. Screens in order: `ImportCardView`, `ReviewPlacesView`, `PlaceDetailView`, `TripMapView`, each with all states from §5 using fixtures.
4. Wire to real data only after the screens match the references.

## 11. Open items
- Dark mode palette: provisional placeholder values are in `spec/design-tokens.json` (`$darkStatus`); Claude Design must confirm or replace them and check 4.5:1 contrast.
- Real map styling: the canvas map is a stand-in, so match Apple Maps default with the day colours for pins and route.
- App name, icon and wordmark (Kie.ai art pipeline: see `docs/05-ART-PIPELINE.md`).
- Export reference PNGs at 3x into `design/reference/` after each approved revision.

## 12. PRD v2 design tasks (added 2026-11-15)
Source: `docs/01-PRD.md` v2. Status "exists" means an artboard with that title is in the 40-artboard canvas; it has **not** been checked against the PRD.

| PRD item | Phase | Canvas artboard(s) | Status / task for Claude Design |
|---|---|---|---|
| Import preview (post summary, creator handle + link back, platform; place checklist with select all/none; Verified / Needs check label; source type + quote or timestamp; map with numbered pins; "Add N places to trip" with day/section picker; Undo toast; thumbs up/down with optional reason; ambiguous picker; unverified listed separately and off by default) | MVP | `2 Review places`, `25 Why is this here`, `16 What Verified means`, import state boards | **Rework `Review` into the Import preview.** Add the missing parts: map pins, select all/none, day picker, Undo toast, thumbs feedback sheet, unverified section. |
| Source-type label (caption / on-screen / voiceover / pasted comment) and quote/timestamp on every stop | MVP | `25 Why is this here` | Define a `SourceTypeLabel` component used on Import preview, Place card and Day plan. |
| Sample reel (first-run) | MVP | none seen | **Design:** first-run entry ("Try a sample reel"), result screen, clear "sample" marking. Content must be synthetic. |
| Instagram capture-first variant of the import card | MVP | `1 Import card`, `9 Capture helper` | Variant of the import card for Instagram that leads with the capture helper (paste, screenshots, recording). |
| Onboarding: max three questions (trip type, who with, budget feel), one notification prompt with a reason, no location "Always" | v1.0 | `Onboarding 1-4`, `18-21 Taste` | **Check against PRD:** the canvas has four Taste screens and four onboarding screens; the PRD allows three questions. Consolidate. Add the single notification prompt. |
| Paywall (natural limit: fourth reel in a month, offline, export; after the first plan; at most once per session; annual plan with trial; UK price in pounds) | v1.0 | none seen | **Design:** paywall sheet, free-limit counter ("2 of 3 reels this month"), Pro locks on gated features, restore purchases, price display in the user's currency. |
| Dark mode (free) | v1.0 | none (light only) | **Design dark variants of every screen** using the provisional dark tokens; confirm or replace; check contrast. |
| Trip tabs: Itinerary, Map, Budget, Notes | v1.0 | `3 Trip map`, `6 Day plan`, `22 Budget` | Tabbed trip container; Notes tab is missing. |
| Fast read-only day view (two taps or fewer) | v1.0 | `6 Day plan` | Add a read-only variant that opens without edit mode. |
| Reality checks ("this day is not doable", leg over 45 min, closed day) | MVP | `3 Trip map` (warning banner) | Add states for each check type and a "leg too long" marker on `TravelConnector`. |
| Budget per meal and trip total; meals "suggested by us" | MVP | `22 Budget`, `7 Meals per route` | Confirm labels: every price shows "estimate" and its source; suggested meals visibly separate from creator picks. |
| Google Maps export link (Pro) | v1.0 | `14 Add to day`, `15 Share sheet` | Add an export sheet with the Pro lock and a "split long days" note. |
| Offline read-only trips (Pro) and route optimisation | v1.1 (moved) | none | Not for the eight-week build; design later. |
| Stay base area, Excursions | not in PRD v2 | `23 Stay`, `24 Excursions` | **Out of PRD scope:** decide whether these are Later or cut. |

### Reference: Wanderlog onboarding (observed in the owner's screenshots; reference for flow only, do not copy visuals)
- Destination step: heading "Where are you traveling?", search field with placeholder "e.g. Paris, Tokyo, Hawaii", a list of suggested destinations with flag emoji (New York City, London, Paris, Tokyo, Oahu, Scotland, Iceland, Bali), a back button and a segmented progress bar at the top, a Continue button pinned to the bottom that is pale (disabled) until a destination is chosen.
- After choosing: a large photo card with the destination name, a close icon, an "Add more" link, Continue becomes active.
- Dates step: heading "Select dates", a scrolling month calendar, today highlighted, range selection with the status line "Nov 18 – Select end date" then "Nov 18 – Dec 1", Continue and Skip.
- Look: dark red-to-orange gradient background, white type, coral primary button.
- **Implications for us:** our flow is reel-first, so destination and dates are usually inferred from the reel; ask for them only when the reel does not imply them and always allow Skip. Use their pattern ideas (progress bar, pinned Continue, Skip, destination chips) but keep our own palette, type and layout. Their onboarding is destination-first and, per the owner's findings, shows a paywall before the user has built anything; ours must show the first plan first.
