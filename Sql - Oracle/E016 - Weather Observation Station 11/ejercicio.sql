-- >>> Weather Observation Station 11
-- >>> https://www.hackerrank.com/challenges/weather-observation-station-11/problem

SELECT DISTINCT CITY FROM STATION 
WHERE LOWER(SUBSTR(CITY, 0, 1)) NOT IN ('a', 'e', 'i', 'o', 'u') 
OR LOWER(SUBSTR(CITY, LENGTH(CITY), 1)) NOT IN ('a', 'e', 'i', 'o', 'u');