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

CREATE PROCEDURE upredforall()
  BEGIN
    DECLARE hasmore INT DEFAULT TRUE;
    DECLARE pid INT;
    DECLARE icur CURSOR FOR SELECT DISTINCT uid
                            FROM rating;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET hasmore = FALSE;
    OPEN icur;
    FETCH icur
    INTO pid;
    WHILE hasmore DO
      CALL upred(pid);
      FETCH icur
      INTO pid;
    END WHILE;
    CLOSE icur;
  END;

CALL upred(2);
CALL upredforall();