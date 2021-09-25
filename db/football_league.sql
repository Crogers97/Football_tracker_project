DROP TABLE IF EXISTS fixture;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    points INT
);

CREATE TABLE fixture (
    id SERIAL PRIMARY KEY,
    home_team VARCHAR(255),
    away_team VARCHAR(255),
    result INT
);
