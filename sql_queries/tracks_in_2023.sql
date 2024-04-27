<<<<<<< HEAD
<<<<<<< HEAD
select *
from tracks
join albums
	on tracks.album_id=albums.album_id
where SUBSTRING(ALBUMS.date_released, 1, POSITION('-' IN 'YYYY-MM-DD') - 1)= '2023'
=======
select artist_name,max(popularity) max_popularity,year,album_id from (select *,strftime('%Y', date_released) year from AlbumArtists join artists on AlbumArtists.artist_id=Artists.artist_id 
join Albums on AlbumArtists.album_id=Albums.album_id) album_join_artist group by year
>>>>>>> ce7c479 (add query)
=======
-- Find all tracks created in 2023
SELECT *
FROM tracks
JOIN albums
	ON tracks.album_id=albums.album_id
WHERE SUBSTRING(ALBUMS.date_released, 1, POSITION('-' IN 'YYYY-MM-DD') - 1)= '2023'
>>>>>>> 085c784 (- Added queries)
