-- This query is used to find artists with minimum number of followers in each genre.
SELECT genre
	,MIN(nbr_of_followers) AS min_followers
FROM genreartists 
NATURAL JOIN artists 
GROUP BY genre
