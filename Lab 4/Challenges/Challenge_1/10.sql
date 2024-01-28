--write a SQL query that lists songs that feature other artists.
SELECT SongName FROM Songs WHERE  SongName LIKE '%feat%'