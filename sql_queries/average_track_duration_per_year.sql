-- Find the average duration of tracks for each year
WITH get_releases AS (
SELECT tracks.*
	,albums.date_released
FROM tracks JOIN albums
	ON albums.album_id = tracks.album_id
)

SELECT LEFT(date_released, 4) AS year_released
	,ROUND(AVG(duration_ms), 2) AS avg_track_duration_ms
FROM get_releases
GROUP BY LEFT(date_released, 4)
ORDER BY LEFT(date_released, 4);