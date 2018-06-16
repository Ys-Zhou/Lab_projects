SELECT
  inter.usera,
  inter.userb,
  inter.cnt / MIN(num.cnt) AS simp
FROM (
       SELECT
         a.uid    AS usera,
         b.uid    AS userb,
         COUNT(*) AS cnt
       FROM rating AS a
         JOIN rating AS b ON a.uid < b.uid AND a.aid = b.aid
       GROUP BY a.uid, b.uid
     ) AS inter
  JOIN (
         SELECT
           uid,
           COUNT(*) AS cnt
         FROM rating
         GROUP BY uid
       ) AS num ON inter.usera = num.uid OR inter.userb = num.uid
GROUP BY usera, userb
ORDER BY simp DESC;