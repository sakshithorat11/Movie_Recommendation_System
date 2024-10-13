

import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    """Fetch the poster URL for a given movie ID from The Movie Database API."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path

def recommend(movie):
    """Recommend movies based on the input movie title."""
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

# Load movies and similarity data from the specified paths
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))  # Changed path according to your second code
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))  # Same path as per your second code

# Streamlit UI
st.title('Movie Recommendation System')

# Movie selection dropdown
selected_movie_name = st.selectbox('Search', movies['title'].values)

if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:
        st.image(posters[0])
        st.text(names[0])

    with col2:
        st.image(posters[1])
        st.text(names[1])

    with col3:
        st.image(posters[2])
        st.text(names[2])

    with col4:
        st.image(posters[3])
        st.text(names[3])

    with col5:
        st.image(posters[4])
        st.text(names[4])