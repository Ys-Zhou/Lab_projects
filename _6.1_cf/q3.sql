WITH cte AS (
    SELECT
      aid,
      COUNT(*) AS cnt
    FROM rating
    GROUP BY aid
)
SELECT
  inter.arta,
  inter.artb,
  inter.cnt / CASE
              WHEN ctea.cnt < cteb.cnt
                THEN ctea.cnt
              ELSE cteb.cnt END AS simp
FROM (
       SELECT
         a.aid    AS arta,
         b.aid    AS artb,
         COUNT(*) AS cnt
       FROM rating AS a
         JOIN rating AS b ON a.aid < b.aid AND a.uid = b.uid
       GROUP BY a.aid, b.aid
     ) AS inter
  JOIN cte AS ctea ON inter.arta = ctea.aid
  JOIN cte AS cteb ON inter.artb = cteb.aid
ORDER BY simp DESC;