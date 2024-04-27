-- ranks artists for every year
SELECT DISTINCT artist_name, 
	year,
	popularity,
	DENSE_RANK() OVER(PARTITION BY YEAR ORDER BY popularity DESC) AS popularity_rank
FROM (SELECT *
	  ,LEFT(ALBUMS.date_released, 4) AS year
	  FROM AlbumArtists
	  JOIN Albums ON AlbumArtists.album_id=Albums.album_id
	  JOIN Artists ON AlbumArtists.artist_id=Artists.artist_id
	  ) AS album_join_artist
ORDER BY YEAR DESC, popularity_RANK