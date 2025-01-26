from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter

# File paths
json_path = r"C:\Users\Hasan\Desktop\py_quran\files\sura_jsons\sura_1.json"
bg_pdf_path = r"C:\Users\Hasan\Desktop\py_quran\files\bg_pdf.pdf"
output_pdf_path = r"C:\Users\Hasan\Desktop\py_quran\files\output_sura_1.pdf"

# Load JSON data
import json

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract sura details
sura_name = data[0]["englishName"]  # Use the first entry to get sura name


# Create the PDF
class QuranPDF(FPDF):
    def header(self):
        self.set_font("Times", "B", 16)
        self.cell(0, 10, sura_name, ln=True, align="C")
        self.ln(10)


pdf = QuranPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set fonts for Quranic text and ayah numbers
pdf.set_font("Times", size=12)

# Add ayah text
for entry in data:
    text = entry["text"]
    aya_number = entry["aya"]
    pdf.multi_cell(0, 10, text)
    pdf.ln(5)
    pdf.set_font("Times", "B", 10)
    pdf.cell(0, 10, f"({aya_number})", ln=True, align="R")
    pdf.set_font("Times", size=12)

# Save the generated content as a temporary PDF
temp_pdf_path = r"C:\Users\Hasan\Desktop\py_quran\files\temp_output.pdf"
pdf.output(temp_pdf_path)

# Apply background PDF
background = PdfReader(bg_pdf_path)
temp_pdf = PdfReader(temp_pdf_path)
writer = PdfWriter()

for page in temp_pdf.pages:
    bg_page = background.pages[0]
    bg_page.merge_page(page)
    writer.add_page(bg_page)

with open(output_pdf_path, "wb") as f:
    writer.write(f)

print(f"PDF generated successfully at {output_pdf_path}")
