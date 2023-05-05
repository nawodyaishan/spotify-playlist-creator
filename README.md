# Spotify Playlist Creator

This project is a simple Python application that uses the [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/) library
to create Spotify playlists based on your top tracks. It features a Tkinter GUI for easy user interaction.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-github-username/spotify-playlist-creator.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your Spotify API credentials. Sign up for a Spotify Developer account and create a new app on
   the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications). Note down the Client ID,
   Client Secret, and set the Redirect URI to `http://localhost:8080`.

Replace `<your_client_id>` and `<your_client_secret>` with your own credentials.

## Usage

1. Run the application:

```bash
python spotify_playlist_gui.py
```

2. The GUI will appear. Follow the on-screen instructions to create your custom Spotify playlists.

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project's root directory and add the following variables with your corresponding Spotify
   API credentials:

```env
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=your_redirect_uri
```

## Project Structure

The project consists of two Python script files:

- `spotify_playlist_gui.py`: The main script, which handles the CLI interface and user input.
- `utils.py`: The utility script, which includes the `create_playlist` function to create playlists based on the user's
  inputs.

## License

This project is licensed under the [MIT License](LICENSE).

---