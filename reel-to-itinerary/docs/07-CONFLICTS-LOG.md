# Conflicts and gaps log (2026-11-15, after PRD v2 sync)

Found while aligning docs to `01-PRD.md` v2. "Resolved" means the docs were changed. "Open" needs a decision.

## Resolved in this pass
1. **Privacy claim.** `00-BUSINESS-HANDOVER.md` said "your saved reels never leave your phone". Replaced with the PRD wording ("Your videos never leave your phone. Only the text we read from them is sent, to find the places."). Same sentence now in `03-LEGAL-GUARDRAILS.md`.
2. **Instagram oEmbed.** `03` listed it as an allowed path and the checklist said "Meta app review". Now: gated by legal sign-off, flag off by default, Instagram supported from day one through user-supplied capture.
3. **Prices.** `00` had only generic price ideas; replaced with the PRD's free/Pro split and price tests.
4. **Build plan.** `04` did not cover the Import preview, sample reel, reality checks, budget, onboarding, paywall, dark mode or trip tabs. Restructured; v1.1 list and cut order added.
5. **Dark tokens.** Were null; now provisional placeholders (`$darkStatus`), contrast unchecked.

## Open: needs a decision
1. **Opening-hours source (blocks M4).** The PRD MVP needs opening hours and "closed day" checks, but Google Places is still an open question (licence, attribution, caching), and I do not believe MapKit exposes opening hours (unverified). Decide the source before M4, or drop closed-day checks from the MVP.
2. **Budget data.** PRD wants budget per meal. Price-level data is unverified for MapKit and for Google fields. The build plan uses creator-stated and user-entered prices plus estimate bands labelled as estimates; confirm that is acceptable.
3. **Photos.** PRD says "photo if licensed" in the Import preview; `CLAUDE.md` rule 4 forbids persisting thumbnails and `03` says never show creator media. Working rule: place photos come only from the map provider (with its attribution), never from creator thumbnails or frames. Add that to `CLAUDE.md` if agreed.
4. **YouTube.** PRD says "caption or description via official oEmbed / API". oEmbed does not return the description (to my knowledge); the YouTube Data API does, with quotas and data-retention rules. `03` has no YouTube terms entry yet.
5. **Sample reel.** PRD makes it MVP but asks whose reel we may use. The plan uses a synthetic fixture; confirm that a synthetic sample is acceptable for the first-run experience.
6. **Meta oEmbed wording.** "Meta describes oEmbed Read as for front-end views" came from the owner's PRD; earlier research found Meta describing it as embed HTML plus basic metadata for public posts. Consistent, but verify against Meta's current reference before telling a lawyer.
7. **Capacity.** MVP plus the chosen v1.0 items is heavy for eight weeks (see cut order in `04`). Offline needs a map-tile solution that MapKit does not provide (unverified); moved to v1.1 with route optimisation.
8. **Offline wording.** PRD lists "offline read-only trips (Pro)" in v1.0; the plan ships trip text offline in M4 (free, because it is local data) and moves paid offline to v1.1. Confirm the Pro gating.

## Docs that still lag the PRD (not changed because they were not in the request)
- `02-ARCHITECTURE.md`: still says "Review Inbox", no feedback endpoint (thumbs up/down needs a text-only `/feedback`, check privacy wording), no StoreKit/paywall, no offline or route optimisation, no Instagram-flag note.
- `CLAUDE.md`: rule 2(a) lists "shared URL + official oEmbed" without the Instagram legal gate; the new "no ad/social-login SDKs" and "no server-side Reddit fetch" rules live only in `03`. Consider copying them into the non-negotiable rules.
- `06-DESIGN-HANDOVER.md` sections 1 to 11 still describe only the original four screens; the 40-artboard canvas was mapped by title only.
- `05-ART-PIPELINE.md`: unchanged; onboarding and paywall art may need new prompts.

## Facts I could not verify
Wanderlog details in the PRD (screenshot import, timestamped quotes, creator credit, onboarding paywall, dark mode and offline as Pro, UK price £30.99 per year or £2.57 per month with a 7-day trial) come from the owner's findings; I could not open wanderlog.com from the sandbox.

## Design canvas vs PRD
- Four Taste screens and four onboarding screens vs a PRD limit of three onboarding questions.
- `23 Stay` and `24 Excursions` are not in PRD v2 scope.
- No paywall, sample reel, dark mode, trip tabs, read-only day view or Google Maps export sheet seen by title.
