-- lists all genres from selected db and displays the number of shows linked to each
SELECT tv_genres.`name` as 'genre', COUNT(tv_show_genres.genre_id) AS 'numbe\
r_shows'
FROM tv_genres
INNER JOIN `tv_show_genres` ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY 2 DESC;
