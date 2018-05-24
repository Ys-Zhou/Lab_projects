INSERT INTO lab.df (word, df)
  SELECT
    word,
    COUNT(*) AS df
  FROM lab.tf
  GROUP BY word;