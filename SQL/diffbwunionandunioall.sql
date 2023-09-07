-- difference between union and union all ---

--- union used to combine the result of two select statements 
-- the result of union will have the duplicates
--- union all is also used to combine the result of two select statements
--- union all result set will eliminate the duplicates and the result will be in the ascending order 

select dept_id from emp1
union
select dept_id from emp2

select dept_id from emp1  -------- this will remove the duplicates and result will be in ascending order 
union all
select dept_id from emp2
