# SEO & Blog Structure Guide

Practical rules for making research-backed blog posts findable. The dossier gives you substantive content; this guide ensures that content is structured for search engines and readers.

---

## Keyword Placement

### Required Placement (every post)

1. **Title (H1)** — The primary keyword or a natural variation appears in the title
2. **First 100 words** — Introduce the keyword naturally in the opening paragraph
3. **2-3 H2 subheadings** — Use the keyword or close variants in section headings where it reads naturally (do not force it into headings where it sounds awkward)
4. **Meta description** — The keyword appears once in the 155-160 character meta description
5. **URL slug** — The slug should contain the primary keyword, hyphenated (e.g., `mini-pottery-wheel-buying-guide`)

### Keyword Density

Target 1-2% density (roughly 1 use per 100-150 words). This should happen naturally when writing about the topic — if you have to force keyword mentions, the post is probably off-topic or too broad.

### Semantic Variations

Use related terms and natural variations throughout the post rather than repeating the exact keyword. The dossier's Market Landscape section (S3) is a natural source of related terms — product categories, alternative names, and needs language all serve as semantic variations.

**Example:** If the primary keyword is "mini pottery wheel," natural variations include: "beginner pottery wheel," "tabletop pottery wheel," "at-home pottery kit," "small pottery wheel for adults," "clay wheel for beginners."

---

## Heading Hierarchy

### Rules

- **Single H1**: The title. Only one per post.
- **H2**: Major sections. Each H2 should represent a distinct topic the reader might search for or scan to.
- **H3**: Subsections within an H2. Used for individual products in a comparison, individual FAQ entries, individual reasons in a listicle.
- **H4**: Rarely needed. Use only for sub-breakdowns within an H3 (e.g., pros/cons within a product spotlight).
- **Never skip levels**: Don't jump from H2 to H4.

### Heading Writing

- Front-load the value: "What to Look For in a Pottery Wheel" beats "Things You Should Consider"
- Use question format for FAQ-style sections: "Is It Too Messy?" outperforms "Mess Considerations"
- Keep headings under 60 characters for consistent display in search results

---

## Meta Description

Write a meta description for every post. This appears in search results below the title.

### Template

```
[Keyword context] + [value prop or curiosity hook] + [proof or specificity]. [CTA or question.]
```

### Examples

```
"Looking for the best mini pottery wheel? We compared 8 top options based on real customer reviews and hands-on research. Find the right one for your skill level."

"Is a pottery wheel kit actually worth it? We break down the 5 most common concerns with honest answers from real buyers."

"Why thousands of adults are picking up pottery as a hobby — and what the research says about why they stick with it."
```

### Rules
- 155-160 characters (Google truncates beyond this)
- Include the primary keyword naturally
- Promise something specific (a number, a comparison, a resolution)
- Don't use generic calls to action ("Click here to learn more")

---

## Blog Post Markdown Frontmatter

Every blog post output starts with YAML frontmatter for CMS import:

```yaml
---
title: "The Complete Mini Pottery Wheel Buying Guide for 2025"
meta_description: "Compared 8 mini pottery wheels based on real customer reviews..."
target_keyword: "mini pottery wheel buying guide"
date: YYYY-MM-DD
author: ""
category: ""
tags: []
---
```

- `title`: The H1 title, also used as the page title
- `meta_description`: 155-160 characters
- `target_keyword`: The primary SEO keyword
- `date`: Generation date (user can update for publication)
- `author`: Left blank for the user to fill
- `category` and `tags`: Left blank or suggested based on post type

---

## Readability

### Targets
- **Sentence length**: Average 15-20 words. Mix short punchy sentences with longer explanatory ones.
- **Paragraph length**: 2-4 sentences. Single-sentence paragraphs are fine for emphasis. Walls of text get skipped.
- **Active voice**: Default to active. Passive is acceptable in evidence-presenting contexts ("The product was rated 4.8 stars").
- **Reading level**: Aim for accessible language. Write for clarity, not sophistication. If a simpler word works, use it.

### Formatting for Scannability
- **Bold** key phrases within paragraphs (1-2 per paragraph max) so scanners can get the gist
- **Bulleted lists** for 3+ parallel items
- **Tables** for comparison data (comparison posts, buying guides)
- **Blockquotes** for customer quotes — these visually break up text and draw the eye

---

## Image Placeholders

Blog posts should indicate where images would add value, since the skill generates text, not visuals.

### Placeholder Format

```markdown
![Alt text describing what the image should show](placeholder)
*Caption: [Suggested caption text]*
```

### Common Placements
- **Hero image**: Below the H1, before the first paragraph
- **Product comparison**: Alongside or within the comparison table
- **Quote highlights**: A designed quote card for the strongest customer quote
- **How-to steps**: If the post includes instructional content
- **Before/after**: If the post type involves transformation

### Alt Text
Write descriptive alt text from the dossier context:
- "Side-by-side comparison of 4 mini pottery wheels showing size differences" (not "product comparison")
- "Customer using Table Clay pottery wheel at kitchen table" (not "product in use")

---

## Internal Linking Strategy

After generating a post, suggest 3-5 other post types from the same dossier that could link to or from this one. This builds a **content cluster** — a group of interlinked posts around a single topic that strengthens SEO for all posts in the cluster.

### How It Works

Each blog post type covers different dossier sections. Posts that share data sources are natural linking partners.

### Linking Suggestion Format

After the blog post, include a section:

```markdown
## Suggested Internal Links

Posts from the same research dossier that pair well with this one:

- **[Buying Guide] ↔ [Comparison Post]**: The buying guide's criteria section
  links naturally to a detailed comparison of specific products.
- **[FAQ Post] ↔ [Problem-Solution Post]**: FAQ answers can link to the
  deeper problem-solution narrative for readers who want more context.
- **[Listicle] ↔ [Educational Post]**: "10 Reasons to Try Pottery" links
  naturally to "Why Pottery Is the Creative Outlet You Need."
```

### Cluster Priority

The ideal first three posts from any dossier form a **core cluster**:
1. **Buying Guide** or **Comparison Post** (decision-stage, high purchase intent)
2. **FAQ / Myth-Busting** (consideration-stage, objection resolution)
3. **Educational / Listicle** (awareness-stage, top-of-funnel traffic)

This covers the full funnel with interlinked content.

---

## What This Guide Does NOT Cover

- **Keyword research**: This skill does not do keyword research. Accept user-provided keywords. If none provided, derive a reasonable keyword from the product name + post type.
- **Backlink strategy**: Off-page SEO is outside this skill's scope.
- **Technical SEO**: Schema markup, site speed, canonical tags, etc. are CMS/platform concerns.
- **Content calendar planning**: The skill generates one post at a time. Calendar strategy is the user's domain.
