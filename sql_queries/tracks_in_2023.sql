-- Find all tracks created in 2023
SELECT *
FROM tracks
JOIN albums
	ON tracks.album_id=albums.album_id
WHERE LEFT(ALBUMS.date_released, 4) = '2023'

