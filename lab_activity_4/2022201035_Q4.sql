Delimiter //
CREATE PROCEDURE print_values_with_cursor()
BEGIN
   DECLARE done INT DEFAULT 0;
   DECLARE name VARCHAR(255) DEFAULT "";
   DECLARE city VARCHAR(255) DEFAULT "";
   DECLARE country VARCHAR(255) DEFAULT "";
   DECLARE grade decimal(10,0) DEFAULT 0.0;
   DECLARE cur CURSOR FOR
   SELECT CUST_NAME,CUST_CITY,CUST_COUNTRY,GRADE FROM CUSTOMER_DB.customer where AGENT_CODE like 'A00%';
   DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
   OPEN cur;
   label:LOOP
   FETCH cur INTO name, city, country, grade;
   IF done = 1 THEN LEAVE label;
   END IF;
   SELECT name,city,country,grade;
   END LOOP label;
   CLOSE cur;
END//
delimiter ;
call print_values_with_cursor();
