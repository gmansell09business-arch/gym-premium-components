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
- Meta Platform Terms / IG oEmbed: apply for oEmbed Read only if the lawyer agrees (see the note below); respect rate limits.
- TikTok: use public oEmbed only; do not use unofficial APIs.
- Apple: App Review 5.1 (privacy), 5.2 (IP); describe the user-supplied-media flow in review notes.
- Maps: store MapKit/Places IDs; respect Google Places caching limits if used.
- Anthropic usage policies; Kie.ai terms for generated art (see 05).

## Meta oEmbed note (added 2026-11-15)
Meta describes oEmbed Read as a way to embed public Instagram/Facebook content in front-end views. Reading captions
with it to extract places is a different use and **needs legal sign-off before it is switched on**
(verify against Meta's current oEmbed Read feature reference). Instagram support from day one therefore rests on
user-supplied capture (pasted caption, screenshots, screen recording read on-device). Keep the Instagram oEmbed
client behind a feature flag that is **off by default**, and if approved use it for display, not as the only source.

## Additional rules (added 2026-11-15; the forbidden list above is unchanged)
- **No server-side Reddit fetch.** Reddit threads and other web text enter only as text the user pastes or screenshots the user supplies, read on-device.
- **No ad or social-login SDKs** (no advertising/attribution SDKs, no "Sign in with Instagram/TikTok/Facebook/Google" SDKs). Audit dependencies before each release. Claim "no ad tracking" only if the build has none.
- **Privacy wording must match behaviour:** "Your videos never leave your phone. Only the text we read from them is sent, to find the places." Never claim that saved reels never leave the phone.

## Release checklist
- [ ] Lawyer review of ToS/privacy policy
- [ ] Legal sign-off on reading Instagram captions via oEmbed; then Meta app review (otherwise leave the flag off)
- [ ] Privacy manifest + nutrition labels match behaviour
- [ ] Data deletion works end-to-end
- [ ] Attribution/link-back on every stop
- [ ] Grep audit: no scraping libs, no platform CDN fetches, no secrets in repo
- [ ] Dependency audit: no ad SDKs, no social-login SDKs; privacy labels match
- [ ] Grep audit: no server-side Reddit/web fetch of user content
- [ ] Privacy policy, App Store labels and in-app wording use the corrected sentence above
