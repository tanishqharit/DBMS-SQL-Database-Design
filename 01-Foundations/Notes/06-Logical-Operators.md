# Logical Operators — AND, OR, NOT

Combine multiple conditions in a `WHERE` clause.

---

## AND — Both Conditions Must Be True

```sql
SELECT name, department, salary
FROM employees
WHERE department = 'Engineering'
  AND salary > 90000;
```

| name  | department  | salary |
|-------|-------------|--------|
| Alice | Engineering | 95000  |
| Eve   | Engineering | 92000  |

---

## OR — At Least One Condition Must Be True

```sql
SELECT name, department
FROM employees
WHERE department = 'Engineering'
   OR department = 'Marketing';
```

| name    | department  |
|---------|-------------|
| Alice   | Engineering |
| Bob     | Engineering |
| Charlie | Marketing   |
| Diana   | Marketing   |
| Eve     | Engineering |

---

## NOT — Reverses the Condition

```sql
SELECT name, department
FROM employees
WHERE NOT department = 'Engineering';
-- Same as: WHERE department != 'Engineering'
```

---

## ⚠️ Operator Precedence — CRITICAL

Precedence (highest to lowest): **`NOT` > `AND` > `OR`**

Always use **parentheses** to make intent clear. This is a **common source of bugs** in interviews.

### Example: The Precedence Trap

```sql
-- WITHOUT parentheses (misleading):
WHERE department = 'Engineering' AND salary > 90000 OR department = 'Marketing'

-- SQL interprets this as:
WHERE (department = 'Engineering' AND salary > 90000) OR (department = 'Marketing')
-- Result: High-paid engineers + ALL marketing employees
```

```sql
-- If you MEANT all Engineering/Marketing employees with salary > 90k:
WHERE (department = 'Engineering' OR department = 'Marketing') AND salary > 90000
-- Result: Only employees in Engineering or Marketing who ALSO earn > 90k
```

> ⚠️ **Interview Rule**: Always use parentheses when mixing AND and OR. Even if the default precedence gives the right answer, parentheses show the interviewer you understand the logic.

---

## Truth Table

| A | B | A AND B | A OR B | NOT A |
|---|---|---------|--------|-------|
| TRUE | TRUE | TRUE | TRUE | FALSE |
| TRUE | FALSE | FALSE | TRUE | FALSE |
| FALSE | TRUE | FALSE | TRUE | TRUE |
| FALSE | FALSE | FALSE | FALSE | TRUE |

With NULL (three-valued logic):

| A | B | A AND B | A OR B |
|---|---|---------|--------|
| TRUE | NULL | NULL | TRUE |
| FALSE | NULL | FALSE | NULL |
| NULL | NULL | NULL | NULL |

---

## Key Points

- `AND` narrows results (more restrictive)
- `OR` broadens results (less restrictive)
- `NOT` inverts the condition
- **Always** use parentheses when combining AND + OR
- NULL with logical operators follows three-valued logic
