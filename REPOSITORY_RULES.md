# Repository Rules and Conventions

ဤစာမျက်နှာသည် `SOCIALAUTOUPLOAD_UNIVERSE` Repository တွင် တသမတ်တည်းဖြစ်စေရန် လိုက်နာရမည့် စည်းမျဉ်းများနှင့် Conventions အားလုံးကို စုစည်းထားခြင်းဖြစ်သည်။

---

## 1. Naming Conventions

### 1.1 Folder Naming Convention
- ဖိုလ်ဒါအမည်များကို **PascalCase** ဖြင့် ရေးပါ။ ဥပမာ: `Part_01_Universe`, `MASTER_BIBLE`။
- အဓိက ဖိုလ်ဒါများကို နံပါတ်စဉ်တပ်ပြီး ဦးစားပေးအလိုက် စီပါ။ ဥပမာ: `00_Front_Matter`, `Part_01_Universe`။
- အတိုကောက်စာလုံးများကို Capital Letter ဖြင့်ရေးပါ။ ဥပမာ: `ASSETS`, `PROMPTS`, `MAPS`။

### 1.2 File Naming Convention
- ဖိုင်အမည်များကို `PREFIX_ID_Description.md` format ဖြင့်ရေးပါ။
- Prefix များသည် ဖိုင်အမျိုးအစားကို ဖော်ပြသည်။ ဥပမာ: `CHAR`, `LOC`, `ORG`, `SE`, `EP`။
- Description ကို PascalCase ဖြင့်ရေးပါ။
- ဥပမာ: `CHAR_001_AungAung.md`, `SE01_EP01_TheBeginning.md`။

## 2. ID Rules

### 2.1 Character ID Rule
- `CHAR-[3-digit number]` format ကိုသုံးပါ။
- ဥပမာ: `CHAR-001`, `CHAR-002`။

### 2.2 Season ID Rule
- `S[2-digit number]` format ကိုသုံးပါ။
- ဥပမာ: `S01`, `S02`။

### 2.3 Episode ID Rule
- `S[SeasonID]E[2-digit number]` format ကိုသုံးပါ။
- ဥပမာ: `S01E01`, `S01E02`။

### 2.4 Location ID Rule
- `LOC-[3-digit number]` format ကိုသုံးပါ။
- ဥပမာ: `LOC-001`, `LOC-002`။

### 2.5 Organization ID Rule
- `ORG-[3-digit number]` format ကိုသုံးပါ။
- ဥပမာ: `ORG-001`, `ORG-002`။

## 3. Versioning Rule
- **Semantic Versioning (Major.Minor.Patch)** ကို အသုံးပြုပါ။
  - **MAJOR:** Canon ကို ထိခိုက်သော ကြီးမားသည့် ပြောင်းလဲမှုများ (Breaking Changes)။
  - **MINOR:** Canon ကို မထိခိုက်သော Feature အသစ်များ၊ ဇာတ်လမ်းအသစ်များ ထည့်သွင်းခြင်း။
  - **PATCH:** စာလုံးပေါင်းအမှားပြင်ခြင်း၊ အသေးစား ပြင်ဆင်မှုများ။
- Version အသစ်တစ်ခုထုတ်တိုင်း `VERSION.md` နှင့် `CHANGELOG.md` ကို မဖြစ်မနေ Update လုပ်ပါ။

## 4. Canon Rule
- အချက်အလက်အားလုံးသည် အစပိုင်းတွင် "Draft" အဆင့်ဖြစ်သည်။
- Canon အဖြစ် သတ်မှတ်လိုပါက `CANON_PROPOSAL` template ကို အသုံးပြု၍ အဆိုပြုလွှာတင်ပါ။
- အတည်ပြုပြီးသော Canon များကို `CANON_INDEX.md` တွင် မှတ်တမ်းတင်ပြီး သက်ဆိုင်ရာ file ၏ metadata တွင် `Canon Level: Canon` ဟု ပြင်ဆင်ပါ။
- Canon အဖြစ် အတည်ပြုပြီးသား အချက်ကို ပြင်လိုပါက Canon Proposal အသစ်ပြန်တင်ရပါမည်။

## 5. Timeline Rule
- အချိန်ဇယားကို `TIMELINE.md` တွင် ဗဟိုမှ ထိန်းချုပ်သည်။
- အဖြစ်အပျက်တိုင်းကို `TIMELINE_TEMPLATE.md` format အတိုင်းရေးပါ။
- အချိန်ကာလကို ရှင်းလင်းစွာ ဖော်ပြရမည်။ (ဥပမာ- `B.E. 2105` - Before Era, `A.E. 15` - After Era)။
- ဇာတ်လမ်းပိုင်းအသစ်ရေးတိုင်း Timeline နှင့် ကိုက်ညီမှုရှိမရှိ စစ်ဆေးပါ။

## 6. Cross-Reference Rule
- Repository အတွင်းရှိ အခြားဖိုင်များကို ချိတ်ဆက်လိုပါက Relative Path ကို အသုံးပြုပါ။
- ဥပမာ: ``[ဇာတ်ကောင် Aung Aung](../Part_03_Characters/CHAR_001_AungAung.md)``
- အခြား Index ဖိုင်များကို ချိတ်ဆက်လျှင် `[CANON_INDEX](./CANON_INDEX.md)` ဟု ရိုးရှင်းစွာ ချိတ်ပါ။

## 7. Markdown Style Guide

### 7.1 Heading Style
- `#` (H1) ကို ဖိုင်၏ အဓိကခေါင်းစဉ်အဖြစ် တစ်ကြိမ်သာ သုံးပါ။
- `##` (H2) ကို အဓိက အပိုင်းခွဲများအတွက် သုံးပါ။
- `###` (H3) ကို H2 အောက်ရှိ အသေးစိတ် အပိုင်းခွဲများအတွက် သုံးပါ။
- ဆက်တိုက် `####` (H4) နှင့် အထက်ကို လိုအပ်မှသာ သုံးပါ။

### 7.2 Table Style
- Table များသည် ရှင်းလင်းပြီး ဖတ်ရလွယ်ကူရမည်။
- Header ကို Bold ဖြင့် ရေးပါ။
- Column များကို `| :--- |` `| :---: |` `| ---: |` သုံး၍ align လုပ်ပါ။

### 7.3 Callout Box Style
- အထူးအာရုံစိုက်စေလိုသော အချက်များအတွက် "Blockquote" (`>`) ကို သုံးပါ။
- ဥပမာ:
  > **Note:** This is an important piece of information.

### 7.4 Placeholder Style
- ဖြည့်စွက်ရန် လိုအပ်သောနေရာများတွင် `[Placeholder Text]` format ကို သုံးပါ။
- ဥပမာ: `[ဇာတ်ကောင်အမည်]`, `[အသေးစိတ်ဖြည့်ရန်]`

### 7.5 Comment Style
- Markdown ဖိုင်အတွင်းတွင် စာရေးသူအတွက်သာဖြစ်သော မှတ်စုများထည့်လိုပါက HTML comment format ကိုသုံးပါ။
- `<!-- This is a comment. It will not be visible in rendered Markdown. -->`
- Template များ၏ထိပ်တွင် ဖိုင်အမည်ပေးပုံကို comment ဖြင့် ညွှန်ကြားထားသည်။
