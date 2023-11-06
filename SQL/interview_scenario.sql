--- Query to find employees earn more than their managers


select name as employee from (
  select id , name , managerId from employee a where 
salary > (select b.salary from employee  b where b.id = a.managerId) )

  -----------------------------------------------------------------------------------------
/*
  A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.
Write a solution to find the employees who are high earners in each of the departments.
Return the result table in any order.
The result format is in the following example.
*/

select depname  as Department  , ename as Employee , 
salary from ( select e.id, e.name as ename, e.departmentid , d.name as depname , e.salary as salary , dense_rank() over(partition by e.departmentid order by salary desc ) as rk
from employee e
left join department d
on e.departmentid = d.id )
where rk between 1 and 3;
