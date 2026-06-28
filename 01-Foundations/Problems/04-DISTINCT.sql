-- ============================================
-- Problem 04: DISTINCT
-- Difficulty: ⭐ Easy
-- Tables: Employee
-- Topics: DISTINCT, ORDER BY
-- ============================================
--
-- QUESTION:
-- List all unique departmentId values from the
-- Employee table. Sort in ascending order.
--
-- EXPECTED OUTPUT:
-- ┌──────────────┐
-- │ departmentId │
-- ├──────────────┤
-- │ 1            │
-- │ 2            │
-- │ 3            │
-- └──────────────┘
--
-- ============================================

SELECT DISTINCT departmentID
FROM Employee
ORDER BY departmentID ASC;