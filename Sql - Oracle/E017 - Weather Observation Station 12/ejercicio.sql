-- >>> Weather Observation Station 12
-- >>> https://www.hackerrank.com/challenges/weather-observation-station-12/problem

SELECT DISTINCT CITY FROM STATION 
WHERE LOWER(SUBSTR(CITY, 0, 1)) NOT IN ('a', 'e', 'i', 'o', 'u') 
AND LOWER(SUBSTR(CITY, LENGTH(CITY), 1)) NOT IN ('a', 'e', 'i', 'o', 'u');