import utility_functions as uf
from get_spotify_client import get_spotify_obj
import data_pull_functions as dp
import sqlite3
import insert_data as id
import time
from random import randint

if __name__ == "__main__":
    print('\nhi im running :D\n')
    try:
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

                playlist_raw_data = dp.get_playlist_data(sp, link)
                time.sleep(randint(1, 30))

                AlbumArtists_data = dp.get_AlbumArtists_table_data(playlist_raw_data)
                AlbumArtists_data_master += AlbumArtists_data
                time.sleep(randint(1, 30))

                Albums_data = dp.get_Albums_table_data(playlist_raw_data)
                Albums_data_master += Albums_data
                time.sleep(randint(1, 30))

                Artists_data = dp.get_Artists_table_data(sp, playlist_raw_data)
                Artists_data_master += Artists_data
                time.sleep(randint(1, 30))

                GenreArtists_data = dp.get_GenreArtists_table_data(sp, playlist_raw_data)
                GenreArtists_data_master += GenreArtists_data
                time.sleep(randint(1, 30))

                Playlists_data = dp.get_playlist_table_data(playlist_raw_data)
                Playlists_data_master += Playlists_data
                time.sleep(randint(1, 30))

                TrackArtists_data = dp.get_TrackArtists_table_data(playlist_raw_data)
                TrackArtists_data_master += TrackArtists_data
                time.sleep(randint(1, 30))

                Tracks_data = dp.get_tracks_table_data(sp, playlist_raw_data)
                Tracks_data_master += Tracks_data
                line_counter += 1
                # if line_counter == 7:
                #     break
                
                    

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
    except:
        print('\n something fucked up lmao\n')

    print("\n Hi I finished running :p\n")