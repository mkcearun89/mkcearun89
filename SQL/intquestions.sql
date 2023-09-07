--- how to find the employees whose dept is not listed in the dept table ----

select emp.* , dept.dept_id from emp 
LEFT JOIN dept where dept.dept_id = emp.dept_id 
where dept_id is null;
/*
this will show all the records from emp table and only the records which has dept id in emp table.and null values to the records 
from dept table. and adding where cluase with dept_id is null will retrun employees dept is not listed in dept table 
*/


--- to find the second rank of a student in each class

select * from (select student_id, rank() over (partition by class order by marks desc) as rank
from students_mark table ) 
where rank = 2;



