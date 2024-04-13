import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials

def get_playlist_data(sp, link):
    """
    Inputs:
        sp: A spotify object
        link: url to the spotify playlist

    Outputs:
        playlist_data: dictionary of two keys (name, items)
            'name' is the name of the playlist
            'items' is a list of attributes to upload in playlists 
    """

# Take the playlist url and pull its data
    playlist = sp.playlist(link)
    playlist_name = playlist.get('name')

# Pull the track information from the playist
    playlist_items = playlist.get('tracks').get('items')
    playlist_data = {'name': playlist_name, 'items': playlist_items}
    return playlist_data


def get_audio_features(sp, tracks: list[str]):
    """
    Inputs:
        sp: A spotify object
        tracks: A list of spotify track URIs to return audio features for (maximum number of tracks to pull data in one call is 100)

    Outputs:
        data: a dictionary with track IDs as keys and audio features as values
    """

    updated_data = {}

# Grab audio features
    data = sp.audio_features(tracks)

#  Update dictionary   
    for feature in data:
        track_id = feature.pop("id")
        updated_data.update({track_id:feature})
    return updated_data
    

def get_playlist_table_data(playlist_data):
    """
    Inputs:
        playlist_data: Output of get_playlist_data()
            This is the raw data of a playlist

    Outputs:
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
    Inputs:
        sp: A spotify object
        playlist_data: Output of get_playlist_data()
            This is the raw data of a playlist

    Outputs:
        table_data:  These are the rows of Tracks
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

# Grab audio features to append to other track data
    audio_features = get_audio_features(sp, ids)
    
# update each row in table_data with audio features for each track
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
    # Update row at index
        table_data[index] = updated_row
    return table_data


def get_Albums_table_data(playlist_data):
    """
    Inputs:
        playlist_data: Output of get_playlist_data()
            This is the raw data of a playlist
    Outputs:
        table_data:  These are the rows of for Albums
    """

# List of items
    items = playlist_data.get("items")
    

    table_data = []
# A playlist can have multiple tracks from the same album, so we want to ignore repeated albums
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
        
    # Avoid already captured albums
        if album_id not in found_albums:
            table_data.append(row)
            found_albums.add(album_id)
        else:
            continue

    return table_data


def get_AlbumArtists_table_data(playlist_data):
    """
    Inputs:
        playlist_data: Output of get_playlist_data()
            This is the raw data of a playlist
    Outputs:
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

    # Grab a list of all artist_ids from artists
        artists_ids = [artist.get('id') for artist in artists]

        for artist_id in artists_ids:
            row = (album_id, artist_id)
            table_data.append(row)

# To confirm we only capture unique albums!
    table_data = set(table_data)
    table_data = list(table_data)
    return table_data


def get_TrackArtists_table_data(playlist_data):
    """
    Inputs:
        playlist_data: Output of get_playlist_data()
            This is the raw data of a playlist
    Outputs:
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

    # Grab a list of all artist_ids from artists
        artists_ids = [artist.get('id') for artist in artists]
        
        for artist_id in artists_ids:
            row = (track_id, artist_id)
            table_data.append(row)

    return table_data


def get_TrackAvailableMarkets_table_data(playlist_data):
    """
    Inputs:
        playlist_data: Output of get_playlist_data()
            This is the raw data of a playlist
    Outputs:
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
        
    # available_markets is a list of markets track is available in
        available_markets = track.get('available_markets')
        
        for market in available_markets:
            row = (track_id, market)
            table_data.append(row)

    return table_data


def get_GenreArtists_table_data(sp, playlist_data):
    """
    Inputs:
        sp: A spotify object
        playlist_data: Output of get_playlist_data()
        This is the raw data of a playlist
    Outputs:
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

    # Grab all artists ids
        artist_ids = [artist.get('id') for artist in artists]
        unique_artist_ids += artist_ids

# Make unique_artist_ids list
    unique_artist_ids = set(unique_artist_ids)
    unique_artist_ids = list(unique_artist_ids)

# Grab the total number of unique ids
    nbr_of_unique_ids = len(unique_artist_ids)

# Partition the data if we have more than 50 ids since url can only handle
# at most 50 ids
    if nbr_of_unique_ids > 50:
    # partition is a list of lists where each list contain ids
        partition = list_partition(unique_artist_ids, 50)
        for group in partition:

        # artist_genre_data returns a dictionary with one kvp "artists" containing
        # each artist obj
            artist_genre_data = sp.artists(group).get('artists')

            for artist_obj in artist_genre_data:
                artist_id = artist_obj.get('id')
                genres = artist_obj.get('genres')

            # create rows for each genre for an artist id
                rows = [(artist_id, genre) for genre in genres]
                table_data += rows
        
        return table_data
    
    else:
        # artist_genre_data returns a dictionary with one kvp "artists" containing
        # each artist obj
        artist_genre_data = sp.artists(unique_artist_ids).get('artists')

        for artist_obj in artist_genre_data:
            artist_id = artist_obj.get('id')
            genres = artist_obj.get('genres')

        # create rows for each genre for an artist id
            rows = [(artist_id, genre) for genre in genres]
            table_data += rows

    return table_data

def get_Artists_table_data(sp, playlist_data):
    """
    Inputs:
        sp: A spotify object
        playlist_data: Output of get_playlist_data()
            This is the raw data of a playlist
    Outputs:
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

# Make unique_artist_ids list
    unique_artist_ids = set(unique_artist_ids)
    unique_artist_ids = list(unique_artist_ids)

# Grab the total number of unique ids
    nbr_of_unique_ids = len(unique_artist_ids)

# Partition the data if we have more than 50 ids since url can only handle
# at most 50 ids
    if nbr_of_unique_ids > 50:

    # partition is a list of lists where each list contain ids
        partition = list_partition(unique_artist_ids, 50)
        for group in partition:
            artist_genre_data = sp.artists(group).get('artists')

            for artist_obj in artist_genre_data:
                artist_id = artist_obj.get('id')
                artist_name = artist_obj.get('name')
                nbr_of_followers = artist_obj.get('followers').get('total')
                popularity = artist_obj.get('popularity')

            # create rows for each genre for an artist id
                row = (artist_id, artist_name, nbr_of_followers, popularity)
                table_data.append(row)
        return table_data
    else:

    # artist_genre_data returns a dictionary with one kvp "artists" containing
    # each artist obj
        artist_genre_data = sp.artists(unique_artist_ids).get('artists')

        for artist_obj in artist_genre_data:
            artist_id = artist_obj.get('id')
            artist_name = artist_obj.get('name')
            nbr_of_followers = artist_obj.get('followers').get('total')
            popularity = artist_obj.get('popularity')

        # create rows for each genre for an artist id
            row = (artist_id, artist_name, nbr_of_followers, popularity)
            table_data.append(row)

        return table_data

# Used to partition lists into smaller lists (less than 50 as requests can be longer than 50)
def list_partition(some_list, size):
    """
        Inputs:
            some_list: A list containing some elements
            size: The desired size you want for a list
        Outputs:
            partition: If the size of some_list is too large, return a list of lists
                containing elements divided into each list
    """
# Initialize partition
    partition = []
# If the number of elements are greater than size partition data!
    if len(some_list) <= size:
        partition.append(some_list)
        return partition
    else:
        partition_one = [some_list[ele] for ele in range(size)]
        partition.append(partition_one)
        partition_two = [some_list[ele] for ele in range(size, len(some_list))]
        return partition + list_partition(partition_two, size)
