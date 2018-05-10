SELECT
  `kiji`,
  `hinshi`,
  COUNT(*)
FROM `lab`.`bow2`
GROUP BY `kiji`, `hinshi`;