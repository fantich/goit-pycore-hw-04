import os
from pathlib import Path

def get_cats_info(path):
    cats_info = []
    
    if not os.path.exists(path):
        print(f"Error: File '{path}' not found.")
        return cats_info
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  
                
                parts = line.split(",")
                if len(parts) != 3:
                    print(f"Warning: Skipping invalid line '{line}'")
                    continue
                
                cat_id, name, age = parts
                cats_info.append({"id": cat_id, "name": name, "age": age})
    
    except Exception as e:
        print(f"Error while reading the file: {e}")
    
    return cats_info

cats_info = get_cats_info("cats_info.txt")
print(cats_info)