select Employe.Name,Employe.Salary,onboarding.joining_date
from Employe
inner join onboarding on Employe.Name=onboarding.Name order by joining_date desc;
