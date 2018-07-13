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

CREATE PROCEDURE apredforall()
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
      CALL apred(pid);
      FETCH icur
      INTO pid;
    END WHILE;
    CLOSE icur;
  END;

CALL apred(2);
CALL apredforall();