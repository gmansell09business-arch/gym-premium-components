# PRD — Reel→Itinerary

## Problem
People save travel reels/posts and never turn them into a plan. Places are scattered across captions,
on-screen text and voiceover.

## Users
Travellers who save creator content on Instagram/TikTok and want a usable trip plan.

## Core flow
1. User taps Share on a reel → picks our app.
2. App immediately parses the **caption via oEmbed** and shows "Found N places".
3. If coverage is thin, app offers "Add a screen recording or screenshots for more" with a 3-step helper.
4. On-device OCR + speech-to-text run on the recording. Text only goes to the extraction service.
5. Candidates are verified with MapKit; user reviews/disambiguates in an **Inbox**.
6. Confirmed places merge into a **Trip** (multiple reels can feed one trip), grouped into days.
7. User edits, views map + travel times, exports (Apple Maps guide / Calendar / share link).

## MVP scope
- Share extension (URL, image, video, text)
- oEmbed + paste caption + user-supplied media
- On-device OCR and transcription
- LLM extraction → MapKit verification → review UI
- Trip timeline + map, day clustering, reorder/edit
- Attribution on every stop, delete-my-data

## Out of scope (by design — legal)
Profile/account import, background crawling, downloading platform media, logging in to IG/TikTok,
storing creator media, republishing creator text.

## Success metrics
- ≥70% of shared reels yield ≥1 verified place (caption + recording)
- Median time share→reviewed list < 60s
- ≥40% of users who see the recording prompt complete it
- <5% of accepted places later deleted as wrong

## Monetisation (later)
Free: 3 reels/month. Pro: unlimited, multi-trip, offline maps, export. Affiliate booking links only with
clear disclosure.
