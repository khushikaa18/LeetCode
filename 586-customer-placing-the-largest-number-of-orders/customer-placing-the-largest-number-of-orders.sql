# Write your MySQL query statement below
SELECT CUSTOMER_NUMBER 
FROM ORDERS
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
