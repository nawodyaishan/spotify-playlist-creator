import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# Function to create a playlist based on time range and number of tracks
def create_playlist(time_range, num_tracks):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-public user-top-read"))

    user_id = sp.current_user()["id"]
    playlist_name = f"Top {num_tracks} Tracks - {time_range}"
    playlist_description = f"Your top {num_tracks} tracks for time range: {time_range}"

    tracks = sp.current_user_top_tracks(limit=num_tracks, time_range=time_range)["items"]
    track_ids = [track["id"] for track in tracks]

    sp.user_playlist_create(user_id, playlist_name, public=True, description=playlist_description)
    return f"Playlist '{playlist_name}' created successfully!"
