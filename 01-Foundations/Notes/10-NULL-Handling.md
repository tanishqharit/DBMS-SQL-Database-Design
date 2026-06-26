# NULL Handling

`NULL` means **unknown/missing value**. It is NOT the same as `0`, `''` (empty string), or `'NULL'` (the string).

---

## The Golden Rule: NULL is Not Equal to Anything

```sql
-- ❌ This will NEVER return rows, even if manager_id IS null
SELECT * FROM employees WHERE manager_id = NULL;

-- ✅ Correct way
SELECT * FROM employees WHERE manager_id IS NULL;
SELECT * FROM employees WHERE manager_id IS NOT NULL;
```

> ⚠️ **This is the #1 NULL trap in interviews.** `NULL = NULL` evaluates to `NULL` (unknown), not `TRUE`. Any comparison with NULL returns NULL, which is treated as FALSE in WHERE.

---

## Three-Valued Logic

SQL uses **three-valued logic**: TRUE, FALSE, and NULL (unknown).

| Expression | Result |
|-----------|--------|
| `NULL = NULL` | NULL |
| `NULL != NULL` | NULL |
| `NULL > 5` | NULL |
| `NULL = 0` | NULL |
| `NULL AND TRUE` | NULL |
| `NULL AND FALSE` | FALSE |
| `NULL OR TRUE` | TRUE |
| `NULL OR FALSE` | NULL |
| `NOT NULL` | NULL |

**Mental model**: NULL means "I don't know." Is unknown equal to unknown? I don't know. Is unknown greater than 5? I don't know.

---

## COALESCE — Replace NULL with a Default

`COALESCE(a, b, c, ...)` returns the **first non-NULL** value:

```sql
SELECT
    name,
    manager_id,
    COALESCE(manager_id, 0) AS manager_id_or_zero
FROM employees;
```

Multiple fallbacks:
```sql
SELECT COALESCE(NULL, NULL, 'hello', 'world');
-- Result: 'hello' (first non-NULL)
```

---

## NULLIF — Return NULL if Values Are Equal

```sql
SELECT NULLIF(10, 10);   -- Returns NULL (because 10 = 10)
SELECT NULLIF(10, 20);   -- Returns 10  (because 10 ≠ 20)
```

**Common use**: Prevent division by zero:
```sql
-- Without NULLIF: crashes if count is 0
SELECT total / count AS average FROM stats;

-- With NULLIF: returns NULL instead of error
SELECT total / NULLIF(count, 0) AS average FROM stats;
```

---

## NULL in Aggregations

| Function | NULL Behavior |
|----------|--------------|
| `COUNT(*)` | Counts **all** rows, including NULLs |
| `COUNT(column)` | Counts only **non-NULL** values |
| `SUM(column)` | Ignores NULLs |
| `AVG(column)` | Ignores NULLs (averages only non-NULL values) |
| `MIN(column)` | Ignores NULLs |
| `MAX(column)` | Ignores NULLs |

```sql
SELECT
    COUNT(*)           AS total_rows,       -- Counts ALL rows
    COUNT(manager_id)  AS has_manager,      -- Only non-NULL
    COUNT(*) - COUNT(manager_id) AS no_manager  -- The difference = NULLs
FROM employees;
```

---

## Key Points

- **Never** use `= NULL` or `!= NULL`. Use `IS NULL` / `IS NOT NULL`
- `NULL = NULL` → NULL (not TRUE)
- `COALESCE(val, default)` — replace NULL with a fallback
- `NULLIF(a, b)` — return NULL if a = b (useful for division-by-zero protection)
- Aggregate functions (SUM, AVG, etc.) **skip** NULL values
- `COUNT(*)` counts all rows; `COUNT(column)` counts non-NULLs
