select min(salary)from Employe where salary in (select top(3) salary from Employe order by salary desc)
