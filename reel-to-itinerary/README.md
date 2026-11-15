# Reel→Itinerary — Claude Code project pack

Hand this folder to Claude Code (run it on a Mac with Xcode for the iOS target).

| File | Purpose |
|---|---|
| `CLAUDE.md` | Rules + conventions Claude Code loads each session |
| `docs/01-PRD.md` | Product requirements |
| `docs/02-ARCHITECTURE.md` | Components, data flow, data model |
| `docs/03-LEGAL-GUARDRAILS.md` | What's allowed, what's not, and why (not legal advice) |
| `docs/04-BUILD-PLAN.md` | Milestones with acceptance criteria and kickoff prompts |
| `docs/05-ART-PIPELINE.md` | Kie.ai art generation workflow |
| `docs/06-DESIGN-HANDOVER.md` | Claude Design ⇄ Claude Code contract: screens, components, states, strings, parity tests |
| `spec/design-tokens.json` | Colours, type, spacing, radii, sizes (source of truth for `Theme.swift`) |
| `spec/extraction.schema.json` | JSON schema the LLM must return |
| `spec/extraction.prompt.md` | System prompt for place extraction |
| `.claude/settings.json` | Denies scraping tools; allows safe dev commands |

**Start:** open Claude Code in this folder and paste the Milestone 0 prompt from `docs/04-BUILD-PLAN.md`.
