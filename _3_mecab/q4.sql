SELECT
  kiji,
  hinshi,
  COUNT(*)
FROM bow2
GROUP BY kiji, hinshi;