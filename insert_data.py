from utility_functions import create_connection
from utility_functions  import execute_sql_query


def insert_tracks(data, conn):
    get_current_data_query = """
    SELECT * FROM Tracks;
    """
    
    insert_query = """
    INSERT INTO Tracks (track_id, track_name) VALUES (?, ?)
    """
    
    cur = conn.cursor()
    with conn:
        
    # grab current data
        current_data = execute_sql_query(get_current_data_query, conn)
        current_data_set = set(current_data)
        data_set = set(data)
        new_data = data_set - current_data_set
        new_rows = list(new_data)
    # to insert data
        cur.executemany(insert_query, new_rows)
        conn.commit()


def insert_albums(data, conn):
    get_current_data_query = """
    SELECT * FROM Albums;
    """
    
    insert_query = """
    INSERT INTO Albums (album_id, album_name) VALUES (?, ?)
    """
    
    cur = conn.cursor()
    with conn:
        
    # grab current data
        current_data = execute_sql_query(get_current_data_query, conn)
        current_data_set = set(current_data)
        data_set = set(data)
        new_data = data_set - current_data_set
        new_rows = list(new_data)
    # to insert data
        cur.executemany(insert_query, new_rows)
        conn.commit()


def insert_artists(data, conn):
    get_current_data_query = """
    SELECT * FROM Artists;
    """
    
    insert_query = """
    INSERT INTO Artists (artist_id, artist_name) VALUES (?, ?)
    """
    
    cur = conn.cursor()
    with conn:
        
    # grab current data
        current_data = execute_sql_query(get_current_data_query, conn)
        current_data_set = set(current_data)
        data_set = set(data)
        new_data = data_set - current_data_set
        new_rows = list(new_data)
    # to insert data
        cur.executemany(insert_query, new_rows)
        conn.commit()