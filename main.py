import spotipy
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st
import pandas as pd

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=st.secrets['id'],
                                               client_secret=st.secrets['secret'],
                                               redirect_uri="http://127.0.0.1:1234",
                                               scope=['user-top-read']))

st.title("Henry's Spotify Data")
st.header("Henry's most listened artists")
artist_time_range = st.selectbox('Short, medium or long-term data?', options=[
    'short', 'medium', 'long'])
artist_time_range = artist_time_range + '_term'

top_artists = sp.current_user_top_artists(time_range=artist_time_range)
top_artists_list = []
for i in range(len(top_artists['items'])):
    top_artists_list.append(top_artists['items'][i]['name'])
artists_ranking = range(1, len(top_artists_list) + 1)
artists_df = pd.DataFrame({'rank': list(artists_ranking), 'artist': top_artists_list})
st.dataframe(artists_df)

st.header("Henry's most listened tracks")
track_time_range = st.selectbox('Short, medium or long-term data?', options=[
    'short', 'medium', 'long'], key=123)
track_time_range = track_time_range + '_term'
top_tracks = sp.current_user_top_tracks(time_range=track_time_range)
top_tracks_list = []
for j in range(len(top_tracks['items'])):
    top_tracks_list.append(top_tracks['items'][j]['name'])
tracks_ranking = range(1, len(top_tracks_list) + 1)
tracks_df = pd.DataFrame({'rank': list(tracks_ranking), 'name': top_tracks_list})
st.dataframe(tracks_df)