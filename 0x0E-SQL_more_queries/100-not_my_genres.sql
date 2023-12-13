-- Uses the hbtn_0d_tvshows database to list all genres NOT linked to that show 'Dexter'

SELECT name
FROM tv_genres
WHERE name NOT IN (
	SELECT name FROM tv_genres
	JOIN tv_show_genres ON tv_genres.id = genre_id
	JOIN tv_shows ON show_id = tv_shows.id
	WHERE title = 'Dexter'
)
ORDER BY name ASC;
