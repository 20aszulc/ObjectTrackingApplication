--write a SQL query to find the total number of songs that have a tempo greater than the average tempo for all songs.
SELECT COUNT(SongNames) FROM Songs
    WHERE tempo > (
    SELECT AVG(energy)
    FROM Songs
);
