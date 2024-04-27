-- selects the most popular album artist per year

select artist_name,album_name,max(popularity),SUBSTRING(date_released, 1, 
POSITION('-' IN date_released) - 1) year from 
(select * from AlbumArtists join Albums on 
AlbumArtists.album_id=Albums.album_id join Artists on 
AlbumArtists.artist_id=Artists.artist_id)  album_join_artist
group by year
