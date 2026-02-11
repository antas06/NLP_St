
---

## Folder Overview

### 1. `data/`
Contains all **raw, intermediate, and processed datasets** used throughout the project.

Typical contents:
- Raw JSON files fetched from APIs
- Intermediate CSV files
- Final cleaned and preprocessed datasets

This folder acts as the central storage for data used across scripts and notebooks.

---

### 2. `data_acquisition/`
Handles **data collection and consolidation** from external sources.

Includes scripts for:
- Fetching movie genres and genre IDs
- Fetching movie ratings and metadata using APIs
- Merging multiple API outputs into a single dataset

Purpose:
- Automate data fetching
- Create a clean, unified dataset for downstream processing

---

### 3. `text_processing/`
Responsible for **cleaning and preprocessing text data**.

Includes scripts for:
- Selecting relevant columns from raw datasets
- Text normalization (lowercasing, punctuation removal)
- Stopword removal
- Tokenization
- Lemmatization
- Exporting final preprocessed text data

Purpose:
- Prepare text data for NLP models and analysis

---

### 4. `notebooks/`
Contains **Jupyter/Colab notebooks** used for:
- Exploration and experimentation
- Testing preprocessing steps
- Analysis and visualization
- Model prototyping (if applicable)

This folder is mainly for iterative development and insights.

---

## Workflow Summary

1. **Data Acquisition**
   - Collect movie data and genres using scripts in `data_acquisition/`

2. **Data Storage**
   - Store raw and merged data in `data/`

3. **Text Processing**
   - Clean and preprocess movie overviews using scripts in `text_processing/`

4. **Exploration & Analysis**
   - Use notebooks in `notebooks/` for experimentation and modeling

3. **Word2Vec Model Training**
   - Training Word2Vec model on Game of thrones data, refer `Word2Vec\Preprop_and_w2v_training.py`

---

## Tech Stack

- Python
- Pandas
- Requests
- NLTK
- TextBlob
- Jupyter / Google Colab

---

## Notes

- API keys should be handled securely (environment variables recommended)
- File paths may need adjustment depending on environment
- The repository is modular to allow easy extension for modeling tasks

---
