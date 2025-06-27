# ##############################################################################

# CODE NÀY TÔI ĐÃ NGỪNG PHÁT TRIỂN VÌ SPOTIFY KHÔNG CÒN CUNG CẤP PHƯƠNG THỨC GET_TRACK_FEATURE NỮA RỒI
# NÊN CÓ LẼ THÔNG TIN KHÔNG ĐỦ ĐỂ PHÂN TÍCH DỮ LIỆU

# ##############################################################################








import requests
import os
import base64
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your Spotify API credentials as environment variables
# Go to https://developer.spotify.com/dashboard/applications to get your credentials
SPOTIFY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("CLIENT_SECRET")

class SpotifyAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.token_expires_at = 0

    def _get_token(self):
        auth_string = f"{self.client_id}:{self.client_secret}"
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

        token_url = "https://accounts.spotify.com/api/token"
        token_data = {"grant_type": "client_credentials"}
        token_headers = {"Authorization": "Basic " + auth_base64}
        result = requests.post(token_url, data=token_data, headers=token_headers)

        if result.status_code == 200:
            print("Token obtained successfully")
            token_json = result.json()
            self.access_token = token_json["access_token"]
            # Spotify tokens typically last 3600 seconds (1 hour)
            self.token_expires_at = time.time() + token_json.get("expires_in", 3600) - 60 # Refresh 1 minute before expiry
            return self.access_token
        else:
            print(f"Error getting token: {result.status_code} - {result.text}")
            return None

    def _get_auth_header(self):
        if not self.access_token or time.time() >= self.token_expires_at:
            self._get_token()
        if not self.access_token:
            return None
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    def get_artist(self, artist_id):
        """Get artist json"""
        headers = self._get_auth_header()
        if not headers:
            return None

        url = f"https://api.spotify.com/v1/artists/{artist_id}"
        result = requests.get(url, headers=headers)
        
        if result.status_code == 200:
            artist_data = result.json()
            return artist_data
        else:
            print(f"Artist test failed: {result.status_code} - {result.text}")
            return None
    
    def get_multiple_artists(self, artist_ids):
        """Get information for multiple artists using a single API call."""
        headers = self._get_auth_header()
        if not headers:
            return None

        ids_param = ",".join(artist_ids)
        url = f"https://api.spotify.com/v1/artists?ids={ids_param}"
        result = requests.get(url, headers=headers)
        
        if result.status_code == 200:
            return result.json().get("artists", [])
        else:
            print(f"Error getting multiple artists: {result.status_code} - {result.text}")
            return None
    
    def search_playlists(self, query="pop"):
        """Search for playlists to get valid IDs"""
        headers = self._get_auth_header()
        if not headers:
            return None

        url = "https://api.spotify.com/v1/search"
        params = {
            "q": query,
            "type": "playlist",
            "limit": 10,
            "market": "VN"
        }
        
        result = requests.get(url, headers=headers, params=params)
        
        
        if result.status_code == 200:
            search_data = result.json()
            return search_data
        else:
            print(f"Search failed: {result.status_code} - {result.text}")
            return None

    def get_playlists(self, playlist_id, market="VN"):
        headers = self._get_auth_header()
        if not headers:
            return None

        url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
        params = {"market": market}
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
        
        result = requests.get(url, headers=headers, params=params)
        
        if result.status_code == 200:
            return result.json()
        else:
            print(f"Error getting playlist tracks: {result.status_code} - {result.text}")
            return None
    

    def get_track(self, track_id):
        headers = self._get_auth_header()
        if not headers:
            return None

        url = f"https://api.spotify.com/v1/tracks/{track_id}"
        
        result = requests.get(url, headers=headers)
        
        if result.status_code == 200:
            track_data = result.json()
            return track_data
        else:
            print(f"Track test failed: {result.status_code} - {result.text}")
            return None

    def get_multiple_tracks(self, track_ids):
        """Get information for multiple tracks using a single API call."""
        headers = self._get_auth_header()
        if not headers:
            return None

        # Spotify API allows up to 50 track IDs per request
        if len(track_ids) > 50:
            print("Warning: Too many track IDs for a single request. Only the first 50 will be used.")
            track_ids = track_ids[:50]

        ids_param = ",".join(track_ids)
        url = f"https://api.spotify.com/v1/tracks?ids={ids_param}"

        result = requests.get(url, headers=headers)

        if result.status_code == 200:
            return result.json().get("tracks", [])
        else:
            print(f"Error getting multiple tracks: {result.status_code} - {result.text}")
            return None

    def get_audio_features(self, track_id):
        """Get audio features for a single track"""
        headers = self._get_auth_header()
        if not headers:
            return None

        url = f"https://api.spotify.com/v1/audio-features/{track_id}"
        result = requests.get(url, headers=headers)
        
        if result.status_code == 200:
            return result.json()
        else:
            print(f"Error getting audio features: {result.status_code} - {result.text}")
            return None

    def get_multiple_audio_features(self, track_ids):
        """Get audio features for multiple tracks (max 100 per request)"""
        headers = self._get_auth_header()
        if not headers:
            return None

        # Spotify API allows up to 100 track IDs per request for audio features
        if len(track_ids) > 100:
            print("Warning: Too many track IDs for audio features request. Only the first 100 will be used.")
            track_ids = track_ids[:100]

        ids_param = ",".join(track_ids)
        url = f"https://api.spotify.com/v1/audio-features?ids={ids_param}"
        result = requests.get(url, headers=headers)
        
        if result.status_code == 200:
            return result.json().get("audio_features", [])
        else:
            print(f"Error getting multiple audio features: {result.status_code} - {result.text}")
            return None

if __name__ == "__main__":
    import time
    
    spotify_api = SpotifyAPI(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

    # All type of song we want
    search_list_VN = ["ballad",
                    #   "rap",
                    #   "pop"
                      ]
    
    print(spotify_api._get_token())
    
    # # Get playlists id
    # playlist_ids = []
    # for each_query in search_list_VN:
    #     search_result = spotify_api.search_playlists(query=each_query)
    #     if search_result:
    #         playlists = search_result.get('playlists', {}).get('items', [])
            
    #         if playlists:
    #             for playlist in playlists:
    #                 if playlist and 'id' in playlist:
    #                     playlist_ids.append(playlist['id'])
    #     if not playlist_ids:
    #         print(f"No valid playlist from search for query: {each_query}")
    #     else:
    #         print(f"Found playlists for '{each_query}': {playlist_ids}")
    
    # # Loop for each playlist_id
    # for p_id in playlist_ids:
    #     # Get playlist
    #     playlist_json = spotify_api.get_playlists(p_id)
        
        
    #     if playlist_json:
            
    #         # Get playlist info
    #         playlist_name = playlist_json.get("name", "Unknown Playlist")
    #         playlist_total_tracks = playlist_json.get("tracks", {}).get("total", 0)
            

    #         # Get all track_id from playlist
    #         tracks_id = []
    #         for track_item in playlist_json.get("tracks", {}).get("items", []):
    #             if track_item and track_item.get("track"):
    #                 tracks_id.append(track_item["track"].get("id"))
    #         tracks_id = [tid for tid in tracks_id if tid] 


    #         tracks_name, tracks_popularity, tracks_artists_id = [], [], []
    #         # Process in batches of 50
    #         for i in range(0, len(tracks_id), 50):
    #             batch_ids = tracks_id[i:i+50]
    #             batch_tracks_data = spotify_api.get_multiple_tracks(batch_ids)
    #             if batch_tracks_data:
    #                 for track_data in batch_tracks_data:
    #                     if track_data:
    #                         tracks_name.append(track_data.get("name", "Unknown Track"))
    #                         tracks_popularity.append(track_data.get("popularity", 0))
    #                         artists = track_data.get("artists")
    #                         artist_id = [artist.get("id") for artist in artists]
    #                         tracks_artists_id.append(artist_id)
            
            
    #         # Get artist_info
    #         get_artists_name = []
    #         for artists_arr in tracks_artists_id:
    #             for artist_id in artists_arr:
    #                 artist_info = spotify_api.get_artist(artist_id)
    #                 if artist_info:
    #                     artist_name = artist_info.get("name", "Unknown Artist")
    #                     get_artists_name.append(artist_name)
                        
                        
    #         # Get audio features
    #         audio_features = []
    #         for i in range(0, len(tracks_id), 100):
    #             batch_ids = tracks_id[i:i+100]
    #             batch_audio_features = spotify_api.get_multiple_audio_features(batch_ids)
    #             if batch_audio_features:
    #                 audio_features.extend(batch_audio_features)
    #             time.sleep(1)
            
            