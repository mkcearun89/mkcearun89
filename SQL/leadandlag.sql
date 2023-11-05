lag analytical function is used to compare the current and previous column value in the table.

Lead analytical function is used to compare the current and next column value in the table

Lag(column) over(order by column2)

Lead(column) over (order by column2)

select num as ConsecutiveNums from (select id,num, 
lag(num) over(order by id) as before,
lead(num) over (order by id) as after 
from logs )
where num=before and after=before 
