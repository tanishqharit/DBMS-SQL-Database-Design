# Comments in SQL

Comments are ignored by the database engine. Use them to explain your queries.

---

## Single-Line Comment

```sql
-- This is a single-line comment
SELECT name FROM employees;  -- inline comment
```

---

## Multi-Line Comment

```sql
/* This is a
   multi-line comment
   spanning several lines */
SELECT name FROM employees;
```

---

## Practical Use

```sql
SELECT
    name,          -- employee's full name
    salary,        /* monthly salary in USD */
    department
FROM employees
-- WHERE salary > 80000   (commented out for debugging)
ORDER BY name;
```

> 💡 **Tip**: Commenting out parts of a query is a great debugging technique — temporarily remove a WHERE clause or a JOIN to isolate issues.
