# Document Patterns

Complete, copy-paste-ready patterns for common document types. Each pattern is a working Node.js script that produces a .docx file.

## Table of Contents

1. [Meeting Notes](#1-meeting-notes) — Title, attendees, section headers (bold+underline), bullet lists, topic subheaders (bold+italic)
2. [Research Dossier](#2-research-dossier) — Title page, heading hierarchy, tables, blockquotes, numbered references
3. [Survey Document](#3-survey-document) — 3-column question tables, screen markers, programming notes

---

## 1. Meeting Notes

Used by: `seurat-meeting-notes`, and similar consulting note-taking workflows.

**Key formatting**: Franklin Gothic Book 11pt, tight bullet spacing, bold+underline section headers, bold+italic topic subheaders.

```javascript
const docx = require("docx");
const fs = require("fs");

const { Document, Paragraph, TextRun, Packer, AlignmentType,
        UnderlineType, convertInchesToTwip } = docx;

// -- Font helper --
const FONT = "Franklin Gothic Book";
const SIZE = 22; // 11pt

function tr(text, opts = {}) {
  return new TextRun({ text, font: FONT, size: SIZE, ...opts });
}

function bullet(children, level = 0) {
  return new Paragraph({
    children: Array.isArray(children) ? children : [tr(children)],
    bullet: { level },
    spacing: { after: 40 },
  });
}

function sectionHeader(text) {
  // Bold + underline header (e.g., "Next Steps", "Key Takeaways")
  return new Paragraph({
    children: [tr(text, { bold: true, underline: { type: UnderlineType.SINGLE } })],
    spacing: { before: 240, after: 120 },
  });
}

function topicHeader(text) {
  // Bold + italic subheader for Full Notes topics
  return new Paragraph({
    children: [tr(text, { bold: true, italics: true })],
    spacing: { before: 160, after: 80 },
  });
}

function spacer() {
  return new Paragraph({ children: [], spacing: { after: 80 } });
}

// -- Build document --
const doc = new Document({
  sections: [{
    properties: {
      page: {
        margin: {
          top: convertInchesToTwip(1),
          right: convertInchesToTwip(1),
          bottom: convertInchesToTwip(1),
          left: convertInchesToTwip(1),
        },
      },
    },
    children: [
      // Title
      new Paragraph({
        children: [tr("Henkel WSI Demand Spaces & Drivers Notes 1.28", { bold: true })],
        spacing: { after: 80 },
      }),

      // Attendees
      new Paragraph({
        children: [tr("Seurat Team: Jill, Clara, Max, Nick", { italics: true })],
        spacing: { after: 40 },
      }),
      new Paragraph({
        children: [tr("Henkel Team: Carlos, Mark, Mindy", { italics: true })],
        spacing: { after: 120 },
      }),

      // --- Next Steps ---
      sectionHeader("Next Steps"),

      bullet([
        tr("Team to ", { bold: true }),
        tr("update demand space naming based on feedback"),
      ]),
      bullet([tr("Circulate revised deck ahead of Feb. 17 meeting")], 1),

      spacer(),

      bullet([
        tr("Henkel to ", { bold: true }),
        tr("regroup with Linda on current-state deliverables"),
      ]),

      // --- Key Takeaways ---
      sectionHeader("Key Takeaways"),

      bullet([
        tr("Henkel aligned that the "),
        tr("updated demand space names are directionally stronger", { bold: true }),
        tr(" and reflect prior feedback well"),
      ]),

      bullet([
        tr("Brand analysis reveals "),
        tr("Got2b has strongest positioning in Fix & Flourish", { bold: true }),
      ]),

      // --- Full Notes ---
      sectionHeader("Full Notes"),

      topicHeader("Demand Map Reactions"),

      bullet([tr('Carlos noted Elevated Expression "works really well"')]),
      bullet([tr("Carlos asked for clarity on Hair Health Haven vs. Healthy Habits")]),

      topicHeader("Brand Mapping"),

      bullet([tr('Carlos confirmed the center-of-gravity framing "really reinforces" the approach')]),
      bullet([tr("Mark asked about coverage across all demand spaces")]),
      bullet([tr('Mark noted this could generate "rich conversation" with the broader team')], 1),
    ],
  }],
});

Packer.toBuffer(doc).then((buffer) => {
  const filename = "Henkel WSI Demand Spaces & Drivers External 1.28.26.docx";
  fs.writeFileSync(filename, buffer);
  console.log(`Created ${filename}`);
});
```

---

## 2. Research Dossier

Used by: `product-research`, and similar long-form research documents.

**Key formatting**: US Letter, 1" margins, title page, heading hierarchy, competitor tables, blockquote-style customer quotes, numbered references.

```javascript
const docx = require("docx");
const fs = require("fs");

const { Document, Paragraph, TextRun, Packer, HeadingLevel,
        AlignmentType, Table, TableRow, TableCell,
        WidthType, BorderStyle, convertInchesToTwip } = docx;

const CONTENT_WIDTH = 9360; // US Letter (12240) minus 2x 1" margins (2x1440)

const doc = new Document({
  sections: [
    // --- Title Page ---
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: {
            top: convertInchesToTwip(1),
            right: convertInchesToTwip(1),
            bottom: convertInchesToTwip(1),
            left: convertInchesToTwip(1),
          },
        },
      },
      children: [
        new Paragraph({ spacing: { before: 4000 } }),
        new Paragraph({
          children: [new TextRun({ text: "Product Name", bold: true, size: 52, font: "Calibri" })],
          alignment: AlignmentType.CENTER,
        }),
        new Paragraph({
          children: [new TextRun({ text: "Deep Research Dossier", size: 32, font: "Calibri", color: "666666" })],
          alignment: AlignmentType.CENTER,
          spacing: { after: 400 },
        }),
        new Paragraph({
          children: [new TextRun({ text: "February 2026", size: 24, font: "Calibri", color: "999999" })],
          alignment: AlignmentType.CENTER,
        }),
      ],
    },
    // --- Body ---
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: {
            top: convertInchesToTwip(1),
            right: convertInchesToTwip(1),
            bottom: convertInchesToTwip(1),
            left: convertInchesToTwip(1),
          },
        },
      },
      children: [
        // H1
        new Paragraph({ text: "1. Executive Summary", heading: HeadingLevel.HEADING_1 }),
        new Paragraph({ text: "Summary content goes here.", spacing: { after: 200 } }),

        // H2
        new Paragraph({ text: "2. Competitor Teardown", heading: HeadingLevel.HEADING_1, spacing: { before: 300 } }),
        new Paragraph({ text: "2.1 Overview", heading: HeadingLevel.HEADING_2 }),

        // Competitor table
        new Table({
          rows: [
            new TableRow({
              children: ["Competitor", "Price", "Positioning", "Gap"].map((h) =>
                new TableCell({
                  children: [new Paragraph({
                    children: [new TextRun({ text: h, bold: true, color: "FFFFFF", font: "Calibri" })],
                  })],
                  width: { size: Math.floor(CONTENT_WIDTH / 4), type: WidthType.DXA },
                  shading: { fill: "4472C4" },
                })
              ),
            }),
            new TableRow({
              children: ["Brand A", "$29.99", "Premium quality", "No bundle option"].map((v) =>
                new TableCell({
                  children: [new Paragraph({ text: v })],
                  width: { size: Math.floor(CONTENT_WIDTH / 4), type: WidthType.DXA },
                })
              ),
            }),
          ],
          width: { size: 100, type: WidthType.PERCENTAGE },
        }),

        new Paragraph({ spacing: { after: 200 } }),

        // Blockquote-style customer quote
        new Paragraph({ text: "3. Voice of Customer", heading: HeadingLevel.HEADING_1, spacing: { before: 300 } }),
        new Paragraph({
          children: [new TextRun({
            text: '"I bought three of these as gifts and every single person loved it."',
            italics: true, color: "555555",
          })],
          indent: { left: convertInchesToTwip(0.5), right: convertInchesToTwip(0.5) },
          spacing: { after: 40 },
        }),
        new Paragraph({
          children: [new TextRun({ text: "— Amazon review, verified purchase", size: 18, color: "999999" })],
          indent: { left: convertInchesToTwip(0.5) },
          spacing: { after: 200 },
        }),

        // References
        new Paragraph({ text: "References", heading: HeadingLevel.HEADING_1, spacing: { before: 300 } }),
        new Paragraph({ text: "[1] https://example.com/source-1", spacing: { after: 40 } }),
        new Paragraph({ text: "[2] https://example.com/source-2", spacing: { after: 40 } }),
      ],
    },
  ],
});

Packer.toBuffer(doc).then((buffer) => {
  const filename = "Product Name — Deep Research Dossier.docx";
  fs.writeFileSync(filename, buffer);
  console.log(`Created ${filename}`);
});
```

---

## 3. Survey Document

Used by: `survey-document-builder`, and similar quantitative research survey workflows.

**Key formatting**: 3-column question tables, blue topic header bars, "NEW SCREEN" markers, programming instruction cells.

```javascript
const docx = require("docx");
const fs = require("fs");

const { Document, Paragraph, TextRun, Packer, Table, TableRow,
        TableCell, WidthType, BorderStyle, AlignmentType,
        convertInchesToTwip } = docx;

const PAGE_WIDTH = 12240;
const MARGIN = convertInchesToTwip(1);
const CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN;

// Column widths for 3-column survey layout
const COL_Q = 800;                              // Q# column
const COL_NOTES = 2400;                         // Notes column
const COL_QUESTION = CONTENT_WIDTH - COL_Q - COL_NOTES; // Question column (remainder)

function screenMarker() {
  return new Paragraph({
    children: [new TextRun({ text: "NEW SCREEN", bold: true, color: "FF0000", size: 20 })],
    alignment: AlignmentType.CENTER,
    spacing: { before: 200, after: 200 },
  });
}

function topicBar(text) {
  // Blue bar header spanning full width
  return new Table({
    rows: [
      new TableRow({
        children: [
          new TableCell({
            children: [new Paragraph({
              children: [new TextRun({ text, bold: true, color: "FFFFFF", size: 22 })],
              alignment: AlignmentType.CENTER,
            })],
            width: { size: 100, type: WidthType.PERCENTAGE },
            shading: { fill: "4472C4" },
            columnSpan: 3,
          }),
        ],
      }),
    ],
    width: { size: 100, type: WidthType.PERCENTAGE },
  });
}

function questionRow(qNum, questionChildren, notesText) {
  return new Table({
    rows: [
      new TableRow({
        children: [
          // Q# cell
          new TableCell({
            children: [new Paragraph({
              children: [new TextRun({ text: qNum, bold: true })],
              alignment: AlignmentType.CENTER,
            })],
            width: { size: COL_Q, type: WidthType.DXA },
            borders: { top: { style: BorderStyle.SINGLE, size: 1 }, bottom: { style: BorderStyle.SINGLE, size: 1 } },
          }),
          // Question cell
          new TableCell({
            children: questionChildren,
            width: { size: COL_QUESTION, type: WidthType.DXA },
            borders: { top: { style: BorderStyle.SINGLE, size: 1 }, bottom: { style: BorderStyle.SINGLE, size: 1 } },
          }),
          // Notes cell
          new TableCell({
            children: [new Paragraph({
              children: [new TextRun({ text: notesText, italics: true, size: 18 })],
            })],
            width: { size: COL_NOTES, type: WidthType.DXA },
            borders: { top: { style: BorderStyle.SINGLE, size: 1 }, bottom: { style: BorderStyle.SINGLE, size: 1 } },
          }),
        ],
      }),
    ],
    width: { size: 100, type: WidthType.PERCENTAGE },
  });
}

const doc = new Document({
  sections: [{
    properties: {
      page: {
        size: { width: PAGE_WIDTH, height: 15840 },
        margin: { top: MARGIN, right: MARGIN, bottom: MARGIN, left: MARGIN },
      },
    },
    children: [
      new Paragraph({
        children: [new TextRun({ text: "Brand Study Survey Document", bold: true, size: 28 })],
        alignment: AlignmentType.CENTER,
        spacing: { after: 200 },
      }),

      topicBar("SCREENER"),
      screenMarker(),

      questionRow("S1",
        [
          new Paragraph({ children: [new TextRun({ text: "What is your age?", bold: true })] }),
          new Paragraph({ children: [new TextRun({ text: "Please select one.", italics: true, size: 18 })] }),
          new Paragraph({ text: "○  Under 18  [TERMINATE]" }),
          new Paragraph({ text: "○  18-24" }),
          new Paragraph({ text: "○  25-34" }),
          new Paragraph({ text: "○  35-44" }),
          new Paragraph({ text: "○  45-54" }),
          new Paragraph({ text: "○  55+" }),
          new Paragraph({ children: [new TextRun({ text: "Do not randomize.", italics: true, size: 18 })] }),
        ],
        "Qualification: Must be 18+"
      ),

      screenMarker(),

      topicBar("MAIN SURVEY"),
      screenMarker(),

      questionRow("Q1",
        [
          new Paragraph({ children: [new TextRun({ text: "Which of the following brands have you purchased in the past 6 months?", bold: true })] }),
          new Paragraph({ children: [new TextRun({ text: "Please select all that apply.", italics: true, size: 18 })] }),
          new Paragraph({ text: "□  Brand A" }),
          new Paragraph({ text: "□  Brand B" }),
          new Paragraph({ text: "□  Brand C" }),
          new Paragraph({ text: "□  None of the above  [Anchor. Mutually Exclusive.]" }),
          new Paragraph({ children: [new TextRun({ text: "Randomize. Anchor last option.", italics: true, size: 18 })] }),
        ],
        "Brand awareness and purchase behavior"
      ),
    ],
  }],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync("Survey Document.docx", buffer);
  console.log("Created Survey Document.docx");
});
```

---

## Tips for All Patterns

1. **Column widths must sum to content width.** For US Letter with 1" margins: `12240 - 2*1440 = 9360` DXA.
2. **Font size is in half-points.** 11pt = `22`, 12pt = `24`, 14pt = `28`.
3. **Spacing is in DXA (twentieths of a point).** `40` ≈ tight, `120` ≈ normal, `240` ≈ generous.
4. **`Packer.toBuffer()` returns a Promise.** Always use `.then()` or `await`.
5. **Adapt, don't copy blindly.** These patterns are starting points — adjust fonts, spacing, and structure to match the calling skill's format requirements.
