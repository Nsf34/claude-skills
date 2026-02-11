# Document Structure Guide

This document specifies the exact formatting and structure for the test path .docx output. The goal is to produce a document indistinguishable from the hand-written reference examples.

## Overall Document Structure

The document is organized as follows:

```
1. Title Block
2. General Checks (Section)
3. Screener Termination Checks (Section)
4. Test Paths (Section per path)
   - Path header with variable summary
   - Question-by-question walkthrough
```

## Title Block

At the top of the document:
- **Project name**: Bold, large font (e.g., "Category Vision" or "Category Expansion")
- **Document type**: "Test Plan"
- **Version**: "v0.1" for initial draft
- No table of contents needed

## Section: General Checks

### Heading
Use Heading 1 style: "General Checks"

### Content
A bulleted list of universal verification items. These are largely standardized across surveys. The standard list (customize only if necessary):

- Ensure all questions are displaying correctly (no broken formatting, missing images, or overlapping elements)
- Ensure all response options are displaying correctly
- Ensure all skip patterns and routing logic are working as programmed
- Ensure all piping is displaying correctly (variable values appear where expected)
- Ensure all randomization is functioning (response options appear in different orders on different runs)
- Ensure all anchored response options remain in their anchored position (typically bottom)
- Ensure all "mutually exclusive" response options deselect other options when chosen and cannot be selected alongside other options
- Ensure all "Other, please specify" options open a text field when selected
- Ensure all open-ended text fields accept input and have appropriate character limits
- Ensure all required questions prevent advancement without a response
- Ensure all grid/matrix questions display all rows and columns correctly
- Ensure all scale questions display the full scale with correct labels
- Ensure all carousel questions cycle through all items
- Ensure progress bar (if present) advances appropriately
- Ensure back button (if enabled) preserves previous selections
- Ensure mobile rendering is acceptable (if mobile is a supported platform)

## Section: Screener Termination Checks

### Heading
Use Heading 1 style: "Screener Termination Checks"

### Structure
Organize by termination type:

**Subheading**: "Immediate Terminations"
For each immediate termination point:
- Question identifier and name (e.g., "S2 – Age")
- Trigger condition (e.g., "Select age below 18 or above 70")
- Expected behavior: "Ensure respondent is terminated immediately and shown the standard termination message"

**Subheading**: "Held Terminations (End of Screener)"
For each held termination point:
- Question identifier and name
- Trigger condition
- Expected behavior: "Ensure respondent continues to see all remaining screener questions, then is terminated after the last screener question with the standard termination message"

**Subheading** (if applicable): "Conditional Terminations"
For terminations that depend on variable combinations:
- Question identifier and name
- Trigger condition with variable dependencies (e.g., "Select R1 in S6 AND respondent is NOT assigned <student>")
- Expected behavior

## Section: Test Paths

### Path Header
Each test path starts with:

**Heading 1**: "Test [N]: [Brief description]"
Example: "Test 1: Ocean Spray / Myself / Grocery / In-Store"

**Variable summary table** (immediately after heading):
A simple table listing the key variable assignments for this path:

| Variable | Value |
|----------|-------|
| `<brand>` | Ocean Spray |
| `<Myself/Purchasing for child(ren)>` | Myself |
| `<channel>` | Grocery |
| `<retailer>` | Kroger |
| ... | ... |

This lets testers quickly understand what this path is testing before diving into the question-by-question detail.

### Question-by-Question Format

For each question in the survey, use this structure:

**Bold question identifier and name**: e.g., **S2 – Age**

Then a bulleted list with:

**Selection instruction** (always first):
- `Select [specific value or R#]` — for questions with matrix-driven selections
- `Select any` — for unconstrained questions
- `Select any EXCEPT R[x] [reason]` — when certain options must be avoided
- `Ensure you DO NOT see this question` — for questions that should be skipped

**Ensure checks** (after selection):
- `Ensure [specific verification]` — each check is its own bullet
- Group related checks logically (display checks, then piping checks, then formatting checks)

**Variable assignment note** (when relevant):
- `After this selection, respondent should be assigned <variable> = value`

### Formatting Rules

- Use bullet points (not numbered lists) for ensure checks within each question
- Use bold for question identifiers and key terms like "Ensure", "Select"
- Use code-style formatting (backticks in markdown, monospace in docx) for variable names
- Use quotation marks around expected piped text
- Indent sub-bullets for nested checks

### How to Handle Different Question Scenarios

**Question with straightforward selection**:
> **S3 – Gender**
> - Select any
> - Ensure single-select
> - Ensure response options are not randomized
> - Ensure "Prefer not to answer" is anchored at bottom
> - Ensure "Prefer not to answer" is mutually exclusive

**Question with matrix-driven selection**:
> **S14 – Brands**
> - Select R1 "Ocean Spray" in C1 and C2
> - Ensure question reads "Which of these brands have you purchased for yourself in the past 3 months?"
> - Ensure multi-select for C1, single-select for C2
> - Ensure respondent must select in C1 before selecting in C2
> - Ensure rows are randomized
> - Ensure "Mainstream private label" and "Premium private label" are kept together
> - Ensure "Other, please specify" is anchored at bottom with open-end field
> - Ensure "I didn't notice/don't remember" is anchored at bottom and mutually exclusive
> - After this selection, respondent should be assigned `<brand>` = "Ocean Spray"

**Question that should be skipped**:
> **M2 – Message for child purchasers**
> - Ensure you DO NOT see this question (respondent is assigned `<Myself>`, not `<Purchasing for child(ren)>`)

**Question with conditional text**:
> **Q301 – High-level Needs**
> - Select any in C1, then select any of the C1 selections in C2
> - Ensure question reads "In the past 3 months, why have **you** consumed shelf-stable juice products?" (because respondent is `<Myself>`, NOT "why have your child(ren)...")
> - Ensure multi-select for C1, single-select for C2
> - Ensure must select in C1 before selecting in C2

**Looped question**:
> **S9 – Consumption Frequency** (Loop 1 of 3: gummy candy)
> - Select any for "gummy candy"
> - Ensure carousel displays "gummy candy" as the category
> - Ensure category name is bolded
> - Ensure single-select
>
> **S9 – Consumption Frequency** (Loop 2 of 3: packaged cookies)
> - Select any for "packaged cookies"
> - Ensure carousel displays "packaged cookies" as the category
> [etc.]

## docx Formatting Specifications

When generating the .docx file, use the docx skill's standard approach. Key formatting:

- **Heading 1**: Section titles ("General Checks", "Screener Termination Checks", "Test 1: ...")
- **Heading 2**: Subsections within sections ("Immediate Terminations", "Held Terminations")
- **Bold text**: Question identifiers, "Ensure", "Select"
- **Normal text**: Body content, bullet items
- **Bullet lists**: All check items and selection instructions
- **Tables**: Variable summary tables at the start of each test path, with header row
- **Page breaks**: Between major sections (General Checks, Termination Checks, each Test Path)

Use US Letter page size, 1-inch margins, 11pt body text, single-spaced.
