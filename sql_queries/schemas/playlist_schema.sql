-- PLAYLIST TABLE SCHEMA --
CREATE TABLE Playlist(
	track_id VARCHAR(32)
	,track_name VARCHAR(32)
	,album_id VARCHAR(32)
	,album_name VARCHAR(32)
	,date_loaded DATE
	,FOREIGN KEY (track_id) REFERENCES Tracks(track_id)
	,FOREIGN KEY (album_id) REFERENCES Albums(album_id)
)
