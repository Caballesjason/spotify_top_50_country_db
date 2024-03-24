import yaml
import os
import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials

def get_spotify_obj():
    '''
    This function grabs your credential information from a yaml file in the super directory
    It then uses the SpotifyClientCredentials function to get access to the spotify port with
    your login credentials.
    The SpotifyClientCredential is then used in the Spotify object to communicate with the spotify API.
    '''
    wd = os.getcwd()
    
# Get path of super directory
    parent_path = os.path.abspath(os.path.join(wd, os.pardir))
    
    with open(parent_path + "/" + 'project_credentials.yaml') as f:
    # Load the .yaml data
        info = yaml.load(f, Loader=yaml.FullLoader)
    # Initialize the SpotifyClientCredentials object
        client_credentials_manager = SpotifyClientCredentials(info.get('client_id'), info.get('client_secret'))
        
    # Create a return the spotify object!
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        return sp