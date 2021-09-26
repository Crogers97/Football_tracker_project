DROP TABLE IF EXISTS fixtures;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    points INT
);

CREATE TABLE fixtures (
    id SERIAL PRIMARY KEY,
    home_team VARCHAR(255),
    away_team VARCHAR(255),
    score VARCHAR(255),
    result VARCHAR(255)
);
