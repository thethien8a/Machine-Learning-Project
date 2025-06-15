import requests
import os
import base64
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your Spotify API credentials as environment variables
# Go to https://developer.spotify.com/dashboard/applications to get your credentials
SPOTIFY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("CLIENT_SECRET")

access_token = None  # Initialize access_token

def get_token():
    global access_token  # Use global access_token
    auth_string = SPOTIFY_CLIENT_ID + ":" + SPOTIFY_CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    token_url = "https://accounts.spotify.com/api/token"
    token_data = {"grant_type": "client_credentials"}
    token_headers = {"Authorization": "Basic " + auth_base64}
    result = requests.post(token_url, data=token_data, headers=token_headers)

    if result.status_code == 200:
        print("Token okay !")
        token_json = result.json()
        access_token = token_json["access_token"]  # Update access_token
        return access_token
    else:
        print(f"Error getting token: {result.status_code} - {result.text}")
        return None

def get_playlist(playlist_id):
    global access_token  # Use global access_token
    if not access_token:
        access_token = get_token()  # Get token if it's None
    if not access_token:
        return None

    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    result = requests.get(url, headers=headers)
    if result.status_code == 200:
        return result.json()
    else:
        print(f"Error getting playlist: {result.status_code} - {result.text}")
        return None

if __name__ == "__main__":
    playlist = get_playlist('37i9dQZF1DX0F4i7Q9pshJ')
    print(playlist)
