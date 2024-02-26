-- TRACKS TABLE SCHEMA --
CREATE TABLE Tracks(
	track_id VARCHAR(32)
	,track_name VARCHAR(32)
	,album_id VARCHAR(32)
	,genre VARCHAR(32)
	,duration_ms INTEGER
	,explicit BOOLEAN
	,PRIMARY KEY  (track_id)
	,FOREIGN KEY  (album_id) REFERENCES Albums(album_id)
	,foremgin key (genre) REFERENCES Genres(genre)
);