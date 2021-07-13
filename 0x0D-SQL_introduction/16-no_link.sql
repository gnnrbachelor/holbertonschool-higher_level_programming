-- Lists all records of second_table from hbtn_0c_0

SELECT score, name FROM second_table WHERE name !='' AND name IS NOT NULL
ORDER BY score DESC;
