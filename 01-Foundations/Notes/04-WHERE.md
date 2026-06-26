# WHERE — Filtering Rows

`WHERE` filters rows based on a condition. Only rows where the condition is `TRUE` are included in the result.

---

## Syntax

```sql
SELECT columns
FROM table_name
WHERE condition;
```

---

## Examples

**Filter by number:**
```sql
-- Employees earning more than 80,000
SELECT name, salary
FROM employees
WHERE salary > 80000;
```

| name  | salary |
|-------|--------|
| Alice | 95000  |
| Bob   | 85000  |
| Eve   | 92000  |

**Filter by text:**
```sql
-- Employees in the Marketing department
SELECT name, department
FROM employees
WHERE department = 'Marketing';
```

| name    | department |
|---------|------------|
| Charlie | Marketing  |
| Diana   | Marketing  |

**Filter by date:**
```sql
-- Employees hired after 2021
SELECT name, hire_date
FROM employees
WHERE hire_date > '2021-01-01';
```

---

## ⚠️ String Quotes — Critical Trap

SQL uses **single quotes** `'text'` for string values. **Double quotes** `"text"` are for column/table names (identifiers).

```sql
WHERE name = 'Alice'        -- ✅ Correct (string value)
WHERE name = "Alice"        -- ❌ Wrong in PostgreSQL (treated as column name)
```

> This trips up many beginners — especially those coming from Python/JavaScript where single and double quotes are interchangeable.

---

## Key Points

- `WHERE` runs **before** `SELECT` in execution order
- Filters individual rows (not groups — that's `HAVING`, covered in Module 03)
- Always use single quotes for string values
- Condition must evaluate to TRUE, FALSE, or NULL (NULL is treated as FALSE)
