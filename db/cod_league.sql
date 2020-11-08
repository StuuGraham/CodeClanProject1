DROP TABLE league;
DROP TABLE games;
DROP TABLE teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255),
    name VARCHAR(255),
    points INT
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
);

CREATE TABLE league (
    id SERIAL PRIMARY KEY,
    team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    game_id INT REFERENCES games(id) ON DELETE CASCADE
);