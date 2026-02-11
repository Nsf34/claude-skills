# Research Anchoring Protocol

This document defines how every piece of content in a blog post traces back to the product research dossier. The goal is simple: no claim in the blog post should exist without a home in the research. This is what separates research-backed content from generic AI writing.

## The Core Principle

The dossier is the single source of truth. The blog post reshapes and repackages dossier findings into a reader-friendly format — it does not introduce new research, fabricate data points, or generate synthetic customer voices.

If a blog section cannot be grounded in a specific dossier section, that section either needs to be rewritten to draw from the research, or it shouldn't exist in the post.

## Dossier Section Reference Key

Use these shorthand codes when building the Research Extract and Research Map:

| Code | Dossier Section | What It Contains |
|------|----------------|-----------------|
| S1 | Executive Summary | Synthesized top findings, go-to-market implications |
| S2 | Top 25 Copy-Ready Quotes | Verbatim customer quotes with source attribution |
| S3 | Market Landscape Overview | 5-8 product categories, alternatives, needs-to-category mapping |
| S4 | Competitor & Offer Teardown | 8-12 competitor table + strengths/gaps narrative |
| S5 | Voice of Customer Analysis | Motivations, objections, themed verbatim quotes |
| S6 | Objection Kill Sheet | 12-15 objections with cause, rebuttal, microcopy, placement |
| S7 | Contextual Positioning | Gift, professional, seasonal, or occasion-based angles |
| S8 | Persona-Specific Positioning | 3-5 personas with messaging, objections, channels |
| S9 | Messaging Hierarchy & Ad Angles | Core promises, supporting bullets, 10-15 ad angle concepts |
| S10 | Pricing & Bundling Insights | Competitive pricing, bundle tiers, pricing psychology |
| REF | References | Numbered citation list (30-80+ sources) |

---

## Building the Research Extract

Before writing any blog post, build a **Research Extract** — a focused brief containing only the dossier data relevant to the chosen post type. This prevents the common failure mode of trying to use everything and ending up with a scattered, unfocused post.

### How to Build an Extract

1. Check the post-type template in `references/post-type-templates.md` for the dossier-section mapping table
2. Pull only the mapped sections from the dossier
3. Within each pulled section, select only the data points that serve the post's angle
4. Organize the extract by blog section order (not dossier section order)

### What to Include in the Extract

For each data point you pull, note:
- The data itself (quote, statistic, competitor name, pricing data, etc.)
- The source section code (S1–S10)
- Where you plan to use it in the blog post

### Example Extract Entry

```
Blog Section: "What Real Customers Say"
Source: S2, Quote #7
Data: "I was shocked how easy it was to center clay on my first try. The YouTube tutorials that come with it actually work." — 5-star Amazon review
Planned Use: Blockquote supporting the ease-of-use argument
```

---

## Content Anchoring Rules

These five rules govern how dossier research appears in the blog post.

### Rule 1: Every Factual Claim Cites a Dossier Section

Any sentence that states a fact, makes a comparison, or asserts a market position must trace back to a specific dossier section.

**Acceptable:**
- "The at-home pottery market has grown significantly, with DIY craft kits seeing sustained interest since 2020." → Sourced from S3 (Market Landscape)
- "Most beginners worry about the mess — and it's the #1 objection across competitor reviews." → Sourced from S6 (Objection Kill Sheet)

**Not acceptable:**
- "Pottery is one of the fastest-growing hobbies in America." → No dossier source, likely hallucinated statistic
- "Studies show that creative activities reduce stress by 45%." → External claim not in the dossier

### Rule 2: Customer Quotes Must Be Verbatim

Never generate synthetic customer quotes. If the dossier has a quote that fits, use it exactly as written with attribution. If no quote fits a section, do not invent one — use a paraphrased insight instead and note the source.

**How to use dossier quotes in blog posts:**

From Section 2 (Top 25 Quotes): These are pre-selected as "copy-ready" — use them as primary blockquotes.

From Section 5 (VoC themed quotes): These provide additional depth by theme — use them to support specific arguments.

**Format in the blog post:**
```markdown
> "I was shocked how easy it was to center clay on my first try. The YouTube tutorials that come with it actually work."
> — Verified Amazon Review
```

Simplify attribution for the blog audience. Dossier says "5★ Amazon review" → blog says "Verified Amazon Review". Dossier says "Reddit r/pottery" → blog says "Reddit user". The reader doesn't need the granularity the dossier provides.

**Quote selection guidance:**
- 3-6 quotes per blog post (varies by post type)
- Spread throughout the post, not clustered in one section
- Choose quotes that do work — proving a claim, humanizing a data point, or overcoming an objection
- Vary the emotional tone across selected quotes (not all enthusiasm — include thoughtful, surprised, relieved)

### Rule 3: Competitor Data Comes from the Dossier Only

Do not introduce competitors, pricing, or product details not present in the dossier's Section 4 (Competitor Teardown) or Section 10 (Pricing).

If the blog post type requires comparing products (Buying Guide, Comparison Post), use the competitor table from S4 as the authoritative source. The blog may feature a subset (3-5 of the 8-12 competitors) for readability, but the data must originate from the dossier.

**Pricing caveat:** Acknowledge that pricing may have changed since research was conducted. Use language like "at the time of our research" or "starting around $X" rather than presenting prices as guaranteed current.

### Rule 4: Persona Content Maps to Dossier Personas

When writing persona-specific content (who a product is "best for," use case sections, audience-targeted paragraphs), draw directly from Section 8's persona profiles.

Use the dossier's persona names, motivations, anxieties, and messaging guidance. Do not invent new personas or rename existing ones in ways that lose the dossier's specificity.

If the blog post targets a single persona, note which one in the Research Map and use only that persona's messaging guidance to set the tone and proof points.

### Rule 5: Objection Handling Uses Section 6 Rebuttals

FAQ sections, myth-busting content, and "common concerns" blocks should draw directly from the Objection Kill Sheet (S6). Each objection entry in the dossier contains:

- The objection in the customer's own words
- Root cause analysis
- Rebuttal strategy
- Ready-to-use microcopy

Adapt the tone for blog format (more conversational than the dossier's strategic tone), but keep the substance intact. The dossier's rebuttals were developed from real customer language — preserve that grounding.

---

## Handling Thin Sections

Some dossiers will have stronger coverage in certain sections than others. Section 7 (Contextual Positioning) is explicitly optional in the dossier template.

When a post type depends on a thin or missing section:

1. **Check if alternative sections can fill the gap.** S5 (VoC) often contains data that could serve S7's purpose. S9 (Ad Angles) often has insights that could supplement S8 (Personas).
2. **Reduce scope rather than fabricate.** If the dossier has weak gift positioning data, write a shorter gift guide section rather than inventing gift angles.
3. **Flag it.** Note in the Research Map which sections were thin and how you adapted. This transparency helps the user decide whether to re-run the product-research skill for deeper coverage.

---

## The Research Map

Every blog post is accompanied by a `_research-map.md` file that documents exactly what came from where. This is the accountability mechanism.

### Research Map Format

```markdown
# Research Map: [Blog Post Title]

## Source Dossier
[Product Name] — Deep Research Dossier.docx
Located at: Desktop/Brands/[BrandName]/

## Section-by-Section Provenance

| Blog Section | Dossier Source(s) | Specific Data Used |
|-------------|-------------------|-------------------|
| Introduction | S5: VoC (motivations) | Top 3 purchase motivations used to frame reader need |
| [Section name] | S3 + S4 | Market categories list, competitor strengths for criteria |
| [Quote block] | S2: Quote #7 | Verbatim: "I was shocked how easy..." |
| [Comparison table] | S4: Competitor Table | 5 of 10 competitors selected for relevance |
| [FAQ entry 1] | S6: Objection #3 | "Is it too messy?" — rebuttal adapted for blog tone |

## Quotes Used

| # | Quote (truncated) | Dossier Source | Blog Location |
|---|-------------------|---------------|---------------|
| 1 | "I was shocked how easy..." | S2, Quote #7 (Amazon) | Section 2, para 3 |
| 2 | "Best gift I ever gave..." | S2, Quote #12 (Reddit) | Conclusion |

## Sections with Thin Source Data
[Note any sections where dossier coverage was limited and how you adapted]

## Unused Research
[Optionally note high-value dossier data that didn't fit this post type — useful for planning the next post]
```

---

## What the Protocol Does NOT Require

- It does not require inline footnotes in the blog post itself. The blog reads clean; the research map is the separate audit trail.
- It does not prohibit transitional prose, introductions, or connective sentences. These are structural necessities — they just shouldn't contain unsourced factual claims.
- It does not prohibit adapting dossier language for blog tone. "Objection Kill Sheet entry #3" should become a conversational FAQ answer, not a copy-paste from the dossier. The substance stays; the voice adapts.
- It does not require using every piece of dossier data. Selectivity makes better content. The Research Map's "Unused Research" section captures what was left on the table for future posts.
