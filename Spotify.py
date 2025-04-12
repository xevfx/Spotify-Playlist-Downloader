import os
import subprocess

def download_spotify_playlist(playlist_url, output_path="/storage/emulated/0/Tools/yt"):
    # Create download directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    try:
        print("Starting download...")
        # Run the spotdl command
        subprocess.run([
            "spotdl",
            playlist_url,
            "--output", output_path
        ])
        print("Download complete.")
    except Exception as e:
        print(f"Error downloading playlist: {e}")

if __name__ == "__main__":
    url = input("Enter Spotify Playlist URL: ")
    download_spotify_playlist(url)