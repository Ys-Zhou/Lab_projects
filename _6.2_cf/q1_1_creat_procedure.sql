CREATE PROCEDURE upred(IN pid INT)
  BEGIN
    SELECT
      pid,
      ref.aid,
      SUM(usim.sim * ref.weight) / SUM(usim.sim) AS pred
    FROM (
           SELECT
             usera,
             userb,
             sim
           FROM usersim
           WHERE usera = pid
           UNION
           SELECT
             userb,
             usera,
             sim
           FROM usersim
           WHERE userb = pid
         ) AS usim
      JOIN rating AS ref ON usim.userb = ref.uid AND ref.aid NOT IN (
        SELECT aid
        FROM rating
        WHERE uid = pid
      )
    GROUP BY ref.aid
    ORDER BY pred DESC
    LIMIT 5;
  END;