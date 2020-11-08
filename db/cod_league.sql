DROP TABLE league;
DROP TABLE matches;
DROP TABLE teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255),
    name VARCHAR(255),
    points INT
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY
);

CREATE TABLE league (
    id SERIAL PRIMARY KEY,
    team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    match_id INT REFERENCES matches(id) ON DELETE CASCADE
);