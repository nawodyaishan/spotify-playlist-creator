import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-public user-top-read"))

# Get user's top tracks
results = sp.current_user_top_tracks(limit=50, time_range="long_term")

# Get track URIs
track_uris = [track["uri"] for track in results["items"]]

# Get user's ID
user_id = sp.current_user()["id"]

# Create a new playlist
playlist = sp.user_playlist_create(user_id, "My Top 50 All Time", public=True,
                                   description="My most listened songs of all time")

# Add tracks to the playlist
sp.playlist_add_items(playlist["id"], track_uris)

print("Playlist created:", playlist["name"])
