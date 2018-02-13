-- >>> Weather Observation Station 5
-- >>> https://www.hackerrank.com/challenges/weather-observation-station-5/problem

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT CITY, LENGTH(CITY) LEN FROM 
(SELECT CITY FROM STATION
WHERE LENGTH(CITY) = (SELECT MIN(LENGTH(CITY)) FROM STATION)
ORDER BY CITY)
WHERE ROWNUM = 1
UNION
SELECT CITY, LENGTH(CITY) LEN FROM 
(SELECT CITY FROM STATION
WHERE LENGTH(CITY) = (SELECT MAX(LENGTH(CITY)) FROM STATION)
ORDER BY CITY)
WHERE ROWNUM = 1;



SELECT CITY,LENGTH_CITY FROM (SELECT A.*, ROWNUM R FROM (SELECT LENGTH(CITY) LENGTH_CITY,CITY FROM STATION ORDER BY LENGTH_CITY, CITY) A) WHERE R IN (1,(SELECT COUNT(*) FROM STATION));