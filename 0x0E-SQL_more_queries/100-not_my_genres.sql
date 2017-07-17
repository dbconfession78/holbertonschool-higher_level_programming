-- uses selected db to list all genres not linke to the show 'Dexter'
-- 1. first get the genre id's related to 'Dexter'
-- 2. then get the genre names related to all genres NOT in 1.


-- 2.
SELECT DISTINCT tv_genres.`name`
FROM tv_genres
JOIN tv_show_genres ON tv_genres.`id` = tv_show_genres.`genre_id`
WHERE tv_genres.`id` NOT IN (

	  -- 1.
	  SELECT DISTINCT tv_genres.`id`
	  FROM tv_genres
	  JOIN tv_show_genres ON tv_genres.`id` = tv_show_genres.`genre_id`
	  JOIN tv_shows ON tv_show_genres.`show_id` = tv_shows.`id`
	  WHERE tv_shows.`title` = 'Dexter'
)
ORDER BY tv_genres.`name` ASC
;
