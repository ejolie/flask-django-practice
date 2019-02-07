CREATE TABLE movies (
    mv_code INTEGER PRIMARY KEY,
    mv_name TEXT,
    watch_grade TEXT,
    director TEXT,
    prdt_year INTEGER,
    audience INTEGER,
    show_time INTEGER,
    country TEXT,
    genre TEXT
);

.mode csv
.mode column
.mode tabs
.separator ,
.import boxoffice.csv movies

SELECT *
FROM movies;