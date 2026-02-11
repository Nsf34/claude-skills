# Quality Checklist — Blog Post Verification

Run this checklist before delivering the final blog post. Score each dimension as Pass / Needs Fix / Fail. A post ships only when all 7 dimensions pass.

## The 7 QC Dimensions

### 1. Research Anchoring (HIGHEST PRIORITY)

Does every substantive claim in the post trace back to the dossier?

Check:
- [ ] Every factual claim maps to a specific dossier section (S1–S10)
- [ ] No statistics, market data, or competitor details were introduced from outside the dossier
- [ ] Transitional prose and structural text don't contain unsourced factual claims
- [ ] The Research Map (`_research-map.md`) has been generated and covers all blog sections
- [ ] The "Unused Research" section of the Research Map notes high-value dossier data left on the table

Scoring:
- **Pass**: Every factual claim is traceable. Research Map is complete.
- **Needs Fix**: 1-2 claims lack clear dossier sourcing. Easily correctable.
- **Fail**: Multiple unsourced claims. Post contains fabricated data or statistics not in the dossier.

### 2. Quote Authenticity

Are all customer quotes verbatim from the dossier?

Check:
- [ ] Every blockquote is an exact copy of a quote from S2 (Top 25 Quotes) or S5 (VoC themed quotes)
- [ ] Zero synthetic or generated quotes (even if they "sound like" something a customer might say)
- [ ] Attributions are simplified appropriately for blog format (e.g., "Verified Amazon Review" not "5★ Amazon review")
- [ ] Quote count falls within the range for the chosen post type
- [ ] Quotes are spread throughout the post, not clustered in one section
- [ ] Each quote does work — proving a claim, humanizing data, or addressing an objection

Scoring:
- **Pass**: All quotes are verbatim from the dossier with appropriate attribution.
- **Needs Fix**: Attribution formatting needs adjustment, but quotes are authentic.
- **Fail**: Any generated or fabricated quote is present.

### 3. Competitor Accuracy

Does competitor data match the dossier exactly?

Check:
- [ ] All competitor names, products, and features come from S4 (Competitor Teardown)
- [ ] Pricing data comes from S4 or S10 and is acknowledged as research-point-in-time
- [ ] No competitors were introduced that aren't in the dossier
- [ ] Competitor strengths and weaknesses are fairly represented per S4 analysis
- [ ] If a subset of competitors was used (e.g., 5 of 10), selection was based on relevance, not just favorability

Scoring:
- **Pass**: All competitor data matches the dossier. Fair and accurate representation.
- **Needs Fix**: Minor data discrepancy (e.g., approximate pricing instead of exact from dossier).
- **Fail**: Competitor data is fabricated or significantly misrepresented.

### 4. SEO Compliance

Does the post follow the SEO guidelines from `references/seo-and-structure-guide.md`?

Check:
- [ ] Primary keyword appears in: title (H1), first 100 words, 2-3 H2 headings, meta description, URL slug
- [ ] Keyword density is 1-2% (natural, not stuffed)
- [ ] Meta description is 155-160 characters and includes the primary keyword
- [ ] YAML frontmatter includes: title, meta_description, target_keyword, date
- [ ] Semantic keyword variations are used naturally throughout

Scoring:
- **Pass**: All SEO placement rules are met. Keywords read naturally.
- **Needs Fix**: Missing 1-2 keyword placements. Easy to add.
- **Fail**: No keyword strategy evident. Meta description missing. Frontmatter incomplete.

### 5. Structural Integrity

Does the post follow correct heading hierarchy and match the post-type template?

Check:
- [ ] Single H1 (the title)
- [ ] Logical H2/H3/H4 nesting (no skipped levels)
- [ ] Post structure matches the chosen template from `references/post-type-templates.md`
- [ ] Word count falls within the target range for the post type
- [ ] Paragraphs are 2-4 sentences (no walls of text)
- [ ] Bold formatting used sparingly for scannability (1-2 per paragraph max)
- [ ] Tables and lists used where appropriate (comparison data, parallel items)
- [ ] Image placeholders included with descriptive alt text where visuals would add value

Scoring:
- **Pass**: Clean structure, correct hierarchy, appropriate length, scannable formatting.
- **Needs Fix**: Minor structural issues (one skipped heading level, slightly over/under word count).
- **Fail**: No heading hierarchy. Post is a wall of undifferentiated text. Template was not followed.

### 6. Tone Calibration

Does the post read like helpful blog content, not a marketing page or research report?

Check:
- [ ] Voice is conversational and informative, not hard-sell or academic
- [ ] Tone matches the post type's guidance (e.g., "balanced and fair" for comparison, "empathetic" for problem-solution)
- [ ] Customer quotes feel naturally integrated, not pasted in as afterthoughts
- [ ] The user's product is featured without the post reading like an advertorial
- [ ] No corporate jargon, marketing speak, or filler phrases ("In today's fast-paced world...")
- [ ] Active voice predominates

Scoring:
- **Pass**: Reads like it was written by a knowledgeable, helpful person. Tone matches post type.
- **Needs Fix**: Tone is mostly right but slips into marketing language in 1-2 sections.
- **Fail**: Reads like a product page, press release, or academic paper. Tone is consistently wrong.

### 7. Completeness

Are all deliverables present and accounted for?

Check:
- [ ] Blog post markdown file (.md) is generated with YAML frontmatter
- [ ] Research Map (`_research-map.md`) is generated and accurate
- [ ] Internal linking suggestions are included (3-5 other post types from the same dossier)
- [ ] If .docx was requested, it is generated with proper formatting
- [ ] All files are saved to the correct output folder: `Desktop/Brands/[BrandName]/Blog Posts/`
- [ ] File naming follows slug convention: `[post-title-slug].md`

Scoring:
- **Pass**: All deliverables present, correctly named, in the right location.
- **Needs Fix**: Missing one optional deliverable (e.g., .docx when it wasn't explicitly requested).
- **Fail**: Core deliverables missing (no Research Map, no markdown output, wrong save location).

---

## QC Report Format

```
BLOG POST QC — "[Post Title]"
==============================
Post Type: [Type]
Word Count: [N] (target: [range])
Quotes Used: [N] (target: [range])

Overall: [X/7 passing] — [SHIP / NEEDS REVISION / REWRITE]

Pass: [list passing dimensions]
Needs Fix: [list with specific issues]
   → [Dimension]: [Exact problem]. Fix: [Specific action]
Fail: [list with critical problems]
   → [Dimension]: [Exact problem]. Fix: [Specific action]
```

## Decision After QC

```
All 7 pass?     → Ship it — deliver to user with completion summary
Only Needs Fix? → Fix the noted issues, then deliver
Any Fail?       → Address the failure before delivering
                  (Research Anchoring or Quote Authenticity failures
                   require rewriting the affected sections)
```
