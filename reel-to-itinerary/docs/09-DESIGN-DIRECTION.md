# Design direction: ceiling, variations and plan (2026-11-16)

Purpose: decide how far to refine the look of the app, and what to explore before Claude Code builds it in SwiftUI.
Evidence: the seven artboards read in full (import card, review, day plan, onboarding 1, budget, evidence, settings), the Wanderlog ad creatives and onboarding screenshots the owner supplied (seen as contact sheets and stills, not the live app), and the constraints in `CLAUDE.md` and `03-LEGAL-GUARDRAILS.md`. Judgements are mine and marked as such. Platform capabilities are from general knowledge of SwiftUI/MapKit/iOS 26 and should be verified on a Mac.

## 1. What we have (observed in our artboards)
- Cool paper background, ink navy text, teal accent, violet/orange/teal day colours, Space Grotesk display + Inter body, white 1 pt-bordered cards at 16 pt radius, 44 pt targets, Verified/Pick one/Unverified pills, evidence timestamps.
- Strengths: coherent token system, accessible contrast, calm and trustworthy, honest labelling, easy to build 1:1 (Claude Code can reproduce it closely).
- Weaknesses (my judgement):
  1. **"Card soup".** Most screens are stacks of identical white bordered cards, so hierarchy is flat and nothing is the hero.
  2. **No imagery or illustration** in the app screens, so low emotional pull and weak App Store screenshots.
  3. **The first impression is a checklist of warnings.** The import card shows three amber "Not captured" rows before any success, which frames the product as incomplete.
  4. **No payoff moment.** Nothing celebrates "your reel became a plan" (the product's core promise and the best 15-second social demo).
  5. **Type is used big only on screen titles**; the trip itself has no strong header.
  6. **Map is a supporting actor**, not the hero.

## 2. What Wanderlog looks like (observed from the owner's material; not the live app)
- Marketing site: white page, bold dark headline, coral/orange accent, phone mock-up in the hero.
- Onboarding: dark red-to-orange gradient, large white bold type, big photo card for the chosen destination, coral primary button, progress bar and back button.
- Ads and in-app glimpses: light UI, map with numbered pins, lists with photo thumbnails, place pages with photo galleries, ratings.
- Reading (my judgement): **photo-first, dense, feature-broad, warm and energetic.** Their strength is breadth and imagery; their onboarding is immersive but long.

## 3. Constraints that set our ceiling
| Constraint | Effect on the look |
|---|---|
| We never show or store creator media (`CLAUDE.md`, `03`) | No creator thumbnails or frames in the UI. |
| Place photos: I am not aware of a MapKit API for place photos (verify); Google Places photos carry licence and attribution rules (open question in PRD) | A photo-first look like Wanderlog's is likely not available at launch. Imagery must come from **our own illustration/art** (Kie.ai text-to-image, `05-ART-PIPELINE.md`) and from **maps and type**. |
| Privacy promise and "no ad or social-login SDKs" | Avoid map SDKs with telemetry or custom-style tiles from third parties; **MapKit** is the default. MapKit allows custom annotations, route polylines, camera animation and a few map styles, but not deep tile restyling (verify). The canvas's stylised map cannot be matched 1:1. |
| Claude Code cloud runs on Linux and cannot run or see the iOS app | Design fidelity is verified by snapshot tests against reference PNGs and by a human on a Mac. Motion, haptics and performance need device testing by a person. |
| Motion cannot be expressed in the static HTML canvas | We need a separate motion spec (durations, easing, sequences) or it will be improvised. |
| iOS 17 minimum (`CLAUDE.md`) with newer features optional | Newer visual APIs (for example mesh gradients, iOS 18; the iOS 26 glass look) need availability checks and fallbacks. |

## 4. Ceiling assessment (what Claude Code can reach in SwiftUI)
| Area | Realistic ceiling | Why |
|---|---|---|
| Static layout, type, spacing, dark mode, Dynamic Type | **High (near 1:1)** | Tokens plus component specs plus snapshot parity. |
| Native feel (navigation, sheets, tab bar, haptics, symbols) | **High** | Use native `NavigationStack`, `TabView`, sheet detents, SF Symbols; built with a current Xcode these should pick up the platform's current look (verify for iOS 26). Our custom bottom sheet and tab bar in the canvas should map to native ones, not be reimplemented. |
| Signature motion (reel → places appearing and pinning, route drawing, Verified stamp) | **Medium-high** | Doable (springs, matched geometry, `Canvas`/shape trims, scroll transitions) but needs a written motion spec and on-device iteration. |
| Map visuals | **Medium** | MapKit annotations, polylines, camera and map style options only. |
| Illustration and destination covers | **Medium, depends on Kie.ai consistency** | A locked prompt kit and a human art review are needed; style drift is the main risk. |
| Photography | **Low unless licensed** | See constraints. |
| Performance polish (scrolling, map with many pins) | **Medium** | Needs Instruments on a device; a human step. |
| Overall | **A polished, native, trustworthy app is highly achievable; a distinctive, delightful one needs deliberate signature moments and art, not just more components.** | |

## 5. Variation axes to explore
1. **Imagery strategy:** typographic only / illustrated destination covers / photographic.
2. **Density:** calm (few elements per screen) / dense (Wanderlog-like).
3. **Palette temperature:** cool (current teal) / warm accent / high-contrast monochrome plus one vivid colour.
4. **Shape language:** soft bordered cards (current) / flat sections with dividers / ticket-and-stamp motifs.
5. **Type:** Space Grotesk + Inter (current) / editorial serif display + Inter / rounded sans.
6. **Map treatment:** standard MapKit / muted style with strong route lines.
7. **Motion:** minimal / three signature moments.

## 6. Three directions to design as variants
| Direction | Summary | Fit to constraints | Differentiation vs Wanderlog | Build effort |
|---|---|---|---|---|
| **A. Refined utility** (today, polished) | Keep the system; fix hierarchy, reframe the import card, bigger trip header. | Excellent | Low | Low |
| **B. Cartographic editorial** | Map and route lines as the hero; big type; illustrated destination covers (ours); "Verified" and timestamp as an ownable evidence motif; signature motion. | Excellent (no creator media, no licensed photos) | **High** | Medium-high |
| **C. Immersive photographic** | Wanderlog-like gradients and photo cards. | Poor (needs licensed photos) | Low (fights their strength) | Medium + licensing |

**Recommendation (judgement): B-lite on top of A.** Keep the token system and accessibility (trust is our positioning), and add a "moment layer": illustrated destination covers, three signature moments, a stronger trip header, native components for sheets and tabs, and a map-forward Day and Trip view. Do not pursue C.

## 7. Hero screens to explore (3 screens x 3 variants = 9 artboards, on the canvas)
1. **Import (reel → places):** variant A calm checklist reframed positively ("4 places found. Add more for better results."); variant B places appear and pin to a mini map as they are read; variant C full-bleed gradient with a progress ring.
2. **Trip home:** A tabbed list with a bigger header; B illustrated cover + big destination type + day route strip; C photo-style hero with stats.
3. **Place card:** A current layout polished; B evidence-first (timeline of where it was heard), credit prominent, link-outs as a row; C photo gallery layout (placeholder only).

Evaluate each with this scorecard (1 to 5): legal fit, SwiftUI build effort, differentiation vs Wanderlog, accessibility and contrast (4.5:1 text), emotional impact in a 15-second screen recording, dark-mode viability, ownability (would a stranger recognise it).

## 8. Plan
1. **Do not gold-plate yet.** The moat is extraction accuracy and trust, so engine and Import preview come first.
2. **One time-boxed exploration sprint** in the canvas (nine hero artboards above), cheap compared with rewriting SwiftUI later. Show the variants to 5 to 8 target users and pick on the scorecard.
3. **Add to the design system before build:** motion tokens (durations, easing, three signature sequences), an art kit (Kie.ai prompt kit, 6 to 8 starter destination covers, icon set), type scale update, dark map treatment, native-component mapping.
4. **Treat marketing as a design constraint:** the first three App Store screenshots and the 15-second demo must show the reel → places → mapped day moment clearly; design that moment so it films well.
5. **Update the pack:** `06-DESIGN-HANDOVER.md` (motion spec, art kit, chosen direction), `design-tokens.json` (motion and any new colour), `04-BUILD-PLAN.md` (signature motion and art in M5).

## 9. Risks
- Over-investing in look before the extraction works, which is the real moat.
- Illustration style drift across destinations.
- Motion that looks good in a prototype but janks on device (needs Instruments).
- Relying on a custom bottom sheet and tab bar that fight the platform's native components.
- Photo-dependent screens that cannot be filled at launch.
