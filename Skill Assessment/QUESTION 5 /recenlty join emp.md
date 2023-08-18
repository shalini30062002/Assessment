# SQL Query: Find Recently Joined Employee and Their Salary

## Introduction

SQL (Structured Query Language) is widely used for managing and querying relational databases. Writing efficient and accurate queries is essential for extracting the required information from database tables. 
This repository provides a simple example of how to write an SQL query to find the recently joined employee and their salary.

### Prerequisites

- A database system (e.g., MySQL, PostgreSQL) with a table named `employees` containing columns `employee_name`, `joining_date`, and `salary`.

## SQL Query
To find the recently joined employee and their corresponding salary from the employees table, you can use the following SQL query:

"""select Employe.Name,Employe.Salary,onboarding.joining_date

from Employe

inner join onboarding on Employe.Name=onboarding.Name

where datediff(year,joining_date,getdate())=0"""

SELECT employee_name, salary-- fetches the name and salary of the recently joined employee.

INNER JOIN --combining rows that have matching values in two or more tables.

WHERE--It is used to extract only those records that fulfill a specified condition.

datediss-- difference between the startdate and enddate.
