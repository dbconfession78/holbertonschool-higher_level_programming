-- lists all shows contained in selected db
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

-- This can also be done with 'WHERE' instead of 'JOIN'
-- SELECT tv_shows.title, tv_show_genres.genre_id
-- FROM tv_shows, tv_show_genres
-- WHERE tv_shows.id = tv_show_genres.show_id
-- ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
