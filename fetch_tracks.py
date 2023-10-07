import csv
import os

def fetch_tracks_from_playlist(sp, playlist_id, playlist_name, owner):
    # Initialize an empty list to hold track details
    track_list = []
    
    # Fetch tracks from the playlist
    tracks = sp.playlist_tracks(playlist_id)
    
    for item in tracks['items']:
        track = item['track']
        if track is None:  # Skip if track is None
            continue
        track_details = {
            'playlist_name': playlist_name,
            'playlist_owner': owner,
            'track_name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'duration': track['duration_ms'],
            'popularity': track['popularity']
        }
        track_list.append(track_details)
    
    # Create output directory if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')
    
    # Write to CSV
    keys = track_list[0].keys()
    with open(f"output/{playlist_name}.csv", 'w', newline='') as output_file:  # Updated path here
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(track_list)

    print(f"Saved output/{playlist_name}.csv")  # Updated print statement
