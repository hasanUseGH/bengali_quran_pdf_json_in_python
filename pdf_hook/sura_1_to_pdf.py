from fpdf import FPDF
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


# Create PDF class
class PDF(FPDF):
    def header(self):
        # Add regular and bold DejaVu font
        self.add_font(
            "DejaVu",
            "",
            r"C:\Users\Hasan\Desktop\py_quran\files\DejaVuSans.ttf",
            uni=True,
        )
        self.add_font(
            "DejaVu",
            "B",
            r"C:\Users\Hasan\Desktop\py_quran\files\DejaVuSans-Bold.ttf",
            uni=True,
        )

        # Set font to DejaVu (Bold for the header)
        self.set_font("DejaVu", style="B", size=20)
        self.cell(0, 10, sura_name, ln=True, align="C")
        self.set_font("DejaVu", size=14)
        self.cell(0, 10, f"({translation})", ln=True, align="C")
        self.ln(10)


pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set background image
pdf.image(background_pdf_path, x=0, y=0, w=210, h=297)

pdf.set_font("DejaVu", size=14)
for ayah in data:
    pdf.multi_cell(0, 10, ayah["text"], align="L")
    pdf.ln(2)
    pdf.set_font("DejaVu", size=12, style="B")
    pdf.cell(0, 10, f'({ayah["aya"]})', align="R")
    pdf.ln(5)
    pdf.set_font("DejaVu", size=14)

# Save the output PDF
pdf.output(output_pdf_path)

print("PDF has been generated successfully.")
