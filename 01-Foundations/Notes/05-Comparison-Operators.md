# Comparison Operators

Used in `WHERE` clauses to compare values.

---

## Operator Reference

| Operator | Meaning | Example |
|----------|---------|---------|
| `=` | Equal to | `WHERE salary = 85000` |
| `!=` or `<>` | Not equal to | `WHERE department != 'Sales'` |
| `>` | Greater than | `WHERE salary > 80000` |
| `<` | Less than | `WHERE salary < 75000` |
| `>=` | Greater than or equal | `WHERE salary >= 85000` |
| `<=` | Less than or equal | `WHERE salary <= 72000` |

> 💡 `!=` and `<>` are equivalent. `<>` is the ANSI SQL standard, `!=` is more commonly used in practice. Both work in PostgreSQL and MySQL.

---

## Comparing Strings

Strings are compared **lexicographically** (dictionary/alphabetical order):

```sql
-- Names that come after 'C' alphabetically
SELECT name FROM employees WHERE name > 'C';
-- Returns: Charlie, Diana, Eve
```

- `'Bob' < 'Charlie'` → TRUE (B comes before C)
- `'alice' > 'Alice'` → depends on collation (case sensitivity)

> 💡 **PostgreSQL**: String comparisons are **case-sensitive** by default. `'Alice' != 'alice'`. Use `ILIKE` for case-insensitive matching (Module 02).

---

## Comparing Dates

Dates work naturally with comparison operators:

```sql
-- Employees hired after 2021
SELECT name, hire_date
FROM employees
WHERE hire_date > '2021-01-01';
```

| name    | hire_date  |
|---------|------------|
| Charlie | 2021-06-10 |
| Diana   | 2021-08-05 |
| Eve     | 2022-01-12 |

Date format: `'YYYY-MM-DD'` is the universal standard. Always use this format.

---

## Key Points

- `=` for equality (not `==` like in Python/JS)
- `<>` is the SQL standard for "not equal", `!=` also works
- String comparison is case-sensitive in PostgreSQL
- Date strings in `'YYYY-MM-DD'` format are automatically compared correctly
