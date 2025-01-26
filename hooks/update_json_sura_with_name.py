import json
import os

# Path to the folder containing sura JSON files
sura_json_folder = r"C:\\Users\\Hasan\\Desktop\\py_quran\\files\\sura_jsons"

# Path to the sura metadata file
sura_data_file = r"C:\\Users\\Hasan\\Desktop\\py_quran\\files\\updated_sura_data.json"

# Load sura metadata
with open(sura_data_file, 'r', encoding='utf-8') as file:
    sura_metadata = json.load(file)

# Convert metadata to a dictionary for easy lookup
sura_info = {str(sura["sura"]): {
                "englishName": sura["englishName"],
                "englishNameTranslation": sura["englishNameTranslation"]
            } for sura in sura_metadata}

# Process each sura JSON file in the folder
for filename in os.listdir(sura_json_folder):
    if filename.startswith("sura_") and filename.endswith(".json"):
        sura_number = filename.split("_")[1].split(".")[0]  # Extract sura number
        
        if sura_number in sura_info:
            file_path = os.path.join(sura_json_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                sura_data = json.load(file)

            # Add sura name and translation to each ayah
            for ayah in sura_data:
                ayah.update(sura_info[sura_number])

            # Rewrite the updated JSON file
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(sura_data, file, ensure_ascii=False, indent=4)

print("All sura JSON files have been updated with sura names successfully.")