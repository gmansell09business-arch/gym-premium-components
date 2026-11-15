# Reel→Itinerary: business handover (paste this into a new chat)

Date: 2026-11-15. Status: product designed, build not started. Purpose of this file: give a marketing / ASO / business-plan chat everything decided so far, with facts separated from hypotheses.

**How to read the labels.** `[Decided]` = chosen by us. `[Fact]` = from a screenshot or source we saw. `[Hypothesis]` = our guess, needs validating. `[Unverified]` = could not be confirmed.

---

## 1. One-paragraph pitch
An iPhone app. The user shares a travel reel/post (TikTok, Instagram, YouTube) to the app. The app reads the caption, on-screen text, voiceover and (optionally) comments, finds every place mentioned, checks each one against the map, and builds an editable day-by-day itinerary with a route map, travel times, meals, budget and links to reviews/menus. Name: not decided (working title "Reel to Itinerary").

## 2. The problem and the customer
- People save travel content and never turn it into a plan; places are scattered across caption, text overlays, voiceover and comments. `[Hypothesis]`
- Target: leisure travellers who save creator content (Gen Z / millennials), couples and friend groups planning city breaks and food trips. `[Hypothesis]`
- Wanderlog's top markets per Sensor Tower: US, UK, Australia. `[Fact]` Wanderlog's top personas include Hotel Hoppers, Frequent Car Renters, Theme Park Goers, Fine Diners (US, Oct 2026). `[Fact]`

## 3. How it works for the user
1. Share a reel to the app from the iOS share sheet (a link arrives). `[Decided]`
2. Instant read of the caption; a checklist shows what was read and what is missing (caption, on-screen text, voiceover, comments). `[Decided]`
3. If something is missing the app offers: add a screen recording, add screenshots, or paste the caption. `[Decided]`
4. On-device OCR + speech-to-text read the recording; only extracted text leaves the phone. `[Decided]`
5. Candidates are verified on the map; ambiguous ones ask the user to pick; unverified ones are never auto-added. `[Decided]`
6. Confirmed places merge into a trip (multiple reels → one trip), grouped into days with routes and travel times. `[Decided]`
7. Each place links out to Google Maps, Apple Maps, reviews, menu/website and booking, and credits the creator. `[Decided]`

## 4. Why this approach (the legal position in plain English)
Not legal advice; get a tech/IP lawyer before public launch. `[Unverified]` for any specific jurisdiction.
- The share sheet only gives a **link**, not the video. `[Fact]` (to be re-tested on device)
- **Low-risk route we chose:** official oEmbed (TikTok reliable; Instagram needs Meta app review, business verification and had field changes in 2025), text the user pastes, and screenshots/recordings the user supplies, read on-device. `[Decided]`
- **We will not:** download videos server-side, log in to platforms, crawl profiles, use scraping vendors, store creator media or republish captions. `[Decided]`
- US case law is more favourable to scraping public data than commonly assumed (Meta v. Bright Data, 2024) but it is one district-court ruling, not settled, and does not cover UK/EU rules. `[Fact, summary]`
- Platform dependency (API/terms changes) is a bigger ongoing risk than lawsuits; the user-supplied recording path protects against it. `[Hypothesis]`
- YouTube is the easiest platform to support officially (Data API for description and comments; quotas and retention rules apply). `[Unverified]` on current policy details.
- Review data: Google Places requires attribution and limits caching (store place IDs only); Tripadvisor has strict display rules; Tabelog has no verified public API, so link out only. `[Fact]` for Google and Tripadvisor; `[Unverified]` for Tabelog's terms.
- Attribution on every stop and a link back to the creator's post. `[Decided]`
- Staged legal plan: prototype and private TestFlight need no lawyer; before public launch do a scoped one-off lawyer review (ingestion approach, privacy policy, terms, attribution, review-data use, incorporation jurisdiction). `[Decided]`

## 5. Competitive landscape
**Wanderlog (the benchmark).** `[Fact]` from Sensor Tower screenshots (third-party estimates, Oct–Nov 2026):
- 287K downloads and $276.5K revenue in last 30 days (about $1 revenue per download), revenue per download all time $1.10, ~158K average daily users, ranked #106 in US Travel downloads, 5M website visits per month, 78,425 App Store ratings, 4.9 rating claimed in their ads. Monetisation: free, in-app purchases, subscriptions.
- Added "Import from anywhere: paste a link or share reels to automatically create an itinerary" in App Store release 2.225 (14 Oct 2026). It is only in release notes: not in the homepage hero, and the two ad videos we saw did not demo it.
- Homepage positioning: "One app for all your travel planning needs".
- Ads run on Instagram, YouTube and Facebook in creator-style (hand-held phone, "I just found this" hooks), several started late Oct 2026.
- We could not open wanderlog.com from our sandbox; how their import works (server fetch vs oEmbed) is unknown. `[Unverified]`

**Smaller apps already doing share-sheet import** (self-reported store listings; search results Nov 2026): ReelTravel, Meily, Rhyme (formerly Roamy), Triply, PlanPin, Itinify, Wingman City Guide, TripTok, Somedays, Routewise. Others named from memory, not verified: Mindtrip, Layla, TripIt, Tripadvisor, Google Maps lists. `[Unverified]`

**Conclusion:** "share a reel, get a trip" is table stakes. The edge has to come from accuracy, trust, planning intelligence and distribution. `[Hypothesis]`

## 6. Planned differentiators (edges)
1. **Trust and accuracy:** show evidence per stop ("seen on screen at 0:14", "from pinned comment"), only verified places added, user corrections improve extraction. `[Decided]`
2. **Comments as a source** (pinned creator comments often hold the full list), via user screenshots. `[Hypothesis]` that competitors under-serve this; needs checking.
3. **Reality checks:** opening hours, closed days, reservation needed, travel time, "this day is not doable". `[Decided]`
4. **Budget per meal**, running trip total, cheaper-nearby swaps. `[Decided]`
5. **Steps/walking goal mode** and walk-aware routing; HealthKit read on-device only. `[Decided]`
6. **Meals for each route**, with "suggested by us" visibly separate from the creator's picks. `[Decided]`
7. **Creator-permissioned trips:** creators submit or approve their own itinerary via a link in bio ("Open this trip in the app"). Licensed content, viral loop, revenue-share potential. `[Hypothesis]`
8. **On-device privacy as a brand claim:** "your saved reels never leave your phone". `[Decided]` (true only while we keep processing on-device)
9. **Saved-place nudges** near you, **Plan B** for rain, **menu translation** (Japan), **group voting**. `[Hypothesis]`
10. **Shareable trip posters** (art via Kie.ai) so every trip markets the app. `[Hypothesis]`
11. **Review layer:** show Google/Tripadvisor ratings side by side, unmodified and attributed, plus first-party "saved by / would go again" signals; no blended score until terms are checked. `[Decided]`

## 7. Product scope and design status
**MVP:** share extension; oEmbed + paste caption + user-supplied media; on-device OCR/speech; verification; review inbox; trip timeline + map; day clustering; attribution; delete-my-data. `[Decided]`
**Out of scope (legal):** profile/account import, background crawling, downloading platform media, logging in to platforms, storing creator media.

**Design canvas (Claude Design), 40 artboards, private link:** https://claude.ai/artifact/M45SQBUpsEHoCUdMcGnieP (screens listed by title; contents not individually reviewed here).
Core: 1 Import card, 2 Review places, 3 Trip map, 4 Place card, 5 Trips list, 6 Day plan, 7 Meals per route, 8 Share-back poster. Capture: 9 Capture helper, 10 reading recording, 11 recording deleted, 12 Building your trip. Editing: 13 Edit day, 14 Add to day, 15 Share sheet, 16 What Verified means. Onboarding 1–4. 17 Settings and privacy. Taste: 18 infer from reel, 19 party and pace, 20 budget feel, 21 interests. Intelligence: 22 Budget, 23 Stay base area, 24 Excursions, 25 Why is this here, plus an intelligence components sheet. State variants for import, review, trip, day and place.
An earlier 4-screen canvas also exists: https://claude.ai/artifact/QgrULd5i1DGQD69NZ2EaKN (superseded).
Visual direction so far: teal (#0B6E6E) accent, ink navy, Space Grotesk + Inter, day colours violet/orange/teal; deliberately different from Wanderlog's orange. Dark mode not designed yet.

## 8. Build plan and effort
Eight-week plan (M0 scaffold → M6 compliance and TestFlight): share-extension caption path first, then on-device recording import, trips/itinerary, art and polish, compliance. A built-in recorder (ReplayKit broadcast extension) is a phase-2 option; MVP uses the iOS built-in screen recorder + "Import latest recording". `[Decided]`
Stack: SwiftUI, SwiftData, App Group, MapKit, Vision, Speech; small TypeScript backend as an LLM proxy (Claude API with structured output); Kie.ai for art; project generated with XcodeGen. Claude Code builds the logic on Linux and the app target on a Mac.
Human-only tasks: Apple Developer account and App Group IDs, Meta app review for oEmbed, lawyer review, API keys on the backend, App Store listing and privacy labels.

## 9. Monetisation (starting hypotheses)
- Free tier: about 3 reels per month; Pro: unlimited reels, multiple trips, offline maps, export. `[Hypothesis]`
- Affiliate booking links only with clear disclosure; creator revenue share later. `[Hypothesis]`
- Benchmark: Wanderlog earns roughly $1 per download over 30 days; room for a stronger paid tier if the product is clearly better. `[Hypothesis]`

## 10. Success metrics (from the PRD) `[Hypothesis]`
- At least 70% of shared reels yield 1+ verified place; median share-to-reviewed-list under 60 seconds.
- At least 40% of users shown the recording prompt complete it.
- Under 5% of accepted places later deleted as wrong.
- A competitor benchmark (about 10 reels each across caption-rich, on-screen-text-only, voiceover-only, carousel) to measure recall and precision against Wanderlog and others before building much.

## 11. Inputs for the marketing, social and ASO chat
**Positioning candidates `[Hypothesis]`:** "Turn any travel reel into a real plan", "Every place from the reel, checked and mapped", "Your saved reels, planned".
**Proof points we can honestly claim (once built):** verified-on-the-map places; evidence shown per stop; on-device reading; credit and link back to the creator; budget, steps and meals per route.
**Do not claim:** that it "automatically" reads any reel with one tap (it needs the user's recording for on-screen text and voice); partnership with or endorsement by Instagram, TikTok or YouTube; unmodified third-party review data we are not licensed to show.
**Social content ideas `[Hypothesis]`:**
- 15-second screen-recording demos: share a reel, watch the checklist fill, get a mapped day. Wanderlog's ads use hand-held-phone creator style, so differentiate with the "evidence per stop" and "budget and steps" moments.
- "I fed 5 viral reels into an app" creator-style comparisons; before/after of a messy saved folder vs a plan.
- Shareable trip poster as a built-in UGC loop; creator "Open this trip in the app" link-in-bio programme.
- Communities: travel subreddits, TikTok travel creators, city-guide creators; seed creators with early access.
**ASO starting points `[Hypothesis]`, validate with a keyword tool:** themes "reel to itinerary", "TikTok travel planner", "save places from Instagram", "trip planner", "itinerary maker", "map saved places". Apple limits: app name 30 characters, subtitle 30, keyword field 100. Check Apple's metadata guidelines and each platform's brand/trademark rules before putting Instagram, TikTok or YouTube in the name, subtitle or keywords, and avoid anything that implies endorsement.
**Compliance for marketing:** disclose affiliate links and paid creator posts (FTC in the US, ASA/CMA in the UK); keep the privacy claims accurate; follow each platform's ad policies. `[Unverified]` on the specifics, so check.

## 12. Open decisions for the business plan
1. App name, wordmark and icon (use Kie.ai art pipeline for options).
2. Launch markets and company jurisdiction (drives privacy law and the lawyer brief); Wanderlog's top markets are US, UK, Australia.
3. Which platform to lead with: TikTok (reliable oEmbed), YouTube (official API), Instagram (needs Meta approval).
4. Free vs paid split and price points.
5. Whether to pursue creator partnerships early.
6. Budget and team: who builds, who runs the lawyer review and Meta app review, who owns marketing.
7. Whether to include review-aggregator data (Google/Tripadvisor attribution and caching rules; Tabelog link-out only) in v1.

## 13. Repository and files
Repo: `gmansell09business-arch/gym-premium-components`, branch `claude/ios-travel-itinerary-social-6hwtac`, folder `reel-to-itinerary/`:
```
CLAUDE.md                        rules and conventions for Claude Code (legal guardrails inside)
README.md                        index
.claude/settings.json            blocks scraping tools; allows safe dev commands
docs/00-BUSINESS-HANDOVER.md     this file
docs/01-PRD.md                   product requirements
docs/02-ARCHITECTURE.md          data flow, modules, data model, privacy
docs/03-LEGAL-GUARDRAILS.md      allowed / forbidden paths, release checklist
docs/04-BUILD-PLAN.md            milestones M0–M6 with prompts and acceptance criteria
docs/05-ART-PIPELINE.md          Kie.ai art workflow
docs/06-DESIGN-HANDOVER.md       Claude Design ⇄ Claude Code contract (written for the 4-screen canvas; needs updating to the 40-screen canvas)
spec/extraction.schema.json      JSON schema for the place-extraction step
spec/extraction.prompt.md        system prompt for extraction
spec/design-tokens.json          colours, type, spacing (light values; dark not designed)
design/reference/                empty; for exported 3x PNGs of canvas screens
```
Known gaps: handover and tokens not yet synced to the 40-screen canvas; no reference PNGs exported; no dark mode; nothing built yet beyond the planning pack.

## 14. Sources used for the facts above
Sensor Tower and App Store screenshots supplied by the owner (Nov 2026); Meta developer pages on oEmbed Read; TikTok developer docs on oEmbed; Google Places policies; Tripadvisor Content API display requirements; court-ruling summaries on Meta v. Bright Data; app-store and Product Hunt listings for the smaller competitors. Details were summarised from search results, so verify before relying on any single claim.
