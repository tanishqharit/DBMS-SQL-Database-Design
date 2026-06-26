# Aliases (AS)

Aliases give temporary names to columns or tables. They make output cleaner and queries more readable.

---

## Column Aliases

```sql
SELECT
    name AS employee_name,
    salary AS current_salary,
    salary * 1.10 AS salary_after_raise
FROM employees;
```

The `AS` keyword is **optional** (but recommended for readability):

```sql
-- These are equivalent:
SELECT name AS employee_name FROM employees;
SELECT name employee_name FROM employees;    -- AS omitted
```

---

## Table Aliases

Essential when working with **JOINs** (Module 04) and **self-referencing queries**:

```sql
SELECT e.name, e.salary
FROM employees AS e
WHERE e.department = 'Engineering';

-- Short form (AS omitted):
SELECT e.name, e.salary
FROM employees e
WHERE e.department = 'Engineering';
```

---

## Common Alias Conventions

| Table | Common Aliases |
|-------|---------------|
| `employees` | `e`, `emp` |
| `departments` | `d`, `dept` |
| `orders` | `o`, `ord` |
| `products` | `p`, `prod` |
| Self-joins | `e1`, `e2` or `a`, `b` |

---

## When Aliases Are Required

1. **Self-joins**: When a table joins with itself, you MUST alias it to distinguish the two copies
2. **Subqueries in FROM**: Derived tables must be aliased (covered in Module 05)
3. **Computed columns**: Giving names to expressions like `salary * 12`

---

## Key Points

- `AS` is optional but recommended for readability
- Column aliases rename output columns
- Table aliases create short references (essential for JOINs)
- Aliases only exist for the duration of the query — they don't change the actual table
