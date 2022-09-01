delimiter //
CREATE PROCEDURE get_names (IN CITY CHAR(25))
       BEGIN
         SELECT CUST_NAME FROM CUSTOMER_DB.customer
         WHERE WORKING_AREA = CITY;
       END//
delimiter ;
call get_names('Bangalore');
