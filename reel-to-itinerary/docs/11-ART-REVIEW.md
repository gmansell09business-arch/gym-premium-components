# Art review (2026-11-16): first OpenArt outputs

Reviewed: 5 preview sheets (10 destination covers, 4 onboarding illustrations, 4 empty/error illustrations, 1 paywall illustration, 4 app-icon concepts). All are 1200x896 previews, so they are **references, not production files**: get the full-resolution originals from OpenArt. Files: `art/candidates/`, status per asset: `art/manifest.json`.

## Verdict
The set works as a brand base. Style is consistent (flat shapes, teal/navy/violet/orange, grain, a violet route line threaded through each scene, open sky for a title), it matches our tokens, and it respects our legal rules (no faces, no logos, no readable text, no creator media). Quality is high enough to use after clean-up. Weak spots: a few specific images, two style tiers, low resolution, and ownership of AI-generated work (below).

## Per set
| Set | Verdict | Notes and fixes |
|---|---|---|
| **Destination covers (10)** | **Use** | Best part of the kit. Each reads as its city (Lisbon tram and tiles, Tokyo lantern lane and train, Paris tower and river, London bus and clock tower, Rome dome and plaza, Barcelona cathedral and mosaic bench, Kyoto gate and pagoda, New York water tower and bridge, Bali terraces and temple gate, Iceland waterfall and red house). The route line with tiny numbered dots ties them to the product. Issues: they are tall (about 9:19), not the 4:5 asked for, so a 390x220 trip header needs a **new wide version** (cropping a tall image loses the sky space meant for the title). Kyoto and New York lean heavily on browns, drifting from the palette; accept or nudge. Tiny digits on the route dots are noise at small sizes; keep dots plain for headers. |
| **Onboarding (4)** | **Use 1 to 3, regenerate 4** | 1 (hand, phone, share arrow), 2 (pin stamped on a map with a tick) and 3 (map with route, pins and clocks) are clear and on-brand. 4 (phone on a bench, dotted path to buildings) is disconnected and confusing. The "1)" to "4)" labels in the sheet are our numbering; crop them out. Hand in 1 is pale violet and low contrast against the background; fine, or darken. |
| **Empty and error (4)** | **Use 2 to 4 with fixes, regenerate 1** | Tangled route line (error) is the strongest. Magnifier over a blank map (no places) is clear. Paper plane over a cloud (offline) is ambiguous: a plane does not say "no connection"; try a cloud with a crossed-out dashed line or a broken route. The open suitcase (no trips) **reads as a laptop**, replace it. All four are pale and low contrast on light paper; need dark-mode versions. |
| **Paywall (1)** | **Use, with a style decision** | Attractive and clear (map unfolding into a path to a flag). It is more shaded (gradients, glow) than the flat covers, so we now have two tiers. Either regenerate it flat or deliberately keep one "shaded hero" tier for the paywall only. Export without the card drop shadow. Do not use countdown or urgency imagery. |
| **App icons (4)** | **Shortlist 2, redraw by hand** | Seal with a pin (top right): clean, reads as "verified location", ties to our Verified label, ownable. Folded map forming a pin (bottom left): strong silhouette, says map and place, good teal/orange contrast. Pin with a route squiggle (top left): the squiggle reads like a clip or switch. Compass (bottom right): generic and busy at small sizes, **reject**. Test the two finalists at 60, 40 and 29 px on busy home-screen backgrounds. The concepts show rounded squares baked in; Apple applies its own mask, so deliver a full-bleed 1024x1024 square with no transparency. |

## Where each is used
- **Covers:** trip header (Trip home), Trips list cards, share-back poster, App Store screenshots and social posts, onboarding hero.
- **Onboarding 1 to 3:** welcome and how-it-works.
- **Empty and error:** Trips empty state, "No places found", offline, extraction failed (P5 states).
- **Paywall hero:** paywall sheet.
- **Icon:** app icon; the seal can also become the Verified motif in the UI (animation in the motion spec).

## Coverage problem (important)
Reels can be about anywhere, but we cannot generate art per user trip on demand (cost, style drift, review). Plan: a curated library of 30 to 50 popular destinations plus **regional fallback covers** (city, coast, mountains, island, desert, countryside, snow) so any trip gets a good-looking header. Fallback must not imply a wrong place (use generic scenery and a neutral label).

## Specs to request for the real files
| Use | Size |
|---|---|
| App icon | 1024x1024, full-bleed, no transparency, no text |
| Cover, tall (poster, stories, App Store) | 1290x2796 or higher |
| Cover, wide trip header | 1170x660 (3x of 390x220), safe area left clear for a title |
| Share poster | 1080x1350 (4:5) and 1080x1920 |
| Onboarding and empty-state illustrations | at least 1200 px on the long side, transparent or matching background, plus dark variant |

## Legal and ownership (check with your lawyer)
- **Copyright:** US Copyright Office guidance, as I understand it, says material produced entirely by AI without enough human authorship is not protected. That means we may not be able to stop others copying these images. For the **app icon and any wordmark, have a human designer redraw** the chosen concept as a vector so there is human authorship you can protect and register as a trademark.
- **Terms:** read OpenArt's commercial-use terms and the terms of the model used before shipping; keep prompt, model, seed and date for each asset (`art/prompts/`).
- **Trademark:** run a search for the icon and app name (App Store, USPTO/EUIPO/UKIPO) before launch.
- **Landmarks:** illustrated landmarks are fine here; avoid night-time light shows of protected structures and any signage text.
- **Rules unchanged:** text prompts only, no creator thumbnails or frames, no faces, no brand logos.

## Next prompts (regenerations and additions)
Use the style anchor and negative prompt from `10-DESIGN-PROMPTS.md`.
```
Wide covers: [style anchor] [CITY] scene as above, wide 16:9, composition weighted to the bottom half, open sky across the top 40% for a title, route line crossing the lower third
```
```
Onboarding 4: [style anchor] a person-free scene: a phone resting on a stone wall in a sunny square, a dotted path leading from the phone along a street to a small cafe awning, one violet pin above the cafe, square 1:1
```
```
Empty trips: [style anchor] an open leather suitcase with a luggage tag, an empty interior and a small folded map tucked in the lid, resting on the floor, front three-quarter view, square 1:1
```
```
Offline: [style anchor] a cloud with a dashed route line that stops in a gap, a small dotted line continuing on the other side, square 1:1
```
```
Paywall (flat version): [style anchor] a folded map unfolding into a winding path of pins over layered flat hills, a flag at the end, no gradients, vertical 4:5
```
```
Regional fallbacks (one prompt each): [style anchor] generic [city skyline | coastline with a small harbour | snow-capped mountains and a cabin | tropical island with palms | desert dunes and a caravan trail | rolling countryside and a farmhouse | snowy village], a thin violet route line, open sky at the top, tall 9:19
```
```
Dark variants: same prompts with "on a deep navy #0E1620 background, lighter teal and violet, no paper grain"
```
