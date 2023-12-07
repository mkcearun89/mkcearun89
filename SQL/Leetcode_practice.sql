/* Write a solution to report the name and bonus amount of each employee with a bonus less than 1000. */


/* Write your PL/SQL query statement below */
select  e.name as name , b.bonus as bonus from employee e Left join
bonus  b on e.empId = b.empId
where NVL(b.bonus,0) < 1000;
