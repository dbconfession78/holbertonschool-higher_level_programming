-- creates a table 'second_table' in the selected db and adds multiple rows
CREATE TABLE IF NOT EXISTS second_table (id INT, name V\
ARCHAR(256), score INT);
INSERT INTO second_table (id, name, score) values (1, '\
John', 10);
INSERT INTO second_table (id, name, score) values (2, '\
Alex', 3);
INSERT INTO second_table (id, name, score) values (3, '\
Bob', 14);
INSERT INTO second_table (id, name, score) values (4, '\
George', 8);