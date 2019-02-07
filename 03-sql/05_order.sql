SELECT *
FROM movies
ORDER BY audience DESC LIMIT 5;

SELECT *
FROM movies
WHERE genre = '애니메이션'
ORDER BY country ASC, audience DESC LIMIT 10;

SELECT director
from movies
ORDER BY show_time DESC LIMIT 10;