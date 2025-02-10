-- <!-- 184. Department Highest Salary

-- Table: Employee

-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | id           | int     |
-- | name         | varchar |
-- | salary       | int     |
-- | departmentId | int     |
-- +--------------+---------+
-- id is the primary key (column with unique values) for this table.
-- departmentId is a foreign key (reference columns) of the ID from the Department table.
-- Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

-- Table: Department

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- +-------------+---------+
-- id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
-- Each row of this table indicates the ID of a department and its name.
 

-- Write a solution to find employees who have the highest salary in each of the departments.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Employee table:
-- +----+-------+--------+--------------+
-- | id | name  | salary | departmentId |
-- +----+-------+--------+--------------+
-- | 1  | Joe   | 70000  | 1            |
-- | 2  | Jim   | 90000  | 1            |
-- | 3  | Henry | 80000  | 2            |
-- | 4  | Sam   | 60000  | 2            |
-- | 5  | Max   | 90000  | 1            |
-- +----+-------+--------+--------------+
-- Department table:
-- +----+-------+
-- | id | name  |
-- +----+-------+
-- | 1  | IT    |
-- | 2  | Sales |
-- +----+-------+
-- Output: 
-- +------------+----------+--------+
-- | Department | Employee | Salary |
-- +------------+----------+--------+
-- | IT         | Jim      | 90000  |
-- | Sales      | Henry    | 80000  |
-- | IT         | Max      | 90000  |
-- +------------+----------+--------+
-- Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department. -->

-- # Write your MySQL query statement below
-- Creating a Common Table Expression (CTE) named Sal_high  
WITH Sal_high AS (  
    -- Selecting relevant employee details along with department name  
    SELECT  
        e.id,  
        d.name AS department_name,   -- Department name  
        e.name AS employee_name,     -- Employee name  
        e.salary,                    -- Employee salary  
        
        -- Assigning a dense rank to employees within each department based on salary in descending order  
        DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS emp_dense_rank  
    FROM Employee e  
    INNER JOIN Department d ON e.departmentId = d.id  -- Joining Employee table with Department table  
)  

-- Selecting only the highest-paid employees (emp_dense_rank = 1) from each department  
SELECT  
    Sal_high.department_name AS Department,  
    Sal_high.employee_name AS Employee,  
    Sal_high.salary AS Salary  
FROM Sal_high  
WHERE Sal_high.emp_dense_rank = 1;
