Click [here](https://dbdiagram.io/d/65dbdc3f5cd0412774c6ba17) and upload the below text to get the E/L diagram!


```
// [A] - Atomic value in spotify API
// [NA] - Non-Atomic value in spotify API
Table Playlists {
    name VARCHAR(32) // playlist.name [A]
    track_id VARCHAR(32) // playlist.tracks.items.track.id [A]
    track_name VARCHAR(32) // playlist.tracks.items.track.name [A]
    album_id VARCHAR(32) // playlist.tracks.items.track.album.id [A]
    album_name VARCHAR(32) // playlist.tracks.items.track.album.name [A]
}

Table Tracks {
    track_id VARCHAR(32) [PRIMARY KEY] // playlist.tracks.items.track.id [A]
    track_name VARCHAR(32) // playlist.tracks.items.track.name [A]
    album_id VARCHAR(32) // playlist.tracks.items.track.album.id [A]
    duration_ms INTEGER // playlist.tracks.items.track.duration_ms [A]
    explicit BOOLEAN // playlist.tracks.items.track.explicit [A]
    current_popularity INTEGER // playlist.tracks.items.track.popularity [A]
    acousticness FLOAT // audio_features.acousticness [A]
    danceability FLOAT // audio_features.danceability [A]
    instrumentalness FLOAT // audio_features.instrumental [A]
    key_signature INTEGER // audio_features.key [A]
    mode CHAR(5) // audio_features.mode [A]
    tempo FLOAT // audio_features.tempo [A]
    time_signature FLOAT // audio_features.time_signature [A]
    valence FLOAT // audio_features.valence [A]
}

Table Albums {
    album_id VARCHAR(32) [PRIMARY KEY]  // playlist.tracks.items.track.album.id [A]
    album_name VARCHAR(32)  // playlist.tracks.items.track.album.name [A]
    total_tracks INTEGER // playlist.tracks.items.track.album.total_tracks [A]
    date_released DATE // YYYY-MM playlist.tracks.items.track.album.release_date [A]

}


Table Artists {
  artist_id VARCHAR(32) [PRIMARY KEY] // playlist.tracks.items.track.artists.id [A]
  artist_name VARCHAR(32) // playlist.tracks.items.track.artists.name [A]
  nbr_of_followers INTEGER // playlist.tracks.items.track.artists.followers.total [A]
  popularity INTEGER // playlist.tracks.items.track.artists.popularity [A]
}

Table TrackArtists {
  track_id VARHCAR(32) // playlist.tracks.items.track.id [A]
  artist_id VARCHAR(32) // playlist.tracks.items.track.artists.id [NA]
}

Table AlbumArtists {
  album_id VARHCAR(32) // playlist.tracks.items.track.album.id [A]
  artist_id VARCHAR(32) // playlist.tracks.items.track.album.artists [A]
}

Table GenresArtists {
 artist_id VARCHAR(32) // playlist.tracks.items.track.album.artists [A]
 genre VARCHAR(32) // playlist.tracks.items.track.album.genres [NA]
}

Table TrackAvailableMarkets {
  track_id VARCHAR(32) // playlist.tracks.items.track.id [A]
  country_code CHAR(2) // playlist.tracks.items.track.available_markets [NA]
}

Table MarketCodes {
  country_code CHAR(2) [PRIMARY KEY] // wikipedia (see spotify API)
  country VARCHAR(32) // wikipedia (see spotify API)
}

Table KeySignatures {
  key_id INTEGER [PRIMARY KEY] // audio_features.key [A]
  key_signature VARCHAR(32) // audio_features.key [A]
}

Ref: Playlists.track_id > Tracks.track_id
Ref: Playlists.album_id > Albums.album_id

Ref: Tracks.album_id > Albums.album_id
Ref: Tracks.key_signature > KeySignatures.key_id

Ref: TrackArtists.track_id > Tracks.track_id
Ref: TrackArtists.artist_id > Artists.artist_id

Ref: AlbumArtists.album_id > Albums.album_id
Ref: AlbumArtists.artist_id > Artists.artist_id

ref: TrackAvailableMarkets.track_id > Tracks.track_id
ref: TrackAvailableMarkets.country_code > MarketCodes.country_code

ref: GenresArtists.artist_id > Artists.artist_id
```