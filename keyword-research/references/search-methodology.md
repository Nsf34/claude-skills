# Search Methodology: Keyword Expansion & Competition Assessment

This guide covers how to expand seed keywords into a full keyword inventory using web search, and how to qualitatively assess competition without paid SEO tools.

---

## Phase 1: Keyword Expansion

Starting from the 15-25 seed keywords extracted from the dossier (see `references/dossier-seed-extraction.md`), expand into a broader inventory using these techniques.

### Technique 1: Autocomplete Mining

Google's autocomplete reveals what people actually search. For each seed keyword, search with different modifiers to trigger autocomplete-style expansions.

**Search patterns to run:**

```
[seed keyword] for ...        → audience/use-case variations
[seed keyword] vs ...         → comparison variations
[seed keyword] how ...        → instructional variations
[seed keyword] best ...       → recommendation variations
[seed keyword] is ...         → question/concern variations
[seed keyword] without ...    → limitation/objection variations
best [seed keyword] ...       → buying-intent variations
how to [seed keyword] ...     → informational variations
why [seed keyword] ...        → motivation/educational variations
```

**What to capture:** The search results themselves will show you what content exists for these queries. Pay attention to:
- Page titles in search results (these are the keywords competitors target)
- Question formats that appear (these become H2s in blog posts)
- "People Also Ask" boxes (covered in Technique 2)

**Practical approach:** Don't search every modifier for every seed. Prioritize:
1. Your top 5 highest-intent seeds → full modifier sweep
2. Remaining seeds → search the 2-3 most relevant modifiers

### Technique 2: People Also Ask (PAA) Mining

When you perform a web search, results often include "People Also Ask" questions. These are Google's explicit signal of related queries with search demand.

**How to mine PAA:**
1. Search each top seed keyword
2. Note all PAA questions that appear in the results
3. These questions become:
   - Long-tail keyword variations
   - H2/H3 subheadings for blog posts
   - FAQ content ideas

**PAA questions tend to cluster into patterns:**
- "What is the best [category] for [use case]?" → Buying Guide
- "Is [product/category] worth it?" → FAQ / Myth-Busting
- "How do I [action] with [product]?" → Problem-Solution / Educational
- "[Product A] vs [Product B]?" → Comparison Post
- "Can you [action] without [prerequisite]?" → Objection-resolution content

**Typical yield:** 3-5 PAA questions per seed keyword × 15 seeds = 40-75 additional keyword ideas.

### Technique 3: Related Search Mining

Search results include related searches — these are variations Google considers relevant. They tend to be:
- More specific long-tail versions of the seed
- Adjacent topics Google clusters together
- Lower competition than the seed keyword itself

**How to capture:** After searching a seed keyword, note the related searches suggested in the results. These expand your keyword list with Google-validated related terms.

### Technique 4: Competitor Blog Content Analysis

This is one of the highest-value expansion techniques. Your competitors have already done keyword research — their blog titles and structures reveal what they're targeting.

**How to do it:**

1. Identify 3-5 competitors from the dossier's S4 (Competitor Teardown)
2. For each competitor, search: `site:[competitor-domain.com] blog` or `[competitor name] blog`
3. Analyze their blog posts:
   - **Page titles** = their target keywords
   - **H2 subheadings** = their secondary keywords and subtopics
   - **Content themes** = their topic clusters
4. Note what they cover and, importantly, **what they don't cover** — these gaps are your opportunities

**What to extract from competitor blogs:**
- Keywords they're clearly targeting (in titles and H1s)
- Topics they cover repeatedly (their content pillars)
- Gaps — subjects the dossier covers that competitors haven't written about
- Weak content — topics where their posts are thin and you could create something better

**Practical approach:** For each competitor, analyze 5-10 of their most relevant blog posts. Don't try to map their entire content library — focus on posts in your product category.

### Technique 5: Question-Based Keyword Expansion

Search AnswerThePublic-style queries to discover question-format keywords. These are valuable because:
- They match how people actually search (conversational, question-based)
- They have lower competition than short head terms
- They map directly to blog content sections (each question = a subheading)

**Search patterns:**
```
"how to" [seed keyword]
"what is the best" [seed keyword]
"is [seed keyword] worth"
"[seed keyword] for beginners"
"[seed keyword] tips"
"[seed keyword] mistakes to avoid"
"[seed keyword] guide"
```

### Technique 6: Google Trends Validation

For your top keyword candidates, check Google Trends to understand:
- **Trending up or down?** — growing keywords are more valuable
- **Seasonal patterns?** — some keywords spike around holidays (gift-related, seasonal products)
- **Related queries rising?** — Google Trends shows "breakout" related queries that signal emerging demand

**How to use:** Search `Google Trends [keyword]` or visit Google Trends directly. Focus on:
- "Interest over time" — is the keyword growing?
- "Related queries" — additional keyword ideas ranked by growth
- Compare 2-3 seed keywords to see which has more relative demand

**When to use Trends:** Not for every keyword — use it for your top 10-15 candidates to validate or compare demand. It's a tiebreaker, not a primary discovery tool.

---

## Phase 2: Deduplication & Filtering

After expansion, you'll have 50-100+ keywords. Clean the list:

### Remove Duplicates and Near-Duplicates
- "pottery wheel for beginners" and "beginner pottery wheel" are the same keyword cluster — keep one as primary, note the other as a variant
- Group synonyms: "pottery kit" / "pottery set" / "pottery starter pack" → one cluster

### Remove Off-Topic Keywords
- Keywords that expanded into irrelevant territory (e.g., seed "craft kit" expanding to "minecraft craft")
- Keywords about products/categories the dossier doesn't cover
- Keywords targeting audiences not in the dossier's personas

### Remove Pure Transactional Keywords
- "buy [product] online," "discount code for [brand]," "[product] free shipping"
- These are product-page keywords, not blog content keywords
- Flag them separately — the user may want them for other purposes, but they don't feed into the blog-post-generator

### Target After Filtering
50-80 unique keywords organized into 8-12 topic clusters.

---

## Phase 3: Competition Assessment

Without paid tools, assess competition qualitatively by analyzing the search results for each keyword.

### Signal 1: Who's Ranking?

Search each top keyword candidate and examine the first page of results.

**High competition signals:**
- Amazon, Wikipedia, major publications (NYT, Forbes) dominate the results
- Established authority sites with large content libraries
- Brand homepages ranking (not blog posts)

**Low competition signals:**
- Forums (Reddit, Quora) ranking in top 5 — means quality content could displace them
- Small blogs or niche sites ranking
- YouTube videos ranking on Google — means written content is under-served
- eHow-style thin content ranking — means a comprehensive post could easily win

**Medium competition signals:**
- Mix of authority sites and smaller sites
- Competitor blogs ranking (you can compete on content quality)
- Pinterest or social media pages ranking

### Signal 2: Content Depth

Open the top 3-5 results for each keyword and assess:

**Opportunity indicators:**
- Top results are short (under 500 words) but the topic is complex → comprehensive content wins
- Top results are old (2+ years) and the topic has evolved → fresh content wins
- Top results answer a different question than the search query implies → better-targeted content wins
- Top results are product pages but the query is informational → blog content can rank

**Difficulty indicators:**
- Top results are comprehensive guides (2,000+ words, well-structured) → need exceptional content to compete
- Top results are recently updated and thorough → already well-served
- Top results from sites with massive authority → hard to outrank regardless of content quality

### Signal 3: SERP Features

What Google shows alongside organic results tells you about intent and opportunity:

| SERP Feature | What It Means | Opportunity |
|-------------|---------------|-------------|
| **Featured snippet** | Google wants a direct answer | Structure your content to win the snippet (list, table, definition) |
| **People Also Ask** | Topic has depth, many related questions | Create comprehensive content addressing multiple PAAs |
| **Shopping results** | High commercial intent | Blog may rank lower; consider commercial angle |
| **Video carousel** | Visual content preferred | Blog + video pairing could work; pure text may underperform |
| **Knowledge panel** | Branded/factual query | Hard to rank for; likely not a blog target |
| **Local pack** | Geographic intent | Not relevant for e-commerce blog content |
| **Image pack** | Visual search intent | Include strong images; optimize alt text |
| **No special features** | Standard organic results | Pure content opportunity — best content wins |

### Competition Scoring

Assign each keyword a competition level based on the signals above:

**Low Competition** (target aggressively)
- Forums, thin content, or old content in top 5
- No major brand dominance
- Your dossier provides data the current top results don't have
- Few or no SERP features competing for clicks

**Medium Competition** (target selectively)
- Mix of authority and smaller sites
- Competitor blogs present but content is average quality
- Some SERP features but organic results still get clicks
- Topic requires research depth that your dossier provides

**High Competition** (target only with strong angle)
- Major brands, publications, or Amazon in top 3
- Existing content is comprehensive and well-maintained
- Heavy SERP features (shopping, knowledge panel) reducing organic click-through
- Would need exceptional content AND domain authority to compete

### Practical Approach

You don't need to SERP-analyze every keyword. Prioritize:

1. **Analyze the top 15-20 keywords** from your filtered list (highest relevance + most likely to convert)
2. **Batch by cluster** — if one keyword in a cluster is low competition, related keywords likely are too
3. **Spend more time on borderline cases** — if a keyword looks medium competition, deeper analysis helps decide whether to target it

---

## Phase 4: Putting It Together

After expansion, filtering, and competition assessment, you have the raw data needed to build the keyword map. The next step is organizing this into the output format defined in `references/keyword-map-template.md`.

### What You're Handing Off

For each keyword or keyword cluster:
- The primary keyword and its variations
- Search intent classification
- Competition level (Low / Medium / High)
- Recommended blog post type
- Which dossier sections support content for this keyword
- Notes on SERP opportunities (featured snippet format, content gaps, etc.)

This feeds directly into the blog-post-generator, where the user picks a keyword cluster and the generator produces the content.
