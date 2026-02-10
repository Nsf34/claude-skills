#!/usr/bin/env python3
"""Generate a 1-page PDF guide for using the Seurat Meeting Notes skill."""

from fpdf import FPDF

LEFT = 16
RIGHT = 16

class SeuratPDF(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', 'Letter')
        self.set_auto_page_break(auto=False)

    def section_header(self, text):
        self.set_font("Helvetica", "BU", 11)
        self.cell(0, 5.5, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def bullet(self, text, indent=0):
        x0 = LEFT + indent
        self.set_x(x0)
        self.set_font("Helvetica", "", 9.5)
        self.cell(4, 4.5, "-")
        w = self.w - self.r_margin - self.get_x()
        self.multi_cell(w, 4.5, text)

    def bold_bullet(self, bold_part, rest, indent=0):
        x0 = LEFT + indent
        self.set_x(x0)
        self.set_font("Helvetica", "", 9.5)
        self.cell(4, 4.5, "-")
        self.set_font("Helvetica", "B", 9.5)
        self.cell(self.get_string_width(bold_part), 4.5, bold_part)
        self.set_font("Helvetica", "", 9.5)
        w = self.w - self.r_margin - self.get_x()
        if w < 10:
            self.ln(4.5)
            self.set_x(x0 + 4)
            w = self.w - self.r_margin - self.get_x()
        self.multi_cell(w, 4.5, rest)

    def body(self, text):
        self.set_font("Helvetica", "", 9.5)
        self.multi_cell(0, 4.5, text)

    def label(self, text):
        self.set_font("Helvetica", "B", 10)
        self.cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.5)

    def code_block(self, lines):
        self.set_fill_color(240, 240, 240)
        h = len(lines) * 4.2 + 3
        self.rect(LEFT + 2, self.get_y(), self.w - LEFT - RIGHT - 4, h, style="F")
        self.set_font("Courier", "", 8.5)
        self.ln(1.5)
        for line in lines:
            self.set_x(LEFT + 5)
            self.cell(0, 4.2, line, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def rule(self):
        self.set_draw_color(170, 170, 170)
        self.line(LEFT, self.get_y(), self.w - RIGHT, self.get_y())
        self.ln(2.5)


pdf = SeuratPDF()
pdf.set_margins(LEFT, 13, RIGHT)
pdf.add_page()

# ── Title ──
pdf.set_font("Helvetica", "B", 14)
pdf.cell(0, 7, "Seurat Meeting Notes Skill", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 10)
pdf.cell(0, 5, "Quick-Start Guide for Windows / Claude Code", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(1.5)
pdf.rule()

# ── What This Skill Does ──
pdf.section_header("What This Skill Does")
pdf.body(
    "Transforms raw meeting transcripts, deck content, and personal notes into polished, "
    "client-ready meeting notes (.docx). Output includes Next Steps, Key Takeaways, and "
    "Full Notes sections following Seurat Group formatting and content-quality standards."
)
pdf.ln(2)

# ── Setup Options ──
pdf.section_header("Setup Options (Windows)")

pdf.label("Option A: Claude Code on the Web  (Recommended)")
pdf.bullet("Go to claude.ai/code and open a session pointed at the claude-skills repository.")
pdf.bullet("The skill triggers automatically when you ask to process meeting notes.")
pdf.bullet("For a persistent slash command, create .claude/commands/meeting-notes.md (see below).")
pdf.ln(1.5)

pdf.label("Option B: Claude Code Desktop App")
pdf.bullet("Install Node.js, then run:  npm install -g @anthropic-ai/claude-code")
pdf.bullet("Clone the repo locally and open a terminal in your project folder, then run: claude")
pdf.bullet("Invoke with /meeting-notes after setting up the slash command below.")
pdf.ln(1.5)

pdf.label("Option C: Claude Chat Projects  (Non-Technical Teammates)")
pdf.bullet("Create a Project at claude.ai. Paste SKILL.md and all three reference files into Knowledge.")
pdf.bullet("Every conversation in that Project will follow the skill automatically.")
pdf.bullet("Note: Chat cannot write .docx files -- copy the formatted output into Word manually.")
pdf.ln(2)

# ── Slash Command Setup ──
pdf.section_header("Slash Command Setup  (Options A & B)")
pdf.body("Create the file  .claude/commands/meeting-notes.md  in your project root with this content:")
pdf.ln(1)
pdf.code_block([
    "Process the attached meeting materials into Seurat-format notes.",
    "Follow the instructions in seurat-meeting-notes/SKILL.md and its",
    "references/ folder. Output a .docx file.",
])
pdf.body("Then invoke it during any session by typing:  /meeting-notes")
pdf.ln(2)

# ── How to Run ──
pdf.section_header("How to Run")
pdf.bold_bullet("1. Start a session  ", "-- Open Claude Code (web or app) in a folder containing the skill repo.")
pdf.bold_bullet("2. Provide materials  ", "-- Paste or attach: (a) call transcript, (b) deck (if any), (c) your notes.")
pdf.bold_bullet("3. Invoke the skill  ", "-- Type /meeting-notes or: \"Turn these into Seurat meeting notes.\"")
pdf.bold_bullet("4. Confirm context  ", "-- Claude asks for meeting title, date, attendees, client. Fill in any gaps.")
pdf.bold_bullet("5. Receive output  ", "-- A .docx is generated with Next Steps, Key Takeaways, and Full Notes.")
pdf.ln(2)

# ── Tips ──
pdf.section_header("Tips")
pdf.bullet("Provide the deck alongside the transcript so Claude knows what NOT to repeat in the notes.")
pdf.bullet("If you have personal highlights, include them -- they help prioritize what mattered most.")
pdf.bullet("Review Key Takeaways first; they are the most judgment-intensive section.")
pdf.ln(3)

# ── Footer ──
pdf.rule()
pdf.set_font("Helvetica", "I", 8)
pdf.cell(0, 4, "Seurat Group  |  Meeting Notes Skill Guide  |  February 2026", align="C")

output_path = "/home/user/claude-skills/Seurat Meeting Notes Skill - Quick Start Guide.pdf"
pdf.output(output_path)
print(f"PDF saved to: {output_path}")
