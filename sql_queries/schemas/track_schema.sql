-- TRACKS TABLE SCHEMA --
CREATE TABLE Tracks(
	track_id VARCHAR(32)
	,track_name VARCHAR(32)
	,artist VARCHAR(32)
	,PRIMARY KEY  (track_id)
	,FOREIGN KEY  (artist) REFERENCES Artists(artist_id)
);

