-- TrackArtists SCHEMA --
CREATE TABLE TrackArtists(
    track_id VARHCAR(32)
    ,artist_id VARCHAR(32)
    ,FOREIGN KEY (track_id) REFERENCES Tracks(track_id)
    ,FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
);