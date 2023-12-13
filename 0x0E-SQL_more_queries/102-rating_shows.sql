-- Uses the hbtn_0d_tvshows_rate database to list all tv shows by their rating (sum)

SELECT title, SUM(rate) AS rating
FROM tv_shows
JOIN tv_show_ratings
ON id = show_id
GROUP BY show_id
ORDER BY rating DESC;
