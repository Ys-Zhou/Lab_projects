WITH cte AS (
    SELECT
      uid,
      SQRT(SUM(POW(tfidf, 2))) AS norm
    FROM tfidf
    GROUP BY uid
)
SELECT
  sub1.u1,
  sub1.u2,
  sub1.dot / (sub2.norm * sub3.norm) AS sim
FROM (
       SELECT
         a.uid                  AS u1,
         b.uid                  AS u2,
         SUM(a.tfidf * b.tfidf) AS dot
       FROM tfidf AS a
         JOIN tfidf AS b ON a.uid > b.uid AND a.word = b.word
       GROUP BY a.uid, b.uid
     ) AS sub1
  JOIN cte AS sub2 ON sub1.u1 = sub2.uid
  JOIN cte AS sub3 ON sub1.u2 = sub3.uid
ORDER BY sim DESC;