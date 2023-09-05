
---List agg.
/*
1. List aggregate is a analytical function 
2. Transform multiple rows into a single row value delimited by a sepecified delimiter
3. can return upto 4000 bytes
*/

----------------Sample query -------------------
select department, listagg (first_name, '-' ) within group (order by first name) as department_staffs
from employees 
group by department order by department;
