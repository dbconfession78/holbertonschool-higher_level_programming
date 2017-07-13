-- lists number of records with same score in 'second_table' of the selected db
SELECT score, COUNT(*) as number FROM second_table GROUP BY score DESC;
