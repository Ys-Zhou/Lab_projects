INSERT INTO df (word, df)
  SELECT
    word,
    COUNT(*) AS df
  FROM tf
  GROUP BY word;