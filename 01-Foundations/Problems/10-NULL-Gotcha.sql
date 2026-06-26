-- ============================================
-- Problem 10: NULL Gotcha (Classic Trap!)
-- Difficulty: ⭐⭐⭐ Medium
-- Tables: Employee
-- Topics: NOT IN, NULL, Three-Valued Logic
-- ============================================
--
-- QUESTION:
-- How many rows does this query return?
--
--   SELECT name, managerId
--   FROM Employee
--   WHERE managerId NOT IN (1, 3, 999);
--
-- Write the correct count, explain WHY some
-- rows are missing, and then write a fixed
-- version that also includes employees with
-- NULL managerId.
--
-- EXPECTED OUTPUT (fixed version):
-- ┌───────┬───────────┐
-- │ name  │ managerId │
-- ├───────┼───────────┤
-- │ Alice │ NULL      │
-- │ Frank │ NULL      │
-- │ Grace │ 6         │
-- └───────┴───────────┘
--
-- ============================================

-- ▸ YOUR ANSWER (how many rows does the original return?):
--
--

-- ▸ YOUR EXPLANATION (why?):
--
--

-- ▸ YOUR FIXED SOLUTION:

