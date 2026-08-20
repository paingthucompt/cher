# Google AI Studio App Build Prompt

Copy the prompt below into Google AI Studio Build mode.

## Prompt

Build a polished, responsive web app called **SocialAutoUpload Studio** for managing a Myanmar royal mystery short-video production project.

This is a production control app, not a marketing landing page. Use a focused editorial-tool interface with a warm parchment background, lacquer red accents, antique gold details, teak-brown text, and restrained blue for the SocialAutoUpload brand. Use an expressive serif display font for episode titles and a clean readable sans-serif for controls. Keep cards compact with square or 6px corners. Do not use purple gradients, oversized hero sections, decorative blobs, or unnecessary marketing copy.

### Product goal

Help the project owner finish episodes safely by managing:

1. Episode production status
2. Character, location, prop, and brand assets
3. Prompt packages and 10-second clip generation checklists
4. Canon and continuity warnings
5. Final assembly and export QA
6. Downloadable production documents
7. Writing and completing all remaining episodes
8. Final video preparation for every completed episode

### Seed project data

Project: `SOCIALAUTOUPLOAD_UNIVERSE`
Brand: `SocialAutoUpload.com`
Current version: `1.0.1`

Episodes:
- `S01E001` - `ပျောက်ဆုံးသော အမိန့်` - status `Final QA`, 7 story clips, final file exists, resolution warning `720x1280; target 1080x1920`
- `S01E002` - status `Prompt Ready`
- `S01E003` through `S01E020` - status `Not Started`
- `S02E021` through `S02E040` - status `Not Started`
- `S03E041` through `S03E042` - status `Not Started`

Characters:
- `CHR001` Min Thant: calm, observant, serious investigator
- `CHR002` King Kyawzwa: responsible ruler, calm authority
- `CHR003` Queen Thiri Devi: composed, sharp, notices hidden details
- `CHR004` U Nanda: ambiguous shadow leader, suspicious, never confesses early

Locations: `LOC001` Maha Shwe Palace, `LOC002` Royal Archives, `LOC003` Messenger Relay Station, `LOC004` Royal Communication Department
Props: `PROP001` Royal Seal, `PROP002` Archive Scroll / Ledger, `PROP004` Messenger Bell
Brand asset: `BRAND001` SocialAutoUpload End Card

### Required screens

1. **Dashboard**
   - Show current project version, episode counts by status, the next recommended action, and a QA warning for S01E001 resolution.
   - Show a prominent Continue Production button that opens the next incomplete task.

2. **Episodes**
   - Searchable and filterable table/list by season and status.
   - Each episode opens a detail workspace with status, synopsis, required assets, prompt package, clip checklist, assembly checklist, QA checklist, and export metadata.
   - Statuses: `Not Started`, `World Setup`, `Prompt Ready`, `Clips In Progress`, `Final Assembly`, `Final QA`, `Complete`.

3. **Episode workspace**
   - Tabs: Overview, Assets, Clips, Assembly, QA, Export.
   - For S01E001, preload the real seven-clip assembly order:
     1. Official opening title card
     2. Clip 01 - Opening Horse Returns
     3. Clip 02 - Missing Bell
     4. Clip 03 - King And Queen Notice The Failure
     5. Clip 04 - Min Thant Finds The Time Mismatch
     6. Clip 05 - Archive Route Scratched Out
     7. Clip 06 - Shadow And Multi Route Dispatch
     8. Clip 07 - End Hook Only
     9. Official BRAND001 end card
   - Each clip has states `Not Generated`, `Generated`, `Approved`, `Needs Revision`.
   - Support notes, approval toggles, and a revision reason.

4. **Prompt Lab**
   - Select an episode, clip, characters, locations, and props.
   - Generate a structured draft prompt in English for Google Flow/Veo with natural spoken Burmese dialogue.
   - Show the prompt in an editable text area with Copy and Download Markdown actions.
   - Never directly mark generated content as canon.
   - Keep generated drafts isolated from official project data until the user explicitly approves them.

5. **Canon Guard**
   - Before approving a prompt or clip, check:
     - Burmese/Myanmar visual identity
     - Existing character and asset consistency
     - No Chinese/Thai/fantasy costume drift
     - No modern phones, laptops, cities, or software UI
     - Burmese natural dialogue only; English only for official opening/end card
     - No generated SocialAutoUpload logo or end card inside story clips
   - Display blocking warnings separately from advisory warnings.

6. **Assembly and Export**
   - Show opening card, story clips, and official end card in ordered rows with drag-to-reorder support.
   - Validate 9:16 aspect ratio, MP4 format, audio presence, clip order, official end card, and exact brand text.
   - Target export: `1080x1920`, filename `S01E001_PyaukSoneThawAmeint_Final_v01.mp4`.
   - Allow an accepted exception for the existing `720x1280` file, but keep the resolution warning visible until the user resolves or accepts it.
   - Provide a final QA report preview and Download QA Report button.

7. **Episode Writer**
   - Add a `Create New Episode` action from the Episodes screen.
   - Let the user choose season, episode number, title, one-sentence story goal, brand metaphor, featured characters, locations, props, and target runtime.
   - Use Gemini to generate a structured episode draft containing: logline, beginning/middle/end, 7-10 numbered scenes, natural spoken Burmese dialogue, visual direction, sound direction, continuity notes, and a cliffhanger.
   - Provide separate actions: `Generate Draft`, `Regenerate Section`, `Edit`, `Save Draft`, `Approve Story`, and `Send To Production`.
   - Every new episode starts as `Draft`; never silently promote AI output to Canon or Complete.
   - Before approval, run Canon Guard against existing characters, locations, props, timeline, language rules, and brand rules.
   - After `Approve Story`, automatically create the episode workspace, scene list, prompt package, clip checklist, assembly checklist, and QA checklist.
   - Allow the user to edit the story manually before any video prompt is generated.
   - Show a visible version history for episode drafts with timestamp, status, and change summary.

8. **Production Queue**
   - Add a queue showing every scene/clip that still needs work across all episodes.
   - For each scene provide `Generate Prompt`, `Copy Prompt`, `Download Prompt`, `Mark Generated`, `Submit For Review`, `Approve Clip`, and `Needs Revision` actions.
   - Use 10-second vertical `9:16` clips as the default production unit.
   - Do not pretend to render a video if the app has no configured video-generation API. In that case, clearly label the item `Ready for Google Flow/Veo` and let the user upload the generated clip for review.
   - If a supported server-side video API is configured, provide a real `Generate Video` action with loading, progress, retry, error, and output states. Keep all API keys server-side.
   - Never put generated logos, opening titles, or end cards inside story clip prompts.

9. **Video Finishing Studio**
   - For any episode with approved clips, open a finishing workspace with a timeline/ordered list.
   - Include official opening title card, approved story clips, optional black cut before the end card, and official BRAND001 end card.
   - Allow upload of locally generated clips and official brand assets. Show thumbnails, duration, aspect ratio, resolution, audio-track presence, and approval state.
   - Support reorder, remove, replace, trim start/end, and short audio crossfade settings. Use hard cuts or very short fades only.
   - Validate clip order, missing clips, duplicate clips, 9:16 ratio, MP4 format, audio, readable exact brand text, and official end-card usage.
   - Add `Build Final Video` and `Download Final Video` actions. If browser rendering is not available, generate a complete FFmpeg command or an export manifest and explain exactly what remains to run.
   - Default export settings: MP4, H.264 video, AAC audio, `1080x1920`, original frame rate, target filename based on episode ID and title.
   - Keep a `720x1280` result as an explicit resolution warning, never as a silent pass.
   - After export, save a downloadable final QA report containing episode ID, clip order, checks, warnings, export settings, filename, duration, resolution, and SHA-256 when available.

10. **Project Completion Flow**
   - The main dashboard must show the next actionable step in this order: write story, approve story, prepare prompts, generate/upload clips, approve clips, assemble, run QA, export final video.
   - A season is complete only when every episode has an approved story, approved clips, passed final QA, and a downloadable final video or explicitly accepted export exception.
   - Add filters for `Needs My Action`, `Blocked`, `Ready For Flow`, `Ready For Assembly`, and `Complete`.
   - Add a completion percentage based on real checklist states, not static placeholder numbers.

### Safety and data rules

- Do not invent new canon facts silently.
- Treat all AI-generated text as Draft until the user approves it.
- Keep official assets separate from generated video prompts.
- Never ask the model to redraw, redesign, recolor, or generate the SocialAutoUpload logo.
- Do not expose API keys in client-side code. Put Gemini calls behind a server-side function or a clearly marked mock provider if server integration is unavailable.
- For this first version, use local seeded state and localStorage so the app works immediately without authentication.
- Add an Export Project JSON action and an Import Project JSON action so project state can be backed up.
- Add a Reset Demo Data action with a confirmation dialog.
- Add a `Project Completion` view showing incomplete episodes and the exact next action for each one.
- Add a `Download Episode Package` action that exports story, prompts, clip checklist, assembly plan, and QA report as a JSON or Markdown bundle.

### Interaction quality

- Add keyboard-accessible buttons, visible focus states, empty states, loading states, and error states.
- Use familiar icons for copy, download, search, filter, warning, check, and settings.
- Keep important actions reachable on mobile with a responsive bottom action bar or stacked controls.
- Do not hide critical QA warnings in tooltips.
- Use Burmese labels where natural, with English technical labels in smaller supporting text.
- Include sample data so every screen is usable on first load.

### Implementation requirements

- Use React and TypeScript.
- Use a small component structure with clear types for Episode, Asset, Clip, ChecklistItem, PromptDraft, and QAResult.
- Keep all seeded data in one typed module.
- Keep business rules in pure functions that can be tested independently.
- Implement pure functions for episode completion percentage, next-action routing, Canon Guard checks, assembly validation, and export filename generation.
- Keep episode drafts, approved stories, generated prompts, uploaded clip metadata, QA results, and final export metadata in separate typed records.
- Do not add a database or authentication for the first version.
- Make the app runnable immediately in AI Studio preview.
- At the end, show a concise list of files created and how to run the app.

Build in this order and keep each step functional before moving on:
1. Dashboard, Episodes table, seeded S01E001 workspace, and localStorage persistence.
2. Episode Writer for creating S01E003 and later episodes from structured drafts.
3. Prompt Lab, Canon Guard, and Production Queue.
4. Video Finishing Studio with upload, timeline validation, export manifest, and final QA report.
5. Project JSON import/export and Download Episode Package.

The app must remain useful when no Gemini or video API is configured: use deterministic demo data and clearly labeled mock generation, never fake a completed video export. Ensure the preview is functional before adding visual polish.
