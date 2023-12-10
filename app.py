import streamlit as st
import pickle


movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list=movies['title'].values

st.header("Movie Recommender System")

selectvalue=st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie, recommend_poster



if st.button("Show Recommend"):
    movie_name, _ = recommend(selectvalue)
    st.text(movie_name[0])
    st.text(movie_name[1])
    st.text(movie_name[2])
    st.text(movie_name[3])
    st.text(movie_name[4])