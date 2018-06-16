WITH cte AS (
    SELECT
      uid,
      COUNT(*) AS cnt
    FROM rating
    GROUP BY uid
)
SELECT
  inter.usera,
  inter.userb,
  inter.cnt / CASE
              WHEN ctea.cnt < cteb.cnt
                THEN ctea.cnt
              ELSE cteb.cnt END AS simp
FROM (
       SELECT
         a.uid    AS usera,
         b.uid    AS userb,
         COUNT(*) AS cnt
       FROM rating AS a
         JOIN rating AS b ON a.uid < b.uid AND a.aid = b.aid
       GROUP BY a.uid, b.uid
     ) AS inter
  JOIN cte AS ctea ON inter.usera = ctea.uid
  JOIN cte AS cteb ON inter.userb = cteb.uid
ORDER BY simp DESC;