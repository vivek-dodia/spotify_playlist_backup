# 🎶 Spotify Playlist Backup 📦

This Python script allows you to back up your Spotify playlists' data in both JSON and CSV formats. Simply follow the steps below to get started!

## Prerequisites

Before using this script, make sure you have the following:

- [x] A Spotify Developer Account
- [x] Spotify Client ID (SPOTIFY_CLIENT_ID)
- [x] Spotify Client Secret (SPOTIFY_CLIENT_SECRET)
- [x] Spotify Username (SPOTIFY_USERNAME)
- [x] Spotify Password (SPOTIFY_PASSWORD)

In the Spotify dev dashboard, make sure to put http://localhost:3000 as your callback URL.

## Getting Started

1. Clone this repository to your local machine.

2. Create a copy of `example.env` and rename it to `.env`. Fill in the required Spotify credentials (Client ID, Client Secret, Username, and Password) in the `.env` file.

3. Install the necessary Python packages by running:

   ```shell
   pip install -r requirements.txt

🚀 Usage
To backup playlist data in JSON format, run:
python script_json.py

If you also want to export the data in CSV format (because why not!), use:
python script_json_csv.py

🎵 Authentication
When you run either script, it will trigger a Chrome tab to open. It will automatically navigate to http://localhost:3000, where you can log in to Spotify to authenticate the script. Don't worry; it will close the tab once it's done! 🚪🔐

📄 Output
The script will scrape your playlist data and save it in the following folders:

JSON files: playlists/
CSV files (if using script_json_csv.py): output/
🎉 Enjoy Your Backed-Up Playlists!
Now you have your precious Spotify playlists backed up in JSON or CSV format. Enjoy peace of mind knowing your music collection is safe! 🎵✨

