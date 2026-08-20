# Future Build System

ဤစာမျက်နှာသည် `SOCIALAUTOUPLOAD_UNIVERSE` Repository ကို အနာဂတ်တွင် PDF, EPUB, Hardcover Website စသည့် ပုံစံအမျိုးမျိုးသို့ အလွယ်တကူ ထုတ်ဝေ (Build) နိုင်ရန်အတွက် ကြိုတင်ပြင်ဆင်ထားသော ဗိသုကာဆိုင်ရာ အချက်အလက်များကို ရှင်းပြရန်ဖြစ်သည်။

ဤအဆင့်တွင် Code များရေးသားခြင်း မရှိသေးသော်လည်း၊ လက်ရှိတည်ဆောက်ထားသော Repository Foundation သည် အနာဂတ် Build Process အတွက် မည်သို့ အထောက်အကူပြုသည်ကို ဖော်ပြထားသည်။

---

## 1. အဓိက နည်းပညာ (Core Technology)

ကျွန်ုပ်တို့၏ Build System သည် **Pandoc** ကို အဓိကထား၍ တည်ဆောက်ရန် ရည်ရွယ်ပါသည်။ Pandoc သည် Markdown ဖိုင်များကို အခြားသော Document Format များ (PDF, EPUB, HTML, DOCX) စသည်သို့ ပြောင်းလဲပေးနိုင်သော universal document converter ဖြစ်သည်။

## 2. ကြိုတင်ပြင်ဆင်ထားမှုများ (Architectural Preparations)

### 2.1 တသမတ်တည်းဖြစ်သော Markdown Syntax
- Repository တစ်ခုလုံးတွင် `REPOSITORY_RULES.md` ၌ သတ်မှတ်ထားသော Markdown Style Guide ကို တသမတ်တည်း လိုက်နာခြင်းသည် Pandoc ဖြင့် ပြောင်းလဲသည့်အခါ ဖြစ်ပေါ်လာနိုင်သော Error များကို အလွန်အမင်း လျှော့ချပေးသည်။
- Heading Style, Table Style, Comment Style တို့ကို စည်းမျဉ်းအတိုင်းသုံးခြင်းဖြင့် ထွက်လာမည့် Output သည် ကြိုတင်ခန့်မှန်းနိုင်ပြီး တည်ငြိမ်မှုရှိမည်ဖြစ်သည်။

### 2.2 Metadata in Templates
- Template ဖိုင်တိုင်း၏ ထိပ်ပိုင်းတွင် `Title`, `Author`, `Version`, `Date` ကဲ့သို့သော Metadata များကို YAML Front Matter ပုံစံ (`--- ... ---`) ဖြင့် အလွယ်တကူ ပြောင်းနိုင်သော ပုံစံဖြင့် ထည့်သွင်းထားသည်။
- Pandoc သည် ဤ Metadata များကို နားလည်ပြီး PDF သို့မဟုတ် EPUB ၏ Title Page, Header/Footer များတွင် အလိုအလျောက် ထည့်သွင်းပေးနိုင်သည်။

### 2.3 အပိုင်းလိုက်ခွဲထားသော ဖွဲ့စည်းပုံ (Modular Structure)
- Master Bible ကို `Part_01`, `Part_02` စသဖြင့် အပိုင်းလိုက်၊ အခန်းလိုက် ဖိုင်များခွဲ၍ တည်ဆောက်ထားခြင်းသည် Build Process ကို လွယ်ကူစေသည်။
- ဥပမာ - PDF ထုတ်သည့်အခါ ဖိုင်အားလုံးကို ပေါင်း၍ စာအုပ်တစ်အုပ်အဖြစ် ထုတ်နိုင်သလို၊ `Part_03_Characters` ကို သီးသန့် "Character Bible" PDF အဖြစ်လည်း ထုတ်နိုင်သည်။
- Pandoc command line တွင် မည်သည့်ဖိုင်များကို မည်သည့်အစဉ်လိုက် ပေါင်းစည်းရမည်ကို သတ်မှတ်ပေးရုံသာဖြစ်သည်။

### 2.4 Cross-Referencing
- `REPOSITORY_RULES.md` တွင် သတ်မှတ်ထားသော Cross-Reference Rule (``[text](path/to/file.md)``) သည် Pandoc ဖြင့် build လုပ်သည့်အခါ Clickable Link များ၊ Page Number Reference များအဖြစ် အလိုအလျောက် ပြောင်းလဲသွားရန် အခြေခံဖြစ်သည်။
- `pandoc-crossref` ကဲ့သို့သော filter များကို အသုံးပြု၍ `@fig:1`, `@tbl:2` ကဲ့သို့သော ပုံများ၊ ဇယားများကို အညွှန်း (label) တပ်ပြီး "see Figure 1 on page 24" ကဲ့သို့သော reference များကို အလိုအလျောက် generate လုပ်နိုင်မည်ဖြစ်သည်။

## 3. အနာဂတ်တွင် Build လုပ်နိုင်မည့် Feature များ

### 3.1 Clickable Table of Contents (TOC)
- Markdown ဖိုင်များတွင် Heading (`#`, `##`, `###`) များကို စနစ်တကျသုံးထားခြင်းကြောင့် Pandoc ဖြင့် `--toc` flag ကိုသုံးလိုက်ရုံဖြင့် Clickable TOC ကို အလွယ်တကူ ထည့်သွင်းနိုင်မည်ဖြစ်သည်။

### 3.2 Header & Footer
- Page Number, Version History, Chapter Title တို့ကို Header/Footer တွင် ထည့်သွင်းရန် LaTeX template များကို အသုံးပြု၍ Pandoc ကို customize လုပ်နိုင်မည်ဖြစ်သည်။ ကျွန်ုပ်တို့၏ metadata structure သည် ၎င်းကို support လုပ်ရန် အသင့်ဖြစ်နေသည်။

### 3.3 Index & Glossary
- `MASTER_INDEX.md` နှင့် `GLOSSARY.md` ဖိုင်များကို စာအုပ်၏ နောက်ဆက်တွဲ Index နှင့် Glossary အဖြစ် အလိုအလျောက် ထည့်သွင်းရန် Pandoc script များ ရေးသားနိုင်မည်ဖြစ်သည်။

## 4. နမူနာ Pandoc Command (အနာဂတ်အတွက်)

```bash
# This is a future example, not for current use.
# Builds a PDF of the entire story from Part 4.

pandoc 
  --from markdown 
  --to pdf 
  --output "SOCIALAUTOUPLOAD_STORY_v1.pdf" 
  --resource-path="." 
  --include-in-header="Styles/header.tex" 
  --toc 
  --toc-depth=2 
  --number-sections 
  -V "title:SOCIALAUTOUPLOAD UNIVERSE - Story Bible" 
  MASTER_BIBLE/Part_01_Universe/CHAP_01_Canon.md 
  MASTER_BIBLE/Part_01_Universe/CHAP_02_Vision.md 
  # ... and so on
```

## နိဂုံးချုပ်
လက်ရှိ Repository ၏ တည်ဆောက်ပုံသည် Manual Copy-Paste လုပ်ရန်မလိုဘဲ၊ Automation ဖြင့် Professional Quality Document များ ထုတ်လုပ်နိုင်ရန် အခြေခံအုတ်မြစ်ကို ခိုင်မာစွာ ချပေးထားပြီးဖြစ်သည်။


## 5. Current Helper Scripts

- `BUILD/validate_repository.py` checks required core files, broken Markdown links, H1 counts, and duplicate chapter numbers.
- `BUILD/master_bible_files.txt` defines the current export order.
- `BUILD/build_master_bible.sh` runs validation first, then builds a PDF when Pandoc is installed.
