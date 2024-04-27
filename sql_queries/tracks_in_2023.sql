select *
from tracks
join albums
	on tracks.album_id=albums.album_id
where SUBSTRING(ALBUMS.date_released, 1, POSITION('-' IN 'YYYY-MM-DD') - 1)= '2023'