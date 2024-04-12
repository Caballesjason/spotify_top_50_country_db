import utility_functions as uf
from get_spotify_client import get_spotify_obj
import data_pull_functions as dp
import sqlite3
import insert_data as id
import time
from random import randint

if __name__ == "__main__":
    print('\nhi im running :D\n')
# Remove all data
    tables = ["AlbumArtists", "Albums", "Artists", "GenreArtists", "KeySignatures",
            "MarketCodes", "Playlists", "TrackArtists", "Tracks"]
    
# Connect to db
    conn = uf.create_connection("SpotifyData.db")
    cur = conn.cursor()

# Drop data from tables in table list
    with conn:
        for table in tables:
            delete_data_from_tables_query = f"DELETE from {table};"
            cur.execute(delete_data_from_tables_query)

# Get Spotify Object
    sp = get_spotify_obj()
    AlbumArtists_data_master = []
    Albums_data_master = []
    Artists_data_master = []
    GenreArtists_data_master = []
    Playlists_data_master = []
    TrackArtists_data_master = []
    Tracks_data_master = []
    line_counter = 0
    with open('countries_top_fifty.txt', "r") as file:
        for line in file:
            row_split = line.strip("").split(",")
            link = row_split[1]
            print(row_split[0])

            playlist_raw_data = dp.get_playlist_data(sp, link)
            print('checkpoint 1')

            AlbumArtists_data = dp.get_AlbumArtists_table_data(playlist_raw_data)
            AlbumArtists_data_master += AlbumArtists_data
            print('checkpoint 2')

            Albums_data = dp.get_Albums_table_data(playlist_raw_data)
            Albums_data_master += Albums_data
            print('checkpoint 3')
    

            Artists_data = dp.get_Artists_table_data(sp, playlist_raw_data)
            Artists_data_master += Artists_data
            print('checkpoint 4')

            GenreArtists_data = dp.get_GenreArtists_table_data(sp, playlist_raw_data)
            GenreArtists_data_master += GenreArtists_data
            print('checkpoint 5')

            Playlists_data = dp.get_playlist_table_data(playlist_raw_data)
            Playlists_data_master += Playlists_data
            print('checkpoint 6')

            TrackArtists_data = dp.get_TrackArtists_table_data(playlist_raw_data)
            TrackArtists_data_master += TrackArtists_data
            print('checkpoint 7')

            time.sleep(5)
            Tracks_data = dp.get_tracks_table_data(sp, playlist_raw_data)
            Tracks_data_master += Tracks_data
            print('checkpoint 8')
            line_counter += 1

            # if line_counter == 2:
            #      break
            
                
    AlbumArtists_data_master = list(set(AlbumArtists_data_master))
    Albums_data_master = list(set(Albums_data_master))
    Artists_data_master = list(set(Artists_data_master))
    GenreArtists_data_master = list(set(GenreArtists_data_master))
    Playlists_data_master = list(set(Playlists_data_master))
    TrackArtists_data_master = list(set(TrackArtists_data_master))
    Tracks_data_master = list(set(Tracks_data_master))
    id.AlbumArtists_insert(AlbumArtists_data_master, conn)
    id.Albums_insert(Albums_data_master, conn)
    id.Artists_insert(Artists_data_master, conn)
    id.GenreArtists_insert(GenreArtists_data_master, conn)
    id.Playlists_insert(Playlists_data_master, conn)
    id.TrackArtists_insert(TrackArtists_data_master, conn)
    id.Tracks_insert(Tracks_data_master, conn)

    print("\n Hi I finished running :p\n")


