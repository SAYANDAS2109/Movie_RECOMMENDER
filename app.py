import streamlit as st
import numpy as np
import pandas as pd
import pickle as pkl

movies = pkl.load(open(r'C:\C LANGUAGE\code2\Movie_Recommeder\movies.pkl','rb'))

similarity = pkl.load(open(r'C:\C LANGUAGE\code2\Movie_Recommeder\similarity.pkl','rb'))

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

st.title("Movie Recommender System")

st.write(
    "Discover movies similar to your favourites using Machine Learning."
)
st.markdown("---")

selected_movie = st.selectbox(
    "Select a Movie",
    movies['title'].values
)

def recommend(movie):
    movie_index = movies[movies["title"]==movie].index[0]

    distances = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]
    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    for movie in recommendations:
        st.write(movie)