-- Lists all the shows contained in the database hbtn_0d_tvshows without a genre linked

SELECT title, genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows
ON  id = show_id
WHERE show_id IS NULL
ORDER BY title, genre_id;
