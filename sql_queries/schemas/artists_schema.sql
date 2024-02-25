-- ARTISTS TABLE SCHEMA -- 
CREATE TABLE Artists(
    artist_id VARCHAR(32)
    ,artist_name VARCHAR(32)
    ,nbr_of_followers INTEGER
    ,popularity INTEGER
    ,PRIMARY KEY (artist_id)
);