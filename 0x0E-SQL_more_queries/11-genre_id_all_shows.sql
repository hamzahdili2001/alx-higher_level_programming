-- lists all the shows contained in the database hbtn_0d_tvshows that have at least one genre linked

SELECT title, genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows
ON  id = show_id
ORDER BY title, genre_id;
