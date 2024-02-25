import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials
import os
from datetime import date

"""
get_global_top_fifty_data returns a list of tuple where each tuple is a track data in the format (track, track_id, album, album_id)
"""
def get_global_top_fifty_playlist(sp):
    playlist_id = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=87c0069b7da449b7"
    top_fifty_global = sp.playlist_tracks(playlist_id)

# This is a list of all tracks in the playlist.  Track objects are dictionaries
    top_fifty_global_tracks = top_fifty_global.get("items")

    tuples = []
    
    for song in top_fifty_global_tracks:
        added_it = song.get('added_at')
        
        song_info = song.get('track')
        track = song_info.get('name')
        track_id = song_info.get('id')
    
        album_info = song_info.get('album')
        album = album_info.get('name')
        album_id = album_info.get('id')
        
        date_loaded = str(date.today())
        row = (track, track_id, album, album_id, date_loaded)
        tuples.append(row)

    return tuples

"""
get_all_song_ids returns a list of all the unique tracks and their ids for the track table as a dict.
"""
def get_all_top_fifty_tracks(sp):
    playlist_id = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=87c0069b7da449b7"
    top_fifty_global = sp.playlist_tracks(playlist_id)

# This is a list of all tracks in the playlist.  Track objects are dictionaries
    top_fifty_global_tracks = top_fifty_global.get("items")

    tuples = []
    ids = {}
    for song in top_fifty_global_tracks:
        track_name = song_info.get('name')
        track_id = song_info.get('id')
    
        if track_id not in ids:
            row = (track_id, track_name)
            tracks.append(row)
        else:
            continue
    return tracks

"""
get_all_top_fifty_artists returns the artist that related to all of the songs in a playlist
"""
def get_all_top_fifty_artists(sp):
    playlist_id = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=87c0069b7da449b7"
    top_fifty_global = sp.playlist_tracks(playlist_id)
    top_fifty_global_tracks = top_fifty_global.get("items")
    tuples = []

    for track in top_fifty_global_tracks:
        # This is a list of dicts containing where each dict is an artist's information
        track_artists = track.get('track').get('artists')
        track_artists_data = [(artist.get('id'), artist.get('name')) for artist in track_artists]
        tuples += track_artists_data

    unique_artists = set(tuples)
    tuples = list(tuples)
    return tuples

"""
get_all_top_fifty_albums returns the artist that related to all of the songs in a playlist
"""
def get_all_top_fifty_albums(sp):
    playlist_id = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=87c0069b7da449b7"
    top_fifty_global = sp.playlist_tracks(playlist_id)
    top_fifty_global_tracks = top_fifty_global.get("items")
    tuples = []

    for track in top_fifty_global_tracks:
        # This is a list of dicts containing where each dict is an artist's information
        album_id = track.get('track').get('album').get('id')
        album_name = track.get('track').get('album').get('name')
        row =(album_id, album_name)
        tuples.append(row)
        
    return tuples