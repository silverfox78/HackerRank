-- >>> Weather Observation Station 6
-- >>> https://www.hackerrank.com/challenges/weather-observation-station-6/problem

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT DISTINCT CITY FROM STATION WHERE LOWER(SUBSTR(CITY, 0, 1)) IN ('a', 'e', 'i', 'o', 'u');