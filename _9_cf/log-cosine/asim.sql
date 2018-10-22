CREATE TABLE lab.cos_asim
(
  arta INT,
  artb INT,
  sim  DOUBLE NOT NULL,
  PRIMARY KEY (arta, artb)
);

INSERT INTO cos_asim
WITH cte AS (SELECT aid, POWER(SUM(POWER(LOG(weight + 1), 2)), 0.5) AS dem FROM rating GROUP BY aid)
SELECT inter.arta, inter.artb, inter.num / (ctea.dem * cteb.dem)
FROM (SELECT a.aid AS arta, b.aid AS artb, SUM(LOG(a.weight + 1) * LOG(b.weight + 1)) AS num
      FROM rating AS a
             JOIN rating AS b ON a.aid < b.aid AND a.uid = b.uid
      GROUP BY a.aid, b.aid) AS inter
       JOIN cte AS ctea ON inter.arta = ctea.aid
       JOIN cte AS cteb ON inter.artb = cteb.aid;

CREATE INDEX cos_asim_arta_index
  ON cos_asim (arta);
CREATE INDEX cos_asim_artb_index
  ON cos_asim (artb);