
--- ROW_NUMBER & RANK & DENSE_RANK --------------
-- They are analytical fuinctions
-- Row_number is giving the sequence number based on the condition over Partition 
-- 
/*
Rank - will give the ranks to the values , if two values are equal then it will give same rank to the values. then the next value
skipped and the next value will be assigned to the rank . total number of records is equal to the total number of rank
/*

/*
Dense_rank - it is also giving the ranks to the records. if two values are equal , same rank will be given to the records 
then the very next rank will be assigned to the values. no of records in the table will not be equal to the total no of the 
ranks
*/

select emp_id , row_number over(partition by dept order by dept)  as rn 
from emp;

select emp_id, rank over(parition by dept) emp_ranks from emp;

select emp_id , dense_rank(partition by dept) enp_dense_ranks from emp;
