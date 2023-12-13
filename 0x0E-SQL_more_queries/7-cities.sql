-- Creates A database, hbtn_0d_usa & a table (on created database), cities on your MySQL server

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create a table, cities, in the hbtn_0d_usa database
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(state_id)
		REFERENCES states(id)
);
