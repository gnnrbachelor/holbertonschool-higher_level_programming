-- Lists all genres from hbtn_0d_tvshows and displays the number linked

SELECT tv_genres.name AS genre,
COUNT(tv_show_genres.show_id) AS total_number
FROM tv_genres
JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY total_number;
