select Employe.Name,Employe.Salary,onboarding.joining_date
from Employe
inner join onboarding on Employe.Name=onboarding.Name 
where datediff(year,joining_date,getdate())=0
