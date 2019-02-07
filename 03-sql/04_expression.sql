SELECT audience
FROM movies;

SELECT mv_name, MAX(audience)
FROM movies;

SELECT genre, MIN(show_time)
FROM movies;

SELECT AVG(audience)
FROM movies
WHERE country = '한국';

SELECT COUNT(mv_code)
FROM movies
WHERE watch_grade = '청소년관람불가';

SELECT COUNT(mv_code)
FROM movies
WHERE show_time >= 100 AND genre = '애니메이션';