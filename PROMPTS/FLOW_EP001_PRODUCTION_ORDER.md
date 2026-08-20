# Google Flow Production Order - EP001

## Correct Order

Video မထုတ်ခင် အောက်ပါအစဉ်အတိုင်းလုပ်ပါ။

1. Create Characters
   - CHR001 Min Thant
   - CHR002 King Kyawzwa
   - CHR003 Queen Thiri Devi
   - CHR004 U Nanda / Shadow Leader

2. Create Locations / Scenes
   - LOC001 Maha Shwe Palace
   - LOC002 Royal Archives
   - LOC003 Messenger Relay Station / Road
   - LOC004 Royal Communication Department

3. Create Props
   - PROP001 Royal Seal
   - PROP002 Archive Scroll / Ledger
   - PROP004 Messenger Bell
   - BRAND001 SocialAutoUpload End Card

4. Then create EP001 video scene.

5. After Clip 01-07 are approved, assemble the final episode.
   - Use `FLOW_S01E001_FINAL_ASSEMBLY_PLAN.md`.
   - Append the official BRAND001 end card separately.
   - Do not generate the logo or end card inside story clips.

## Why This Order

Flow/Veo video consistency အတွက် character face, costume, location color, prop design ကိုအရင် lock လုပ်ရမည်။ အဲ့ဒါမလုပ်ဘဲ episode prompt တန်းထည့်လျှင် character မတူခြင်း၊ palace style မတူခြင်း၊ Myanmar culture consistency ပျက်ခြင်း ဖြစ်နိုင်သည်။

## Browser Note

Flow prompt box သည် automation paste/fill နှင့် crash ဖြစ်နိုင်သည်။ Therefore:

- Codex prepares prompts.
- User manually pastes each prompt into Flow.
- Codex reviews output and iterates prompts.

## EP001 After Setup

Characters/scenes/props created ပြီးပြီဖြစ်သောကြောင့် Flow video generation အတွက် `FLOW_S01E001_10S_CLIP_PROMPTS.md` ကိုအရင်သုံးပါ။ Flow ၏ current video mode သည် 10s clip ဖြစ်ပြီး long prompt paste လုပ်လျှင် UI crash ဖြစ်နိုင်သောကြောင့် S01E001 ကို Clip 01 မှ Clip 07 အထိ ခွဲထုတ်ပါ။

`FLOW_S01E001_FINAL_VIDEO_PROMPT.md` သည် episode တစ်ခုလုံးအတွက် full reference prompt ဖြစ်ပြီး, `PROMPT_S01E001_Package.md` သည် episode concept skeleton အဖြစ်သာထားပါ။

Clip 01 မှ Clip 07 အထိ approve ပြီးသွားလျှင် final edit အတွက် `FLOW_S01E001_FINAL_ASSEMBLY_PLAN.md` ကိုသုံးပါ။ Story clips ထဲတွင် logo/end card မထည့်ရပါ။ Official `logo.png` ပါသော BRAND001 end card ကို final edit အဆုံးတွင်သာ append လုပ်ရမည်။
