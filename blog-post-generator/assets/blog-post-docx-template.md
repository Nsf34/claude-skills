# Blog Post .docx Formatting Specification

Use this spec when the user requests a Word document output in addition to the default markdown. The .docx should match the dossier's typography conventions (Arial, US Letter) but adapt the layout for blog-post readability.

---

## Page Setup

- **Paper size**: US Letter (8.5" x 11")
- **Margins**: 1" all sides
- **Content width**: 6.5" (9,360 DXA)

## Typography

### Title (H1)
- Font: Arial, 24pt, bold
- Alignment: Left
- Color: #1a1a1a (near-black)
- Spacing: 24pt after

### Section Headings (H2)
- Font: Arial, 18pt, bold
- Color: #1a1a1a
- Spacing: 18pt before, 8pt after
- Border: 1pt bottom border, #e0e0e0 (light gray), full width

### Subsection Headings (H3)
- Font: Arial, 14pt, bold
- Color: #333333
- Spacing: 14pt before, 6pt after

### Sub-subsection Headings (H4)
- Font: Arial, 12pt, bold
- Color: #333333
- Spacing: 10pt before, 4pt after

### Body Text
- Font: Arial, 11pt
- Color: #333333
- Line spacing: 1.4 (140%)
- Paragraph spacing: 8pt after
- First line indent: None

### Bold Text
- Same as body but bold weight
- Used for key phrases within paragraphs (sparingly)

---

## Special Elements

### Customer Quote Blockquotes
- Left indent: 0.5"
- Right indent: 0.5"
- Font: Arial, 11pt, italic
- Color: #555555
- Left border: 3pt solid, brand color or #3b82f6 (blue)
- Background: #f8f9fa (very light gray)
- Padding: 8pt all sides
- Attribution line: Arial, 10pt, regular, color #777777, preceded by em-dash

### Comparison Tables
- Full content width (9,360 DXA)
- Header row: Bold text, background #f1f5f9 (light blue-gray)
- Body rows: Alternating white / #fafafa
- Cell padding: 6pt
- Borders: 1pt #e0e0e0
- Font: Arial, 10pt (slightly smaller for table density)

### Bulleted Lists
- Font: Arial, 11pt
- Indent: 0.25" per level
- Bullet character: Standard round bullet
- Spacing: 4pt between items

### FAQ Question Headings
- Use H3 formatting
- Prefix with the question in customer voice (e.g., "Is it too messy?")

---

## Document Header

- **Title**: [Blog Post Title]
- **Subtitle**: Arial, 12pt, color #666666 — "[Post Type] | Generated from [Product Name] Research Dossier"
- **Date**: Arial, 10pt, color #999999

## Document Footer

- Font: Arial, 9pt, color #999999
- Content: "Generated from [Product Name] — Deep Research Dossier | [Date]"
- Alignment: Center

---

## Image Placeholders (in .docx)

Since the skill generates text-only output, image placeholders appear as styled callout boxes:

- Border: 2pt dashed #cccccc
- Background: #f5f5f5
- Content: "[IMAGE: Alt text description]" in Arial 10pt italic, color #999999
- Caption below: Arial 10pt, color #666666

---

## Generation Notes

Use the `docx-js` library or equivalent approach for programmatic .docx generation. The markdown file is the primary output — the .docx is a convenience format for users who need to share with collaborators or prefer Word for review.

When generating the .docx:
1. Parse the completed markdown blog post
2. Apply the formatting rules above to each element type
3. Preserve the heading hierarchy exactly as in the markdown
4. Convert markdown blockquotes to the styled blockquote format
5. Convert markdown tables to the styled table format
6. Add header and footer
7. Save to the same output folder as the markdown file
