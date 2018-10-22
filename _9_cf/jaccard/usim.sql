CREATE TABLE lab.jac_usim
(
  usera INT,
  userb INT,
  sim   DOUBLE NOT NULL,
  PRIMARY KEY (usera, userb)
);

INSERT INTO jac_usim
WITH cte AS (SELECT uid, COUNT(*) AS cnt FROM rating GROUP BY uid)
SELECT inter.usera, inter.userb, inter.cnt / (ctea.cnt + cteb.cnt - inter.cnt)
FROM (SELECT a.uid AS usera, b.uid AS userb, COUNT(*) AS cnt
      FROM rating AS a
             JOIN rating AS b ON a.uid < b.uid AND a.aid = b.aid
      GROUP BY a.uid, b.uid) AS inter
       JOIN cte AS ctea ON inter.usera = ctea.uid
       JOIN cte AS cteb ON inter.userb = cteb.uid;

CREATE INDEX jac_usim_usera_index
  ON jac_usim (usera);
CREATE INDEX jac_usim_userb_index
  ON jac_usim (userb);