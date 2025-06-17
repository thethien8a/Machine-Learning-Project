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
        print("Token obtained successfully")
        token_json = result.json()
        access_token = token_json["access_token"]  # Update access_token
        return access_token
    else:
        print(f"Error getting token: {result.status_code} - {result.text}")
        return None

def get_artist(artist_id):  
    """Test if our token works by getting artist info"""
    global access_token
    if not access_token:
        access_token = get_token()
    if not access_token:
        return None

    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    print(f"Testing artist endpoint: {url}")
    result = requests.get(url, headers=headers)
    print(f"Artist test - Status: {result.status_code}")
    
    if result.status_code == 200:
        artist_data = result.json()
        print(f"SUCCESS! Got artist: {artist_data.get('name', 'Unknown')}")
        return artist_data
    else:
        print(f"Artist test failed: {result.status_code} - {result.text}")
        return None

def search_playlists(query="pop"):
    """Search for playlists to get valid IDs"""
    global access_token
    if not access_token:
        access_token = get_token()
    if not access_token:
        return None

    url = "https://api.spotify.com/v1/search"
    params = {
        "q": query,
        "type": "playlist",
        "limit": 10,
        "market": "VN"
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    print(f"Searching playlists with query: {query}")
    result = requests.get(url, headers=headers, params=params)
    print(f"Search - Status: {result.status_code}")
    
    if result.status_code == 200:
        search_data = result.json()
        return search_data
    else:
        print(f"Search failed: {result.status_code} - {result.text}")
        return None

def get_playlists(playlist_id, market="VN"):
    global access_token  # Use global access_token
    if not access_token:
        access_token = get_token()  # Get token if it's None
    if not access_token:
        return None

    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    params = {"market": market}
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
    }
    
    result = requests.get(url, headers=headers, params=params)
    
    if result.status_code == 200:
        return result.json()
    else:
        print(f"Error getting playlist tracks: {result.status_code} - {result.text}")
        return None
    
def get_track(track_id):
    global access_token
    if not access_token:
        access_token = get_token()
    if not access_token:
        return None

    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    result = requests.get(url, headers=headers)
    
    if result.status_code == 200:
        track_data = result.json()
        return track_data
    else:
        print(f"Track test failed: {result.status_code} - {result.text}")
        return None

if __name__ == "__main__":
    # All type of song we want
    search_list_VN = ["ballad",
                    #   "rap",
                    #   "pop"
                      ]
    
    # Get playlists id
    for each_query in search_list_VN:
        search_result = search_playlists(query=each_query)
        
        playlist_id = []
        if search_result:
            playlists = search_result.get('playlists', {}).get('items', [])
            print(f"Debug: Got {len(playlists)} playlists from search")
            if playlists:
                for playlist in playlists:
                    if playlist and 'id' in playlist:
                        playlist_id.append(playlist['id'])

        if not playlist_id:
            print(f"No valid playlist from search")
        else:
            print(playlist_id)
    
    # Get playlist info and get tracks from playlist
    for p_id in playlist_id:
        print(f"Getting tracks for playlist ID: {p_id}")
        playlist_json = get_playlists(p_id)
        
        list_track_id = []
        if playlist_json:
            
            # Get playlist info
            playlist_name = playlist_json.get("name",{})
            playlist_total_tracks = playlist_json.get("tracks",{}).get("total",{})
            
            # Get all track_id frorm playlist    
            for track in playlist_json.get("tracks",{}).get("items",{}):
                list_track_id.append(track.get("track",{}).get("id",{}))

    