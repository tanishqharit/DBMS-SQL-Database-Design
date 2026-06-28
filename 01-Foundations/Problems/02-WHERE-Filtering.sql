-- ============================================
-- Problem 02: WHERE Filtering
-- Difficulty: ⭐ Easy
-- Tables: Employee
-- Topics: SELECT, WHERE, ORDER BY
-- ============================================
--
-- QUESTION:
-- Find all employees who earn more than 80,000.
-- Show their name, departmentId, and salary.
-- Sort by salary descending.
--
-- EXPECTED OUTPUT:
-- ┌───────┬──────────────┬────────┐
-- │ name  │ departmentId │ salary │
-- ├───────┼──────────────┼────────┤
-- │ Alice │ 1            │ 95000  │
-- │ Ivy   │ 1            │ 95000  │
-- │ Eve   │ 1            │ 92000  │
-- │ Hank  │ 1            │ 88000  │
-- │ Bob   │ 1            │ 85000  │
-- └───────┴──────────────┴────────┘
--
-- ============================================

SELECT name, departmentID, salary
FROM Employee
WHERE salary > 80000
ORDER BY salary DESC