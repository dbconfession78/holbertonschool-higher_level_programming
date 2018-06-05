-- 2. then get all the show titles related to all genre id's NOTin 1.
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN (

-- 1. first get all shows with the genre id for Comedy
SELECT tv_shows.title
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = 'Comedy'
)
ORDER by tv_shows.title ASC
;
