-- Write your PostgreSQL query statement below
SELECT SCORE,
 DENSE_RANK() OVER (ORDER BY score DESC) AS rank 
from scores;