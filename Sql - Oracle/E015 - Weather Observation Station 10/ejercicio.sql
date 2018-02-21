-- >>> Weather Observation Station 10
-- >>> https://www.hackerrank.com/challenges/weather-observation-station-10/problem

SELECT DISTINCT CITY FROM STATION 
WHERE LOWER(SUBSTR(CITY, LENGTH(CITY), 1)) NOT IN ('a', 'e', 'i', 'o', 'u');