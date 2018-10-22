CREATE TABLE lab.cos_usim
(
  usera INT,
  userb INT,
  sim   DOUBLE NOT NULL,
  PRIMARY KEY (usera, userb)
);

INSERT INTO cos_usim
WITH cte AS (SELECT uid, POWER(SUM(POWER(LOG(weight + 1), 2)), 0.5) AS dem FROM rating GROUP BY uid)
SELECT inter.usera, inter.userb, inter.num / (ctea.dem * cteb.dem)
FROM (SELECT a.uid AS usera, b.uid AS userb, SUM(LOG(a.weight + 1) * LOG(b.weight + 1)) AS num
      FROM rating AS a
             JOIN rating AS b ON a.uid < b.uid AND a.aid = b.aid
      GROUP BY a.uid, b.uid) AS inter
       JOIN cte AS ctea ON inter.usera = ctea.uid
       JOIN cte AS cteb ON inter.userb = cteb.uid;

CREATE INDEX cos_usim_usera_index
  ON cos_usim (usera);
CREATE INDEX cos_usim_userb_index
  ON cos_usim (userb);