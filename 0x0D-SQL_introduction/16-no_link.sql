-- script that lists all records of second_table of database hbtn_0c_0
-- listing all rows with non null name
SELECT score, name
FROM second_table
WHERE name IS NOT null
ORDER BY score DESC;
