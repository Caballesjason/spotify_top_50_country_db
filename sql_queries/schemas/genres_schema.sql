-- GENRES TABLE SCHEMA --
CREATE TABLE Genres(
    track_id VARCHAR(32)
    ,genre VARCHAR(32)
    ,FOREIGN KEY (track_id) REFERENCES Tracks(track_id)
);