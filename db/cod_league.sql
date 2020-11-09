DROP TABLE leagues;
DROP TABLE matches;
DROP TABLE teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255),
    name VARCHAR(255),
    points INT
    league_id INT REFERENCES leagues(id) ON DELETE CASCADE,
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY
);

CREATE TABLE leagues (
    id SERIAL PRIMARY KEY,
    year VARCHAR(255)
    -- team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    -- match_id INT REFERENCES matches(id) ON DELETE CASCADE
);