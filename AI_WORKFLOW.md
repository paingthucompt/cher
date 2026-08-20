# AI-Assisted Writing Workflow

ဤစာမျက်နှာသည် `SOCIALAUTOUPLOAD_UNIVERSE` Repository တွင် မတူညီသော AI Models (ChatGPT, Gemini, Claude, etc.) ကို အသုံးပြု၍ အတူတကွ အလုပ်လုပ်ရာတွင် တသမတ်တည်းဖြစ်စေရန်နှင့် Conflict များ၊ Canon ပျက်စီးမှုများ မဖြစ်စေရန် လိုက်နာရမည့် Workflow ကို သတ်မှတ်ပေးထားသည်။

---

## 1. AI အသီးသီး၏ အခန်းကဏ္ဍ (Roles of Each AI)

AI တစ်ခုချင်းစီတွင် အားသာချက်၊ အားနည်းချက်များ ရှိသောကြောင့် အောက်ပါအတိုင်း အခန်းကဏ္ဍများ ခွဲခြား၍ အသုံးပြုရန် အကြံပြုပါသည်။

### 1.1 Gemini (by Google)
- **Primary Role: World-building & Research**
- **ဘာလုပ်မလဲ:**
  - **Concept Generation:** ဇာတ်ကောင်၊ နေရာ၊ အဖွဲ့အစည်း၊ နည်းပညာ အသစ်များအတွက် အတွေးအခေါ်အကြမ်းများ ဖန်တီးခြင်း။
  - **Research & Fact-Checking:** သိပ္ပံ၊ သမိုင်း၊ ယဉ်ကျေးမှုဆိုင်ရာ အချက်အလက်များ ရှာဖွေခြင်းနှင့် စစ်ဆေးခြင်း။
  - **Structured Data Creation:** ဇာတ်ကောင် Profile, Location Profile များအတွက် အချက်အလက်များ ဇယားကွက်ဖြင့် ဖန်တီးခြင်း။
- **ဘယ်အချိန်သုံးမလဲ:** စီမံကိန်း၏ အခြေခံအုတ်မြစ်များ တည်ဆောက်သည့်အခါ၊ ကမ္ဘာကြီးကို အသေးစိတ် ဖန်တီးသည့်အခါ။

### 1.2 ChatGPT (by OpenAI)
- **Primary Role: Narrative & Dialogue**
- **ဘာလုပ်မလဲ:**
  - **Drafting:** ဇာတ်လမ်းအခန်းများ၊ Episode အကြမ်းများ ရေးသားခြင်း။
  - **Dialogue Generation:** ဇာတ်ကောင်များ၏ ကိုယ်ရည်ကိုယ်သွေးနှင့် ကိုက်ညီသော စကားပြောများ ဖန်တီးခြင်း။
  - **Plot Development:** ဇာတ်လမ်းအကွက်များ (Plot points) နှင့် Twists များ ဖန်တီးခြင်း။
- **ဘယ်အချိန်သုံးမလဲ:** ဇာတ်လမ်းပိုင်းများ၊ အခန်းများကို တကယ်တမ်းရေးသားသည့်အခါ။

### 1.3 Claude (by Anthropic)
- **Primary Role: Editing & Refinement**
- **ဘာလုပ်မလဲ:**
  - **Summarization:** ရှည်လျားသော စာသားများကို အကျဉ်းချုပ်ခြင်း။
  - **Refinement & Polishing:** ရေးပြီးသား Draft များကို ပိုမိုကောင်းမွန်အောင်၊ ပိုမိုဖတ်ရှု၍ ကောင်းအောင် ပြင်ဆင်တည်းဖြတ်ခြင်း (Tone, Pacing, Style)။
  - **Canon Consistency Check:** ရေးသားထားသော စာသည် ရှိပြီးသား Canon နှင့် ကိုက်ညီမှုရှိမရှိ အကြမ်းဖျင်း စစ်ဆေးပေးခြင်း။
- **ဘယ်အချိန်သုံးမလဲ:** First draft ရေးပြီးနောက် Final version မဖြစ်မီ ကြားအဆင့်တွင် သုံးပါ။

### 1.4 Cursor / Codex
- **Primary Role: Automation & Tooling (For Advanced Users)**
- **ဘာလုပ်မလဲ:**
  - **Batch Processing:** ဖိုင်များစွာကို တစ်ပြိုင်နက် ပြင်ဆင်ခြင်း (ဥပမာ - ဖိုင်ခေါင်းစဉ်များ format ပြောင်းခြင်း)။
  - **Linting & Formatting:** Markdown ဖိုင်များ၏ Style Guide ကိုက်ညီမှုရှိမရှိ စစ်ဆေးခြင်း။
  - **Scripting:** Repository ကို စီမံခန့်ခွဲရန် အထောက်အကူပြု script များ ရေးသားခြင်း (ဥပမာ - Index ဖိုင်များကို auto-update လုပ်ခြင်း)။
- **ဘယ်အချိန်သုံးမလဲ:** Repository ကို maintain လုပ်သည့်အခါ၊ workflow ကို automate လုပ်ချင်သည့်အခါ။

## 2. Workflow & Conflict Avoidance

**Canon မပျောက်၊ Conflict မဖြစ်စေရန် အောက်ပါအဆင့်များကို လိုက်နာပါ။**

**Step 1: Define the Goal & Choose the Right AI**
- သင်ဘာလုပ်ချင်သလဲ (ဥပမာ- ဇာတ်ကောင်အသစ်ဖန်တီး၊ ဇာတ်လမ်းရေး) ကို တိတိကျကျ သတ်မှတ်ပါ။
- အပေါ်တွင် ဖော်ပြထားသော အခန်းကဏ္ဍအလိုက် သင့်တော်သည့် AI ကို ရွေးချယ်ပါ။

**Step 2: Prepare the Prompt**
- `PROMPT_TEMPLATE.md` ကို အသုံးပြု၍ Prompt တစ်ခုကို ဂရုတစိုက် ပြင်ဆင်ပါ။
- **အရေးကြီးဆုံးမှာ Context ဖြစ်သည်။** AI ကို အလုပ်မခိုင်းမီ၊ သက်ဆိုင်ရာ Character Profile, Timeline, Canon Rules များကို Prompt ထဲတွင် ရှင်းလင်းစွာ ထည့်သွင်းပေးပါ။ `Link` များ ብቻမက၊ အကျဉ်းချုပ်ကိုပါ ကူးထည့်ပေးခြင်းက ပိုကောင်းသည်။

**Step 3: Generate & Isolate**
- AI မှထုတ်ပေးသော အဖြေ (Output) ကို **မူရင်းဖိုင်ထဲသို့ တိုက်ရိုက်မထည့်ပါနှင့်။**
- Output ကို `DRAFTS` သို့မဟုတ် `SCRATCHPAD` ကဲ့သို့သော ယာယီဖိုင်တစ်ခုထဲတွင် အရင်သိမ်းဆည်းပါ။

**Step 4: Review & Refine (Human-in-the-Loop)**
- AI ၏ အဖြေကို လူကိုယ်တိုင် ပြန်လည်စစ်ဆေးပါ။
- **Canon & Continuity Check:** ရှိပြီးသား Canon၊ Timeline တို့နှင့် ကိုက်ညီရဲ့လား။
- **Quality Check:** ဇာတ်လမ်း၊ ဇာတ်ကောင်တို့၏ အရည်အသွေးကို ထိခိုက်ရဲ့လား။
- လိုအပ်ပါက Claude ကဲ့သို့သော AI ကိုသုံး၍ Refine လုပ်ပါ၊ သို့မဟုတ် ကိုယ်တိုင်ပြင်ဆင်ပါ။

**Step 5: Integrate & Document**
- စစ်ဆေးပြီး၊ ပြင်ဆင်ပြီးသော အချက်အလက်ကိုမှ သက်ဆိုင်ရာ တရားဝင်ဖိုင် (ဥပမာ - `CHARACTER_010.md`) ထဲသို့ ထည့်သွင်းပါ။
- ဤပြောင်းလဲမှုကို `CHANGELOG.md` တွင် မဖြစ်မနေ မှတ်တမ်းတင်ပါ။ `[AI: Gemini]` ဟု မှတ်ချက်ထည့်ပေးပါက ပိုကောင်းသည်။
- အကယ်၍ ဤပြောင်းလဲမှုသည် Canon ဖြစ်ရန်လိုအပ်ပါက `CANON_PROPOSAL` workflow ကို လိုက်နာပါ။

## 3. Canon ကို ဘယ်လိုထိန်းမလဲ (Maintaining Canon)

- **Single Source of Truth:** `CANON_INDEX.md` သည် တစ်ခုတည်းသော အမှန်တရား (Source of Truth) ဖြစ်သည်။ AI တစ်ခုခုက ပြောတိုင်း Canon မဖြစ်ပါ။
- **Human Approval:** AI က ဖန်တီးသမျှသည် "Draft" သာဖြစ်သည်။ လူသား (Project Lead/Author) က အတည်ပြုပြီး `CANON_INDEX.md` တွင် မှတ်တမ်းတင်မှသာ Canon ဖြစ်သည်။
- **Version Control:** AI prompt များကို `PROMPTS` ဖိုလ်ဒါတွင် version ခွဲ၍ သိမ်းဆည်းပါ။ မည်သည့် prompt version က မည်သည့်ရလဒ်ကို ထုတ်ပေးခဲ့သည်ကို ခြေရာခံနိုင်ရန်ဖြစ်သည်။
