-- AlbumArtists Schema --
CREATE TABLE AlbumArtists(
    album_id VARHCAR(32)
    ,artist_id VARCHAR(32)
    ,FOREIGN KEY (album_id) REFERENCES Tracks(album_id)
    ,FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
);