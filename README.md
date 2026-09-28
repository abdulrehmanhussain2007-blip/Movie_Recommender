# 🎬 AR Movie Recommender

## 📌 Project Overview

AR Movie Recommender is a Python-based movie recommendation system that suggests movies based on genre similarity.

The project uses **Cosine Similarity** to identify movies with similar genres and integrates the TMDB API to retrieve movie posters.

A Gradio interface allows users to enter a movie title and view five recommended movies with their posters.

## ✨ Features

* Movie recommendations based on genre similarity.
* Cosine Similarity for measuring movie similarity.
* Genre preprocessing using Pandas.
* Movie poster retrieval through the TMDB API.
* Interactive Gradio web interface.
* Displays five recommended movies with their posters and titles.
* Case-insensitive movie title search.

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Requests
* Gradio
* TMDB API

## 📂 Dataset

**Dataset:** `movies.csv`

The dataset contains movie information, including:

* Movie titles
* Genres

The genre column is transformed into binary genre features using Pandas `str.get_dummies()`.

These features are used to calculate similarity between movies.

## ⚙️ How It Works

### 1. Data Loading

Loads movie information from `movies.csv` using Pandas.

### 2. Genre Preprocessing

Converts the genre column into separate binary columns using:

`str.get_dummies("|")`

Each movie is represented by its genre features.

### 3. Cosine Similarity

Uses Scikit-learn's `cosine_similarity()` to calculate similarity between movie genre vectors.

Movies with more similar genre representations receive higher similarity scores.

### 4. Movie Recommendation

When a user enters a movie title:

* The system searches for a matching movie.
* Retrieves its similarity scores.
* Sorts movies by similarity.
* Excludes the selected movie.
* Displays the top five recommendations.

### 5. TMDB API Integration

Uses The Movie Database (TMDB) API to search for movie posters.

Poster images are retrieved using the movie title and displayed in the Gradio interface.

### 6. Gradio Interface

The application provides:

* Movie title input
* Recommendation button
* Five movie poster displays
* Five corresponding movie title fields

## 🤖 Machine Learning Component

The project also includes a Logistic Regression classifier trained to predict whether a movie belongs to the Comedy genre based on its genre features.

The model is evaluated using accuracy.

**Note:** Logistic Regression is an additional classification exercise. The movie recommendation system itself uses cosine similarity rather than the trained classifier.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd AR-Movie-Recommender
```

### 3. Install dependencies

```bash
pip install numpy pandas matplotlib seaborn scikit-learn requests gradio
```

### 4. Add the dataset

Place `movies.csv` in the project directory.

### 5. Configure your TMDB API key

Set your TMDB API key as an environment variable rather than hardcoding it in the source code.

### 6. Run the application

```bash
python movie_recommender.py
```

## 📚 Learning Outcomes

Through this project, I practiced:

* Data preprocessing with Pandas.
* Converting categorical genres into numerical features.
* Calculating cosine similarity.
* Building a content-based recommendation system.
* Training a Logistic Regression classifier.
* Integrating external APIs using Requests.
* Creating interactive machine learning applications using Gradio.

## 👨‍💻 Author

**Abdul Rehman Hussain**

Python | Machine Learning | Data Science
