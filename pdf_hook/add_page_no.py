import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Function to add page numbers to each page of the PDF
def add_page_numbers(input_pdf_path, output_pdf_path):
    # Create a PdfReader and PdfWriter
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Create a temporary PDF to hold the page numbers
    temp_pdf_path = "temp_page_numbers.pdf"
    c = canvas.Canvas(temp_pdf_path, pagesize=letter)

    # Loop through each page in the input PDF and add page number
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]

        # Create a new page in the temporary PDF for page number
        c.setFont("Helvetica", 10)
        c.drawString(270, 20, f"Page {page_num + 1}")  # Draw page number at bottom center
        c.showPage()

    # Save the temporary PDF with page numbers
    c.save()

    # Read the temporary PDF with page numbers
    temp_reader = PdfReader(temp_pdf_path)
    
    # Merge the page numbers with the original PDF pages
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        overlay_page = temp_reader.pages[i]

        # Merge the page number onto the original page
        page.merge_page(overlay_page)
        
        # Add the page to the writer
        writer.add_page(page)

    # Write the output PDF
    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)

    # Clean up the temporary PDF file
    os.remove(temp_pdf_path)

    print(f"Page numbers added successfully. Output saved at {output_pdf_path}")

# Path to the merged PDF
input_pdf_path = r"C:\Users\Hasan\Desktop\py_quran\bn_pdf\merged_sura.pdf"
output_pdf_path = r"C:\Users\Hasan\Desktop\py_quran\bn_pdf\merged_with_page_numbers.pdf"

# Call the function to add page numbers
add_page_numbers(input_pdf_path, output_pdf_path)
