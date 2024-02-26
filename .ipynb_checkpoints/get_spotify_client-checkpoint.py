import yaml
import os
import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials

def get_spotify_obj():
    '''
    This function grabs your credential information from a yaml file in the directory directly outside of your project
    directory.  It then uses the SpotifyClientCredentials function to get access to the spotify port. The
    SpotifyClientCredentials' return value gets put into the Spoify object able to access the apito access the api using the
    Spotify object.
    '''
    wd = os.getcwd()
    parent_path = os.path.abspath(os.path.join(wd, os.pardir))
    
    with open(parent_path + "/" + 'credentials.yaml') as f:
        info = yaml.load(f, Loader=yaml.FullLoader)
        client_credentials_manager = SpotifyClientCredentials(info.get('client_id'), info.get('client_secret'))
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        return sp