import json

# File path to the JSON file
file_path = r"C:\\Users\\Hasan\\Desktop\\py_quran\\files\\sura_data.json"

# Load the JSON data from the file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract only the required fields
filtered_data = {
    "data": [
        {
            "number": sura["number"],
            "englishName": sura["englishName"],
            "englishNameTranslation": sura["englishNameTranslation"]
        }
        for sura in data["data"]
    ]
}

# Save the filtered data back to a JSON file
output_path = r"C:\\Users\\Hasan\\Desktop\\py_quran\\files\\filtered_sura_data.json"
with open(output_path, 'w', encoding='utf-8') as outfile:
    json.dump(filtered_data, outfile, ensure_ascii=False, indent=4)

print("Filtered JSON file has been saved successfully.")
