-- ALBUMS TABLE SCHEMA -- 
	CREATE TABLE Albums(
	album_id VARCHAR(32)
	,album_name VARCHAR(32)
	,label VARCHAR(64)
	,total_tracks INTEGER
	,date_released DATE
	,PRIMARY KEY (album_id)
	,FOREIGN KEY (label) REFERENCES labels(label)
);