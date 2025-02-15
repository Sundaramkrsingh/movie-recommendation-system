import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies_pickle[movies_pickle['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies:
        recommended_movies.append(movies_pickle.iloc[i[0]].title)

    return recommended_movies

movies_pickle = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_pickle['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie = st.selectbox('Select a movie of your choice', movies_list)

if st.button('recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)
