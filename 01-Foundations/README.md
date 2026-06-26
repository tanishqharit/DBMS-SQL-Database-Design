# Module 01: SQL Foundations

> **Goal**: By the end of this module, you should be able to write basic SQL queries — selecting data, filtering rows, sorting results, and handling NULL values. This covers ~30% of LeetCode Easy problems.

## 📚 Notes

Theory, syntax, and examples.

| # | Topic | File |
|---|-------|------|
| 01 | What is SQL? | [Notes/01-What-is-SQL.md](./Notes/01-What-is-SQL.md) |
| 02 | Databases, Tables, Rows, Columns | [Notes/02-Tables-Rows-Columns.md](./Notes/02-Tables-Rows-Columns.md) |
| 03 | SELECT — Retrieving Data | [Notes/03-SELECT.md](./Notes/03-SELECT.md) |
| 04 | WHERE — Filtering Rows | [Notes/04-WHERE.md](./Notes/04-WHERE.md) |
| 05 | Comparison Operators | [Notes/05-Comparison-Operators.md](./Notes/05-Comparison-Operators.md) |
| 06 | Logical Operators (AND, OR, NOT) | [Notes/06-Logical-Operators.md](./Notes/06-Logical-Operators.md) |
| 07 | DISTINCT — Removing Duplicates | [Notes/07-DISTINCT.md](./Notes/07-DISTINCT.md) |
| 08 | ORDER BY — Sorting Results | [Notes/08-ORDER-BY.md](./Notes/08-ORDER-BY.md) |
| 09 | LIMIT & OFFSET — Pagination | [Notes/09-LIMIT-OFFSET.md](./Notes/09-LIMIT-OFFSET.md) |
| 10 | NULL Handling | [Notes/10-NULL-Handling.md](./Notes/10-NULL-Handling.md) |
| 11 | SQL Execution Order ⭐ | [Notes/11-Execution-Order.md](./Notes/11-Execution-Order.md) |
| 12 | Aliases (AS) | [Notes/12-Aliases.md](./Notes/12-Aliases.md) |
| 13 | Comments | [Notes/13-Comments.md](./Notes/13-Comments.md) |

## 💻 Practice Problems

> ⚠️ **Run the setup script before solving problems:**
> `python3 00-Setup/runner.py 00-Setup/seed.sql`

| # | Problem | Difficulty | File |
|---|---------|------------|------|
| 01 | Basic SELECT | ⭐ Easy | [Problems/01-Basic-SELECT.sql](./Problems/01-Basic-SELECT.sql) |
| 02 | WHERE Filtering | ⭐ Easy | [Problems/02-WHERE-Filtering.sql](./Problems/02-WHERE-Filtering.sql) |
| 03 | AND + OR | ⭐ Easy | [Problems/03-AND-OR.sql](./Problems/03-AND-OR.sql) |
| 04 | DISTINCT | ⭐ Easy | [Problems/04-DISTINCT.sql](./Problems/04-DISTINCT.sql) |
| 05 | NULL Handling | ⭐⭐ Easy-Medium | [Problems/05-NULL-Handling.sql](./Problems/05-NULL-Handling.sql) |
| 06 | COALESCE | ⭐⭐ Easy-Medium | [Problems/06-COALESCE.sql](./Problems/06-COALESCE.sql) |
| 07 | Second Highest Salary | ⭐⭐ Medium | [Problems/07-Second-Highest-Salary.sql](./Problems/07-Second-Highest-Salary.sql) |
| 08 | Execution Order | ⭐⭐ Medium | [Problems/08-Execution-Order.sql](./Problems/08-Execution-Order.sql) |
| 09 | Combined Concepts | ⭐⭐ Medium | [Problems/09-Combined-Concepts.sql](./Problems/09-Combined-Concepts.sql) |
| 10 | NULL Gotcha | ⭐⭐⭐ Medium | [Problems/10-NULL-Gotcha.sql](./Problems/10-NULL-Gotcha.sql) |

## ✅ Solutions

All solutions with explanations can be found in:
[Solutions/solutions.sql](./Solutions/solutions.sql)

---

## 🎯 Summary

| Concept | Key Syntax | Watch Out For |
|---------|-----------|---------------|
| SELECT | `SELECT col1, col2 FROM table` | Avoid `SELECT *` in production |
| WHERE | `WHERE condition` | Single quotes for strings, not double |
| Comparison | `=, !=, <>, >, <, >=, <=` | `<>` is the ANSI standard for "not equal" |
| Logic | `AND, OR, NOT` | Precedence: NOT > AND > OR. Use parentheses! |
| DISTINCT | `SELECT DISTINCT col` | Applies to all selected columns combined |
| ORDER BY | `ORDER BY col ASC/DESC` | Without it, order is NOT guaranteed |
| LIMIT | `LIMIT n OFFSET m` | OFFSET is 0-based (skip m rows) |
| NULL | `IS NULL, IS NOT NULL` | Never use `= NULL` or `!= NULL` |
| COALESCE | `COALESCE(val, default)` | Returns first non-NULL argument |
| Execution Order | FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY→LIMIT | Can't use aliases in WHERE |

## What's Next?

→ **Module 02: Filtering & Pattern Matching** — `LIKE`, `IN`, `BETWEEN`, `CASE WHEN`, type casting
