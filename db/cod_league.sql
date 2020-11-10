DROP TABLE matches;
DROP TABLE teams;
DROP TABLE leagues;

CREATE TABLE leagues (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    year VARCHAR(255)
);

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255),
    name VARCHAR(255),
    points INT,
    league_id INT REFERENCES leagues(id) ON DELETE CASCADE
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    team1_id INT REFERENCES teams(id) ON DELETE CASCADE,
    team2_id INT REFERENCES teams(id) ON DELETE CASCADE,
    league_id INT REFERENCES leagues(id) ON DELETE CASCADE,
    winner VARCHAR(255)
);