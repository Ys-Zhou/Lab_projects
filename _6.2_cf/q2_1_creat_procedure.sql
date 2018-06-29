CREATE PROCEDURE apred(IN pid INT)
  BEGIN
    SELECT
      ref.uid,
      asim.arta,
      SUM(asim.sim * ref.weight) / SUM(asim.sim) AS pred
    FROM (
           SELECT
             arta,
             artb,
             sim
           FROM artsim
           UNION
           SELECT
             artb,
             arta,
             sim
           FROM artsim
         ) AS asim
      JOIN rating AS ref ON asim.artb = ref.aid AND ref.uid = pid AND asim.arta NOT IN (
        SELECT aid
        FROM rating
        WHERE uid = pid
      )
    GROUP BY asim.arta
    ORDER BY pred DESC
    LIMIT 5;
  END;