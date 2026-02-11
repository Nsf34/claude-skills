---
name: blog-post-generator
description: |
  Research-backed blog post generator. Reads a product research dossier from Desktop/Brands/[BrandName]/ and transforms it into SEO-optimized blog posts where every claim, quote, and data point traces directly back to the research. Supports 8 post types: buying guides, comparison posts, problem-solution articles, FAQ/myth-busting, gift guides, educational posts, customer stories, and listicles. Outputs CMS-ready markdown with a companion research map that documents exactly which dossier section sourced each piece of content. No generic filler — everything is research-anchored.

  TRIGGERS: blog post, write a blog, buying guide, comparison article, comparison post, product comparison, FAQ post, gift guide article, listicle, reasons why, content from research, blog from dossier, write content from the dossier, SEO content, content marketing, blog post for [brand], create a buying guide, write a comparison post, turn research into content, blog content, product blog, customer story post, myth-busting post, educational post

  Do NOT use for: creating research dossiers (use product-research), ad copy or image generation (use ad-swipe-engine or native-image-ad-generator), Meta Ad Library research (use meta-ads-research), email marketing, social media posts, landing page copy, or video scripts.
---

# Blog Post Generator

Transforms a product research dossier into a blog post where every claim is traceable to the research. The dossier is the single source of truth — the blog post reshapes and repackages those findings for a reader, never introducing unsourced claims or fabricated quotes.

## Why This Matters

Generic AI blog posts are full of vague claims, synthetic quotes, and filler. This skill produces something different: content where every factual statement, every customer quote, every competitor comparison comes from a rigorous research dossier that was built from real market data, real reviews, and real competitive intelligence. The research map companion document makes the provenance verifiable.

## Quick Reference

| Step | What Happens | User Interaction |
|---|---|---|
| 1. Input | Receive brand, product, and preferences | User provides these |
| 2. Find dossier | Locate in `Desktop/Brands/[BrandName]/` | None (auto) or confirm if ambiguous |
| 3. Select post type | Choose from 8 types | User selects or auto-detected from request |
| 4. Extract research | Build focused brief from relevant dossier sections | None (internal) |
| 5. Generate post | Write section by section, anchored to research | None (auto) |
| 6. Format & output | Save markdown + research map | Deliver to user |
| 7. Quality check | Verify against 7 QC dimensions | Report results |

## Workflow

### Step 1: Gather Inputs

The user provides:
- **Brand name** (required) — used to locate the dossier folder
- **Product name** (required if multiple dossiers exist for the brand)
- **Post type** (optional) — if not specified, recommend based on the user's goal or present choices
- **Target keyword** (optional) — primary SEO keyword. If not provided, derive from product name + post type
- **Tone preference** (optional) — informational, conversational, authoritative. Defaults per post type
- **Word count target** (optional) — defaults per post type

If the user's request implies a post type (e.g., "write a buying guide for Table Clay"), auto-select it. If the request is open-ended (e.g., "write a blog post about Table Clay"), present the 8 types and let them choose.

### Step 2: Locate and Read the Dossier

Research dossiers live in `Desktop/Brands/` on the user's computer:

```
Desktop/Brands/
├── [BrandName]/
│   ├── [Product Name] — Deep Research Dossier.docx
│   └── ...
```

**Locating the file:**
1. List `Desktop/Brands/[BrandName]/` (try casing variations: exact, title case, lowercase)
2. Match `.docx` files containing "Deep Research Dossier" to the user's product name (fuzzy match)
3. If no match or ambiguous, show available files and ask

**Reading the dossier:**
Use `python -m markitdown [file.docx]` to extract the full dossier content. If markitdown is unavailable, use python-docx extraction as a fallback.

Read the entire dossier. Parse it into the 10 standard sections (S1–S10 + References). Briefly confirm to the user which dossier you found and that it loaded successfully.

### Step 3: Select Post Type

If not already determined from the user's request, present the options:

| # | Post Type | Best For | Draws From |
|---|-----------|----------|------------|
| 1 | **Buying Guide** | Decision-stage readers comparing options | Market landscape, competitors, pricing |
| 2 | **Problem-Solution** | Readers who know their problem, not the solution | Pain points, objections, personas |
| 3 | **Comparison Post** | "[Product A] vs [Product B]" searches | Competitor teardown, pricing, VoC |
| 4 | **Educational ("Why [Category]")** | Top-of-funnel awareness | Market trends, motivations, personas |
| 5 | **Gift Guide** | Seasonal/occasion-driven traffic | Gift positioning, personas, pricing tiers |
| 6 | **FAQ / Myth-Busting** | Objection-heavy search queries | Objection kill sheet, VoC concerns |
| 7 | **Customer Story / Use Case** | Social proof and relatability | Verbatim quotes, personas, VoC |
| 8 | **Listicle ("X Reasons")** | Shareable, scannable content | Ad angles, motivations, competitor gaps |

If the user doesn't have a preference, recommend based on which dossier sections are richest. A dossier with a strong Objection Kill Sheet suggests FAQ/Myth-Busting. One with rich Contextual Positioning suggests a Gift Guide. Strong competitor data suggests a Buying Guide or Comparison Post.

### Step 4: Extract Relevant Research

Before writing, build a **Research Extract** — the focused subset of dossier data that feeds the chosen post type. This prevents scattered, unfocused content.

Read `references/research-anchoring-protocol.md` for the extraction rules.

Read the relevant section of `references/post-type-templates.md` for the dossier-section mapping table for the chosen post type. This table tells you exactly which dossier sections feed which blog sections.

For each mapped section:
1. Pull the relevant data from the dossier
2. Note the source code (S1–S10)
3. Note where it will appear in the blog post

Also pull 3-6 verbatim quotes from S2 (Top 25 Quotes) and S5 (VoC themed quotes) that serve the post's angle.

### Step 5: Generate the Blog Post

Write the blog post section by section, following the structural template from `references/post-type-templates.md`.

**Core rules:**

1. **Research anchoring** — every factual claim traces to a dossier section. See `references/research-anchoring-protocol.md` for the five anchoring rules.

2. **Verbatim quotes only** — customer quotes come from the dossier's S2 or S5. Never generate synthetic quotes. Format as blockquotes with simplified attribution.

3. **Dossier-sourced competitor data** — competitor names, pricing, and features come from S4 and S10 only. No ad-hoc web lookups.

4. **Persona-grounded audience content** — "who this is for" sections draw from S8 persona profiles.

5. **Blog voice, not dossier voice** — the dossier is analytical and strategic. The blog post should be conversational, warm, and reader-friendly. Adapt the substance without copying the dossier's tone.

**SEO integration:**

Read `references/seo-and-structure-guide.md` for SEO rules. Key requirements:
- Primary keyword in title, first 100 words, 2-3 H2 headings, meta description
- YAML frontmatter with title, meta_description, target_keyword, date
- Heading hierarchy: single H1, logical H2/H3 nesting
- Include image placeholders with descriptive alt text where visuals would add value

### Step 6: Format and Output

Generate these deliverables:

**A. Blog post markdown (.md)** — Primary output
- YAML frontmatter (title, meta_description, target_keyword, date, author, category, tags)
- Full blog post content
- Internal linking suggestions at the end (3-5 other post types from the same dossier)
- Save to: `Desktop/Brands/[BrandName]/Blog Posts/[post-title-slug].md`

**B. Research map (.md)** — Provenance document
- Maps every blog section to its dossier source(s)
- Lists all quotes used with their dossier origin
- Notes thin sections and unused high-value research
- Save to: `Desktop/Brands/[BrandName]/Blog Posts/[post-title-slug]_research-map.md`

**C. Word document (.docx)** — Optional, only if the user requests it
- Professional formatting per `assets/blog-post-docx-template.md`
- Save to: `Desktop/Brands/[BrandName]/Blog Posts/[post-title-slug].docx`

Create the `Blog Posts/` subfolder if it doesn't exist.

### Step 7: Quality Check

Before delivering, run the QC checklist from `references/quality-checklist.md`. Seven dimensions:

1. **Research Anchoring** — every claim traces to dossier
2. **Quote Authenticity** — all quotes verbatim from dossier
3. **Competitor Accuracy** — data matches dossier
4. **SEO Compliance** — keyword placement, meta description, frontmatter
5. **Structural Integrity** — heading hierarchy, word count, template adherence
6. **Tone Calibration** — blog voice, not marketing or academic
7. **Completeness** — all deliverables present, correctly saved

Report the QC results to the user briefly. If any dimension needs fixing, fix it before delivering.

**Delivery message format:**

```
Done — [word count]-word [post type] generated.
[N] verbatim customer quotes used, [N] competitors referenced,
[N] objections addressed.

Blog post: [path]
Research map: [path]

Suggested next posts from this dossier: [2-3 post types that
would complement this one and build a content cluster]
```

## Post Type Reference

For the full structural template, dossier mapping, tone guidance, and word count for each post type, read `references/post-type-templates.md`.

## Research Anchoring Rules

For the complete protocol on how every claim traces back to the dossier — including the Research Extract process, the five anchoring rules, quote handling, and the Research Map format — read `references/research-anchoring-protocol.md`.

## SEO Guidelines

For keyword placement rules, heading hierarchy, meta descriptions, readability targets, and internal linking strategy, read `references/seo-and-structure-guide.md`.

## Quality Checklist

For the 7-dimension QC rubric with Pass/Needs Fix/Fail scoring, read `references/quality-checklist.md`.

## .docx Formatting

If the user requests Word output, read `assets/blog-post-docx-template.md` for the formatting spec.

## Error Handling

### Research dossier not found
List contents of `Desktop/Brands/` and subfolders. Ask user to confirm brand/product name. If no dossier exists, suggest running the product-research skill first.

### Dossier section is thin or missing
Check if alternative sections can fill the gap. If not, reduce scope rather than fabricate content. Note the gap in the Research Map. If a critical section for the chosen post type is missing, suggest an alternative post type that works better with the available data.

### python-docx / markitdown extraction failure
Try the alternative extraction method. If both fail, ask the user to export the dossier content manually (copy-paste or PDF export).

### No target keyword provided
Derive a reasonable keyword from the product name + post type. For example: brand "Table Clay" + product "Mini Pottery Wheel" + post type "Buying Guide" → keyword "mini pottery wheel buying guide."

## Scope

**Handles:** Transforming product research dossiers into 8 types of SEO-optimized blog posts with full research provenance tracking.

**Does NOT handle:** Creating research dossiers (use product-research), ad copy/images (use ad-swipe-engine or native-image-ad-generator), Meta Ad Library research (use meta-ads-research), video scripts, email marketing, social media content, landing page copy, keyword research, or content calendar planning.

## Content Cluster Strategy

A single research dossier supports all 8 post types. After generating the first post, suggest which additional post types would work well — prioritizing:

1. A **decision-stage** post (Buying Guide or Comparison) for high-intent traffic
2. A **consideration-stage** post (FAQ or Problem-Solution) for objection resolution
3. An **awareness-stage** post (Educational or Listicle) for top-of-funnel reach

Three interlinked posts from the same dossier create a content cluster that strengthens SEO for all posts in the group.
