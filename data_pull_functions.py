import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials

def get_playlist_data(sp, link):
    """
    inputs:
        sp: A spotify object
        link: url to the spotify playlist
    outputs:
        dictionary of two keys (name, followers, items)
        'name' is the name of the playlist
        'items' is a list of attributes to upload in playlists 
        Track objects are one of those attributes
        Track objects are just dict
    """

    playlist = sp.playlist(link)
    playlist_name = playlist.get('name')
    playlist_items = playlist.get('tracks').get('items')
    playlist_data = {'name': playlist_name, 'items': playlist_items}
    return playlist_data


def get_audio_features(sp, tracks: list[str]):
    """
    inputs:
        sp: A spotify object
        tracks: A list of spotify track URIs to return audio features for (maximum number of tracks to pull data in one call is 100)
    outputs:
        a dictionary with track IDs as keys and audio features as values
    """
    if len(tracks) > 100:
        raise Exception("Too many tracks in 'tracks' argument")
    else:
        data = sp.audio_features(tracks)
        updated_data = {}
        for feature in data:
            track_id = feature.pop("id")
            updated_data.update({track_id:feature})
        return updated_data
    


def get_playlist_table_data(playlist_data):
    """
    inputs:
        playlist_data: Output of get_playlist_data()
            This is the raw data of a playlist
    outputs:
        table_data:  These are the rows of for Playlist
    """
# Name of playlist
    name = playlist_data.get("name")
# List of items
    items = playlist_data.get("items")
    
# Table Data
    table_data = []
    for item in items:
    # Get the track obj
        track = item.get('track')
        
        track_id = track.get('id')
        track_name = track.get('name')
        album_id = track.get('album').get('id')
        album_name = track.get('album').get('name')
        row = (name, track_id, track_name, album_id, album_name)
        table_data.append(row)
    return table_data
        

def get_tracks_table_data(sp, playlist_data):
    """
    inputs:
        sp: A spotify object
        playlist_data: Output of get_playlist_data()
            This is the raw data of a playlist
    outputs:
        table_data:  These are the rows of for Tracks
    """
# List of items
    items = playlist_data.get("items")
    
# Table Data
    table_data = []

    for item in items:
    # Get the track obj
        track = item.get('track')

    # Get track info from track
        track_id = track.get('id')
        track_name = track.get('name')
        album_id = track.get('album').get('id')
        duration_ms = track.get('duration_ms')
        explicit = track.get('explicit')
        current_popularity = track.get('popularity')
        row = (track_id, track_name, album_id, duration_ms, explicit, current_popularity)
        table_data.append(row)
    
# Use track_id to pull audio features
    get_ids = lambda tup: tup[0]
    ids = [get_ids(tup) for tup in table_data]
    audio_features = get_audio_features(sp, ids)

# update each row in table_data
    table_data_length = len(table_data)
    for index in range(table_data_length):
        row = table_data[index]
        track_id = row[0]
        track_audio_features = audio_features.get(track_id)
        acousticness = track_audio_features.get('acousticness')
        danceability = track_audio_features.get('danceability')
        instrumentalness = track_audio_features.get('instrumentalness')
        key_signature = track_audio_features.get('key')
        mode = track_audio_features.get('mode')
        tempo = track_audio_features.get('tempo')
        time_signature = track_audio_features.get('time_signature')
        valence = track_audio_features.get('valence')
        audio_feature_attributes = (acousticness, danceability, instrumentalness,
                                    key_signature, mode, tempo, time_signature,
                                    valence)
        updated_row = row + audio_feature_attributes
        table_data[index] = updated_row
    return table_data


def get_Albums_table_data(playlist_data):
    """
    inputs:
        playlist_data: Output of get_playlist_data()
            This is the raw data of a playlist
    outputs:
        table_data:  These are the rows of for Albums
    """

# List of items
    items = playlist_data.get("items")
    
# Table Data
# table_data is a dict to ensure return of unique album IDs since multiple tracks from an album
# can be in a playlist
    table_data = []
    found_albums = set()
    for item in items:
    # Get the track obj
        track = item.get('track')
        album = track.get('album')
        album_id = album.get('id')
        album_name = album.get('name')
        total_tracks = album.get('total_tracks')
        date_released = album.get('release_date')
        row = (album_id, album_name, total_tracks, date_released)
        
        if album_id not in found_albums:
            table_data.append(row)
            found_albums.add(album_id)
        else:
            continue

    return table_data


def get_AlbumArtists_table_data(playlist_data):
    """
    inputs:
        playlist_data: Output of get_playlist_data()
            This is the raw data of a playlist
    outputs:
        table_data:  These are the rows of for AlbumArtists
    """

# List of items
    items = playlist_data.get("items")
    
# Table Data
    table_data = []
    for item in items:
    # Get the track obj
        track = item.get('track')
        album = track.get('album')
        album_id = album.get('id')
    
    # artists is a list of artist obj
        artists = album.get('artists')
        artists_ids = [artist.get('id') for artist in artists]
        for artist_id in artists_ids:
            row = (album_id, artist_id)
            table_data.append(row)

    table_data = set(table_data)
    table_data = list(table_data)
    return table_data

def get_TrackArtists_table_data(playlist_data):
    """
    inputs:
        playlist_data: Output of get_playlist_data()
            This is the raw data of a playlist
    outputs:
        table_data:  These are the rows of for TrackArtists
    """

# List of items
    items = playlist_data.get("items")
    
# Table Data
    table_data = []
    for item in items:
    # Get the track obj
        track = item.get('track')
        track_id = track.get('id')
        
    # artists is a list of artist obj
        artists = track.get('artists')
        artists_ids = [artist.get('id') for artist in artists]
        
        for artist_id in artists_ids:
            row = (track_id, artist_id)
            table_data.append(row)

    table_data = set(table_data)
    table_data = list(table_data)
    return table_data

def get_TrackAvailableMarkets_table_data(playlist_data):
    """
    inputs:
        playlist_data: Output of get_playlist_data()
            This is the raw data of a playlist
    outputs:
        table_data:  These are the rows of for TrackAvailableMarkets
    """

# List of items
    items = playlist_data.get("items")
    
# Table Data
    table_data = []
    for item in items:
    # Get the track obj
        track = item.get('track')
        track_id = track.get('id')
        available_markets = track.get('available_markets')
        
        for market in available_markets:
            row = (track_id, market)
            table_data.append(row)

    table_data = set(table_data)
    table_data = list(table_data)
    return table_data

def get_GenreArtists_table_data(sp, playlist_data):
    """
    inputs:
        sp: A spotify object
        playlist_data: Output of get_playlist_data()
        This is the raw data of a playlist
    outputs:
        table_data:  These are the rows of for GenreArtists
    """
# List of items
    items = playlist_data.get("items")
   
# Table Data
    table_data = []

# Grab all unique artist ids to get their genre later
    unique_artist_ids = []
    for item in items:
    # Get the track obj
        track = item.get('track')

    # artists is a list of artist obj
        artists = track.get('artists')
    # a dictionary of artist ids and their corresponding genres
        artist_ids = [artist.get('id') for artist in artists]
        unique_artist_ids += artist_ids

    unique_artist_ids = set(unique_artist_ids)
    unique_artist_ids = list(unique_artist_ids)

# artists returns a dictionary with one kvp "artists" containing each artist obj
    artist_genre_data = sp.artists(unique_artist_ids).get('artists')

    for artist_obj in artist_genre_data:
        artist_id = artist_obj.get('id')
        genres = artist_obj.get('genres')
    # create rows for each genre for an artist id
        rows = [(artist_id, genre) for genre in genres]
        table_data += rows
    
    table_data = set(table_data)
    table_data = list(table_data)
    return table_data

def get_Artists_table_data(sp, playlist_data):
    """
    inputs:
        sp: A spotify object
        playlist_data: Output of get_playlist_data()
            This is the raw data of a playlist
    outputs:
        table_data:  These are the rows of for GenreArtists
    """
# List of items
    items = playlist_data.get("items")
   
# Table Data
    table_data = []

# Grab all unique artist ids to get their genre later
    unique_artist_ids = []
    for item in items:
    # Get the track obj
        track = item.get('track')

    # artists is a list of artist obj
        artists = track.get('artists')
    # a dictionary of artist ids and their corresponding genres
        artist_ids = [artist.get('id') for artist in artists]
        unique_artist_ids += artist_ids

    unique_artist_ids = set(unique_artist_ids)
    unique_artist_ids = list(unique_artist_ids)

# artists returns a dictionary with one kvp "artists" containing each artist obj
    artist_genre_data = sp.artists(unique_artist_ids).get('artists')

    for artist_obj in artist_genre_data:
        artist_id = artist_obj.get('id')
        artist_name = artist_obj.get('name')
        nbr_of_followers = artist_obj.get('followers').get('total')
        popularity = artist_obj.get('popularity')
    # create rows for each genre for an artist id
        row = (artist_id, artist_name, nbr_of_followers, popularity)
        table_data.append(row)
    
    table_data = set(table_data)
    table_data = list(table_data)
    return table_data