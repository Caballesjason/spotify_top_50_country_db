-- This data was used to pull information on tracks and what countries they are popular in for a project on Clustering!
WITH count_track_nbr_of_countries AS(
    SELECT DISTINCT
	track_id
    ,COUNT(name)  AS num_countries
    FROM Playlists
    GROUP BY track_id
    )
SELECT  
	Playlists.name
	,count_track_nbr_of_countries.num_countries
	,Tracks.*
FROM Playlists
JOIN Tracks
	ON Tracks.track_id = Playlists.track_id
JOIN count_track_nbr_of_countries
	ON count_track_nbr_of_countries.track_id =  Playlists.track_id;