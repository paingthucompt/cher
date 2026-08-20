# Changelog

All notable changes to this project will be documented in this file.

---

## [1.0.1] - 2026-07-29

### Fixed
- Aligned existing control documents with the confirmed business goal: SocialAutoUpload.com marketing through standalone AI short episodes.
- Updated runtime guidance from streaming-first to short-form-first while retaining long-form compilation and optional streaming formats.
- Marked Brand Bible, standalone brand exposure, product-feature mapping, and CTA rules as required before creating new story chapters.
- Synchronized version references to `1.0.1`.
- Repository maintenance pass: filled empty core index files and synchronized `MASTER_INDEX.md`, Table of Contents, and Writing Roadmap with existing chapter files.
- Added repository validator at `BUILD/validate_repository.py` for broken links, empty required files, H1 count warnings, and duplicate chapter-number warnings.
- Added lightweight build helpers: `BUILD/master_bible_files.txt` and `BUILD/build_master_bible.sh`.
- Converted placeholder example links in documentation to inline code so link checkers do not treat them as real repository links.

## [1.0.0] - 2026-07-22

### Added
- **Project Foundation:** Initialized the entire repository structure, rules, and templates.
- **Chapter 1 - Canon:** Created the first draft of the foundational "Canon" chapter, defining the universe's source of truth. (`/MASTER_BIBLE/Part_01_Universe/CHAP_01_Canon.md`)
- **Chapter 2 - Vision:** Created the first draft of the "Vision" chapter, outlining the project's mission and long-term goals. (`/MASTER_BIBLE/Part_01_Universe/CHAP_02_Vision.md`)
- **Chapter 3 - Core Theme:** Created the first draft of the "Core Theme" chapter, detailing the project's central thematic questions. (`/MASTER_BIBLE/Part_01_Universe/CHAP_03_CoreTheme.md`)
- **Chapter 4 - Story Philosophy:** Created the first draft of the "Story Philosophy" chapter, establishing the principles of narrative design. (`/MASTER_BIBLE/Part_01_Universe/CHAP_04_StoryPhilosophy.md`)
- **Chapter 5 - Kingdom:** Created the first draft of the "Kingdom" chapter, introducing the main setting of Ascendia. (`/MASTER_BIBLE/Part_02_World/CHAP_05_Kingdom.md`)
- **Chapter 6 - Geography:** Created the first draft of the "Geography" chapter, detailing the physical environment of Ascendia. (`/MASTER_BIBLE/Part_02_World/CHAP_06_Geography.md`)
- **Chapter 7 - Government:** Created the first draft of the "Government" chapter, detailing the political structure of Ascendia. (`/MASTER_BIBLE/Part_02_World/CHAP_07_Government.md`)

## 2026-07-29 - Chapter Continuity Alignment

- Rewrote Chapter 8 RCD world overview to remove legacy Ascendia/Oracle/suppression concepts and align it with သီရိမာလာ, Chapter 12, and the SocialAutoUpload.com product metaphor.
- Updated Chapter 4 Story Philosophy from generic sci-fi framing to Myanmar-culture royal mystery / brand story framing.
- Cleaned Character Bible files so internal headings no longer conflict with numbered story chapters.
- Added Brand & Runtime Alignment Lock notes to existing episode blueprint chapters before writing any new chapters.

## 2026-07-29 - Numbering Cleanup

- Corrected internal CHAPTER headings in World Bible Chapter 5-7 to match filenames and table of contents.
- Converted Character Bible numeric section prefixes from old chapter numbers to CHAR/CHR identifiers.

## 2026-07-29 - Brand And Production Foundation

- Created Part XI Brand Bible files for SocialAutoUpload branding, logo usage, opening/ending rules, marketing strategy, standalone exposure, product mapping, and CTA rules.
- Aligned end-card tagline to `Post Once. Publish Everywhere.`.
- Added prompt, asset, image, map, episode-pack, and production-checklist foundation files.
- Updated build file list to include Brand Bible files.
- Cleaned stale Character Bible maintenance note from Master Index.
- Synced central timeline with current season/episode blueprint state.

## 2026-07-29 - Episode Product Mapping

- Added per-episode Brand/Product Mapping blocks to Episodes 001-042.
- Added Brand Bible Episode Product Map for Episodes 001-042.
- Linked the new map from Master Index, Table of Contents, and build file list.

## 2026-07-29 - Prompt Package Alignment

- Aligned S01E001 production pack and prompt package with Episode Product Map PF001.
- Added prompt package index for Episodes 001-042.

## 2026-07-29 - Natural Burmese Dialogue Lock

- Added natural spoken Burmese dialogue rule to Chapter 15.
- Added Dialogue Language Lock to Google Flow/Gemini/Veo prompt master.
- Added Burmese dialogue style guide under PROMPTS.
- Updated S01E001 prompt package, episode template, and production checklist to require natural Burmese dialogue.

## 2026-07-29 - Flow Character And Scene Setup Packs

- Added Flow setup prompt packs for characters, locations/scenes, props, and EP001 production order.
- Updated asset manifest and production checklist with correct Flow setup sequence before video generation.
