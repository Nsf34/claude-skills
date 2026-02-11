---
name: docx-generator
description: "Generate professional .docx Word documents using the docx npm package (JavaScript). Use this skill whenever you need to create a Word document, produce .docx output, format a document with headings/bullets/tables, or when another skill says 'use the docx skill'. Triggers on: creating Word docs, generating .docx files, formatted document output, meeting notes docs, survey docs, research dossiers, or any task requiring structured Word document generation."
---

# Docx Generator

Generate professional `.docx` Word documents programmatically using the `docx` npm package (v9.x) in Node.js.

## When to Use

Use this skill whenever the output needs to be a `.docx` file. Other skills reference this one for their document generation step — when they say "use the docx skill," follow the approach below.

## Core Approach

Write a self-contained Node.js script that:
1. Imports from `docx` (Document, Paragraph, TextRun, Table, etc.)
2. Builds the document structure declaratively
3. Uses `Packer.toBuffer()` to serialize
4. Writes the buffer to a `.docx` file with `fs.writeFileSync()`

The script is generated fresh each time, tailored to the specific document content. There is no fixed template — the structure adapts to whatever the calling skill or user needs.

## Quick Start Pattern

Every docx generation script follows this skeleton:

```javascript
const docx = require("docx");
const fs = require("fs");

const { Document, Paragraph, TextRun, Packer, HeadingLevel,
        AlignmentType, Table, TableRow, TableCell,
        WidthType, BorderStyle, convertInchesToTwip,
        UnderlineType, TabStopType, TabStopPosition } = docx;

const doc = new Document({
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },      // US Letter in DXA
        margin: {
          top: convertInchesToTwip(1),
          right: convertInchesToTwip(1),
          bottom: convertInchesToTwip(1),
          left: convertInchesToTwip(1),
        },
      },
    },
    children: [
      // Document content goes here — Paragraphs, Tables, etc.
    ],
  }],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync("output.docx", buffer);
  console.log("Created output.docx");
});
```

## Key Building Blocks

### Text Formatting

```javascript
// Bold text
new TextRun({ text: "Bold text", bold: true })

// Italic text
new TextRun({ text: "Italic text", italics: true })

// Bold + Italic
new TextRun({ text: "Bold italic", bold: true, italics: true })

// Underline
new TextRun({ text: "Underlined", underline: { type: UnderlineType.SINGLE } })

// Bold + Underline (for section headers like "Next Steps")
new TextRun({ text: "Next Steps", bold: true, underline: { type: UnderlineType.SINGLE } })

// Custom font and size (size is in half-points: 22 = 11pt)
new TextRun({ text: "Custom", font: "Franklin Gothic Book", size: 22 })

// Mixed formatting in one paragraph
new Paragraph({
  children: [
    new TextRun({ text: "Team to ", bold: true }),
    new TextRun({ text: "update the positioning document" }),
  ],
})
```

### Paragraphs and Headings

```javascript
// Simple paragraph
new Paragraph({ text: "Plain text paragraph" })

// Heading levels
new Paragraph({ text: "Title", heading: HeadingLevel.HEADING_1 })
new Paragraph({ text: "Section", heading: HeadingLevel.HEADING_2 })
new Paragraph({ text: "Subsection", heading: HeadingLevel.HEADING_3 })

// Paragraph with spacing control (values in DXA / twentieths of a point)
new Paragraph({
  children: [new TextRun({ text: "Tight spacing" })],
  spacing: { after: 40 },  // Tight: 40. Normal: 200. Between sections: 80-120
})

// Alignment
new Paragraph({
  text: "Centered text",
  alignment: AlignmentType.CENTER,
})
```

### Bullet Lists

```javascript
// Top-level bullet
new Paragraph({
  children: [new TextRun({ text: "Main point" })],
  bullet: { level: 0 },
  spacing: { after: 40 },
})

// Sub-bullet (indented)
new Paragraph({
  children: [new TextRun({ text: "Supporting detail" })],
  bullet: { level: 1 },
  spacing: { after: 40 },
})

// Bullet with mixed formatting
new Paragraph({
  children: [
    new TextRun({ text: "Client noted ", font: "Franklin Gothic Book", size: 22 }),
    new TextRun({ text: "strong alignment", bold: true, font: "Franklin Gothic Book", size: 22 }),
    new TextRun({ text: " on the updated positioning", font: "Franklin Gothic Book", size: 22 }),
  ],
  bullet: { level: 0 },
  spacing: { after: 40 },
})
```

### Tables

```javascript
const table = new Table({
  rows: [
    // Header row
    new TableRow({
      children: [
        new TableCell({
          children: [new Paragraph({ text: "Name", alignment: AlignmentType.CENTER })],
          width: { size: 3000, type: WidthType.DXA },
          shading: { fill: "4472C4" },  // Blue header background
        }),
        new TableCell({
          children: [new Paragraph({ text: "Value" })],
          width: { size: 7240, type: WidthType.DXA },
        }),
      ],
    }),
    // Data row
    new TableRow({
      children: [
        new TableCell({
          children: [new Paragraph({ text: "Item 1" })],
          width: { size: 3000, type: WidthType.DXA },
        }),
        new TableCell({
          children: [new Paragraph({ text: "Description" })],
          width: { size: 7240, type: WidthType.DXA },
        }),
      ],
    }),
  ],
  width: { size: 100, type: WidthType.PERCENTAGE },
});
```

### Page Breaks

```javascript
new Paragraph({ children: [], pageBreakBefore: true })
```

## Applying a Consistent Font

When a skill requires a specific font throughout (e.g., Franklin Gothic Book 11pt), set it on every `TextRun` and use a helper:

```javascript
const FONT = "Franklin Gothic Book";
const SIZE = 22; // 11pt in half-points

function tr(text, opts = {}) {
  return new TextRun({ text, font: FONT, size: SIZE, ...opts });
}

// Usage
new Paragraph({
  children: [
    tr("Team to ", { bold: true }),
    tr("circulate updated deck"),
  ],
  bullet: { level: 0 },
  spacing: { after: 40 },
})
```

## Spacing Guidelines

Spacing values are in DXA (twentieths of a point):

| Context | `spacing.after` | Notes |
|---------|-----------------|-------|
| Tight bullets | `40` | Standard for meeting notes, dense lists |
| Between bullet groups | `80` | Visual break between topics |
| Normal paragraphs | `120`-`200` | Standard body text |
| Section headers | `120` | Space after a header before content |
| Before section headers | `200`-`240` | Space above a new section |

Avoid `spacing: { after: 200 }` on individual bullets — it creates excessive whitespace.

## Common Document Patterns

Read `references/document-patterns.md` for complete, copy-paste-ready patterns for:
- Meeting notes documents (title, attendees, sections with bullets)
- Research dossiers (title page, ToC, heading hierarchy, tables, blockquotes)
- Survey documents (3-column tables, screen markers, programming notes)

## Execution

After writing the script, run it:

```bash
node generate-doc.js
```

The `docx` package is already installed in this project (`npm:docx@9.5.1`). No additional installation needed.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Font doesn't render | Font must be installed on the machine opening the doc. The .docx references it by name but doesn't embed it. This is normal — Word will substitute a fallback. |
| Bullets don't appear | Make sure you use `bullet: { level: 0 }` on the Paragraph, not a manual dash/hyphen. |
| Table columns misaligned | Column widths must sum to the content width (page width minus margins). For US Letter with 1" margins: `12240 - 2*1440 = 9360` DXA total. |
| Huge gaps between bullets | Check `spacing.after` values. Use `40` for tight bullets, never `200`+. |
| Script crashes on `Packer` | Ensure you're using `Packer.toBuffer(doc).then(...)` — it returns a Promise. |
