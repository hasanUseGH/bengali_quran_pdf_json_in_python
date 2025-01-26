import os
from PyPDF2 import PdfMerger

# Folder where the PDFs are stored
pdf_folder = r"C:\Users\Hasan\Desktop\py_quran\bn_pdf"

# List to keep track of file paths to merge
pdf_files = []

# Add PDFs to the list in the order required
for sura_number in range(1, 115):
    pdf_path = os.path.join(pdf_folder, f"sura_{sura_number}.pdf")
    pdf_files.append(pdf_path)

# Create a PdfMerger instance
merger = PdfMerger()

# Merge the PDFs in groups of 9
for i in range(0, len(pdf_files), 9):
    # Select the PDFs to merge (from current index to the next 9 PDFs)
    files_to_merge = pdf_files[i:i+9]
    for pdf_file in files_to_merge:
        merger.append(pdf_file)

# Output the merged PDF to a new file
output_pdf_path = r"C:\Users\Hasan\Desktop\py_quran\bn_pdf\merged_sura.pdf"
merger.write(output_pdf_path)

# Close the merger
merger.close()

print(f"PDF merged successfully into: {output_pdf_path}")
