CREATE TABLE lab.tf
(
  uid  VARCHAR(20),
  word VARCHAR(20),
  tf   DOUBLE NOT NULL,
  CONSTRAINT tf_pk PRIMARY KEY (uid, word)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;