Click [here](https://dbdiagram.io/d/65dbdc3f5cd0412774c6ba17) and upload the below text to get the E/L diagram!

```
Table Playlist {
    track_id VARCHAR(32)
    track_name VARCHAR(32)
    album_id VARCHAR(32)
    album_name VARCHAR(32)
    date_loaded DATE
}

Table Tracks {
    track_id VARCHAR(32) [PRIMARY KEY]
    track_name VARCHAR(32)
    album_id VARCHAR(32)
    duration_ms INTEGER
    explicit BOOLEAN
}

Table Albums {
    album_id VARCHAR(32) [PRIMARY KEY]
    album_name VARCHAR(32)
    genre VARCHAR(32)
    label VARCHAR(64)
    total_tracks INTEGER
    date_released DATE

}
Table Genres {
  track_id VARCHAR(32)
  genre VARCHAR(32)
}

Table Labels {
  label VARCHAR(32) [PRIMARY KEY]
}
Table Artists {
  artist_id VARCHAR(32) [PRIMARY KEY]
  artist_name VARCHAR(32)
  nbr_of_followers INTEGER
  popularity INTEGER
}

Table TrackArtists {
  track_id VARHCAR(32)
  artist_id VARCHAR(32)
}

Table AlbumArtists {
  album_id VARHCAR(32)
  artist_id VARCHAR(32)
}

Ref: Playlist.track_id > Tracks.track_id
Ref: Playlist.album_id > Albums.album_id

Ref: Tracks.album_id > Albums.album_id

Ref: Genres.track_id > Tracks.track_id

Ref: Albums.label > Labels.label

Ref: TrackArtists.track_id > Tracks.track_id
Ref: TrackArtists.artist_id > Artists.artist_id

Ref: AlbumArtists.album_id > Albums.album_id
Ref: AlbumArtists.artist_id > Artists.artist_id
```
