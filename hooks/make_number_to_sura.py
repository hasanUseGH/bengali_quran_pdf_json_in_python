import json

# File path to the filtered JSON file
file_path = r"C:\\Users\\Hasan\\Desktop\\py_quran\\files\\filtered_sura_data.json"

# Load the JSON data from the file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Convert "number" key to "sura"
for sura in data:
    sura["sura"] = sura.pop("number")

# Save the updated data back to a JSON file
output_path = r"C:\\Users\\Hasan\\Desktop\\py_quran\\files\\updated_sura_data.json"
with open(output_path, 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)

print("Updated JSON file has been saved successfully.")
