-- Albums Schema -- 
	CREATE TABLE Albums(
	album_id VARCHAR(32)
	,album_name VARCHAR(32)
	,total_tracks INTEGER
	,date_released DATE
	,PRIMARY KEY (album_id)
);