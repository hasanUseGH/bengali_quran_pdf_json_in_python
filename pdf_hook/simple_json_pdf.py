from fpdf import FPDF
import json

# File paths
json_file_path = r"C:\Users\Hasan\Desktop\py_quran\files\sura_jsons\sura_1.json"
output_pdf_path = r"C:\Users\Hasan\Desktop\py_quran\files\sura_1_output.pdf"
font_path = r"C:\Users\Hasan\Desktop\Downloads\Kalpurush\Kalpurush.ttf"  # Path to the Kalpurush font file

# Load JSON data
with open(json_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract sura name for heading
sura_name = data[0]["englishName"]
translation = data[0]["englishNameTranslation"]


# Create PDF class
class PDF(FPDF):
    def header(self):
        # Add custom font (Kalpurush) for regular style
        self.add_font("Kalpurush", "", font_path, uni=True)
        self.set_font("Kalpurush", "", 16)

        # Title
        self.cell(0, 10, f"{sura_name} ({translation})", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        # Use regular font style in the footer
        self.set_font("Kalpurush", "", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")


# Create PDF object
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set font for the content (Kalpurush)
pdf.set_font("Kalpurush", "", 14)

# Add each Ayah to the PDF
for ayah in data:
    text = ayah["text"]
    aya_number = ayah["aya"]

    # Add the text of the Ayah
    pdf.multi_cell(0, 10, f"Aya {aya_number}: {text}", align="L")
    pdf.ln(2)

# Save the output PDF
pdf.output(output_pdf_path)

print("PDF has been generated successfully.")
