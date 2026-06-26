-- ============================================
-- Module 01: SQL Foundations - Solutions
-- ============================================

-- ────────────────────────────────────────────
-- Problem 01: Basic SELECT
-- ────────────────────────────────────────────
SELECT name, salary
FROM Employee
ORDER BY name ASC;


-- ────────────────────────────────────────────
-- Problem 02: WHERE Filtering
-- ────────────────────────────────────────────
SELECT name, departmentId, salary
FROM Employee
WHERE salary > 80000
ORDER BY salary DESC;


-- ────────────────────────────────────────────
-- Problem 03: AND + OR
-- ────────────────────────────────────────────
SELECT name, departmentId, salary
FROM Employee
WHERE (departmentId = 1 AND salary > 90000)
   OR departmentId = 2;


-- ────────────────────────────────────────────
-- Problem 04: DISTINCT
-- ────────────────────────────────────────────
SELECT DISTINCT departmentId
FROM Employee
ORDER BY departmentId ASC;


-- ────────────────────────────────────────────
-- Problem 05: NULL Handling
-- ────────────────────────────────────────────
SELECT name, departmentId
FROM Employee
WHERE managerId IS NULL;


-- ────────────────────────────────────────────
-- Problem 06: COALESCE
-- ────────────────────────────────────────────
SELECT
    name,
    COALESCE(email, 'no-email@unknown.com') AS email
FROM Customer
ORDER BY name;


-- ────────────────────────────────────────────
-- Problem 07: Second Highest Salary
-- ────────────────────────────────────────────
SELECT DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

-- Note: The full LeetCode solution handles the empty case:
-- SELECT (
--     SELECT DISTINCT salary
--     FROM Employee
--     ORDER BY salary DESC
--     LIMIT 1 OFFSET 1
-- ) AS SecondHighestSalary;


-- ────────────────────────────────────────────
-- Problem 08: Execution Order
-- ────────────────────────────────────────────
-- WHY DOES THE ORIGINAL FAIL?
-- The WHERE clause is executed BEFORE the SELECT clause.
-- Therefore, the alias 'annual_salary' does not exist when
-- the WHERE clause is trying to filter the rows.

-- FIXED SOLUTION:
SELECT name, salary * 12 AS annual_salary
FROM Employee
WHERE salary * 12 > 1000000
ORDER BY annual_salary DESC;


-- ────────────────────────────────────────────
-- Problem 09: Combined Concepts
-- ────────────────────────────────────────────
SELECT
    name,
    salary,
    CASE
        WHEN salary >= 90000 THEN 'Senior'
        WHEN salary >= 80000 THEN 'Mid'
        ELSE 'Junior'
    END AS tier
FROM Employee
WHERE departmentId = 1
ORDER BY salary DESC
LIMIT 3;


-- ────────────────────────────────────────────
-- Problem 10: NULL Gotcha
-- ────────────────────────────────────────────
-- YOUR ANSWER:
-- The original query returns 1 row (Grace).

-- YOUR EXPLANATION:
-- managerId NOT IN (1, 3, 999) expands to:
-- managerId != 1 AND managerId != 3 AND managerId != 999.
-- If managerId is NULL, NULL != 1 evaluates to NULL.
-- The WHERE clause requires the condition to be TRUE.
-- Since NULL is not TRUE, the row is excluded.

-- FIXED SOLUTION (Option 1 - explicitly include NULLs):
SELECT name, managerId
FROM Employee
WHERE managerId NOT IN (1, 3, 999) OR managerId IS NULL;

-- FIXED SOLUTION (Option 2 - using COALESCE):
-- SELECT name, managerId
-- FROM Employee
-- WHERE COALESCE(managerId, -1) NOT IN (1, 3, 999);
