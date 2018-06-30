CREATE TABLE lab.tf (
  uid  VARCHAR(20),
  word VARCHAR(20),
  tf   DOUBLE NOT NULL,
  PRIMARY KEY (uid, word)
)
  COLLATE = utf8mb4_bin;