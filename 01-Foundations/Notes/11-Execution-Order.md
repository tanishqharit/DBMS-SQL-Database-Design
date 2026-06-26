# SQL Execution Order ⭐ (CRITICAL)

This is one of the **most important concepts** in SQL. The query is NOT executed in the order you write it.

---

## Written Order vs. Execution Order

```
WRITTEN ORDER          EXECUTION ORDER
─────────────          ───────────────
1. SELECT              5. SELECT
2. FROM                1. FROM
3. WHERE               2. WHERE
4. GROUP BY            3. GROUP BY
5. HAVING              4. HAVING
6. ORDER BY            6. ORDER BY
7. LIMIT               7. LIMIT
```

---

## The Execution Pipeline (Visualized)

```
FROM     → Which table(s) to read from?
  ↓
WHERE    → Filter individual rows
  ↓
GROUP BY → Group rows together
  ↓
HAVING   → Filter groups (after aggregation)
  ↓
SELECT   → Choose which columns to output (+ compute expressions)
  ↓
ORDER BY → Sort the results
  ↓
LIMIT    → Cut off at N rows
```

---

## Why This Matters

### ❌ Can't Use Aliases in WHERE

```sql
-- ❌ Error: "annual" doesn't exist yet when WHERE runs
SELECT salary * 12 AS annual
FROM employees
WHERE annual > 100000;

-- ✅ Correct: repeat the expression
SELECT salary * 12 AS annual
FROM employees
WHERE salary * 12 > 100000;
```

**Why?** `WHERE` runs at step 2, but `annual` alias is created at step 5 (`SELECT`).

### ✅ CAN Use Aliases in ORDER BY

```sql
-- ✅ This works because ORDER BY runs AFTER SELECT
SELECT salary * 12 AS annual
FROM employees
ORDER BY annual DESC;
```

---

## Alias Availability by Dialect

| Clause | PostgreSQL | MySQL |
|--------|-----------|-------|
| WHERE | ❌ No aliases | ❌ No aliases |
| GROUP BY | ✅ Allows aliases | ✅ Allows aliases |
| HAVING | ❌ No aliases | ✅ Allows aliases |
| ORDER BY | ✅ Allows aliases | ✅ Allows aliases |

---

## ⚠️ Interview Favorite

> **Q: "Why can't you use a column alias in WHERE?"**
>
> **A:** Because of SQL execution order. WHERE is evaluated at step 2, before SELECT (step 5) where aliases are defined. The alias simply doesn't exist yet when WHERE runs.

---

## Key Points

- Execution order: `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`
- You **cannot** use SELECT aliases in WHERE or HAVING (in PostgreSQL)
- You **can** use SELECT aliases in ORDER BY
- This is the foundation for understanding why certain queries work or fail
