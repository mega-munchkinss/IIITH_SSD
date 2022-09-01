delimiter //
CREATE PROCEDURE get_names_grade ()
       BEGIN
         SELECT CUST_NAME,GRADE FROM CUSTOMER_DB.customer
         WHERE OPENING_AMT + RECEIVE_AMT > 10000.00;
       END//
delimiter ;
call get_names_grade();
