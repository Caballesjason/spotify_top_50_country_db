-- AlbumArtists Schema --
CREATE TABLE AlbumArtists(
    album_id VARHCAR(32)
    ,artist_id VARCHAR(32)
    ,FOREIGN KEY (album_id) REFERENCES Albums(album_id)
    ,FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
);

-- Albums Schema -- 
	CREATE TABLE Albums(
	album_id VARCHAR(32)
	,album_name VARCHAR(32)
	,total_tracks INTEGER
	,date_released DATE
	,PRIMARY KEY (album_id)
);

-- Artists Schema -- 
CREATE TABLE Artists(
    artist_id VARCHAR(32)
    ,artist_name VARCHAR(32)
    ,nbr_of_followers INTEGER
    ,popularity INTEGER
    ,PRIMARY KEY (artist_id)
);

-- GenreArtists Schema --
CREATE TABLE GenreArtists(
    artist_id VARCHAR(32)
    ,genre VARCHAR(32)
    ,FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
);

-- KeySignatures Schema --
CREATE TABLE KeySignatures(
    key_id INTEGER
    ,key_signature varchar(32)
    ,PRIMARY KEY (key_id)
);

-- MarketCodes Schema --
CREATE TABLE MarketCodes(
    country_code CHAR(2)
    ,country VARCHAR(32)
    ,PRIMARY KEY (country_code)
);

-- Playlists Schema --
CREATE TABLE Playlists(
	[name] VARCHAR(32)
	,track_id VARCHAR(32)
	,track_name VARCHAR(32)
	,album_id VARCHAR(32)
	,album_name VARCHAR(32)
	,FOREIGN KEY (track_id) REFERENCES Tracks(track_id)
	,FOREIGN KEY (album_id) REFERENCES Albums(album_id)
);

-- TrackArtists Schema --
CREATE TABLE TrackArtists(
    track_id VARHCAR(32)
    ,artist_id VARCHAR(32)
    ,FOREIGN KEY (track_id) REFERENCES Tracks(track_id)
    ,FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
);

-- TrackAvailableMarkets Schema --
CREATE TABLE TrackAvailableMarkets(
    track_id VARHCAR(32)
    ,country_code VARCHAR(32)
    ,FOREIGN KEY (track_id) REFERENCES Tracks(track_id)
    ,FOREIGN KEY (country_code) REFERENCES MarketCodes(country_code)
);

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