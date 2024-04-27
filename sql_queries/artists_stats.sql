-- Grab artist name, follower count, popularity, album count, track count, genre count
WITH genres AS(
	SELECT DISTINCT
	artist_id
	, COUNT(genre) OVER (partition by artist_id) AS genre_count
	FROM genreartists
),

albums AS(
SELECT DISTINCT
artist_id
,COUNT(album_id) OVER (partition by artist_id) AS album_count FROM albumartists
),

tracks AS(
SELECT DISTINCT
artist_id
,COUNT(track_id) OVER (partition by artist_id) AS track_count FROM trackartists
)

SELECT artists.*
	,album_count
	,track_count
	,genre_count
FROM ARTISTS
JOIN albums ON albums.artist_id = artists.artist_id
JOIN tracks ON tracks.artist_id = artists.artist_id
JOIN genres ON genres.artist_id = artists.artist_id
ORDER BY track_count DESC