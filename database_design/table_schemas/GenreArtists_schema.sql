-- GenreArtists Schema --
CREATE TABLE GenreArtists(
    artist_id VARCHAR(32)
    ,genre VARCHAR(32)
    ,FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
);