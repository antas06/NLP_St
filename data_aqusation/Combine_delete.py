import json
import os

files = [
    r"NLP_St\data\Movie_Ratings\movie_review_all.json",
    r"NLP_St\data\Movie_Ratings\movie_review_all2.json",
    r"NLP_St\data\Movie_Ratings\movie_review_all4.json",
    r"NLP_St\data\Movie_Ratings\movie_review_all6.json",
    r"NLP_St\data\Movie_Ratings\movie_review_all8.json"
]

all_data = []  # master list


for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        all_data.extend(data) # merge into one list

output_path = r"NLP_St\data\Movie_Ratings\movie_reviews.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=4, ensure_ascii=False)

print("Merged all 5 files")

for file_path in files:
    try:
        os.remove(file_path)
        print(f"Deleted {file_path}")
    except OSError as e:
        print(f"Error deleting {file_path}: {e}")

print("deleted older files")