"""Generate PDF versions of Figure application materials."""
from pathlib import Path
from fpdf import FPDF

BASE = Path(__file__).parent

class ResumePDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def txt_to_pdf(src: Path, dst: Path, title: str = ""):
    pdf = ResumePDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Helvetica", size=10)
    text = src.read_text(encoding="utf-8")
    for line in text.splitlines():
        line = line.replace("\t", "    ")
        if not line.strip():
            pdf.ln(3)
            continue
        # fpdf2 core fonts are latin-1; replace common unicode chars
        line = (
            line.replace("—", "-")
            .replace("–", "-")
            .replace(""", '"')
            .replace(""", '"')
            .replace("'", "'")
            .replace("'", "'")
            .replace("→", "->")
            .replace("·", "-")
        )
        try:
            pdf.multi_cell(0, 5, line)
        except Exception:
            pdf.multi_cell(0, 5, line.encode("latin-1", "replace").decode("latin-1"))
    pdf.output(str(dst))
    print(f"Wrote {dst}")

def main():
    for role_dir in sorted(BASE.iterdir()):
        if not role_dir.is_dir() or role_dir.name.startswith("_"):
            continue
        for name in ("resume.txt", "cover-letter.txt"):
            src = role_dir / name
            if src.exists():
                txt_to_pdf(src, role_dir / name.replace(".txt", ".pdf"))

if __name__ == "__main__":
    main()
