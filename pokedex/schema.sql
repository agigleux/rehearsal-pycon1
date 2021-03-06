DROP TABLE IF EXISTS POKEDEX;

CREATE TABLE POKEDEX (
    id INTEGER PRIMARY KEY,
    pokemon_name TEXT NOT NULL,
    image_url TEXT NOT NULL,
    description TEXT NOT NULL
);

DROP TABLE IF EXISTS SUBSCRIBERS;

CREATE TABLE SUBSCRIBERS (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE
);
