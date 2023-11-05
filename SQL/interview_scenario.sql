--- Query to find employees earn more than their managers


select name as employee from (
  select id , name , managerId from employee a where 
salary > (select b.salary from employee  b where b.id = a.managerId) )
