--  that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

SELECT city, AVG(value) AS avg_temp FROM temperature GROUP BY CITY ORDER BY avg_temp DESC;
