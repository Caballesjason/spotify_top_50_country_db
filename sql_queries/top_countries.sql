-- This query shows the number of countries charted for each track.
select playlists.track_id,playlists.track_name,count(playlists.name) as num_countries from playlists join tracks on playlists.track_id=tracks.track_id
group by (playlists.track_id,playlists.track_name) order by num_countries desc
