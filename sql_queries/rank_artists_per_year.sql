-- ranks artists for every year

select artist_name, year,popularity, rank() over (partition by year order by popularity desc) popularity_rank from
(select *, SUBSTRING(date_released, 1, POSITION('-' IN date_released) - 1) year from AlbumArtists join Albums on AlbumArtists.album_id=Albums.album_id join Artists on AlbumArtists.artist_id=Artists.artist_id group by artist_name,year) as album_join_artist