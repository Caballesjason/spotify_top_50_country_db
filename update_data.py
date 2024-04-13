import utility_functions as uf
from get_spotify_client import get_spotify_obj
import data_pull_functions as dp
import sqlite3
import insert_data as id
import time
from random import randint

if __name__ == "__main__":
    print('\n---- BEGIN DATA LOAD ----\n')
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
# Initialize lists for to populate data from Spotify API
    AlbumArtists_data_master = []
    Albums_data_master = []
    Artists_data_master = []
    GenreArtists_data_master = []
    Playlists_data_master = []
    TrackArtists_data_master = []
    TrackAvailableMarkets_data_master = []
    Tracks_data_master = []

# Read each "Top 50 - COUNTRY"  Playlist and append its data to the correspending master playlists
    with open('countries_top_fifty.txt', "r") as file:
        for line in file:
            row_split = line.strip("").split(",")
            playlist_url = row_split[1]
            country = row_split[0]
            print(f"---- Top 50 - {country} Data Load -----\n")

        # Grab raw data from playlist
            playlist_raw_data = dp.get_playlist_data(sp, playlist_url)
            print('Successfully loaded raw playist data')

        # Grabbing AlbumArtists data
            AlbumArtists_data = dp.get_AlbumArtists_table_data(playlist_raw_data)
            AlbumArtists_data_master += AlbumArtists_data
            print('Successfully loaded AlbumArtists data')

        # Grabbing Albums data
            Albums_data = dp.get_Albums_table_data(playlist_raw_data)
            Albums_data_master += Albums_data
            print('Successfully loaded Albums data')
    
        #  Grabbing Artists data
            Artists_data = dp.get_Artists_table_data(sp, playlist_raw_data)
            Artists_data_master += Artists_data
            print('Successfully loaded Artists data')

        # Grabbing GenreArtists data
            GenreArtists_data = dp.get_GenreArtists_table_data(sp, playlist_raw_data)
            GenreArtists_data_master += GenreArtists_data
            print('Successfully loaded GenreArtists data')

        # Grabbing Playlists data
            Playlists_data = dp.get_playlist_table_data(playlist_raw_data)
            Playlists_data_master += Playlists_data
            print('Successfully loaded Playlists data')

        # Grabbing TrackArtists data
            TrackArtists_data = dp.get_TrackArtists_table_data(playlist_raw_data)
            TrackArtists_data_master += TrackArtists_data
            print('Successfully loaded TrackArtists data')

        # Grabbing TrackAvailableMarkets data
            TrackAvailableMarkets_data = dp.get_TrackAvailableMarkets_table_data(playlist_raw_data)
            TrackAvailableMarkets_data_master += TrackAvailableMarkets_data
            print('Successfully loaded TrackAvailableMarkets data')


        # Grabbing Tracks data
            time.sleep(5)
            Tracks_data = dp.get_tracks_table_data(sp, playlist_raw_data)
            Tracks_data_master += Tracks_data
            print('Successfully loaded Tracks data\n\n')

#  These are required to be ensure unqiueness of repetitive data
    AlbumArtists_data_master = list(set( AlbumArtists_data_master))
    GenreArtists_data_master = list(set(GenreArtists_data_master))
    Albums_data_master = list(set(Albums_data_master))
    Artists_data_master = list(set(Artists_data_master))
    Tracks_data_master = list(set(Tracks_data_master))
    Playlists_data_master = list(set(Playlists_data_master))
    TrackArtists_data_master = list(set(TrackArtists_data_master))
    TrackAvaliableMarkets_insert = list(set(TrackAvailableMarkets_data_master))
# Upload all data to their tables
    id.AlbumArtists_insert(AlbumArtists_data_master, conn)
    id.Albums_insert(Albums_data_master, conn)
    id.Artists_insert(Artists_data_master, conn)
    id.GenreArtists_insert(GenreArtists_data_master, conn)
    id.Playlists_insert(Playlists_data_master, conn)
    id.TrackArtists_insert(TrackArtists_data_master, conn)
    id.Tracks_insert(Tracks_data_master, conn)
    id.TrackAvaliableMarkets_insert(TrackAvailableMarkets_data_master, conn)

    print("\n---- DATA SUCCESSFULLY LOADED ----\n")


