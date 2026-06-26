# DISTINCT — Removing Duplicates

`DISTINCT` removes duplicate rows from the result set.

---

## Basic Usage

```sql
-- All unique departments
SELECT DISTINCT department
FROM employees;
```

| department  |
|-------------|
| Engineering |
| Marketing   |
| Sales       |

Without `DISTINCT`, "Engineering" would appear 4 times (once for each Engineering employee).

---

## DISTINCT on Multiple Columns

When applied to multiple columns, `DISTINCT` removes duplicate **combinations**:

```sql
SELECT DISTINCT department, salary
FROM employees;
```

This returns unique `(department, salary)` pairs — NOT unique departments or unique salaries separately.

---

## DISTINCT vs. GROUP BY

These produce the same result for simple cases:

```sql
-- These are equivalent:
SELECT DISTINCT department FROM employees;
SELECT department FROM employees GROUP BY department;
```

The difference: `GROUP BY` lets you use aggregate functions (`COUNT`, `SUM`, etc.). `DISTINCT` is just for removing duplicates.

---

## COUNT(DISTINCT column)

Extremely common in LeetCode — counts unique values:

```sql
SELECT COUNT(DISTINCT department) AS unique_departments
FROM employees;
```

| unique_departments |
|-------------------|
| 3                 |

> 💡 We'll cover `COUNT` and other aggregate functions in detail in Module 03.

---

## Key Points

- `DISTINCT` applies to the **entire row** (all selected columns combined)
- `SELECT DISTINCT col1, col2` = unique (col1, col2) pairs
- `COUNT(DISTINCT col)` counts unique non-NULL values — LeetCode favorite
- If you need both deduplication AND aggregation, use `GROUP BY` instead
