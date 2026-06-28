-- ============================================
-- Problem 03: AND + OR
-- Difficulty: ⭐ Easy
-- Tables: Employee
-- Topics: WHERE, AND, OR, Operator Precedence
-- ============================================
--
-- QUESTION:
-- Find employees who are either:
--   - In department 1 (Engineering) with salary > 90,000
--   - OR in department 2 (Marketing), any salary
-- Show name, departmentId, salary.
--
-- EXPECTED OUTPUT:
-- ┌─────────┬──────────────┬────────┐
-- │ name    │ departmentId │ salary │
-- ├─────────┼──────────────┼────────┤
-- │ Alice   │ 1            │ 95000  │
-- │ Charlie │ 2            │ 72000  │
-- │ Diana   │ 2            │ 68000  │
-- │ Eve     │ 1            │ 92000  │
-- │ Ivy     │ 1            │ 95000  │
-- │ Jack    │ 2            │ 62000  │
-- └─────────┴──────────────┴────────┘
--
-- ============================================

SELECT name, departmentID, salary
FROM Employee
WHERE (departmentID = 1 AND salary > 90000) OR departmentID = 2;
