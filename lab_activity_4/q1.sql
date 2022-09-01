delimiter //
create procedure add_num(in v1 int,in v2 int)
   begin
   declare Value1 int;
   declare Value2 int;
   set Value1=v1;
   set Value2=v2;
   select Value1,Value2,Value1+Value2 as S;
   end
   //
delimiter ;
call add_num(10,20);
