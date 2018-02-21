-- >>> Weather Observation Station 8
-- >>> https://www.hackerrank.com/challenges/weather-observation-station-8/problem

SELECT DISTINCT CITY FROM STATION 
WHERE LOWER(SUBSTR(CITY, 0, 1)) IN ('a', 'e', 'i', 'o', 'u') 
AND LOWER(SUBSTR(CITY, LENGTH(CITY), 1)) IN ('a', 'e', 'i', 'o', 'u');