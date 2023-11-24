How will you retrieve 50% of the records from the table?

	select * from employee where rownum <= select count(*)/2 from employee;

Difference between having and where clause?

	Having clause is used to filter the records after the grouping.

	Having used for aggregate functions.

	Where clause is used to filter the records from the table.

	order of executing where --> group by --> having 

Difference between Join and Union 

	Join is used to retrieve data from two tables
	
	union used to combine the data from the two select statments

	union will remove the duplicates from the select statements

	Union all will include the duplicates

How many primary keys can a table have?
	
	A table can have only one primary key

null values 
	
	A primary key can not have a null value
	
	A unique key can have only one null value

difference between code and decode ?

	we can not use relational operators other than "="
	
	We can use other relational operator in case "<", ">"
	
	Case is easily readable
	
	Decode is more faster than case

INSTR - string function

	INSTR is used for return the position of a charater in the string.




