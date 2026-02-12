# Brand Context Template

Use this template to generate brand context files. Start with the Standard sections. Add the Extended sections only when the brand has enough product complexity and the user needs structured ad creative support.

---

## Standard Sections (Always Include)

```markdown
# {Brand Name} Brand Context

## Brand Overview

**Brand name:** {Brand Name}
**Instagram handle:** {handle or _TBD_}
**Facebook page:** {page name or _TBD_}
**TikTok handle:** {handle or _TBD_}
**Chrome profile name:** {exact Chrome profile name for automation, or _TBD_}

**Brand Positioning:** {1-2 sentence positioning statement distilled from research doc}

---

## Products

| Product | Price | Description |
|---------|-------|-------------|
| {Product 1} | {$XX or _TBD_} | {One-line description} |
| {Product 2} | {$XX or _TBD_} | {One-line description} |

---

## Target Customers

- **{Segment 1}** — {who they are and why they buy}
- **{Segment 2}** — {who they are and why they buy}
- **{Segment 3}** — {who they are and why they buy}

---

## Content Themes

- {Theme 1 — what topics to look for and engage with in feeds}
- {Theme 2}
- {Theme 3}
- {Theme 4}
- {Theme 5}

---

## Competitors

| Account | Why They Compete |
|---------|-----------------|
| {handle} | {one-line reason} |
| {handle} | {one-line reason} |
| {handle} | {one-line reason} |
| {handle} | {one-line reason} |
| {handle} | {one-line reason} |

---

## Brand Voice

{2-3 sentences describing the social media personality. How should comments and replies sound? What's the vibe? Include what the voice is NOT.}

**Tone examples:**
- "{Example comment 1 — sounds like a real person on social media}"
- "{Example comment 2}"
- "{Example comment 3}"
- "{Example comment 4}"

---

## Source Research

This brand context file was distilled from the deep research document:
- **Research doc**: `research/{brand-name}-research.md`
- **Last synced**: {YYYY-MM-DD}

For comprehensive brand strategy, market analysis, customer research, and detailed product specifications, refer to the full research document.
```

---

## Extended Sections (Add When Needed for Ad Creative)

Insert these sections between "Content Themes" and "Competitors" when the brand needs structured ad creative support.

```markdown
## Tag Taxonomy

### Angles by Product Line

**{product_line_enum}:**
- `{angle_enum}` - {What this angle communicates}
- `{angle_enum}` - {What this angle communicates}
- `{angle_enum}` - {What this angle communicates}

**{product_line_enum}:**
- `{angle_enum}` - {What this angle communicates}
- `{angle_enum}` - {What this angle communicates}

---

### Personas

| Persona | Enum | Description |
|---------|------|-------------|
| {Persona Name} | `{enum}` | {One-line description} |
| {Persona Name} | `{enum}` | {One-line description} |

**By Product Line:**
- {product_line}: `{persona_enum}`, `{persona_enum}`, `{persona_enum}`

---

### Intent Context (Job-to-be-Done)

| Context | Enum |
|---------|------|
| {What the customer is trying to accomplish} | `{enum}` |
| {What the customer is trying to accomplish} | `{enum}` |

---

### Objection Targets by Product Line

**{product_line_enum}:**
| Objection | Enum | Counter |
|-----------|------|---------|
| {Common concern} | `{enum}` | {How the brand addresses it} |
| {Common concern} | `{enum}` | {How the brand addresses it} |

---

### Proof Types by Product Line

**{product_line_enum}:**
- `{proof_type}` - {What kind of evidence/content this is}
- `{proof_type}` - {What kind of evidence/content this is}

---

### Ad Creative Enums

**Funnel Stage:**
- `tof` - Top of funnel (awareness)
- `mof` - Middle of funnel (consideration)
- `bof` - Bottom of funnel (decision)
- `rt` - Retargeting

**Format:**
- `video`
- `static`
- `carousel`

**Ratio:**
- `9x16` - Vertical (Stories/Reels)
- `4x5` - Portrait (Feed)
- `1x1` - Square

**Offer Type:**
- `none`
- `bundle`
- `free_shipping`
- `limited_drop`
- `giftable`
- `discount`

### Filename Convention

{Brand}_{ProductLine}_{Format}_{FunnelStage}_{Concept}_{Angle}_{ProofType}_{HookKey}_{V#}_{Ratio}
```

---

## Guidelines for Filling the Template

1. **Products table**: Include all products the brand currently sells. If pricing isn't known, use `_TBD_`. Descriptions should be one line — enough to understand what it is, not a full product page.

2. **Target customers**: Pull directly from the research doc's persona/customer analysis. Translate academic persona language into plain English. "Millennial urban professionals seeking convenience-oriented solutions" becomes "Busy city workers who want things that save time."

3. **Content themes**: Think about what the brand's target audience scrolls past on social media. These themes guide what posts to engage with, not what the brand itself posts.

4. **Competitors**: Prioritize accounts with active social media presence. A competitor with 100K followers and daily posts is more useful for engagement strategy than a Fortune 500 company with a dormant Instagram.

5. **Brand voice**: This is the most important section. The tone examples are used directly by engagement and content skills as style references. Make them sound like real comments from a real person, not marketing copy.

6. **Enums (Extended only)**: Use lowercase_snake_case. Keep them short and descriptive. They're used as tags in filenames and databases, so they need to be consistent and parseable.
