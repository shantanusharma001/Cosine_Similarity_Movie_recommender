import streamlit as st
import pickle
import pandas as pd 
import numpy as np

#Loading all the data that we dumped from our notebook. 
cosine_sim = np.load('similar.npy')
cosine_dataframe = pd.read_pickle('cosine.pkl')

#HEre we import the functions we dfefined in the jupyter notebook to retrieve data from our dataframes. 
def get_index(movie):
    row_index = cosine_dataframe.index.get_loc(cosine_dataframe[cosine_dataframe['original_title']== movie].index[0])
    return row_index

def get_similar(movie):
    index = get_index(movie)
    sim_row = cosine_sim[index]
    top_10 = sorted(list(enumerate(sim_row)), reverse=True, key=lambda x:x[1])[1:11]
    movie_names = []
    for i in range (10):
       movie_names.append(cosine_dataframe['original_title'].iloc[top_10[i][0]])
    return movie_names     

#Creating a title for our webpage
st.title("Content based filtering Movie recommendation system")

#Creating a box that can be typed in and has a dropdown menu which displays all the movies from our datasets. 
option = st.selectbox(
    'Please a enter a movie that you like ',
    (cosine_dataframe['original_title'].tolist()))

st.write('Movies similar to', option, "are:")

#Creating the logic for what happens on a button press. It calls the get_similar function we defined and the creates buttons for all the results so that we can link the user to a google webpage that displays more information.
if st.button('Recommend'):
    movies = get_similar(option)
    for i in range(10):
        st.link_button(movies[i], f"https://www.google.com/search?q={movies[i]}")
    