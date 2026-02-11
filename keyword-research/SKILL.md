---
name: keyword-research
description: |
  SEO keyword research for e-commerce blog content. Takes a brand name and product, mines the existing product-research dossier for seed keywords (customer language, competitor names, objection phrasing), then expands via web search (autocomplete, People Also Ask, related searches, competitor blog analysis). Classifies intent, assesses competition qualitatively, groups keywords into topic clusters, and outputs a keyword map that feeds directly into the blog-post-generator. Works without paid SEO tools — uses web search + dossier data exclusively.

  TRIGGERS: keyword research, SEO keywords, find keywords, keyword map, what should I write about, blog topic ideas, content strategy, keyword analysis, SEO research, search terms, what are people searching for, keyword opportunities, topic clusters, blog keyword plan, content planning, keyword discovery, find blog topics for [brand], SEO plan for [product]

  Do NOT use for: writing blog posts (use blog-post-generator), creating research dossiers (use product-research), ad copy or image generation (use ad-swipe-engine or native-image-ad-generator), technical SEO audits, backlink analysis, or site-level SEO recommendations.
---

# Keyword Research

Discovers and evaluates SEO keywords for e-commerce blog content by combining two sources: the product-research dossier (which contains the exact language your target audience uses) and systematic web search expansion. Outputs a keyword map that feeds directly into the blog-post-generator.

## Why the Dossier Matters

Most keyword research starts from a blank seed — you type a product name and hope the tool finds something useful. This skill starts from 15-30 pages of validated market research. The dossier's Voice of Customer section alone contains the exact words customers use to describe their problems, motivations, and concerns. Those words are what they type into Google. The dossier gives you a proprietary seed source that generic keyword tools can't match.

## What This Skill Does NOT Provide

Be upfront about limitations:
- **No exact search volume numbers.** Without API access to Ahrefs, SEMrush, or Google Keyword Planner, we cannot provide monthly search volume. We use relative demand signals (Google Trends, autocomplete breadth, PAA depth) instead.
- **No precise difficulty scores.** Competition is assessed qualitatively (Low/Medium/High) based on SERP analysis, not domain authority metrics.
- **No backlink data.** We don't know how many backlinks the ranking pages have.

What we DO provide: a research-grounded keyword map with intent classification, qualitative competition assessment, topic clustering, blog post type recommendations, and dossier cross-references — all actionable without paid tools.

## Quick Reference

| Step | What Happens | User Interaction |
|---|---|---|
| 1. Input | Receive brand, product, and optional seeds | User provides these |
| 2. Find dossier | Locate in `Desktop/Brands/[BrandName]/` | Confirm if ambiguous |
| 3. Extract seeds | Mine dossier for 15-25 seed keywords | None (auto) |
| 4. Expand | Web search for autocomplete, PAA, related searches, competitor blogs | None (auto) |
| 5. Classify & assess | Intent classification + competition scoring | None (auto) |
| 6. Cluster & map | Group into topic clusters, map to blog post types | None (auto) |
| 7. Deliver | Save keyword map, present summary | User receives the map |

## Workflow

### Step 1: Gather Inputs

The user provides:
- **Brand name** (required) — used to locate the dossier
- **Product name** (required if multiple dossiers exist)
- **Product category / niche** (optional) — useful if broader than a single product
- **Seed keywords** (optional) — any keywords the user already has in mind
- **Specific focus** (optional) — e.g., "I want to focus on gift-related keywords" or "I'm most interested in comparison keywords"

### Step 2: Locate and Read the Dossier

Follow the same dossier discovery pattern as the blog-post-generator:

```
Desktop/Brands/[BrandName]/[Product Name] — Deep Research Dossier.docx
```

1. List `Desktop/Brands/[BrandName]/` (try casing variations)
2. Match `.docx` files containing "Deep Research Dossier"
3. Read the full dossier via `python -m markitdown` or python-docx fallback

**If no dossier exists:** The skill can still run, but with reduced quality. Fall back to the product name + category as seeds, and suggest the user run product-research first for better results.

### Step 3: Extract Seed Keywords from Dossier

Read `references/dossier-seed-extraction.md` for the complete extraction guide.

Mine each dossier section systematically:

| Dossier Section | What to Extract | Keyword Type |
|----------------|-----------------|-------------|
| S3: Market Landscape | Product categories, alternatives, needs mapping | Category keywords, alternative keywords |
| S4: Competitor Teardown | Competitor names, products, positioning | "X vs Y" keywords, "[competitor] alternative" |
| S5: Voice of Customer | Customer language for motivations, objections, experiences | Long-tail customer language keywords |
| S6: Objection Kill Sheet | Objections in customer's words, root causes | FAQ/problem keywords |
| S7: Contextual Positioning | Occasions, gift angles, contexts | Seasonal/occasion keywords |
| S8: Persona Positioning | Audience descriptors, persona needs | Audience-targeted keywords |
| S9: Messaging & Ad Angles | Hooks, promises, angle names | Validated demand keywords |
| S10: Pricing & Bundling | Price ranges, value language | Price comparison keywords |

Combine user-provided seed keywords with extracted seeds. Deduplicate. Target: **15-25 unique seed keywords** to carry into expansion.

### Step 4: Expand via Web Search

Read `references/search-methodology.md` for the complete expansion methodology.

For each seed keyword, use web search to discover related keywords through:

1. **Autocomplete mining** — search with modifiers (for, vs, how, best, is, without) to trigger Google's autocomplete suggestions visible in search results
2. **People Also Ask (PAA)** — capture all PAA questions from search results
3. **Related searches** — note related search suggestions
4. **Competitor blog analysis** — search competitor sites for blog content, extract their target keywords from titles and headings
5. **Question expansion** — search "how to [seed]," "is [seed] worth it," "[seed] for beginners" etc.
6. **Google Trends validation** — for top candidates, check trends to validate demand direction

**Practical pacing:** Don't try to exhaustively search every seed. Prioritize:
- Top 5-8 seeds from customer language (S5/S6) → full expansion
- Comparison seeds (S4) → focus on "vs" and "alternative" searches
- Category seeds (S3) → focus on "best" and "for [audience]" searches

Target after expansion: **50-80 keywords** before filtering.

### Step 5: Classify and Assess

**Intent classification** — categorize every keyword:

| Intent | Signal Words | Blog Post Types |
|--------|-------------|-----------------|
| **Informational** | how, what, why, guide, tips, learn, ideas | Educational, Listicle, Customer Story |
| **Commercial** | best, top, review, vs, comparison, alternative | Buying Guide, Comparison Post |
| **Problem-Aware** | can I, without, despite, hard, help, struggle | Problem-Solution, FAQ / Myth-Busting |
| **Transactional** | buy, order, price, discount, coupon, shop | NOT for blog — flag separately |

Remove transactional keywords from the blog keyword list. Flag them for the user's product page / landing page strategy.

**Competition assessment** — for the top 15-20 keyword candidates, perform SERP analysis:

| Signal | Low Competition | High Competition |
|--------|----------------|-----------------|
| Who ranks? | Forums, small sites, thin content | Amazon, Wikipedia, major brands |
| Content depth | Short, surface-level posts | Comprehensive, well-maintained guides |
| Content freshness | Old/outdated results (2+ years) | Recently updated content |
| SERP features | Minimal — pure organic results | Shopping results, knowledge panels |

Score each keyword: **Low** / **Medium** / **High** competition.

Read `references/keyword-map-template.md` for the full scoring framework.

### Step 6: Cluster and Map

**Group keywords into topic clusters** — sets of related keywords that one blog post can target. A cluster has:
- One **primary keyword** (the main target for the page title/H1)
- 2-5 **secondary keywords** (variations that become H2/H3 subheadings)
- A **recommended blog post type** from the blog-post-generator's 8 types

**Keyword-to-post-type mapping:**

| Keyword Pattern | Blog Post Type |
|----------------|---------------|
| "best [product/category]" | Buying Guide |
| "[product A] vs [product B]" | Comparison Post |
| "is [product] worth it / [objection]?" | FAQ / Myth-Busting |
| "how to [use case]" | Problem-Solution or Educational |
| "[product] for [occasion]" | Gift Guide |
| "why [category]" | Educational ("Why [Category]") |
| "[N] reasons to [action]" | Listicle |
| "[product] review / experience" | Customer Story / Use Case |

**Cross-reference with the dossier** — for each cluster, note which dossier sections provide supporting content. This pre-maps the blog-post-generator's Step 4 (Research Extract).

**Prioritize clusters** by: relevance to the product × low competition × blog-appropriate intent. The priority order becomes the recommended content calendar.

### Step 7: Generate and Deliver the Keyword Map

Read `references/keyword-map-template.md` for the complete output format.

Generate the keyword map and save to:
```
Desktop/Brands/[BrandName]/Blog Posts/keyword-map.md
```

Create the `Blog Posts/` folder if it doesn't exist.

**Delivery message format:**
```
Done — keyword map generated for [Brand] [Product].

[N] seed keywords extracted from dossier
[N] total keywords discovered after expansion
[N] topic clusters identified
[N] priority clusters recommended (start here)

Keyword map: [path]

Top 3 opportunities:
1. [Cluster name] — [primary keyword] — [competition] competition,
   [intent] intent → [post type]
2. [Cluster name] — ...
3. [Cluster name] — ...

Next step: Pick a cluster and run blog-post-generator with the
primary keyword and recommended post type.
```

## Integration with Blog Post Generator

The keyword map is designed as the direct input to the blog-post-generator:

1. User picks a cluster from the keyword map
2. The cluster provides: primary keyword, post type, secondary keywords for subheadings
3. The dossier cross-reference tells the blog generator which sections to extract
4. The blog generator produces research-anchored content targeting that keyword cluster

This creates a complete pipeline: **dossier → keyword map → blog post → research map**.

## Error Handling

### No dossier available
The skill can still run using the product name and user-provided seeds, but results will be less targeted. Recommend the user runs product-research first. Without the dossier, skip Step 3's section-by-section extraction and go straight to web search expansion with basic seeds.

### Dossier sections are thin
Some sections may have limited content. If S7 (Contextual Positioning) is missing, skip occasion/gift keywords. If S4 has few competitors, comparison keywords will be limited. Note gaps in the keyword map's methodology section.

### Web search returns limited results
Some niche products may have very few autocomplete suggestions or PAA questions. This is actually a positive signal — it suggests low competition and content gaps. Note the limited expansion and emphasize the opportunity.

### Too many keywords discovered
If expansion produces more than 100 keywords, be more aggressive about filtering and clustering. Focus on the 8-12 strongest clusters rather than trying to catalog everything.

## Scope

**Handles:** Discovering, classifying, and prioritizing SEO keywords for e-commerce blog content using dossier data and web search.

**Does NOT handle:** Writing blog posts (use blog-post-generator), creating dossiers (use product-research), providing exact search volumes (requires paid tools), technical SEO audits, backlink analysis, or paid ad keyword strategy.

## Re-Running Keyword Research

Keyword landscapes change. Recommend re-running this skill:
- When the product-research dossier is updated (new competitors, new VoC data)
- Quarterly, to catch trending keywords and seasonal shifts
- When entering a new market segment or targeting a new persona
- After publishing 5-10 blog posts, to find the next round of opportunities
