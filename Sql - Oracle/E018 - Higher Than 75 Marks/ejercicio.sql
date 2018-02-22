-- >>> Higher Than 75 Marks
-- >>> https://www.hackerrank.com/challenges/more-than-75-marks/problem

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT NAME
FROM STUDENTS
WHERE MARKS > 75
AND LOWER(SUBSTR(TRIM(NAME), LENGTH(TRIM(NAME)) - 2, 3)) IN 
(SELECT LOWER(SUBSTR(TRIM(NAME), LENGTH(TRIM(NAME)) - 2, 3)) AS NAME
FROM STUDENTS
WHERE MARKS > 75
GROUP BY LOWER(SUBSTR(TRIM(NAME), LENGTH(TRIM(NAME)) - 2, 3)))
ORDER BY LOWER(SUBSTR(TRIM(NAME), LENGTH(TRIM(NAME)) - 2, 3)), ID;