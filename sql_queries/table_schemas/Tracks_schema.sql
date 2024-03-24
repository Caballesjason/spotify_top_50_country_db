-- Tracks Schema --
CREATE TABLE Tracks(
	track_id VARCHAR(32)
	,track_name VARCHAR(32)
	,album_id VARCHAR(32)
	,duration_ms INTEGER
	,[explicit] BOOLEAN
	,current_popularity INTEGER
	,acousticness FLOAT
	,danceability FLOAT
	,instrumentalness FLOAT
	,key_signature INTEGER
	,mode CHAR(5)
	,tempo FLOAT
	,time_signature FLOAT
	,valence FLOAT
	,PRIMARY KEY  (track_id)
	,FOREIGN KEY  (album_id) REFERENCES Albums(album_id)
	,FOREIGN KEY (key_signature) REFERENCES KeySignatures(key_id)
);