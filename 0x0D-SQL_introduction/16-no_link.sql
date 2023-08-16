--  script to lists all records in second_table with name not null
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
