---
name: brand-context-builder
description: Generate structured brand context files for the social media system (engagement, ads research, content creation) by distilling existing deep research documents into actionable brand profiles. Use whenever a user wants to add a new brand, create a brand profile, set up brand context, or says things like "new brand", "add brand", "brand file", "brand context for [name]", "set up [brand name]", or wants to turn a research document into a usable brand context file. Also use when updating or editing an existing brand context file. The skill reads the brand's deep research document (30-80 page .md files stored in GitHub), interviews the user for anything missing, researches competitors, and outputs a complete brand-{name}.md file ready for use across all social media skills.
---

# Brand Context Builder

This skill turns deep brand research documents into structured brand context files (`.md`) that power the entire social media system — engagement commenting, ad research, content creation, and competitive analysis.

Every brand in the system has a deep research document (typically 30-80 pages) that contains comprehensive market analysis, customer research, product details, and strategic context. These research docs are the source of truth. This skill distills them into a focused, structured "quick reference card" that other skills and automations can consume without loading 80 pages of context.

## How It Fits Into the System

```
github-repo/
├── research/
│   ├── tableclay-research.md       ← Deep research doc (30-80 pages, SOURCE OF TRUTH)
│   ├── preppack-research.md
│   ├── aniwove-research.md
│   ├── leaflofts-research.md
│   └── trendytee-research.md
├── brands/
│   ├── brand-tableclay.md          ← What this skill creates (distilled context)
│   ├── brand-preppack.md
│   └── ...
└── skills/
    └── social-media-engagement/
        └── ...
```

The deep research docs contain everything — market sizing, customer interview transcripts, competitive landscape, product specs, brand strategy, etc. The brand context file this skill creates is a curated extract: just the pieces that social media skills need to do their job.

## Workflow

### Step 1: Locate and Read the Deep Research Document

When the user says they want to create or update a brand context file:

1. **Ask which brand** (if not obvious from the conversation)
2. **Ask for the research doc** — either a file path, a GitHub URL, or have them paste/upload it
3. **Read the full research document** — this is your primary source material

The research doc is the backbone. Everything in the brand context file should trace back to it. If the research doc doesn't cover something (like social media handles or Chrome profile name), that's where the user interview fills gaps.

### Step 2: Extract Key Information from the Research Doc

Read through the research document and pull out:

**From the research doc (should be in there):**
- Brand name, positioning, and value proposition
- Product lines with descriptions, features, and pricing
- Target customer segments and personas
- Market positioning and competitive landscape
- Brand personality and communication style
- Key selling points and objection handling
- Content themes and cultural context the brand operates in

**Likely NOT in the research doc (ask the user):**
- Social media handles (Instagram, TikTok, Facebook)
- Chrome profile name (for automation — the exact name of the Chrome profile logged into this brand's accounts)
- Specific competitors' social handles (research doc may have competitor names but not their IG handles)

For anything not in the research doc, ask the user. But keep it light — mark unknowns as `_TBD_` rather than blocking the whole file on missing Instagram handles.

### Step 3: Research Social Media Competitors

The research doc likely names competitors, but may not include their social media handles or assess their social presence specifically. Use web search to:

1. Find the social handles for competitors named in the research doc
2. Assess which ones have active social media presence (follower counts, post frequency)
3. Add 1-2 additional competitors the research doc missed — specifically social media competitors (accounts the target audience follows that may not be direct product competitors)

For each competitor, capture:
- Their primary social handle (Instagram preferred)
- Why they compete (one line)
- Approximate follower count if available

### Step 4: Craft the Brand Voice for Social Media

The research doc likely describes brand personality and tone in a marketing/strategy context. Your job is to translate that into a social media engagement voice — how the brand sounds when leaving comments, replying to DMs, posting stories.

This translation matters because "premium, trustworthy, innovative" (strategy voice) becomes something like "confident but approachable, like a knowledgeable friend who's genuinely excited about the product" (social voice).

To nail this:
1. Pull the brand personality descriptors from the research doc
2. Translate them into social media comment style
3. Write 3-4 example comments that capture the tone — these are the north star. They should sound like a real human on social media, not a brand guideline document.
4. Note what the voice is NOT (not salesy, not corporate, not preachy, etc.)

If the research doc doesn't have enough on voice, ask the user: "If your brand were a person commenting on someone's Instagram post, what would they sound like?"

### Step 5: Determine Output Depth

The template has two levels:

**Standard (for most brands):** Brand overview, products, target customers, content themes, competitors, brand voice, and a reference back to the deep research doc. This covers social media engagement, content planning, and basic strategy.

**Extended (for brands with active ad programs):** Adds tag taxonomy (angles by product line with enums), detailed personas, intent context (job-to-be-done), objection targets with counters, proof types, and filename conventions. Build this when the brand has enough product complexity and the user needs structured ad creative support.

If the research doc has detailed persona work, objection handling, and product angle analysis, default to Extended — the information is already there, you're just structuring it. If the research doc is more high-level, start with Standard.

### Step 6: Generate the Brand Context File

Use the template in `references/brand-template.md` to produce the final file.

At the bottom, always include the reference back to the source research document:

```markdown
## Source Research

This brand context file was distilled from the deep research document:
- **Research doc**: `research/{brand-name}-research.md`
- **Last synced**: {date}

For comprehensive brand strategy, market analysis, customer research, and detailed product specifications, refer to the full research document.
```

This creates a clear chain: research doc → brand context file → social media skills. Anyone reading the brand context file knows where to go for deeper information.

### Step 7: Save and Confirm

Save the file as `brand-{name}.md` (kebab-case, lowercase). Confirm with the user by:
- Summarizing what sections are filled out
- Flagging any `_TBD_` fields
- Noting whether it's Standard or Extended format
- Confirming the research doc path is correct

## Output Naming Convention

Files are always named `brand-{name}.md` where `{name}` is the brand name in lowercase kebab-case:
- Table Clay → `brand-tableclay.md`
- PrepPack → `brand-preppack.md`
- Leaf Lofts → `brand-leaflofts.md`

## When Updating an Existing Brand File

If the user wants to update a brand context file:
1. Read the existing brand context file
2. Read the current research doc (it may have been updated)
3. Identify what's changed in the research doc since last sync
4. Update the brand context file accordingly
5. Update the "Last synced" date

## Common Patterns

**User provides the research doc directly**: Best case — read it, distill it, ask a few gap-filling questions, output the file.

**User describes the brand conversationally (no research doc yet)**: Build the brand context file from their description + competitor research. Note in the Source Research section that no deep research doc exists yet: `Research doc: _Not yet created_`.

**User wants multiple brands at once**: Read all research docs, research competitors in parallel, output all files together.

**User says "update the brand file, the research doc changed"**: Diff the research doc against the existing brand context file, update only what's changed, bump the sync date.

## Reference Files

- `references/brand-template.md` — The fill-in template for both Standard and Extended formats
- `references/example-tableclay.md` — A complete example showing the Extended format with all sections filled out, distilled from the Table Clay research document
