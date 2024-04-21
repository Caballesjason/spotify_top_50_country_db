-- This query is used to find artists with minimum number of followers in each genre.
select genre,min(nbr_of_followers) 
	  as min_followers from genreartists 
	  natural join artists 
	  group by genre
