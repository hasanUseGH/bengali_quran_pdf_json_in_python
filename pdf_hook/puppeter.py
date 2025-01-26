import json
import asyncio
from pyppeteer import launch

# Read the JSON data from the file
json_path = r"C:\Users\Hasan\Desktop\py_quran\files\sura_jsons\sura_2.json"
with open(json_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Generate the HTML content for the PDF
html_content = """
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 60px;
            padding: 2;
             margin-bottom: 100px;
              margin-top: 60;
        }
        h2 {
            color: #000000;
            text-align: center;
            font-size: 30px;
            margin-top: 10;
        }
        p {
            margin: 0;
            padding: 0;
            font-size: 13px;
            color: #000000;
        }
        .sura {
            margin-bottom: 30px;
        }
        .verse-group {
            margin-bottom: 20px;
        }
        .margin-bottom-50 {
            margin-bottom: 50px;
        }
    </style>
</head>
<body>
"""

# Initialize a variable to keep track of the number of verses processed and to group verses
verse_count = 0
sura_name_added = False
verse_group = []

# Create the content for each verse
for item in data:
    sura = item.get("englishName", "")
    text = item.get("text", "")
    aya = item.get("aya", "")

    # Add the sura name only once at the top
    if not sura_name_added:
        html_content += f"""
        <h2>{sura}</h2>
        """
        sura_name_added = True

    # Add the verse to the current group
    verse_group.append(f"{text} ({aya})")

    # After every 10 verses, wrap them in a paragraph and add a margin
    verse_count += 1
    if verse_count % 10 == 0:
        html_content += f"""
        <div class="verse-group">
            <p>{" ".join(verse_group)}</p>
        </div>
        <div class="margin-bottom-50"></div>
        """
        verse_group = []  # Reset the verse group

# If there are remaining verses that are less than 10, add them
if verse_group:
    html_content += f"""
    <div class="verse-group">
        <p>{" ".join(verse_group)}</p>
    </div>
    """

# Close the HTML content
html_content += "</body></html>"


from playwright.sync_api import sync_playwright


def generate_pdf():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Set content for the page
        page.set_content(html_content)

        # Define page options with margins and page numbers
        page.pdf(
            path="pdf/sura_2.pdf",
            format="A4",
            margin={"top": "40px", "bottom": "40px", "left": "20px", "right": "20px"},

        )

        browser.close()


generate_pdf()
print("PDF generated successfully!")
