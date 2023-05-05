import os
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv
from utils import create_playlist

load_dotenv()


# Creating a class for the main application window that inherits from tk.Tk
class SpotifyPlaylistCreatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Spotify Playlist Creator")
        self.geometry("400x200")

        self.create_widgets()

    # create and configure the necessary widgets
    def create_widgets(self):
        # Time range label and combobox
        time_range_label = ttk.Label(self, text="Time Range:")
        time_range_label.grid(column=0, row=0, padx=10, pady=10, sticky="W")

        self.time_range_var = tk.StringVar()
        time_range_combobox = ttk.Combobox(self, textvariable=self.time_range_var)
        time_range_combobox["values"] = ("All-time", "Last 6 months", "Last month")
        time_range_combobox.current(0)
        time_range_combobox.grid(column=1, row=0, padx=10, pady=10, sticky="W")

        # Number of tracks label and entry
        num_tracks_label = ttk.Label(self, text="Number of Tracks:")
        num_tracks_label.grid(column=0, row=1, padx=10, pady=10, sticky="W")

        self.num_tracks_var = tk.StringVar()
        num_tracks_entry = ttk.Entry(self, textvariable=self.num_tracks_var)
        num_tracks_entry.grid(column=1, row=1, padx=10, pady=10, sticky="W")

        # Create playlist button
        create_playlist_button = ttk.Button(self, text="Create Playlist", command=self.create_playlist)
        create_playlist_button.grid(column=1, row=2, padx=10, pady=10)

        #

    def create_playlist(self):
        time_ranges = {
            "All-time": "long_term",
            "Last 6 months": "medium_term",
            "Last month": "short_term",
        }
        time_range = time_ranges[self.time_range_var.get()]
        num_tracks = int(self.num_tracks_var.get())

        create_playlist(time_range, num_tracks)


if __name__ == "__main__":
    app = SpotifyPlaylistCreatorApp()
    app.mainloop()
