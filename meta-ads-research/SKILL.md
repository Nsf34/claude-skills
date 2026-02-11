---
name: meta-ads-research
description: |
  Deep competitor research using Meta Ad Library. Use when analyzing competitor Facebook/Instagram ads, extracting ad angles and hooks, identifying winning ad patterns, or building creative strategy from competitor intelligence.

  TRIGGERS: Meta Ad Library, Facebook ads research, Instagram ads competitor analysis, ad library analysis, competitor ad research, creative strategy research, ad angle extraction, winning ad patterns

  This skill uses browser automation to navigate Meta Ad Library URLs, screenshot ads, extract copy/creative details, and generate structured analysis reports with actionable insights. Works for any brand — provide brand context or use it generically.
---

# Meta Ads Library Research

Research competitor ads in the Meta Ad Library using browser automation. Screenshot and catalog their ads, extract the strategic angle/hook/promise/pain/proof/offer/objection for each ad, and produce a research report and creative brief.

---

## Pre-Flight Checklist

Before navigating anywhere, confirm these inputs:

1. **Competitor target** — Brand name or Meta Ad Library URL. If user gives a brand name, construct: `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=[BrandName]`
2. **Brand context** (optional) — If the user has a brand context file (product lines, personas, angles taxonomy), read it now. If not provided, the skill works generically and skips brand-mapping steps. Check for a file at `references/brand-context.md` or any context file the user provides.
3. **Output location** — Default to `ad-research/[BrandName]/` inside the user's workspace/outputs folder. Create the directory structure before starting captures.
4. **Scope** — Default: 5-10 ads from 1 competitor, ~60 min. Adjust if user specifies.

Set up the capture folder immediately:
```
ad-research/
└── [BrandName]/
    ├── captures/                    ← Screenshots go here
    ├── [BrandName]_Research_Report.md
    └── [BrandName]_Creative_Brief.md
```

---

## Phase 1: Navigate and Orient

### Step 1: Load the Ad Library

Navigate to the Meta Ad Library URL. The page loads a search interface first — you need to trigger a search or let the URL parameters do it.

**What to expect on the page:**
- A search bar at top with the brand name pre-filled (from URL `q=` param)
- Filter controls below: Country, Ad Category, Platform, Media Type
- Results area with ad cards — initially may show a loading spinner or "Searching..."
- Each ad card has: creative thumbnail, primary text (often truncated), headline, CTA, start date, platform icons

**JavaScript to verify results loaded:**
```javascript
// Wait for ad cards to appear — they render inside a scrollable container
const checkResults = () => {
  const cards = document.querySelectorAll('[role="listitem"], [class*="AdCard"], [class*="ad-card"]');
  const countText = document.body.innerText.match(/(\d+)\s+results?/i);
  return { cardCount: cards.length, totalResults: countText ? countText[1] : 'unknown' };
};
checkResults();
```

### Step 2: Set Filters

Confirm these filters are set (most should be pre-filled from URL params):
- **Country**: United States (default)
- **Ad Category**: All ads
- **Status**: Active ads (this is the default for US)

If researching specific formats, also filter by:
- **Platform**: Facebook only / Instagram only
- **Media type**: Video / Images / Memes

### Step 3: Capture the Overview

Take a screenshot of the full results page. This captures:
- Total ad count (shown near the top, e.g., "About X results")
- First batch of visible ads
- Filter state confirmation

**Save as**: `captures/00_overview.png`

Note the total ad count. This number tells you the scale of the competitor's ad program — a brand with 5 active ads vs. 150 tells a very different story about their paid strategy.

### Failure Handling: Navigation and Loading

| Problem | What You See | Fix |
|---------|-------------|-----|
| **No results** | "No ads match your search" or 0 results | Try alternate spellings, the company's Facebook page name, or the parent company name. Search for the domain (e.g., "tableclay.com") instead of the brand name. If still nothing, tell the user this brand has no active US ads and suggest checking EU regions or trying related brands. |
| **Login wall** | Facebook login modal blocking the page | The Ad Library is publicly accessible without login. Look for a "Not now" or X/close button on the modal. If it persists, navigate directly to `facebook.com/ads/library` and search from the search bar there. |
| **Region-locked content** | Ads show "[Content not available in your region]" | Change the Country filter to the target market. Note this limitation in the report. |
| **CAPTCHA / rate limit** | Verification challenge or "Please try again later" | Wait 30 seconds and retry once. If it persists, tell the user — this is a Meta-side rate limit, not something we can work around. |
| **Page layout changed** | Elements don't match expected structure (Meta redesigns frequently) | Fall back to pure visual analysis. Take screenshots and extract information from what's visible. Don't try to force-find elements that aren't there — note in the report that the page structure may have changed. |
| **Slow loading** | Spinner or skeleton UI visible for >10 seconds | Wait up to 30 seconds. Scroll slightly to trigger lazy loading. If still loading, take a screenshot of current state and work with what's visible. |

---

## Phase 2: Capture Ads

The goal is to screenshot 5-10 ads that show signals of being winners. Don't capture everything — be selective.

### How Ads Render in the Library

Each ad appears as a card containing:
- **Creative**: Image or video thumbnail (click to expand/play)
- **Primary text**: The main ad copy — **often truncated**. Look for a "See more" link to expand.
- **Headline**: Below the creative
- **CTA button**: "Shop Now", "Learn More", etc.
- **Metadata**: "Started running on [date]", platform icons (FB/IG), "See ad details" link
- **"Low count" label**: Appears on ads with < ~100 impressions — these are tests

**Critical**: Ad copy is often truncated to 2-3 lines. You MUST click "See more" on each ad to reveal the full primary text before screenshotting. The truncated version hides proof points, offer details, and objection handling that lives in the body copy. This is where the strategy is — the hook is in the first line, but the selling is in the expanded text.

### Loading More Ads

The Ad Library uses infinite scroll — there's no "next page" button. To load more results:

1. Scroll to the bottom of the currently visible ads
2. Wait 2-3 seconds for the next batch to load (watch for a loading spinner at the bottom)
3. Once the spinner disappears, new ad cards have loaded
4. Repeat until you have enough candidates or reach the end of results

```javascript
// Scroll to load more and wait for new content
window.scrollTo(0, document.body.scrollHeight);
// After 3 seconds, check if new cards appeared
```

For brands with many ads (50+), don't scroll through all of them. The first 2-3 pages of results plus selective deep scrolling is usually sufficient.

### Selecting Which Ads to Capture

You can't see spend or conversion data, so use these proxy signals to identify likely winners:

**1. Longevity** — Ads running for weeks or months. Brands kill losers fast, so a long-running ad is likely profitable. Check the "Started running on [date]" field. An ad running for 60+ days is almost certainly a winner.
- *Validate*: Look for fresh engagement and new variations of the same angle launching alongside it.
- *False positive*: Could be a low-spend retargeting ad, or simply forgotten. Cross-reference with other signals.

**2. Creative families** — Multiple ads with the same angle but minor variations (different hook text, slightly different image, different aspect ratio). This means the brand is A/B testing this angle — they believe in it enough to invest in iteration. The longest-running variant within a family is likely the best performer.
- *What to capture*: Screenshot the longest-running variant. Note the family size in your extraction notes.

**3. Offer persistence** — The same discount, bundle, or CTA appearing across many ads over weeks. If "Free shipping + bonus pack" shows up in 6 different ads spanning 2 months, that offer converts.
- *Validate*: Compare to seasonal promos — if the offer persists outside holiday periods, it's a steady performer, not a seasonal play.

**4. Cross-format presence** — Same angle appearing in video AND static AND carousel, or across Feed + Stories + Reels placements. This means they're scaling the angle across the platform — a strong signal of confidence.

**5. Cross-brand convergence** — When multiple competitors in the same niche independently arrive at the same hook or angle. Independent discovery of the same idea is one of the strongest signals available — the angle is probably working across the category.

**Skip these:**
- Ads with "Low count" label (< ~100 impressions) — likely a test that hasn't proven anything. Exception: if the angle is novel and worth noting, mention it as "observed test" but don't treat it as a winner.
- Ads that appear to be retargeting only (very specific messaging to existing customers, e.g., "Still thinking about it?")
- Duplicate variants within the same creative family — capture the longest-running variant only.

### For Each Ad to Capture

1. Click "See more" to expand the full primary text
2. Click "See ad details" if available to get more metadata
3. Take a screenshot that includes: the full creative, ALL expanded text, headline, CTA, start date, and platform indicators
4. If the creative is a video, the screenshot captures the thumbnail — note "video" in your extraction and describe what's visible in the thumbnail

### Screenshot Naming Convention

Name captures so they're self-documenting and easy to reference in the report:

```
captures/[##]_[BrandName]_[angle-keyword]_[format].png

Examples:
captures/01_NovaCeramics_stress-relief_video.png
captures/02_NovaCeramics_gift-guide_carousel.png
captures/03_NovaCeramics_leakproof-test_static.png
captures/04_ClayKits_beginner-confidence_video.png
```

The `##` prefix (01-10) is the capture sequence number. The angle keyword is 2-3 words describing the core angle. This naming convention lets you reference captures by number in the report and makes the folder browsable at a glance.

### Screenshot Failure Handling

| Problem | Fix |
|---------|-----|
| **Screenshot is blank or black** | The creative may be a video whose thumbnail hasn't loaded. Wait 3 seconds, scroll the ad fully into the viewport, try again. |
| **Text is cut off** | Click "See more" to expand, then re-screenshot. If "See more" isn't clickable, try clicking the ad card itself. As a fallback, extract the visible text and note it was truncated. |
| **Ad disappeared** | The ad may have been paused between finding it and screenshotting. Note it as "observed but no longer active" — the angle is still worth noting even without a capture. |
| **Video won't play / thumbnail unclear** | Screenshot the thumbnail as-is. Note in your extraction that the creative was a video and describe whatever is visible. |
| **Page scrolls away from target ad** | Use JavaScript to scroll a specific element into view, or take the screenshot immediately after scrolling to the ad's position. |

---

## Phase 3: Extract Strategy from Each Ad

This is where the value is. For each captured ad, extract seven strategic elements. The goal is not to describe what's in the ad — it's to identify the **strategic hypothesis** behind it. Why did someone decide to make this ad? What are they betting will persuade the viewer?

### The Extraction Framework

| Element | What It Is | How to Extract It |
|---------|-----------|-------------------|
| **Angle** | The core persuasion hypothesis — the testable belief the ad is built around. This is the *why* behind the ad. | Ask: "What single belief does this ad want me to adopt?" Classify by type: **Functional** (what the product does — solves a problem, saves time/money), **Emotional** (how it makes you feel — stress relief, confidence, connection), **Identity** (who you become — creative person, good parent, mindful adult), or **Social** (how others perceive you — impressive gift-giver, aesthetic home, eco-conscious). Most ads blend 2 types — identify the primary and secondary. |
| **Hook** | The first 1-3 seconds (video) or first line (static) that earns attention. This is what stops the scroll. | Identify the pattern: **Question** ("Tired of [pain]?", "What if you could [promise]?"), **Statement** ("This changed everything about my [routine]", "I never thought I'd [benefit]"), **Visual** (satisfying process/ASMR, before/after, unexpected use case, reaction shot), or **Pattern interrupt** (counter-intuitive claim, controversy, breaking fourth wall). Quote the exact text or describe the exact visual. |
| **Promise** | The transformation or benefit offered — what the customer gets. | Ask: "What outcome is being sold?" This is the positive result, not the product features. "Stress relief and family bonding" not "a pottery wheel." The promise should be expressible as a before/after: "Before: [pain state] → After: [promise state]." |
| **Pain** | The problem, frustration, or desire being addressed. | Ask: "What itch does this scratch?" Look for the tension the ad creates or assumes exists. Good pain identification is specific: "parental guilt about kids' screen time" not just "bored kids." |
| **Proof** | The evidence shown to make the promise believable. | Ask: "Why should I believe this?" Identify the type and rate its strength: **Demo** (product in action, a test — HIGH, seeing is believing), **Testimonial** (customer quote, review screenshot — HIGH, social proof), **Stats** ("10,000+ sold", "4.9★ rating" — MEDIUM, quantifiable), **Authority** ("As seen on [media]", expert endorsement — MEDIUM, borrowed trust), **Comparison** (side-by-side vs competitor — MEDIUM, relative value), **Guarantee** ("30-day money back" — LOW, risk reversal), **Specs** (technical details, materials — LOW, for detail-oriented buyers). |
| **Offer** | The deal, discount, bundle, or CTA. | Ask: "What's the deal?" Note exact terms: "20% off with code SPRING20", "Free shipping over $50", "Buy 2 get 1 free", or "No offer — pure brand awareness play." The specificity matters for pattern analysis. |
| **Objection** | The concern or doubt the ad preemptively addresses. | Ask: "What objection does this overcome?" Look for phrases like "No mess", "Easy cleanup", "Fits any cupholder", "Won't break" — these are rebuttals baked into the ad copy or visuals. Not every ad addresses an objection; leave blank if none is present. |

### Extraction Quality Standard

The difference between useful and useless extraction:

**Example 1 — Pottery wheel video ad:**

| Element | ❌ Weak (generic, lazy) | ✅ Strong (strategic, specific) |
|---------|----------------------|-------------------------------|
| Angle | "pottery wheel ad" | Screen-free family bonding (emotional + identity) — hypothesis: parents will buy when positioned as anti-screen-time alternative |
| Hook | "shows a mom" | "Another rainy day at home..." text over shot of bored kid on tablet → hard cut to same kid at pottery wheel, laughing |
| Promise | "fun for kids" | Transform screen time into creative family time — kid produces something tangible (finished painted mug shown at end) |
| Pain | "bored kids" | Parental guilt about screen time + running out of rainy-day indoor activities |
| Proof | "testimonial" | "Over 5,000 families tried it" stat overlay + 3-sec clip of child holding finished painted mug (outcome proof — strongest type for this angle) |
| Offer | "discount" | Starter Bundle: wheel + 2 lbs clay + tools + free shipping. Price crossed out $89 → "Launch Price $69" |
| Objection | "easy" | "Too messy?" — 2-second scene showing clay wiping off table with wet cloth. Directly kills the #1 parent objection. |

**Example 2 — Travel mug static ad:**

| Element | Extraction |
|---------|------------|
| **Angle** | Leakproof commute (functional) — hypothesis: commuters will buy if they trust it won't leak in their bag |
| **Hook** | Split-image: left = coffee-stained bag interior, right = clean bag with mug. Text overlay: "Never again." (before/after visual hook) |
| **Promise** | Hot coffee for 6+ hours, zero spills. Before: ruined bags and lukewarm 10am coffee. After: confident commute, hot coffee on arrival. |
| **Pain** | Ruined bags/clothes from leaky travel mugs. Lukewarm coffee by mid-morning. Frustration with products that promise leak-proof but aren't. |
| **Proof** | Customer review screenshot: "KEEPS IT HOT ALL DAY! - Sarah M. ★★★★★" (testimonial — high strength) + close-up of ceramic interior lining (spec/demo hybrid) |
| **Offer** | Free lid upgrade + 15% off first order (code: COMMUTE15). Time-limited: "This week only" |
| **Objection** | "Plastic taste?" — callout box: "100% ceramic interior — no metallic or plastic aftertaste." Targets the #1 objection for ceramic vs. stainless mugs. |

**Example 3 — Gift-focused carousel ad:**

| Element | Extraction |
|---------|------------|
| **Angle** | Unique memorable gift (emotional + social) — hypothesis: gift shoppers will buy when positioned as "the gift that makes you the favorite aunt/uncle/friend" |
| **Hook** | Slide 1: Unwrapping scene — child tears open box, camera catches genuine surprised reaction. Text: "The gift they'll actually remember." (visual hook + statement combo) |
| **Promise** | Be the gift-giver who gives something creative and memorable, not another Amazon generic. The gift creates an experience, not just an object. |
| **Pain** | Gift shopping anxiety — everything feels generic, impersonal, forgettable. "I never know what to get them." |
| **Proof** | "As featured on Today Show" text overlay (authority — medium strength) + slide 3 shows customer photo of finished pieces with caption "My daughter made these!" (UGC/outcome proof) |
| **Offer** | Holiday Special: Gift bundle + free gift wrap + "Order by Dec 20th for guaranteed delivery" (scarcity + convenience) |
| **Objection** | "Will they actually use it?" — slide 4 shows family pottery night scene with text "3 months later, still their favorite Saturday activity" (longevity proof kills the "gathering dust" objection) |

### Per-Ad Extraction Template

Use this structure for each ad in your working notes. This feeds directly into the report:

```markdown
### Ad [##]: [2-3 word descriptor]

**Screenshot**: captures/[##]_[filename].png
**Format**: video / static / carousel
**Running Since**: [date from ad metadata]
**Platforms**: FB / IG / Both
**Low Count?**: yes / no

| Element | Extraction |
|---------|------------|
| **Angle** | [angle + type classification + strategic hypothesis] |
| **Hook** | [exact text or scene description + hook pattern type] |
| **Promise** | [transformation, not features — express as before/after if possible] |
| **Pain** | [specific frustration or desire — be precise] |
| **Proof** | [evidence type + strength rating + specific details] |
| **Offer** | [exact terms, not "discount"] |
| **Objection** | [what doubt + how addressed — or "none"] |

**Winning signals**: [Why selected — longevity? family size? cross-format?]
**Creative family notes**: [# of variants observed, how they differ]
```

---

## Phase 4: Pattern Analysis

After extracting all individual ads, zoom out. The pattern analysis reveals the competitor's *strategy*, not just their individual ads.

### What to Analyze

**Angle distribution** — Which angles appear most frequently? If 6/8 ads use "stress relief," that's their core tested angle. One lonely "gift" ad = they're just testing it. This tells you where they've found product-market fit in their messaging.

**Proof strategy** — What proof types dominate? All demos = product-confidence brand (they believe showing it working is enough). All testimonials = social-proof-dependent. No proof at all = either top-of-funnel brand awareness or an early-stage company that hasn't collected proof yet.

**Hook patterns** — Do they favor questions, statements, visual hooks, or pattern interrupts? Is there a dominant opening strategy? If every ad opens with a question, that's a formula they've tested.

**Offer strategy** — Same offer everywhere = proven converter they've settled on. Different offers per ad = still testing what converts. No offers = top-of-funnel brand play or premium positioning that avoids discounting.

**Creative families** — How many *distinct* angles are they actually testing? Ten ads might only represent 3 real angles with variants. Group the ads into families. Large families (4+ variants) = high confidence in that angle. Singleton ads = tests.

**Format allocation** — Are they investing in video, static, or carousel? What ratio? Brands often start with static (cheap to produce), move to video when an angle proves out, then build carousels for consideration-stage retargeting. Their format mix reveals their funnel maturity.

---

## Phase 5: Brand Mapping (If Context Provided)

This phase only runs when the user has provided brand context — a document with their product lines, angle taxonomy, personas, and objection lists. If no brand context was provided, skip to Phase 6. The report and brief will still be valuable without brand mapping; they'll just be generic competitive intelligence rather than mapped to specific taxonomies.

When brand context IS available (loaded from `references/brand-context.md` or user-provided file):

1. **Map competitor angles to your brand's angle taxonomy** — For each competitor angle, find the closest match in the brand's predefined angle enums. If no match exists, that's a gap worth flagging — either the brand hasn't considered this angle, or it's intentionally excluded.

2. **Identify persona overlap** — Which of the brand's target personas would respond to each competitor ad? This reveals which segments competitors are fighting for vs. which are underserved.

3. **Flag objection gaps** — What objections are competitors addressing that the brand doesn't have in its objection list? These are potential vulnerabilities — customers have these concerns and competitors are handling them.

4. **Note proof types to test** — What evidence strategies are competitors using that the brand hasn't tried? If every competitor uses demo videos but the brand only uses testimonials, that's a production opportunity.

5. **Gap analysis** — This is the most valuable output. Two kinds of gaps:
   - **Offensive gaps**: Angles competitors are running that the brand hasn't tested. These are proven angles with evidence of working.
   - **Defensive gaps**: Objections competitors are handling that the brand ignores. These are vulnerabilities.

---

## Phase 6: Generate Deliverables

Produce two files saved to `ad-research/[BrandName]/`:

### Deliverable 1: Research Report

**File**: `[BrandName]_Research_Report.md`
**Template**: [assets/report-template.md](assets/report-template.md)

Contents:
1. **Competitor Overview** — Brand name, total active ad count, date analyzed, Library URL
2. **Winning Ad Signals Summary** — The macro patterns: what signals indicate success across their program
3. **Top Ads Deep-Dive** (3-5 ads) — Full extraction tables from Phase 3, with screenshots referenced
4. **Pattern Analysis** — Angle distribution, proof types, hook patterns, offer strategy, creative families from Phase 4
5. **Brand Mapping** (if context provided) — Angle mappings, persona overlap, gap analysis from Phase 5
6. **Strategic Recommendations** — Angles to test, gaps to exploit, proof types to try, objections to address
7. **Content Production Ideas** — Specific ad concepts with immediate tests and backlog items
8. **Appendix** — Table of ALL captured ads with basic tags (every ad you screenshotted, not just the deep-dive ones)

### Deliverable 2: Creative Brief

**File**: `[BrandName]_Creative_Brief.md`
**Template**: [assets/creative-brief-template.md](assets/creative-brief-template.md)

The brief distills research into 3-5 producible ad concepts. For each concept:
1. **Angle + hook** — The specific opening and persuasion strategy
2. **Body copy direction** — Not final copy, but the message flow after the hook
3. **Proof elements needed** — What footage, assets, or testimonials are required to produce this
4. **Offer/CTA** — The deal and call-to-action
5. **Objection addressed** — What concern this concept handles
6. **Production checklist** — What needs to be shot, sourced, or designed
7. **Complexity rating** — Quick win (repurpose existing assets) / Medium (new footage needed) / Full shoot (scripted production)
8. **Priority ranking** — Biggest uncontested gaps first, quick wins weighted up

Include a **Competitor Angle Map** showing which competitor insight inspired each concept, and a **Testing Plan** (Week 1 quick wins, Week 2-3 medium-lift items, measurement criteria).

### Share with User

Link to both files individually using `computer://` paths when complete. Also link to the captures folder so the user can browse screenshots.

---

## Pacing and Guardrails

- **Time**: ~60 minutes per competitor scan. If past 45 minutes and still capturing ads, stop capturing and move to extraction with what you have.
- **Ad count**: 5-10 ads per competitor. More than 10 rarely adds insight and significantly slows the workflow.
- **Breadth over depth**: Better to cover 2-3 competitors shallowly than obsess over 1. For multi-competitor requests, do a quicker pass per competitor.
- **Don't copy production style**: Focus on the *angle/hook/strategy*, not editing tricks or production polish. A Fortune 500 brand's cinematic ad isn't replicable at SME budgets — but their *angle* might be.
- **Screenshot immediately**: Ad Library links expire when ads stop running. Never plan to "come back later" for a screenshot. Capture the moment you identify an ad worth analyzing.
- **Low-count = test**: "Low count" label means < ~100 impressions. It's a test that hasn't proven anything. Note novel angles but don't treat them as winners.
- **Stay strategic**: The value is in the extraction framework and pattern analysis, not in comprehensively cataloging every ad. Ten perfectly extracted ads with pattern analysis beats fifty with just screenshots.

---

## How Meta Ad Library Works (Quick Reference)

Essential context for interpreting what you see:

- **US Library = active ads only** — Shows only ads currently running. Once an ad stops, it disappears from the Library entirely. No historical archive for non-political US ads.
- **EU-targeted ads** — Archived for 12 months under DSA regulations, so EU searches show more history. Political ads archived for 7 years.
- **No performance data visible** — You cannot see clicks, conversions, spend, or impressions (except limited EU/DSA data). This is why proxy signals (longevity, creative families, etc.) matter.
- **~24 hour delay** — New ads appear roughly 24 hours after their first impression.
- **Links expire** — Direct links to specific ads break once the ad stops running. This is why immediate screenshots are non-negotiable.
- **What IS visible**: Publisher page name, ad start date, placements (FB vs IG), headline, primary text, CTA, creative (image/video thumbnail).
- **What is NOT visible**: Spend, impressions, clicks, conversions, audience targeting, A/B test group assignments, end date.

---

## Building a Competitor Set

When the user doesn't specify which competitors to research, or asks "who should I look at?":

- **In-league** — Similar-size DTC brands in the same category. These share your audience and budget constraints. Primary research focus.
- **Out-of-league** — Large retailers or big brands in your space. Scan for angle ideas, but their production values aren't replicable. Scale the *idea* back to your level.
- **Adjacent / job-to-be-done** — Brands solving the same customer need through different products. A pottery wheel competes with STEM kits for "creative kids activity." A travel mug competes with premium thermoses for "commute companion." Adjacent competitors reveal emotional hooks and angles you'd never find looking only at direct competitors.
- **Positioning filter** — If every competitor hammers "low price," there's an opening for premium/quality positioning. If they all go premium, there might be a value gap. Pick competitors across strategies to see the full landscape.
- **Regional/seasonal** — EU-targeted ads are archived longer (12 months), so EU searches reveal more history. Seasonal/holiday brands may show trends useful for planning.

---

## Reference Files

- [methodology.md](references/methodology.md) — Extended research playbook: daily/weekly workflow cadence, building competitor sets, 10 common pitfalls
- [brand-context.md](references/brand-context.md) — Loadable brand context file. Replace with your brand's taxonomy for brand-mapped reports. Default example: Table Clay (ceramics/pottery ecommerce)
- [report-template.md](assets/report-template.md) — Research report output template with completed example sections
- [creative-brief-template.md](assets/creative-brief-template.md) — Creative brief output template with completed example sections
