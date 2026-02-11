# Keyword Map Template

This document defines the output format for the keyword research skill, including how to classify search intent, score competition, and organize keywords into actionable topic clusters.

---

## Output File

Save the keyword map to:
```
Desktop/Brands/[BrandName]/Blog Posts/keyword-map.md
```

This puts it alongside the blog posts it's designed to inform. If the `Blog Posts/` folder doesn't exist, create it.

---

## Keyword Map Structure

```markdown
# Keyword Map: [Brand] — [Product/Category]

**Generated**: [Date]
**Source Dossier**: [Product Name] — Deep Research Dossier.docx
**Seeds Extracted**: [N] seed keywords from dossier
**Total Keywords Discovered**: [N] after expansion
**Topic Clusters**: [N] clusters identified

---

## How to Use This Map

1. Pick a cluster from the Priority Keywords section
2. Note the recommended blog post type and primary keyword
3. Run the blog-post-generator skill with that keyword and post type
4. Use the secondary keywords as H2/H3 subheadings in the blog post
5. Repeat with the next cluster

---

## Priority Keywords (Start Here)

These are the highest-opportunity keywords: relevant to your product,
lower competition, and clear blog-appropriate intent.

### 1. [Cluster Name]

| Field | Value |
|-------|-------|
| **Primary Keyword** | [keyword] |
| **Secondary Keywords** | [keyword 2], [keyword 3], [keyword 4] |
| **Search Intent** | [Informational / Commercial / Problem-Aware] |
| **Competition** | [Low / Medium / High] |
| **Recommended Post Type** | [Buying Guide / Comparison / FAQ / etc.] |
| **Dossier Support** | [S3, S5, S6 — which sections have data for this] |
| **SERP Notes** | [Brief: what's ranking now, content gaps, snippet opportunity] |
| **Why It's Priority** | [1-2 sentences: why this keyword is worth targeting first] |

### 2. [Cluster Name]
[Same table format]

### 3. [Cluster Name]
[Same table format]

[Continue for top 5-8 priority clusters]

---

## Full Keyword Inventory

All discovered keywords organized by topic cluster.

### Cluster: [Topic Name]
**Theme**: [What this cluster is about]
**Post Type**: [Recommended blog-post-generator post type]
**Competition**: [Overall cluster competition level]
**Dossier Sections**: [Which sections support this cluster]

| Keyword | Intent | Competition | Notes |
|---------|--------|-------------|-------|
| [primary keyword] | Commercial | Low | PAA present, thin existing content |
| [variation 1] | Informational | Low | Question format, good for H2 |
| [variation 2] | Commercial | Medium | Competitor blog ranks #3 |
| [variation 3] | Problem-Aware | Low | Forum results in top 5 |

[Repeat for each cluster — typically 8-12 clusters total]

---

## Blog Post Recommendations

Specific blog posts to write, in priority order.

### Post 1: [Suggested Title]

| Field | Value |
|-------|-------|
| **Post Type** | [From blog-post-generator's 8 types] |
| **Primary Keyword** | [keyword] |
| **Secondary Keywords** | [keywords for H2s/subheadings] |
| **Target Word Count** | [From post type default] |
| **Competition** | [Low / Medium / High] |
| **Dossier Sections Needed** | [S3, S4, S5, etc.] |
| **Content Angle** | [1-2 sentences: what makes this post different from what's ranking] |
| **Estimated Cluster Traffic** | [Relative: High / Medium / Low based on Trends + expansion breadth] |

### Post 2: [Suggested Title]
[Same format]

[Continue for 5-10 recommended posts]

---

## Keyword-to-Dossier Cross-Reference

Shows which dossier sections provide supporting data for each keyword cluster.
Helps the blog-post-generator's Step 4 (Research Extract) by pre-mapping data sources.

| Keyword Cluster | S2 Quotes | S3 Market | S4 Competitors | S5 VoC | S6 Objections | S7 Context | S8 Personas | S9 Angles | S10 Pricing |
|----------------|-----------|-----------|---------------|--------|--------------|------------|------------|-----------|------------|
| [Cluster 1]    | 3 quotes  | category X | 4 competitors | 5 quotes | objection #2, #7 | gift angle | persona 1, 3 | angle #4 | tier data |
| [Cluster 2]    | 2 quotes  | —         | 2 competitors | 8 quotes | objection #1, #3, #5 | — | persona 2 | angle #1, #6 | price range |
| [Cluster 3]    | ...       | ...       | ...           | ...    | ...          | ...        | ...        | ...       | ...        |

---

## Methodology Notes

**Tools Used**: [Web search, Google Trends, competitor blog analysis]
**Limitations**: Search volume estimates are relative (not exact monthly numbers).
Competition scores are qualitative based on SERP analysis, not domain authority metrics.
**Dossier Currency**: Keywords derived from [Product Name] dossier dated [date].
Competitor data and pricing may have changed since research was conducted.
**Recommendation**: Re-run keyword research quarterly or when the dossier is updated.
```

---

## Search Intent Classification

Every keyword gets classified into one of four intent categories. Intent determines which blog post type is appropriate.

### Informational
The searcher wants to learn or understand something.

**Signal words:** how, what, why, guide, tutorial, tips, learn, understand, explain, ideas
**Examples:** "how to center clay on a pottery wheel," "why pottery is relaxing," "craft ideas for adults"
**Blog post types:** Educational ("Why [Category]"), Listicle ("X Reasons"), Customer Story

### Commercial Investigation
The searcher is researching options before a purchase decision.

**Signal words:** best, top, review, comparison, vs, versus, recommended, which, alternative
**Examples:** "best pottery wheel for beginners," "Sculpd vs Table Clay," "pottery kit review 2025"
**Blog post types:** Buying Guide, Comparison Post

### Problem-Aware
The searcher has a problem and is looking for solutions or reassurance.

**Signal words:** problem, issue, how to fix, can I, without, despite, struggle, hard, difficult, help
**Examples:** "pottery without a kiln," "is pottery too messy for apartments," "crafts for people with no talent"
**Blog post types:** Problem-Solution, FAQ / Myth-Busting

### Transactional
The searcher is ready to buy — looking for a specific product, price, or purchase path.

**Signal words:** buy, order, price, cost, discount, coupon, free shipping, where to buy, shop
**Examples:** "buy pottery wheel online," "Table Clay discount code," "pottery kit free shipping"
**Blog post types:** Not blog-appropriate — flag for product page / landing page use. Do not include in blog keyword recommendations.

### Mixed Intent
Some keywords have ambiguous intent. "Pottery wheel" could be informational (what is it?), commercial (which one should I buy?), or transactional (where to buy?).

For mixed-intent keywords:
- Check the SERP — what type of content ranks? That reveals what Google interprets as the dominant intent.
- Classify based on the dominant SERP intent.
- Note the ambiguity in the keyword map so the user can make an informed decision.

---

## Competition Scoring Framework

Each keyword gets a competition score: **Low**, **Medium**, or **High**.

### Low Competition

Characteristics:
- Forums (Reddit, Quora) or user-generated content in top 5 results
- Thin content (under 500 words) ranking for a topic that deserves depth
- Content older than 2 years with no recent updates
- Small or niche sites ranking (not major brands)
- YouTube or Pinterest ranking on Google (means written content is under-served)
- No featured snippet claimed yet

Implication: A well-researched, comprehensive blog post should rank within 3-6 months.

### Medium Competition

Characteristics:
- Mix of authority sites and smaller sites in results
- Competitor blogs present but content quality is average
- Some content is comprehensive but older
- Featured snippet exists but could be improved
- Domain authority matters somewhat — established sites have an edge

Implication: Rankable with strong content + time. May take 6-12 months. Content must be noticeably better than what currently ranks.

### High Competition

Characteristics:
- Amazon, Wikipedia, major publications in top 3
- Comprehensive, recently updated guides from authority sites
- Heavy SERP features (shopping results, knowledge panels) reducing organic clicks
- High domain authority required to compete
- Content is already excellent — hard to differentiate

Implication: Only target if you have a unique angle the current results don't cover, or if the keyword is so strategically important that long-term investment is justified.

---

## Relative Demand Signals

Since exact search volume isn't available without paid tools, use these proxy signals to estimate relative keyword popularity:

### Higher Demand Signals
- Google Trends shows upward trajectory
- Many autocomplete variations exist (Google expands it in many directions)
- Multiple PAA questions appear (Google has lots of related query data)
- Competitor blogs all cover this topic (they've validated the demand)
- AnswerThePublic/question tools show many related questions

### Lower Demand Signals
- Google Trends shows flat or declining interest
- Few autocomplete variations
- No or minimal PAA questions
- Competitors haven't written about this topic (may indicate low demand OR an untapped opportunity)
- Very niche or specific queries with no related expansions

### Using Demand Signals in the Map

Don't assign fake numbers. Instead, use relative categories:

| Demand Level | What It Means | In the Keyword Map |
|-------------|---------------|-------------------|
| **High** | Broad topic, many variations, trending up, competitors all cover it | Note as "High relative demand" |
| **Medium** | Some variations, stable or slight growth, some competitor coverage | Note as "Medium relative demand" |
| **Low** | Few variations, niche, limited competitor coverage | Note as "Low relative demand — niche opportunity or limited audience" |

The combination of **demand × competition** determines priority:
- High demand + Low competition = **Top priority** (rare but golden)
- Medium demand + Low competition = **Strong opportunity**
- High demand + Medium competition = **Worth pursuing with strong content**
- Low demand + Low competition = **Niche wins — easy but limited traffic**
- Any demand + High competition = **Only with a unique angle**
