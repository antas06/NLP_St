# Data Acquisition

This folder contains scripts for collecting and managing movie-related data from the TMDB (The Movie Database) API. The data collected here is used for further analysis and NLP-related tasks.

## Files

### 1. Movie_genre_api.py
Fetches movie genres and their corresponding IDs from the TMDB API and stores them in a JSON file.

**Output:**
- `genres_id.json`

---

### 2. Movie_rating_api.py
Fetches top-rated movie data from TMDB across multiple pages and saves the results in a JSON file.

**Output (example):**
- `movie_review_all8.json`

---

### 3. Combine_delete.py
Merges multiple movie rating JSON files into a single dataset and deletes the intermediate files.

**Final Output:**
- `movie_reviews.json`

---

## Usage Flow
1. Run `Movie_genre_api.py` to fetch genre mappings  
2. Run `Movie_rating_api.py` to collect movie data  
3. Run `Combine_delete.py` to merge all files into one dataset  

## Notes
- API keys/tokens should ideally be managed securely.
- This folder is only responsible for data acquisition.
- File paths may need adjustment based on project structure.