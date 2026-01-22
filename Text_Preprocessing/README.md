# Text Processing

This folder contains scripts for cleaning and preprocessing movie review text data.  
The processed output is used for NLP tasks such as modeling, analysis, or feature extraction.

## Files

### 1. movie_review_processing.py
Prepares the raw movie dataset for text preprocessing.

**What it does:**
- Loads the complete movie dataset
- Selects relevant columns (`genre_ids`, `overview`, `title`)
- Loads genre ID mappings
- Exports the filtered data to a CSV file

**Output:**
- `df_use_csv.csv`

---

### 2. text_processing.py
Performs text preprocessing on movie overviews.

**Steps performed:**
- Converts text to lowercase  
- Removes punctuation  
- Corrects spelling  
- Removes stopwords  
- Tokenizes text  
- Lemmatizes tokens  

**Final Output:**
- `text_preprocessed.csv`

---

## Usage Flow
1. Run `movie_review_processing.py` to prepare the CSV file  
2. Run `text_processing.py` to clean and preprocess the text data  

## Notes
- Requires `pandas`, `nltk`, and `textblob`
- NLTK resources are downloaded during execution
- This folder only handles text processing, not modeling