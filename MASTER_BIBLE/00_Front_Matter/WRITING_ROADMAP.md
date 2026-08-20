# Writing Roadmap

## Working Method

Existing-document alignment first, then chapter-by-chapter development with validation and PDF update after each completed chapter.


## Current Priority Before New Chapters

အသစ် chapter မရေးမီ အောက်ပါ existing alignment issues များကို အရင်ရှင်းရမည်။

1. Brand Bible layer ကို `Planned` မှ `Required` အဖြစ်သတ်မှတ်ပြီး SocialAutoUpload.com marketing purpose နှင့်ချိတ်ရန်။
2. Episode တစ်ခုချင်းစီ သီးသန့်ကြည့်လည်း SocialAutoUpload.com ကို သိနိုင်စေရန် opening, ending, CTA rules များသတ်မှတ်ရန်။
3. 45-minute streaming runtime ကို secondary format အဖြစ်ထားပြီး 30-90 second short-form runtime ကို primary production format အဖြစ်ပြင်ရန်။
4. Product features ကို story metaphor များနှင့် map လုပ်ရန်။
5. Prompt/asset folders မဖြည့်မီ reusable prompt standards ကို existing production chapters တွင် align လုပ်ရန်။

## Phase Plan

- Phase 1: Chapter 1 - Canon -> PDF Export
- Phase 2: Chapter 2 - Vision -> PDF Update
- Phase 3: Chapter 3 - Core Theme & Story Philosophy -> PDF Update
- Phase 4: Chapter 4 - Story Philosophy -> PDF Update
- Phase 5: Chapter 5 - The Kingdom of သီရိမာလာ -> PDF Update
- Phase 6: Chapter 6 - Geography & Official World Map -> PDF Update
- Phase 7: Chapter 7 - The Grand Royal Palace Bible -> PDF Update
- Phase 8: Chapter 8 - Royal Communication Department -> PDF Update
- Phase 9: Character Design System -> PDF Update
- Phase 10: Character Dossier 001 - Min Thant -> PDF Update
- Phase 11: Character Dossier 002 - King Kyawzwa -> PDF Update
- Phase 12: Character Dossier 003 - Queen Thiri Devi -> PDF Update
- Phase 13: Character Dossier 004 - The Shadow Leader -> PDF Update
- Phase 14: Chapter 12 - Royal Communication Department Bible -> PDF Update
- Phase 15: Chapter 13 - Protocol & Crisis Manual -> PDF Update
- Phase 16: Chapter 14 - Timeline & Historical Chronicle -> PDF Update
- Phase 17: Chapter 15 - Language, Culture & Royal Etiquette -> PDF Update
- Phase 18: Chapter 16 - Episode Architecture & Story Engine -> PDF Update
- Phase 19: Chapter 17 - Character Arc Matrix -> PDF Update
- Phase 20: Chapter 18 - Mystery & Reveal Design Bible -> PDF Update
- Phase 21: Chapter 19 - Scene Construction Bible -> PDF Update
- Phase 22: Chapter 20 - Visual Language & Cinematography Bible -> PDF Update
- Phase 23: Chapter 21 - AI Production Pipeline -> PDF Update
- Phase 24: Chapter 22 - Asset Library & Canon Database -> PDF Update
- Phase 25: Chapter 23 - Episode Master Blueprint (Arc I, Episodes 1-20) -> PDF Update
- Phase 26: Chapter 24 - Episode Master Blueprint (Episodes 6-10) -> PDF Update
- Phase 27: Chapter 25 - Episode Master Blueprint (Episodes 11-15) -> PDF Update
- Phase 28: Chapter 26 - Episode Master Blueprint (Episodes 16-20, Season 1 Finale) -> PDF Update
- Phase 29: Chapter 27 - Season 2 Master Blueprint -> PDF Update
- Continue phase cycle through all planned chapters and appendices

## Required Checks Before PDF Export

1. Run `python3 BUILD/validate_repository.py`.
2. Fix all errors.
3. Review warnings for intentional placeholders or deferred sections.
4. Update `CHANGELOG.md` and `VERSION.md` when the content state changes.

## Why This Method Works

- Prevents context overload during writing
- Enables deep polishing per chapter
- Keeps official book always export-ready
- Makes future upgrades simple (`v2.0`, `v3.0`)
- Supports expansion to Season 6, Spin-off, Movie, Game
