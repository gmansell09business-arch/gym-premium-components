# Art pipeline — Kie.ai

(Assumes "KIE" = Kie.ai image API. If you meant Unity-side tooling, tell Claude Code and adjust.)

## Use for (design-time / brand assets)
App icon concepts, onboarding illustrations, empty states, category icons (restaurant/hotel/activity),
destination-style cover illustrations generated **from text prompts**, share-card templates.

## Don't use for
- Feeding creator thumbnails/frames into image models (copyright, derivative risk)
- Imitating a named creator's or brand's style/logo
- Fake photos of real venues presented as real

## Architecture
Dev script `Backend/scripts/generate-art.ts` → Kie.ai REST (async task: create → poll/callback → download).
Key in `KIE_API_KEY` env var (backend only, never committed, never in app). Outputs committed to
`App/Assets.xcassets` after human review. Prompts live in `art/prompts/*.md` with model + seed + date
for reproducibility. Check Kie.ai's current docs for model names, endpoints and commercial-use terms
before relying on them.

## Style guide (edit to taste)
Warm, editorial travel look; flat shapes + soft grain; one accent colour; consistent icon stroke;
export @1x/@2x/@3x PNG or PDF vectors; dark-mode variants.

## Optional: Unity
If Unity is used for a 3D globe/onboarding scene, embed via UnityFramework only after MVP; not needed for v1.
