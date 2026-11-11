# Legal & platform guardrails

> Engineering guidance, **not legal advice**. Get a tech/IP lawyer to review before launch.

## Position
User-initiated, one item at a time, on-device analysis of content the user is already viewing, extracting
facts (place names) and linking back — closer to a read-later app/Live Text than a crawler.
The main risk is **platform ToS/access**, not copyright.

## Allowed paths
| Path | Why |
|---|---|
| Shared URL + official oEmbed | Sanctioned API (IG needs Meta app review for oEmbed Read) |
| User pastes caption | User-supplied |
| User supplies screenshot/screen recording | User-supplied; we never fetch from platform |
| On-device OCR/ASR of user media | No platform interaction |

## Forbidden (enforced in CLAUDE.md + settings.json)
Server-side downloading of reel video; logged-in/automated access; headless browsers on IG/TikTok;
private/reverse-engineered endpoints; third-party scraping vendors; profile/hashtag crawling;
storing/redistributing creator media; verbatim republishing of captions.

## Copyright
Facts aren't protectable; a creator's video, wording and curated arrangement have thin protection.
→ paraphrase, store minimal fields, always attribute + link back, never show creator media in our UI
(embed via official embed if ever needed).

## Privacy (GDPR/UK GDPR/CCPA)
Creator handles and voices are personal data. Transcribe on-device, discard audio/frames, no voiceprints,
no identifying people, minimal retention, user data export/delete, honest privacy policy
("we send extracted text to our processor to identify places").

## Third-party terms
- Meta Platform Terms / IG oEmbed: apply for oEmbed Read; respect rate limits.
- TikTok: use public oEmbed only; do not use unofficial APIs.
- Apple: App Review 5.1 (privacy), 5.2 (IP); describe the user-supplied-media flow in review notes.
- Maps: store MapKit/Places IDs; respect Google Places caching limits if used.
- Anthropic usage policies; Kie.ai terms for generated art (see 05).

## Release checklist
- [ ] Lawyer review of ToS/privacy policy
- [ ] Meta app review for oEmbed
- [ ] Privacy manifest + nutrition labels match behaviour
- [ ] Data deletion works end-to-end
- [ ] Attribution/link-back on every stop
- [ ] Grep audit: no scraping libs, no platform CDN fetches, no secrets in repo
