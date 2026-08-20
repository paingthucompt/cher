<!-- PROMPT TEMPLATE -->
<!-- 
----------------------------------------------------------------------
File-naming convention: PRMPT_[TargetAI]_[Purpose]_[Version].md
Example: PRMPT_Gemini_CharacterGen_v1.md
----------------------------------------------------------------------
-->

# Prompt: [Prompt ၏ ရည်ရွယ်ချက်]

- **Prompt ID:** `[PRMPT-YYYYMMDD-NN]`
- **Target AI:** `[Gemini, ChatGPT, Claude, etc.]`
- **Purpose:** `[ဥပမာ - Character Backstory Generation, Plot Outline, Dialogue Polishing]`
- **Version:** `1.0`
- **Author:** `[အသုံးပြုသူအမည်]`

---

## 1. Prompt ၏ ရည်မှန်းချက် (Goal of the Prompt)

_(ဤ Prompt ကို အသုံးပြု၍ ဘာကိုရရှိလိုသည်ကို ရှင်းလင်းစွာဖော်ပြပါ။ ဥပမာ - "ဇာတ်ကောင် A အတွက် ကြေကွဲစရာ ကောင်းသော နောက်ခံဇာတ်လမ်းတစ်ခု ဖန်တီးရန်။")_

## 2. Context / ထည့်သွင်းရမည့် အချက်အလက်

> **အောက်ပါအချက်အလက်များကို Prompt မRunမီ ထည့်သွင်းရန် လိုအပ်ပါသည်။**

- **[Context 1: ဥပမာ - Character Profile Link]:** `[Link to CHAR_... .md]`
- **[Context 2: ဥပမာ - Story Bible Link]:** `[Link to relevant bible file]`
- **[Context 3: ဥပမာ - Key Constraints]:**
  - _Constraint 1: ဇာတ်လမ်းသည် အနာဂတ်တွင် ဖြစ်ပွားရမည်။_
  - _Constraint 2: ဇာတ်ကောင်သည် မိဘမဲ့ဖြစ်ရမည်။_

---

## 3. Prompt Body

> **Copy the text below and paste it into the AI.**

```
# ROLE
You are a world-class sci-fi author and world-builder. Your task is to generate creative and compelling content based on the provided context, adhering strictly to all constraints.

# CONTEXT
---
[Provide Character Profile Summary Here]
---
[Provide World Anvil / Universe Rules Here]
---

# TASK
[Clearly state the task here. For example: "Write a 500-word backstory for the character described above. The story must include a tragic event and explain their motivation to join 'The Rebellion'."]

# CONSTRAINTS
- [Constraint 1]
- [Constraint 2]
- Do not invent new major characters without permission.
- Adhere to the existing timeline.

# OUTPUT FORMAT
[Specify the desired output format, e.g., "Provide the output in Markdown format, with a clear heading for the backstory."]

```

---

## 4. အသုံးပြုပုံ မှတ်စု (Usage Notes)

_(ဤ Prompt ကို အကောင်းဆုံးအသုံးပြုနည်း၊ မည်သည့် AI Model Version နှင့် အဆင်ပြေဆုံးဖြစ်는지၊ နှင့် သတိပြုရမည့်အချက်များကို မှတ်သားပါ။)_

## 5. ผลลัพธ์ နမူနာ (Example Output)

<details>
<summary>Click to view a sample output</summary>

```markdown
(ဤနေရာတွင် AI မှ ရရှိခဲ့သော ကောင်းမွန်သည့် နမူနာအဖြေတစ်ခုကို ထည့်သွင်းထားနိုင်သည်)
```

</details>

---

## 6. Version History

- **v1.0 (DD-MM-YYYY):** Initial prompt creation.
- **v1.1 (DD-MM-YYYY):** Refined the TASK section for more clarity.
