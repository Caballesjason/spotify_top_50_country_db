-- This query shows the number of countries charted for each track.
SELECT playlists.track_id
,playlists.track_name
,COUNT(playlists.name) AS num_countries
FROM playlists
	JOIN tracks ON
		playlists.track_id=tracks.track_id
GROUP BY (playlists.track_id,playlists.track_name)
ORDER BY num_countries DESC
