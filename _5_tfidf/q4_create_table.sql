CREATE TABLE lab.tfidf
(
  uid  VARCHAR(20),
  word VARCHAR(20),
  tfidf   DOUBLE NOT NULL,
  CONSTRAINT tfidf_pk PRIMARY KEY (uid, word)
)
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_bin;