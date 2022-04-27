-- Basic select statement
-- 1.  Write a query to display the names (first_name, last_name)
-- using an alias name “First Name”, “Last Name” from the employee table.
select first_name AS First_Name, last_name AS Last_Name from employees;

-- 2. Write a query to get unique departments ID from the employee table (ie. without duplicates).

SELECT 
	DISTINCT department_id
	FROM
		employees;

-- 3. Write a query to get the details of all employees from the employee table, do so in descending order by first name.

select * from employees order by first_name desc;

-- 4. Write a query to get the names (first_name, last_name), salary and 15% of salary as PF (ie. alias) for all the employees.

select First_Name, Last_Name, salary, salary * 0.15 as PF from employees;

-- 5. Write a query to get the employee IDs, names (first_name, last_name) and salary in ascending order according to their salary.

select employee_id, First_Name, Last_Name, salary from employees order by salary asc;

-- 6. Write a query to get the total sum of all salaries paid to the employees.
SELECT SUM (salary)
FROM employees;

-- 7. Write a query to get the maximum and minimum salaries paid to the employees.
SELECT MAX (salary), MIN (salary)
FROM employees;

-- 8. Write a query to get the average salary paid to the employees.
SELECT AVG (salary)
FROM employees;

-- 9. Write a query to get the number of employees working in the company.
SELECT COUNT (*)
FROM employees;

-- 10. Write a query to get all the first names from the employees table in upper case.
SELECT UPPER(first_name) from employees;

-- 11. Write a query to get the first three characters of each first name of all the employees in the employees table.
SELECT LEFT(first_name,3) from employees;

-- 12. Write a query to get the full names of all the employees in the employees table. You have to include the first name and last name.
select concat(first_name,' ',last_name) as full_name from employees;

-- 13. Write a query to get the first name, last name and the length of the full name of all the employees from the employees table.
SELECT concat(first_name,' ',last_name) as full_name, LENGTH(concat(first_name,' ',last_name)) from employees;

-- 14. Write a query to check whether the first_name column of the employees table contains any numbers.
select * from employees where first_name like '[%0-95]';

-- 15. Write a query to select the first ten records from a table.
select * from employees limit 10;


-- Restricting and sorting
--     1. Write a query to display the first_name, last_name and salary of all employees whose salary is between $10,000 and $15,000.
select first_name, last_name, salary from employees where salary between 10000 and 15000;

--     2. Write a query to display the first_name, last_name and hire date of all employees who were hired in 1987.
select first_name, last_name, hire_date from employees where hire_date>'1987-01-01' and hire_date <'1987-12-31';

--     3. Write a query to get the all employees whose first_name has both the letters ‘c’ and ‘e’.
select * from employees where first_name like '%c%' or first_name like'%e';

--     4. Write a query to display the last_name, job, and salary of all the employees who don’t work as Programmers or Shipping Clerks, and who don’t receive a salary equal to $4,500, $10,000, or $15,000.
select last_name, job_title, salary
from employees, jobs where jobs.job_id = employees.job_id
and job_title != 'Programmer' and job_title != 'Shipping Clerk'
and salary != 4500 and salary != 10000 and salary != 15000;

--     5. Write a query to display the last names of all employees whose last name contains exactly six characters.
select last_name from employees where LENGTH(last_name) = 6;

--     6. Write a query to display the last name of all employees who have the letter ‘e’ as the third character in the name.
select last_name from employees where left(last_name, 3) like '%e';

--     7. Write a query to display the jobs title appearing in the employees table.
select job_title as "Job available" from jobs, employees where jobs.job_id = employees.job_id;
select distinct job_title from jobs, employees where jobs.job_id = employees.job_id; 

--     8. Write a query to select all information of employees whose last name is either ‘JONES’ or ‘BLAKE’ or ‘SCOTT’ or ‘KING’ or ‘FORD’.
select * from employees where last_name = 'Jones' or last_name = 'Blake' or last_name = 'Scott' or last_name = 'King' or last_name = 'Ford';

