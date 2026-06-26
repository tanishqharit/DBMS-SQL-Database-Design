# SELECT — Retrieving Data

The `SELECT` statement is the most fundamental SQL command. It retrieves data from a table.

---

## Syntax

```sql
SELECT column1, column2, ...
FROM table_name;
```

---

## Select Specific Columns

```sql
SELECT name, salary
FROM employees;
```

| name    | salary |
|---------|--------|
| Alice   | 95000  |
| Bob     | 85000  |
| Charlie | 72000  |
| Diana   | 68000  |
| Eve     | 92000  |

---

## Select ALL Columns (`*`)

```sql
SELECT *
FROM employees;
```

> ⚠️ **Interview Tip**: Avoid `SELECT *` in production code. It's slower (fetches unnecessary data) and fragile (breaks if columns are added/removed). Always name your columns. However, on LeetCode, `SELECT *` is fine for quick solutions.

---

## Computed Columns (Expressions)

You can do math and transformations right in SELECT:

```sql
SELECT
    name,
    salary,
    salary * 12 AS annual_salary,
    salary / 12.0 AS monthly_salary
FROM employees;
```

| name    | salary | annual_salary | monthly_salary |
|---------|--------|---------------|----------------|
| Alice   | 95000  | 1140000       | 7916.67        |
| Bob     | 85000  | 1020000       | 7083.33        |

---

## Select Without a Table

Useful for quick calculations and tests:

```sql
SELECT 1 + 1 AS result;
SELECT 'Hello' AS greeting;
SELECT CURRENT_DATE AS today;
```

> 🔧 **Try it**: `python3 00-Setup/runner.py -q "SELECT 1 + 1 AS result;"`

---

## Key Points

- `SELECT` chooses **which columns** to display
- `FROM` specifies **which table** to read from
- You can compute new columns using expressions
- `*` means "all columns" — avoid in production, fine for LeetCode
