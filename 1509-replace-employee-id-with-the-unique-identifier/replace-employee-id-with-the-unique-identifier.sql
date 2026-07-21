# Write your MySQL query statement below
select eu.unique_id , e.name from 
EmployeeUNI eu
right join
employees e
on eu.id=e.id;