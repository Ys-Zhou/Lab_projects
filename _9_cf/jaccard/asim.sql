CREATE TABLE lab.jac_asim
(
  arta INT,
  artb INT,
  sim  DOUBLE NOT NULL,
  PRIMARY KEY (arta, artb)
);

INSERT INTO jac_asim
WITH cte AS (SELECT aid, COUNT(*) AS cnt FROM rating GROUP BY aid)
SELECT inter.arta, inter.artb, inter.cnt / (ctea.cnt + cteb.cnt - inter.cnt)
FROM (SELECT a.aid AS arta, b.aid AS artb, COUNT(*) AS cnt
      FROM rating AS a
             JOIN rating AS b ON a.aid < b.aid AND a.uid = b.uid
      GROUP BY a.aid, b.aid) AS inter
       JOIN cte AS ctea ON inter.arta = ctea.aid
       JOIN cte AS cteb ON inter.artb = cteb.aid;

CREATE INDEX jac_asim_arta_index
  ON jac_asim (arta);
CREATE INDEX jac_asim_artb_index
  ON jac_asim (artb);