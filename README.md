# 🎬 Movie Recommender System

A **Content-Based Movie Recommendation System** built using **Machine Learning** and **Natural Language Processing (NLP)**. The system recommends movies similar to a selected movie by analyzing genres, cast, crew, keywords, and movie overviews using **CountVectorizer** and **Cosine Similarity**.

The project is deployed with **Streamlit**, providing an interactive web interface for discovering similar movies.

---

## 🚀 Live Demo

🔗 **App:** *(https://movierecommender-gt4vzhbg5krt8kff9axuic.streamlit.app/)*

---

## 📂 GitHub Repository

🔗 **Repository:** https://github.com/SAYANDAS2109/Movie_RECOMMENDER

---

# 📌 Features

- 🎬 Content-Based Movie Recommendation
- 🧠 NLP-based Feature Engineering
- 🔍 Similarity Search using Cosine Similarity
- 📖 Movie Metadata Processing
- ⚡ Fast Recommendation Generation
- 💻 Interactive Streamlit Web Application
- 📊 Clean and Professional User Interface

---

# 🛠 Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn

### Natural Language Processing
- NLTK
- CountVectorizer

### Data Processing
- Pandas
- NumPy

### Deployment
- Streamlit

---

# 📁 Dataset

This project uses the **TMDB 5000 Movie Dataset**, containing movie metadata such as:

- Genres
- Keywords
- Cast
- Crew
- Movie Overview
- Titles
- Movie IDs

---

# ⚙️ Project Workflow

## 1️⃣ Data Collection

- Imported TMDB 5000 Movies Dataset
- Imported TMDB 5000 Credits Dataset

---

## 2️⃣ Data Preprocessing

Performed extensive preprocessing including:

- Removing unnecessary columns
- Handling missing values
- Merging datasets
- Selecting useful features

---

## 3️⃣ Feature Engineering

Extracted and processed:

- Genres
- Keywords
- Top 3 Cast Members
- Director
- Movie Overview

Created a unified **Tags** feature by combining all relevant information.

---

## 4️⃣ Text Preprocessing

Applied:

- Lowercase conversion
- Tokenization
- Stemming using NLTK Porter Stemmer

to normalize textual information.

---

## 5️⃣ Vectorization

Converted movie tags into numerical vectors using:

- CountVectorizer

This transformed textual movie information into machine-readable features.

---

## 6️⃣ Similarity Calculation

Calculated movie similarity using:

- Cosine Similarity

This allows the system to identify movies with similar characteristics.

---

## 7️⃣ Recommendation Engine

Implemented a recommendation function that:

- Finds the selected movie
- Retrieves similarity scores
- Sorts movies by similarity
- Returns the Top 5 Recommendations

---

## 8️⃣ Deployment

Developed an interactive Streamlit application allowing users to:

- Select a movie
- Generate recommendations instantly
- Explore similar movies



---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/SAYANDAS2109/Movie_RECOMMENDER.git
```

Move into the project directory

```bash
cd Movie_RECOMMENDER
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```


# 💡 Future Improvements

- 🎬 Movie Posters using TMDB API
- ⭐ Movie Ratings
- 📅 Release Year
- 🎭 Genres
- 📖 Movie Overview
- 🎞 Netflix-style User Interface
- 🤖 Hybrid Recommendation System
- 🔥 Collaborative Filtering

---

# ⚠️ Note

The similarity matrix (`similarity.pkl`) is generated from the processed dataset and is included for faster recommendations during deployment.

---

# 👨‍💻 Author

**Sayan Das**


---

