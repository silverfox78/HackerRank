-- >>> Higher Than 75 Marks
-- >>> https://www.hackerrank.com/challenges/more-than-75-marks/problem

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT NAME, row_number() over (partition by ID order by NAME, ID) as rn, LOWER(SUBSTR(NAME, LENGTH(NAME) - 2, 3))
FROM STUDENTS
WHERE MARKS > 75
/*AND LOWER(SUBSTR(NAME, LENGTH(NAME) - 3, 3)) IN (SELECT DISTINCT LOWER(SUBSTR(NAME, LENGTH(NAME) - 3, 3)) FROM STUDENTS)*/
ORDER BY LOWER(SUBSTR(NAME, LENGTH(NAME) - 2, 3)), ID;


https://dba.stackexchange.com/questions/6368/how-to-select-the-first-row-of-each-group

https://asktom.oracle.com/pls/apex/asktom.search?tag=howto-select-first-value-in-a-group-by-bunch-of-rows