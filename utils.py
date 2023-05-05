import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()


def create_playlist(time_range, limit):
    # Initialize the Spotify API client with the required scopes
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-public user-top-read"))

    # Get the current user's ID
    user_id = sp.current_user()["id"]

    # Create the playlist name based on the time range and limit
    playlist_name = f"Top {limit} Tracks - {time_range}"

    # Create the playlist for the current user
    playlist = sp.user_playlist_create(user_id, playlist_name)

    # Get the user's top tracks based on the time range and limit
    top_tracks = sp.current_user_top_tracks(limit=limit, time_range=time_range)["items"]

    # Extract the track IDs from the top tracks
    track_ids = [track["id"] for track in top_tracks]

    # Add the top tracks to the created playlist
    sp.playlist_add_items(playlist["id"], track_ids)

    # Print a success message
    print(f"Playlist '{playlist_name}' created successfully!")
