CREATE TABLE lab.rating
(
  uid    INT,
  aid    INT,
  weight INT NOT NULL,
  PRIMARY KEY (uid, aid)
);