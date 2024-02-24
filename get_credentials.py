import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials


def get_spotify_credentials(client_id, client_secret):
    
# SpotifyClientCredentials is an object to access your spotify apps credentials.  This allows you to pull from spotify's API
    
    client_credentials_manager = SpotifyClientCredentials(client_id='7800ae1c94e04926af2f73e507708e3e',
                                                         client_secret='aad2354a68cb40b68bb637d123a9a04d')
    return client_credentials_manager
