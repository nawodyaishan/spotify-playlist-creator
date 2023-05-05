import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils import create_playlist


class SpotifyPlaylistCreatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Welcome message
        welcome_message = "Welcome to Spotify Playlist Creator! Use this app to create custom playlists based on your top tracks."
        messagebox.showinfo("Welcome", welcome_message)

        # Time range dropdown
        self.time_range_var = tk.StringVar()
        time_range_label = ttk.Label(self, text="Select time range:")
        time_range_label.grid(row=0, column=0, padx=10, pady=10)
        time_range_dropdown = ttk.Combobox(self, textvariable=self.time_range_var)
        time_range_dropdown["values"] = ("long_term", "medium_term", "short_term")
        time_range_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Number of tracks entry
        self.num_tracks_var = tk.StringVar()
        num_tracks_label = ttk.Label(self, text="Enter number of tracks:")
        num_tracks_label.grid(row=1, column=0, padx=10, pady=10)
        num_tracks_entry = ttk.Entry(self, textvariable=self.num_tracks_var)
        num_tracks_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create playlist button
        create_playlist_button = ttk.Button(self, text="Create Playlist", command=self.create_playlist_gui)
        create_playlist_button.grid(row=2, column=1, padx=10, pady=10)

        # Credits button
        credits_button = ttk.Button(self, text="Credits", command=self.show_credits)
        credits_button.grid(row=3, column=1, padx=10, pady=10)

        # Exit confirmation
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

    # Function to create a playlist with selected options
    def create_playlist_gui(self):
        time_range = self.time_range_var.get()
        num_tracks = int(self.num_tracks_var.get())
        message = create_playlist(time_range, num_tracks)
        messagebox.showinfo("Success", message)

    # Function to show credits
    def show_credits(self):
        credits = "Spotify Playlist Creator\nDeveloped by\nGitHub: \nnawodyaishan"
        messagebox.showinfo("Credits", credits)

    # Function to show exit confirmation
    def on_exit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.destroy()


if __name__ == "__main__":
    app = SpotifyPlaylistCreatorApp()
    app.title("Spotify Playlist Creator")
    app.geometry("400x200")
    app.resizable(False, False)
    app.mainloop()
