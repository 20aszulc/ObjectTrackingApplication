-- write a SQL query that lists the names of any songs that have danceability, and energy less than 0.6.
SELECT * FROM Songs WHERE danceability < 0.6 AND energy < 0.6;