-- Find all available tracks in the United States
SELECT Tracks.* 
FROM Tracks
JOIN trackavailablemarkets AS markets
	ON markets.track_id = Tracks.track_id
WHERE markets.country_code =  (
	SELECT country_code
	FROM marketcodes
	WHERE country =  'United States of America'
)
ORDER BY Tracks.track_id;
