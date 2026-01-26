# Text Vectorisation

This folder contains scripts for converting preprocessed IMDB movie review text into numerical vectors for NLP tasks.

## File

### IMBD_vectorisation.py
Applies common text vectorisation techniques on preprocessed reviews.

**Includes:**
- One-Hot Encoding  
- Bag of Words (Unigrams)  
- N-grams (Bigrams)  
- TF-IDF Vectorisation  

**Output:**
- `IMDB_tf-idf.csv`

## Notes
- Requires preprocessed, tokenized text
- Used for feature extraction before modeling