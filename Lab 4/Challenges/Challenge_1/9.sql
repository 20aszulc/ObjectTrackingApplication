--In 9.sql, write a SQL query find the average speechiness for each artist that have more than 3 songs
SELECT artist, speechiness FROM SONGS GROUP BY artist having COUNT(SongName) > 3;