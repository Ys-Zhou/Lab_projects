INSERT INTO tfidf (uid, word, tfidf)
  SELECT
    tf.uid,
    tf.word,
    tf.tf * LOG(cnt.d / (df.df + 1)) AS tfidf
  FROM tf
    JOIN df
      ON tf.word = df.word
    JOIN (SELECT COUNT(DISTINCT uid) AS d
          FROM tf) cnt;