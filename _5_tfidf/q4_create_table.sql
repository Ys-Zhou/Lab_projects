CREATE TABLE lab.tfidf
(
  uid  VARCHAR(20),
  word VARCHAR(20),
  tfidf   DOUBLE NOT NULL,
  PRIMARY KEY (uid, word)
)
  COLLATE = utf8mb4_bin;