from utility_functions import create_connection
from utility_functions  import execute_sql_query


def AlbumArtists_insert(data, conn):
    insert_query = """
    INSERT INTO AlbumArtists (album_id, artist_id) VALUES (?, ?)
    """
    cur = conn.cursor()
    with conn:
    # to insert data
        cur.executemany(insert_query, data)
        conn.commit()

def Albums_insert(data, conn):
    insert_query = """
    INSERT INTO Albums (album_id, album_name, total_tracks, date_released) VALUES (?,?,?,?)
    """
    cur = conn.cursor()
    with conn:
    # to insert data
        cur.executemany(insert_query, data)
        conn.commit()

def Artists_insert(data, conn):
    insert_query = """
    INSERT INTO Artists (artist_id, artist_name, nbr_of_followers, popularity) VALUES (?,?,?,?)
    """
    cur = conn.cursor()
    with conn:
    # to insert data
        cur.executemany(insert_query, data)
        conn.commit()

def GenreArtists_insert(data, conn):
    insert_query = """
    INSERT INTO GenreArtists (artist_id, genre) VALUES (?,?)
    """
    cur = conn.cursor()
    with conn:
    # to insert data
        cur.executemany(insert_query, data)
        conn.commit()

def Playlists_insert(data, conn):
    insert_query = """
    INSERT INTO Playlists (name, track_id, track_name, album_id, album_name) VALUES (?,?,?,?,?)
    """
    cur = conn.cursor()
    with conn:
    # to insert data
        cur.executemany(insert_query, data)
        conn.commit()

def TrackArtists_insert(data, conn):
    insert_query = """
    INSERT INTO TrackArtists (track_id, artist_id) VALUES (?,?)
    """
    cur = conn.cursor()
    with conn:
    # to insert data
        cur.executemany(insert_query, data)
        conn.commit()

def Tracks_insert(data, conn):
    insert_query = """
    INSERT INTO Tracks (track_id,track_name,album_id,duration_ms,explicit,
    current_popularity,acousticness,danceability,instrumentalness, key_signature,
    mode,tempo,time_signature,valence) VALUES (?,?,?,?,?,?,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL)
    """
    cur = conn.cursor()
    with conn:
    # to insert data
        cur.executemany(insert_query, data)
        conn.commit()