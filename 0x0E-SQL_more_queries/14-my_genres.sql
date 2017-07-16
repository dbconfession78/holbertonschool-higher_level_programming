-- uses selected db to list all genres of the show Dexter
SELECT DISTINCT tv_genres.`name`
FROM tv_show_genres
INNER JOIN tv_genres ON tv_genres.`id` = tv_show_genres.`genre_id`
INNER JOIN tv_shows ON tv_show_genres.`show_id` = tv_shows.`id`
WHERE tv_shows.`title` = 'Dexter'
ORDER BY tv_genres.`name` ASC;
