-- lists all genres from selected db and displays the number of shows linked to each
File Edit Options Buffers Tools SQL Help
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_sho\
ws
FROM tv_genres JOIN tv_show_genres
WHERE tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_shows DESC;
