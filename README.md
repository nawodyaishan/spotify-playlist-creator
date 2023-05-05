# Spotify Playlist Creator

A CLI-based Python application that creates Spotify playlists with your top tracks based on different time ranges. Users
can create playlists for their all-time top tracks, top tracks from the last 6 months, or top tracks from the last
month.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a Spotify account and have access to your `Client ID`, `Client Secret`, and `Redirect URI`.
- You have Python 3.6 or later installed on your system.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/spotify-playlist-creator.git
cd spotify-playlist-creator
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux and macOS
venv\Scripts\activate     # For Windows
```

3. Install the required dependencies:

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

## Usage

Run the `spotify_playlist.py` script to start the application:

```bash
python spotify_playlist.py
```

The application will display a main menu with the available options. Follow the prompts and input the required
information when prompted.

## Project Structure

The project consists of two Python script files:

- `spotify_playlist.py`: The main script, which handles the CLI interface and user input.
- `utils.py`: The utility script, which includes the `create_playlist` function to create playlists based on the user's
  inputs.

## License

This project is licensed under the [MIT License](LICENSE).

---