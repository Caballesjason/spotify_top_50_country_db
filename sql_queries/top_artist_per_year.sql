-- selects the most popular artist for an album for every year
WITH data AS(
SELECT AA.ALBUM_ID
	,AA.artist_id
	,artists.artist_name
	,albums.album_name
	,CAST(LEFT(albums.date_released, 4) AS INT) AS year_released
	,artists.popularity
	,MAX(Artists.popularity) OVER (PARTITION BY aa.album_id) AS max_popularity_in_album
FROM albumartists AS AA
	JOIN Albums ON AA.album_id=Albums.album_id
	JOIN Artists ON AA.artist_id=Artists.artist_id
)
SELECT DISTINCT album_name
	,artist_name
	,popularity
	,year_released
FROM data
WHERE popularity = max_popularity_in_album
ORDER BY year_released DESC, album_name;