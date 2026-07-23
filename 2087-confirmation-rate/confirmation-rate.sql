# Write your MySQL query statement below
SELECT S.USER_ID , 
ROUND(
    IFNULL(AVG(
    CASE
        WHEN C.action = 'confirmed' THEN 1
        ELSE 0
    END
    ),0
),2) AS CONFIRMATION_RATE
FROM SIGNUPS S
LEFT JOIN CONFIRMATIONS C 
ON S.USER_ID = C.USER_ID 
GROUP BY 
S.USER_ID;

