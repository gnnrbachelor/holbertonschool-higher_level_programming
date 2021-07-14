-- Uses the hbtn_0d_tvshows database to list all genres of Dexter

SELECT tv_genres.name
FROM tv_show_genres
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
