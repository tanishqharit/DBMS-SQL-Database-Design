# ORDER BY — Sorting Results

`ORDER BY` sorts the result set. **Without it, SQL does NOT guarantee any particular row order.**

---

## Syntax

```sql
SELECT columns
FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;
```

- `ASC` — Ascending (default): smallest first → A→Z, 1→9, oldest→newest
- `DESC` — Descending: largest first → Z→A, 9→1, newest→oldest

---

## Single Column Sort

```sql
-- Sort by salary, highest first
SELECT name, salary
FROM employees
ORDER BY salary DESC;
```

| name    | salary |
|---------|--------|
| Alice   | 95000  |
| Eve     | 92000  |
| Bob     | 85000  |
| Charlie | 72000  |
| Diana   | 68000  |

---

## Multi-Column Sort

When the first column has ties, the second column breaks them:

```sql
-- By department (A-Z), then salary (high to low) within each department
SELECT name, department, salary
FROM employees
ORDER BY department ASC, salary DESC;
```

| name    | department  | salary |
|---------|-------------|--------|
| Alice   | Engineering | 95000  |
| Eve     | Engineering | 92000  |
| Bob     | Engineering | 85000  |
| Charlie | Marketing   | 72000  |
| Diana   | Marketing   | 68000  |

---

## Sorting by Column Position

```sql
-- Sort by the 3rd column in the SELECT list
SELECT name, department, salary
FROM employees
ORDER BY 3 DESC;    -- Same as ORDER BY salary DESC
```

> ⚠️ Avoid positional ordering in production — it's fragile and hard to read. Fine for quick LeetCode solutions.

---

## NULLs in ORDER BY

**PostgreSQL default**: NULLs sort **last** in ASC, **first** in DESC.

You can control this explicitly:

```sql
ORDER BY column ASC NULLS FIRST    -- NULLs come first
ORDER BY column ASC NULLS LAST     -- NULLs come last (PostgreSQL default for ASC)
ORDER BY column DESC NULLS FIRST   -- NULLs come first (PostgreSQL default for DESC)
ORDER BY column DESC NULLS LAST    -- NULLs come last
```

> 💡 **MySQL difference**: MySQL treats NULLs as the smallest value (first in ASC, last in DESC). MySQL doesn't support `NULLS FIRST/LAST`. PostgreSQL gives you explicit control.

---

## Key Points

- **Without ORDER BY, row order is random** — never assume order
- `ASC` is the default (can be omitted)
- Multi-column: sorts by first column, then uses second column to break ties
- PostgreSQL lets you control NULL placement with `NULLS FIRST/LAST`
- You can use column aliases from SELECT in ORDER BY (because ORDER BY runs after SELECT)
