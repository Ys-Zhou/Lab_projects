CREATE TABLE lab.df (
  word VARCHAR(20) PRIMARY KEY,
  df   INT NOT NULL
)
  COLLATE = utf8mb4_bin;

INSERT INTO df
  SELECT
    word,
    COUNT(*) AS df
  FROM tf
  GROUP BY word;