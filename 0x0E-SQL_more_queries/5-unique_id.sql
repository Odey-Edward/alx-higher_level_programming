-- a script that creates the table unique_id on your MySQL server.
-- If the table unique_id already exists, your script should not fail
CREATE TABLE IF NOT EXISTS unique_id(
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
