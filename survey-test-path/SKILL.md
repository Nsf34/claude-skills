---
name: survey-test-path
description: "Generate survey test path documents from survey documents and test matrices. A test path is a detailed QA walkthrough that specifies—for each question in a survey—exactly what a tester should select, verify, and expect to see or not see. Use this skill whenever the user mentions 'test path', 'test plan', 'test matrix', 'survey QA', 'survey testing', 'test path document', 'test grid', or wants to create testing documentation for a programmed survey. Also trigger when the user uploads a survey document alongside a test matrix/grid and asks for test paths, QA documentation, or testing instructions. This skill handles complex survey logic including variable assignments, conditional branching, piping, looping, termination logic, randomization, and anchoring verification."
---

# Survey Test Path Generator

## What This Skill Does

This skill transforms a survey document and test matrix into a complete test path document—a .docx file that QA testers use to systematically verify every branch, variable, pipe, and display rule in a programmed survey. Each test path walks through the entire survey question by question, specifying exactly what to select, what to verify, and what should or shouldn't appear based on the path's variable assignments.

This is high-stakes work. Surveys are expensive to field, and errors in programming logic (wrong piping, broken skip patterns, incorrect termination) can invalidate data. The test paths must be exhaustive and precise—every response option number must be correct, every conditional display rule must be checked, and every piped variable must be verified.

## Inputs Required

1. **Survey Document** (.docx): The full survey specification containing all questions, response options, programming instructions, variable assignments, conditional logic, quotas, and piping rules.

2. **Test Matrix** (.xlsx or similar): A grid where rows are key survey variables and columns are individual test paths. Each cell specifies the value that variable should take for that path.

Before starting, read both input files completely. Read the survey document at least twice—once for overall flow, once for variable/conditional logic detail. Understanding the full survey structure before writing any test paths prevents cascading errors.

## Core Workflow

### Phase 1: Deep Survey Analysis

Before writing a single test path, build a complete mental model of the survey. Read `references/survey-analysis-guide.md` for the detailed procedure on how to extract and catalog:

1. **All variables created** — Every hidden variable, assignment, and computed value
2. **All conditional display rules** — Which questions/options appear based on which variables
3. **All termination points** — Immediate vs. held terminations, and what triggers each
4. **All piping rules** — Where variable values get inserted into question text or response options
5. **All looping/carousel logic** — Questions that repeat for multiple category or brand assignments
6. **All randomization and anchoring rules** — What gets randomized, what stays anchored, what stays grouped together
7. **Response option numbering** — Map every response option to its R# for each question

This analysis phase is the foundation. Rushing it causes errors that cascade through every test path. Take the time to build a thorough variable map before proceeding.

### Phase 2: Parse the Test Matrix

The test matrix defines which variable combinations each path should exercise. For each column (test path):

1. Identify every variable assignment specified in that column
2. Trace the implications of those assignments forward through the survey — what becomes visible, what gets piped, what gets skipped
3. Determine the specific response options (R# in C#) needed at each question to produce those variable assignments. This requires cross-referencing the survey document's response tables.
4. Identify questions where the path has no specific matrix requirement — these will typically be "Select any" unless certain options would cause termination, unwanted variable assignments, or unintended skip patterns

### Phase 3: Determine Response Selections for Non-Matrix Questions

For questions not directly driven by a matrix variable, the skill must reason about what to select:

- **Default**: "Select any" — when no selection affects the path
- **Avoid termination**: "Select any EXCEPT R[x]" — when certain options would terminate the respondent before the path is complete. Identify these by checking the survey doc's termination instructions for each question.
- **Avoid unwanted assignments**: "Select any EXCEPT R[x]" — when certain options would assign a variable that conflicts with the path's intended route
- **Avoid skipping content**: Sometimes selecting certain options causes the respondent to skip questions the tester should verify. Select options that keep the tester in the fullest version of the path.
- **Ensure downstream visibility**: If a later question requires a particular earlier response (e.g., "Only show if respondent selected R1 in S10"), make sure the earlier selection supports this

### Phase 4: Write the Test Path Document

Generate a .docx file using the docx skill. Read `references/document-structure.md` for the exact formatting specification.

The document has these sections, in order:

#### Section 1: General Checks
A standardized list of formatting and behavior checks that apply across all survey testing. These are mostly consistent across projects. Read `references/general-checks-template.md` for the standard template. Customize only if the survey has unusual formatting requirements.

#### Section 2: Screener Termination Checks
Lists every termination point in the screener section with:
- The question number and termination trigger
- Whether it's an immediate termination or held until end of screener
- What the tester should verify (e.g., "Ensure respondent is shown all remaining screener questions before being terminated")

Generate this by scanning the survey document's screener section for every termination instruction. Group by immediate vs. held terminations.

#### Section 3: Test Paths (one per matrix column)

Each test path is a numbered column (Test 1, Test 2, etc.) that walks through every survey question in order. For each question, include:

**a) Selection instruction**: What the tester should select
- Use exact R# and C# notation from the survey document (e.g., "Select R3 in C1 and C2")
- For "select any" scenarios, still be specific about exclusions
- For open-ended responses, specify what to type if it matters for piping

**b) Ensure checks**: What the tester should verify at this question
- Question text contains correct piped values (e.g., "Ensure question text reads 'How often do you drink Ocean Spray shelf-stable juice?'")
- Correct response options are visible/hidden based on conditional display
- Randomization is working (options appear in different order)
- Anchored items remain at bottom/top
- Grouped items stay together ("Keep R1 and R2 together")
- Correct question type (single-select vs multi-select)
- Conditional messages appear/don't appear
- Scale labels and carousel behavior are correct

**c) Variable assignment verification**: What variables should be assigned after this question
- "After selection, respondent should be assigned variable_name = value"

**d) Skip/routing verification**: If this question should be skipped for this path
- "Ensure you DO NOT see this question" with explanation of why

### Phase 5: Cross-Reference and Verify

After generating all paths, verify:

1. **Every matrix variable is exercised** — Each variable value in the matrix has at least one path that tests it
2. **No termination conflicts** — Selections in each path don't accidentally terminate the respondent
3. **Piping consistency** — Variables assigned early in the path are correctly referenced in later "Ensure" checks
4. **Response option accuracy** — Every R# reference matches the actual position in the survey document's response tables (R1 is the first option, R2 is the second, etc.)
5. **Skip logic completeness** — Every conditional display rule in the survey is verified in at least one path (either "should see" or "should NOT see")
6. **Loop/carousel handling** — Questions that loop for multiple categories are properly expanded with the right categories for each path

## Critical Rules

These rules exist because errors here have caused real problems in past test plans:

**Response option numbering**: R1 is always the first response option listed in the survey document's table for that question, R2 is the second, etc. Do not skip numbers, do not renumber. If the survey document's table shows 10 options, they are R1-R10 in order. Column numbering follows the same pattern (C1, C2, C3...).

**Pipe verification must use actual values**: When checking piped text, don't write "Ensure question pipes correctly." Write the actual expected text: "Ensure question reads 'Which of these brands have you purchased for yourself in the past 3 months?'" — using the exact words that should appear given the path's variable assignments.

**Termination awareness at every selection**: Before writing "Select any" for a question, check if ANY response option at that question triggers termination. If so, write "Select any EXCEPT R[x]" and explain why.

**Held vs. immediate terminations**: These are different and the test plan must distinguish them. Immediate terminations end the survey right away. Held terminations let the respondent continue through the screener (seeing all remaining screener questions) before terminating at the end.

**Question numbering**: Use the question identifiers from the survey document (S1, S2, Q301, etc.). If the survey document uses custom numbering (like "S10" for screener question 10, or "Q503" for main survey question), mirror that exactly.

## Output Quality Standards

The finished document should be indistinguishable from one a senior researcher wrote by hand. This means:

- No placeholder text or TODO markers in the final output
- Every R#/C# reference has been verified against the survey document
- Piped text uses the actual variable values, not variable names
- The document is complete — no "continue pattern for remaining questions" shortcuts
- Formatting is clean and consistent with the reference examples

## Reference Documents

Read these before generating output:

| Reference | When to Read | What It Contains |
|-----------|-------------|-----------------|
| `references/survey-analysis-guide.md` | Always, first | How to systematically extract variables, conditions, and logic from a survey document |
| `references/document-structure.md` | Before writing output | Exact formatting spec for the .docx output, including heading styles, bullet formats, and table structure |
| `references/general-checks-template.md` | Before writing General Checks section | Standard boilerplate for the General Checks section |
| `references/example-patterns.md` | When writing test path entries | Common patterns showing how to write selection instructions and ensure checks for different question types |

## Messages vs. Questions

Survey documents contain two distinct element types. Treat them differently:

**Messages (M1, M2, M3, etc.)** are standalone display elements that appear between question batteries. They serve as transition markers and sometimes carry piped data. In test paths:
- Messages never have "Select" instructions — they are verification-only
- Write: "M2: Ensure you see message" or "M2: Ensure you do not see message"
- If the message contains piped text: "M7: Ensure you see message with [variable] piped through"
- Messages signal section transitions (e.g., M2 often marks screener-to-main-survey transition, M3 marks entry to category-level questions)

**Questions (S1, Q301, D1, etc.)** always have both selection instructions and ensure checks.

## Survey Numbering Convention

Surveys follow a hierarchical numbering system. Mirror the survey document's exact numbering:

- **S-series (S1, S2, S10, S10A...)**: Screener questions — qualification, demographics, category engagement
- **M-series (M1, M2, M3...)**: Messages — transition markers between sections, no selections
- **Q-series with hundreds grouping**: Main survey questions grouped by battery
  - Q1xx: Category/brand perception
  - Q2xx: Brand-specific exploration (often looped per brand)
  - Q3xx: Decision/consideration factors
  - Q4xx: Feature importance / attitudes
  - Q5xx: Future intent / consumer segments
- **D-series (D1, D2, D3...)**: Demographics — always at the end of the survey
- **Sub-questions (S10A, Q211A)**: Follow-ups or carousel continuations within a question block

## Test Matrix Section in the Document

Between the Screener Termination Checks and the Test Paths, include the **Test Matrix** as a reference table. This reproduces the matrix grid the user provided, formatted as a table in the .docx with:
- Rows = key survey variables being tested
- Columns = test path numbers (Test 1, Test 2, etc.)
- Cells = the assigned values for each variable in each path

This gives testers a quick reference for understanding what each path is designed to exercise, without needing to read through the full path detail.

## Exact Language for "Ensure" Checks

Use these exact phrasings — they match the established standard and testers are trained to look for them:

**Visibility**: "Ensure you see [element]" / "Ensure you do not see [element]"
**Piping**: "Ensure [variable value] is piped through" / "Ensure [variable value] is piped through in question text" / "Ensure [variable value] is piped through in R14 response option text"
**Question format**: "Ensure multi select in C1 and C2" / "Ensure single select" / "Ensure question is a [N] point scale" / "Ensure question is a [N] point agreement scale"
**Anchoring**: "Ensure [option text] is anchored at bottom and mutually exclusive" / "Ensure [option text] is anchored to the bottom and open-end"
**Grouping**: "Ensure R1 & R2 are together" / "Ensure R3-R8 are together"
**Assignment**: "Ensure assigned [variable]" / "Ensure assigned [variable] = [value]"
**Looping**: "Ensure you are looped through Q503-Q507 for each response to Q502" / "Ensure all possible questions in Q201-Q229 are looped up to two times for all assigned [brand]"
**Formatting**: "Ensure '[text]' is bolded" / "Ensure '[text]' is underlined"

## Common Question Types and How to Handle Them

### Single-select questions
Selection: "Select R[x]" — one option only
Checks: "Ensure single-select", anchoring, randomization, mutual exclusivity on "None of the above" type options

### Multi-select questions
Selection: "Select R[x] and R[y]" — can select multiple
Checks: "Ensure multi-select", anchoring, randomization, mutual exclusivity on exclusive options

### Grid/matrix questions (multi-column)
Selection: "Select R[x] in C1, R[y] in C2"
Checks: Column labels correct, must-select-in-C1-before-C2 logic works, proper piping per column

### Carousel/scale questions
Selection: "Select [value] for [item]"
Checks: All items appear, scale labels correct, randomization of items (not scale)

### Open-ended questions
Selection: "Type '[specific text]'" when piping matters, or "Type any response" when it doesn't
Checks: Text field appears, character limits if specified

### Looped questions
These repeat for each assigned category/brand. Expand them fully — write out each iteration with the specific category/brand piped in.
Selection: Specify for each iteration
Checks: Correct number of iterations, correct piping per iteration

### Conditional display questions
For paths where the question SHOULD appear: Write normal selection and checks
For paths where the question should NOT appear: "Ensure you do not see this question" (use exact phrasing)

### Messages
No selection. Verification only: "Ensure you see message" or "Ensure you do not see message"
If piped: "Ensure you see message with [actual piped value] piped through"
