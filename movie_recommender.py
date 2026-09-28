import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import matplotlib

matplotlib.use('TkAgg')

from sklearn.metrics.pairwise import cosine_similarity

import requests

import gradio as gr

TMDB_API_KEY="f404083951ce90fd0fe65bf7ef678bc3"

df=pd.read_csv("movies.csv")
print(df.head())
print(df.columns)
print(df.describe)

genres=df["genres"].fillna("").str.get_dummies("|")

df=pd.concat([df,genres],axis=1)

x = genres.drop(columns=["Comedy"])
print(x)
y = genres["Comedy"]
print(y)

#sns.pairplot(df)
#plt.show()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
print(x_test)

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy",accuracy)

movie = input("Enter movie name: ")

# Find movie
result = df[df["title"].str.contains(movie, case=False, na=False)]

if result.empty:
    print("Movie not found")

else:
    index = result.index[0]

    # Find movies with similar genres
    similarity = cosine_similarity(genres)
    scores=similarity[index]

    # Get top 5
    recommendations = scores.argsort()[::-1]

    print("\nRecommended Movies:")

    count = 0
    for i in recommendations:
        if i != index:
            print(df.loc[i, "title"])
            count += 1

        if count == 5:
            break

def get_poster(movie_title):


    movie_title = movie_title.split(" (")[0]

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "query": movie_title
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    if len(data["results"]) == 0:
        return None

    # Check results until we find a poster
    for movie in data["results"]:

        if movie["poster_path"] is not None:

            return "https://image.tmdb.org/t/p/w500" + movie["poster_path"]

    return None

# =========================================================
# ADDED: GRADIO FUNCTION
# =========================================================

def gradio_recommend(movie):

    result = df[
        df["title"].str.contains(
            movie,
            case=False,
            na=False
        )
    ]

    if result.empty:
        return None, "Movie not found", None, "", None, "", None, "", None, "", None, ""

    index = result.index[0]

    scores = similarity[index]

    recommendations = scores.argsort()[::-1]

    movies = []

    count = 0

    for i in recommendations:

        if i != index:

            title = df.loc[i, "title"]

            poster = get_poster(title)

            movies.append((poster, title))

            count += 1

        if count == 5:
            break

    return (
        movies[0][0], movies[0][1],
        movies[1][0], movies[1][1],
        movies[2][0], movies[2][1],
        movies[3][0], movies[3][1],
        movies[4][0], movies[4][1]
    )


# =========================================================
# ADDED: GRADIO FRONTEND
# =========================================================

with gr.Blocks() as app:

    gr.Markdown("# 🎬 Hello, Welcome to AR Movie Recommender")

    movie_input = gr.Textbox(
        label="Enter Movie Name",
        placeholder="Example: Toy Story"
    )

    process_button = gr.Button("🎯 Recommend Movies")

    gr.Markdown("## Recommended Movies")


    with gr.Row():

        poster1 = gr.Image(label="Movie 1")
        title1 = gr.Textbox(label="Title")


    with gr.Row():

        poster2 = gr.Image(label="Movie 2")
        title2 = gr.Textbox(label="Title")


    with gr.Row():

        poster3 = gr.Image(label="Movie 3")
        title3 = gr.Textbox(label="Title")


    with gr.Row():

        poster4 = gr.Image(label="Movie 4")
        title4 = gr.Textbox(label="Title")


    with gr.Row():

        poster5 = gr.Image(label="Movie 5")
        title5 = gr.Textbox(label="Title")


    process_button.click(
        gradio_recommend,
        inputs=movie_input,
        outputs=[
            poster1, title1,
            poster2, title2,
            poster3, title3,
            poster4, title4,
            poster5, title5
        ]
    )


app.launch()