---
name: ugc-video-script
description: "Generate UGC (user-generated content) style video ad scripts from a brand or product research dossier. Use this skill whenever the user wants to create video ad scripts for Higgsfield (or similar AI video tools), write car-talk / selfie-style UGC scripts, turn a research document into ad copy, or produce short-form social video dialogue. Triggers: \"ugc script\", \"video ad script\", \"higgsfield script\", \"car talk ad\", \"ugc ad\", \"talking head script\", \"write me a ugc video\", \"make a video script from this research doc\", \"turn this into an ad\", or whenever a research dossier is uploaded and the user wants ad output."
---

# UGC Video Script Generator

You are creating **UGC car-talk style video ad scripts** for Higgsfield (an AI video generation platform). The format is a person filming themselves talking directly into their phone — authentic, unscripted-feeling, like a friend telling you about something they genuinely love. The user will upload a starting photo and ending photo to Higgsfield separately; your job is purely to write the **spoken dialogue**, broken into clips.

---

## Step 1: Extract the Research Doc

If the user has uploaded a `.docx` research dossier, extract its text using python-docx:

```python
pip install python-docx --break-system-packages -q
```

```python
from docx import Document
import glob, os

upload_dir = next((p for p in [
    os.path.expanduser("~/mnt/uploads"),
    "/mnt/user-data/uploads",
] if os.path.exists(p)), None)

docx_files = glob.glob(os.path.join(upload_dir, "*.docx")) if upload_dir else []
if docx_files:
    doc = Document(docx_files[0])
    text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
    print(text[:10000])
```

Focus on extracting:
- **Product name** and core description
- **Top VoC (Voice of Customer) quotes** — real customer language is gold
- **Key benefits / motivations** (what people love about it)
- **Primary objections** (what holds people back)
- **Ad angles / hooks** already in the doc (Section G or "Messaging/Creative Playbook")
- **Target personas** (who buys this: stressed adults, parents, gift buyers, etc.)

---

## Step 2: Ask the User for Parameters

Use `AskUserQuestion` to gather:

1. **How many clips?** (determines video length)
   - 4 clips ≈ 16–24 seconds
   - 5 clips ≈ 20–30 seconds
   - 6 clips ≈ 24–36 seconds

2. **Which ad angle / hook?** Present 4–6 options pulled directly from the research doc's ad angles. Common types:
   - 🎯 **Discovery** — "I found this and had to tell you guys"
   - 😤 **Skeptic-to-Believer** — "I thought this was gonna be a gimmick but..."
   - 😩 **Problem/Solution** — "I've been looking for something to help me [pain point]..."
   - 🎁 **Gift Reveal** — "Okay I just wrapped the best gift ever..."
   - 👨‍👩‍👧 **Parent Win** — "I finally found something that gets my kids off screens..."
   - ✨ **Before/After** — "This time last month I had no idea how to [skill], now..."
   - (Add more based on what is actually in the research doc)

3. **Target persona?** (Optional — if the research doc has distinct personas like parents vs. adults vs. gift buyers)

---

## Step 3: Write the Script

### The Car-Talk UGC Voice

This is someone in their car, talking directly to camera on their phone. The tone is:
- **Conversational and genuine** — like a friend telling you something, not a spokesperson selling you something
- **Energetic but natural** — slightly breathless, excited, but not performative
- **Direct** — "I" statements, "you guys", "honestly", "I'm not kidding", "okay so"
- **No corporate speak** — no "introducing", no "premium quality", no "order today"
- **Uses real customer language** — pull actual phrases from the VoC section of the research doc

### Clip Structure (The Arc)

Each clip is ~4-6 seconds of natural speech = **15-22 words max**.

| Clip | Role | What It Does |
|------|------|--------------|
| 1 | **Hook** | Grabs attention — starts mid-thought, sparks curiosity or strong emotion |
| 2 | **Problem / Setup** | Establishes the relatable pain point or desire |
| 3 | **Discovery** | Introduces the product naturally, first impressions |
| 4 | **Proof / Detail** | One specific benefit or feature that lands the claim |
| 5 (if 5+) | **Social Proof / Detail** | Another proof point, what is included, or a result |
| Last clip | **Soft CTA** | Natural close — "I'll link it below", "10/10 recommend", "you need this" |

### Word Count Target

Aim for **15-20 words per clip** (conversational speech pace = 3-4 words/second, so 15-20 words = 4-5 seconds with natural pauses).

Avoid going over 22 words — it will feel rushed when spoken aloud.

### What Makes a Great UGC Hook (Clip 1)

The first clip must do one of these:
- Start mid-story: "Okay so I've been doing this thing every night..."
- Make a bold claim: "This completely changed how I decompress after work"
- Create curiosity: "I did NOT expect this to actually work"
- Flip expectation: "I thought this was gonna be some dumb little toy, but..."

**Never** start with the product name or brand name in clip 1. The viewer has not earned that yet.

---

## Step 4: Output Format

Use this exact format for each script:

## [AD ANGLE NAME] — [Product Name]
**Persona:** [Target Persona] | **Length:** [X clips x ~5s = ~Xs]

**[CLIP 1]** 0:00 - 0:05
"[Exact dialogue here — as it would be spoken]"
(X words)

**[CLIP 2]** 0:05 - 0:10
"[Dialogue]"
(X words)

**[CLIP N]** ...

Higgsfield Notes:
- Upload starting photo for Clip 1 hook feel
- Upload ending photo for final CTA clip
- Each clip = separate Higgsfield generation

---

## Step 5: Quality Check

Before outputting, mentally read each line at natural speech pace. Ask:

- Does it sound like something a real person would actually say in their car?
- Is it under 22 words?
- Does the arc build and land with a satisfying close?
- Does the script use any actual customer language from the VoC section?
- Does the hook (clip 1) create curiosity without revealing the product name too early?
- Is there at least one concrete, specific detail (not just vague benefits)?

---

## Example Output Reference

SKEPTIC-TO-BELIEVER — Table Clay Mini Pottery Wheel
Persona: Stressed Adult / Creative Hobbyist | Length: 5 clips x ~5s = ~25s

[CLIP 1] 0:00 - 0:05
"Okay I need to tell you about the thing that actually gets me off my phone for an hour."
(19 words)

[CLIP 2] 0:05 - 0:10
"I thought a mini pottery wheel was gonna be some little kids toy, honestly was skeptical."
(17 words)

[CLIP 3] 0:10 - 0:15
"But I've been doing it every night to decompress and it is genuinely so therapeutic."
(16 words)

[CLIP 4] 0:15 - 0:20
"Clay comes with it, the tools, everything — you plug it in and you're literally throwing pots."
(17 words)

[CLIP 5] 0:20 - 0:25
"I'm not a crafty person at all but I'm actually proud of what I made. Link's below."
(18 words)

---

## Notes on Research Doc Sections to Mine

- **"Top 25 Copy-Ready Quotes"** — Use these verbatim or near-verbatim in scripts
- **"Voice of Customer (VoC)"** — Real language from actual buyers
- **"Ad Angles" (usually Section G or "Creative Playbook")** — Pre-built angle ideas
- **"Objection Kill Sheet"** — Turn objections into script moments
- **"Above-the-Fold Promises"** — These often make great clip 2 or 3 hooks
- **"Gift Positioning"** — For gift-angle scripts specifically

The best scripts do not sound like marketing copy — they sound like a real customer who absorbed the key selling points without realizing it.
