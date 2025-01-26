import json
import os

# File path to the ayats JSON file
file_path = r"C:\\Users\\Hasan\\Desktop\\py_quran\\files\\ayats_bn.json"

# Output directory for individual sura JSON files
output_dir = r"C:\\Users\\Hasan\\Desktop\\py_quran\\files\\sura_jsons"
os.makedirs(output_dir, exist_ok=True)

# Load the JSON data from the file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Group data by sura number
sura_dict = {}
for item in data:
    sura_number = item["sura"]
    if sura_number not in sura_dict:
        sura_dict[sura_number] = []
    sura_dict[sura_number].append(item)

# Save each sura data into separate JSON files
for sura_number, ayahs in sura_dict.items():
    output_file_path = os.path.join(output_dir, f"sura_{sura_number}.json")
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        json.dump(ayahs, outfile, ensure_ascii=False, indent=4)

print("All sura JSON files have been saved successfully.")
