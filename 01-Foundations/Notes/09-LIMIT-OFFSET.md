# LIMIT & OFFSET — Pagination

Restrict the number of rows returned and skip rows.

---

## LIMIT — Restrict Row Count

```sql
-- Top 3 highest-paid employees
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;
```

| name  | salary |
|-------|--------|
| Alice | 95000  |
| Eve   | 92000  |
| Bob   | 85000  |

---

## OFFSET — Skip Rows

```sql
-- Skip the first 2, then return the next 3
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3 OFFSET 2;
```

| name    | salary |
|---------|--------|
| Bob     | 85000  |
| Charlie | 72000  |
| Diana   | 68000  |

---

## Pagination Pattern

Used to display results page-by-page:

```
Page 1: LIMIT 10 OFFSET 0   (rows 1-10)
Page 2: LIMIT 10 OFFSET 10  (rows 11-20)
Page 3: LIMIT 10 OFFSET 20  (rows 21-30)

Formula: OFFSET = (page_number - 1) * page_size
```

---

## LeetCode Pattern: Nth Highest Value

"Find the Nth highest salary" uses `LIMIT 1 OFFSET N-1`:

```sql
-- Second highest salary
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

| salary |
|--------|
| 92000  |

> This is literally **LeetCode #176: Second Highest Salary**. The full solution requires handling the edge case where there IS no second highest (return NULL), which uses a subquery — we'll revisit this in Module 05.

---

## PostgreSQL Alternative: FETCH

PostgreSQL also supports `FETCH FIRST N ROWS ONLY` (ANSI SQL standard):

```sql
SELECT name FROM employees
ORDER BY salary DESC
FETCH FIRST 3 ROWS ONLY;
```

Equivalent to `LIMIT 3`. `FETCH` is ANSI standard; `LIMIT` is more widely used in practice.

---

## Key Points

- `LIMIT n` — return at most n rows
- `OFFSET m` — skip the first m rows (0-based)
- Always use `ORDER BY` with `LIMIT` — otherwise which rows you get is random
- `LIMIT 1 OFFSET N-1` is the classic "Nth value" pattern
- `FETCH FIRST N ROWS ONLY` is the ANSI-standard alternative
