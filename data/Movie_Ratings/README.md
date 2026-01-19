# Dataset README (Data Folder)

## 📌 Overview (Data Directory)

This dataset contains information about **200 movies**, focusing on their **genres**, **plot overviews**, and **titles**. It is well‑suited for **Natural Language Processing (NLP)** tasks, **recommendation systems**, and **machine learning experiments** such as text classification and clustering.

The dataset structure resembles commonly used movie metadata sources (e.g., TMDB‑style data).

---

## 📁 Files in `data/` Directory

The `data/` folder contains multiple files used at different stages of the project pipeline.

| File Name               | Description                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------- |
| `df_use.csv`            | Core dataset used for modeling; contains cleaned and selected movie records                  |
| `text_preprocessed.csv` | Text-preprocessed version of movie overviews (tokenization, cleaning, normalization applied) |
| `genre_ids.json`        | Mapping of genre IDs to human-readable genre names                                           |
| `movie_reviews.json`    | Movie reviews data used for sentiment analysis or text augmentation                          |

---

## 🧱 Dataset Structure

### 1️⃣ `df_use.csv`

| Column Name | Description                                 |
| ----------- | ------------------------------------------- |
| `title`     | Movie title                                 |
| `overview`  | Original movie plot overview                |
| `genre_ids` | List of genre IDs associated with the movie |

### 2️⃣ `text_preprocessed.csv`

| Column Name      | Description                            |
| ---------------- | -------------------------------------- |
| `title`          | Movie title                            |
| `processed_text` | Cleaned and preprocessed overview text |

### 3️⃣ `genre_ids.json`

```json
{
  "28": "Action",
  "12": "Adventure",
  "18": "Drama"
}
```

### 4️⃣ `movie_reviews.json`

Contains user or critic reviews mapped to movie titles or IDs, useful for:

* Sentiment analysis
* Text enrichment
* Multi-source NLP tasks

---

---------|----------|-------------|
| `title` | String | Movie title |
| `overview` | String | Short plot summary of the movie |
| `genre_ids` | List[int] | List of genre identifiers associated with the movie |

### Example Record

```text
Title: The Shawshank Redemption
Genres: [18, 80]
Overview: Imprisoned in the 1940s for the double murder of his wife and her lover, a banker begins a new life at the Shawshank prison...
```
---

## 📌 Notes

* Genre IDs are numeric and can be mapped to genre names using an external mapping.
* The dataset is compact and ideal for **prototyping** and **academic projects**.

---