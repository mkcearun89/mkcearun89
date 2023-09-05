DECLARE
v_employee_id NUMBER (6):= 104;
v_email_id VARCHAR2(50);
v_phone_number NUMBER;
v_first_name VARCHAR2(100);
 
BEGIN
 Select first_name, email_id , phone_number  into v_first_name , v_email_id , v_phone_number from emp_details Where em_id = v_employee_id;


DBMS_OUTPUT.PUT_LINE ('Employee ID: ' || v_employee_id , 'First_name :' || v_first_name ,   'email_id  :'  || v_email_id , 'phone_number :' || v_phone_number );

Exception 
When NO_DATA_FOUND
	DBMS_OUTPUT.PUT_LINE ( ' No data found for 104');
When too_many_rows
	DBMS_output.put_line (' more than one entries available for emp id : ' v_employee_id);
When others 
	Dbms_output.put_line (  'ERROR  :' || substr(SQLCODE, 1,5) , 
					'ERROR MSG : ' || substr(SQLERRM,1,10));  
END;
/![image](https://github.com/mkcearun89/mkcearun89/assets/144054180/e4b2a299-f149-4621-bdc9-d4a15f70fcd9)
