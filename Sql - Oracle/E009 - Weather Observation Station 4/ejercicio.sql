-- >>> Weather Observation Station 4
-- >>> https://www.hackerrank.com/challenges/weather-observation-station-4/problem

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT TOTAL.SUMA - DISTINTOS.SUMA FROM (SELECT COUNT(CITY) SUMA FROM STATION) TOTAL, (SELECT COUNT (DISTINCT CITY) SUMA FROM STATION) DISTINTOS;