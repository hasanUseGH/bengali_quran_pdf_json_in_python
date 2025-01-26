from fpdf import FPDF
from pdf2image import convert_from_path
import json

# File paths
json_file_path = r"C:\\Users\\Hasan\\Desktop\\py_quran\\files\\sura_jsons\\sura_1.json"
background_pdf_path = r"C:\Users\Hasan\Desktop\py_quran\files\bg_pdf-1.jpg"
output_pdf_path = r"C:\\Users\\Hasan\\Desktop\\py_quran\\files\\sura_1_output.pdf"

# Load JSON data
with open(json_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract sura name for heading
sura_name = data[0]["englishName"]
translation = data[0]["englishNameTranslation"]

# Convert background PDF to image (assuming it's the first page)
images = convert_from_path(background_pdf_path, first_page=1, last_page=1)
background_image_path = "background_page.jpg"
images[0].save(background_image_path, "JPEG")


# Create PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", style="B", size=20)
        self.cell(0, 10, sura_name, ln=True, align="C")
        self.set_font("Arial", size=14)
        self.cell(0, 10, f"({translation})", ln=True, align="C")
        self.ln(10)


pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set background image
pdf.image(background_image_path, x=0, y=0, w=210, h=297)

# Add sura text content
pdf.set_font("Arial", size=14)
for ayah in data:
    pdf.multi_cell(0, 10, ayah["text"], align="L")
    pdf.ln(2)
    pdf.set_font("Arial", size=12, style="B")
    pdf.cell(0, 10, f'({ayah["aya"]})', align="R")
    pdf.ln(5)
    pdf.set_font("Arial", size=14)

# Save the output PDF
pdf.output(output_pdf_path)

print("PDF has been generated successfully.")
