CREATE TABLE lab.tfidf (
  uid   VARCHAR(20),
  word  VARCHAR(20),
  tfidf DOUBLE NOT NULL,
  PRIMARY KEY (uid, word)
)
  COLLATE = utf8mb4_bin;

INSERT INTO tfidf
  SELECT
    tf.uid,
    tf.word,
    tf.tf * LOG(cnt.d / (df.df + 1)) AS tfidf
  FROM tf
    JOIN df ON tf.word = df.word
    JOIN (
           SELECT COUNT(DISTINCT uid) AS d
           FROM tf
         ) AS cnt;

CREATE INDEX tfidf_uid_index
  ON tfidf (uid);
CREATE INDEX tfidf_word_index
  ON tfidf (word);