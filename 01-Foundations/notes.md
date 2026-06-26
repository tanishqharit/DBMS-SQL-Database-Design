# Module 01: SQL Foundations

> **Goal**: By the end of this module, you should be able to write basic SQL queries — selecting data, filtering rows, sorting results, and handling NULL values. This covers ~30% of LeetCode Easy problems.

---

## Table of Contents

1. [What is SQL?](#1-what-is-sql)
2. [Databases, Tables, Rows, Columns](#2-databases-tables-rows-columns)
3. [SELECT — Retrieving Data](#3-select--retrieving-data)
4. [WHERE — Filtering Rows](#4-where--filtering-rows)
5. [Comparison Operators](#5-comparison-operators)
6. [Logical Operators (AND, OR, NOT)](#6-logical-operators-and-or-not)
7. [DISTINCT — Removing Duplicates](#7-distinct--removing-duplicates)
8. [ORDER BY — Sorting Results](#8-order-by--sorting-results)
9. [LIMIT & OFFSET — Pagination](#9-limit--offset--pagination)
10. [NULL Handling](#10-null-handling)
11. [SQL Execution Order](#11-sql-execution-order--critical)
12. [Aliases (AS)](#12-aliases-as)
13. [Comments in SQL](#13-comments-in-sql)
14. [Practice Problems](#14-practice-problems)

---

## 1. What is SQL?

**SQL** (Structured Query Language) is the standard language for interacting with **relational databases**. It lets you:

- **Query** data (ask questions about your data)
- **Insert** new data
- **Update** existing data
- **Delete** data
- **Create** and modify database structure

### SQL is Declarative

Unlike Python or JavaScript where you tell the computer **how** to do something step-by-step, in SQL you tell the database **what** you want, and it figures out how to get it.

```
-- Python (imperative): You describe HOW
result = []
for row in employees:
    if row.salary > 80000:
        result.append(row.name)

-- SQL (declarative): You describe WHAT
SELECT name FROM employees WHERE salary > 80000;
```

### SQL Dialects

SQL has a standard (ANSI SQL), but each database adds its own extensions:

| Database | Used By | Notes |
|----------|---------|-------|
| **PostgreSQL** 🐘 | Uber, Instagram, Spotify, Reddit | Our focus. Most feature-rich open-source DB |
| **MySQL** | Facebook, Twitter, YouTube | LeetCode uses this by default |
| **SQLite** | Mobile apps, embedded systems | Lightweight, file-based |
| **SQL Server** | Enterprise/Microsoft shops | T-SQL dialect |
| **Oracle** | Banks, large enterprises | PL/SQL dialect |

> 💡 **For LeetCode**: ~95% of syntax is identical across PostgreSQL and MySQL. I'll note differences when they matter.

---

## 2. Databases, Tables, Rows, Columns

Think of a database like a spreadsheet application:

```
Database  =  The entire spreadsheet file (e.g., "company.xlsx")
Table     =  A single sheet (e.g., "employees" sheet)
Column    =  A column header (e.g., "name", "salary")
Row       =  A single record/entry (e.g., Alice's data)
```

### Example: `employees` Table

| id | name    | department  | salary | hire_date  |
|----|---------|-------------|--------|------------|
| 1  | Alice   | Engineering | 95000  | 2020-01-15 |
| 2  | Bob     | Engineering | 85000  | 2020-03-22 |
| 3  | Charlie | Marketing   | 72000  | 2021-06-10 |
| 4  | Diana   | Marketing   | 68000  | 2021-08-05 |
| 5  | Eve     | Engineering | 92000  | 2022-01-12 |

- **5 rows** (5 employees)
- **5 columns** (id, name, department, salary, hire_date)
- Each row is uniquely identified by `id` (this is called a **Primary Key** — more on this in Module 12)

---

## 3. SELECT — Retrieving Data

The `SELECT` statement is the most fundamental SQL command. It retrieves data from a table.

### Syntax

```sql
SELECT column1, column2, ...
FROM table_name;
```

### Examples

**Select specific columns:**
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

**Select ALL columns (use `*`):**
```sql
SELECT *
FROM employees;
```

> ⚠️ **Interview Tip**: Avoid `SELECT *` in production code. It's slower (fetches unnecessary data) and fragile (breaks if columns are added/removed). Always name your columns. However, on LeetCode, `SELECT *` is fine for quick solutions.

**Select with expressions (computed columns):**
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

**Select without a table (useful for quick tests):**
```sql
SELECT 1 + 1 AS result;
SELECT 'Hello' AS greeting;
SELECT CURRENT_DATE AS today;
```

> 🔧 **Try it**: `python3 00-Setup/runner.py -q "SELECT 1 + 1 AS result;"`

---

## 4. WHERE — Filtering Rows

`WHERE` filters rows based on a condition. Only rows where the condition is `TRUE` are included.

### Syntax

```sql
SELECT columns
FROM table_name
WHERE condition;
```

### Examples

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

> ⚠️ **Critical**: SQL uses single quotes `'text'` for string values. Double quotes `"text"` are for column/table names (identifiers). This trips up many beginners.

```sql
WHERE name = 'Alice'        -- ✅ Correct (string value)
WHERE name = "Alice"        -- ❌ Wrong in PostgreSQL (treated as column name)
```

---

## 5. Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `=` | Equal to | `WHERE salary = 85000` |
| `!=` or `<>` | Not equal to | `WHERE department != 'Sales'` |
| `>` | Greater than | `WHERE salary > 80000` |
| `<` | Less than | `WHERE salary < 75000` |
| `>=` | Greater than or equal | `WHERE salary >= 85000` |
| `<=` | Less than or equal | `WHERE salary <= 72000` |

> 💡 **Note**: `!=` and `<>` are equivalent. `<>` is the ANSI SQL standard, `!=` is more commonly used in practice. Both work in PostgreSQL and MySQL.

### Comparing strings

Strings are compared **lexicographically** (alphabetical order):

```sql
-- Names that come after 'C' alphabetically
SELECT name FROM employees WHERE name > 'C';
-- Returns: Charlie, Diana, Eve
```

### Comparing dates

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

---

## 6. Logical Operators (AND, OR, NOT)

Combine multiple conditions using logical operators.

### AND — Both conditions must be true

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

### OR — At least one condition must be true

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

### NOT — Reverses the condition

```sql
SELECT name, department
FROM employees
WHERE NOT department = 'Engineering';
-- Same as: WHERE department != 'Engineering'
```

### Combining operators (use parentheses!)

```sql
-- Engineering employees earning > 90k OR any Marketing employee
SELECT name, department, salary
FROM employees
WHERE (department = 'Engineering' AND salary > 90000)
   OR department = 'Marketing';
```

> ⚠️ **Operator Precedence**: `NOT` > `AND` > `OR`. Always use parentheses to make intent clear. This is a **common source of bugs** in interviews.

```sql
-- WITHOUT parentheses (misleading):
WHERE department = 'Engineering' AND salary > 90000 OR department = 'Marketing'
-- This is interpreted as:
WHERE (department = 'Engineering' AND salary > 90000) OR (department = 'Marketing')

-- If you MEANT all Engineering/Marketing employees with salary > 90k:
WHERE (department = 'Engineering' OR department = 'Marketing') AND salary > 90000
```

---

## 7. DISTINCT — Removing Duplicates

`DISTINCT` removes duplicate rows from the result.

```sql
-- All unique departments
SELECT DISTINCT department
FROM employees;
```
| department  |
|-------------|
| Engineering |
| Marketing   |

```sql
-- DISTINCT on multiple columns = unique combinations
SELECT DISTINCT department, salary
FROM employees;
```

This returns unique `(department, salary)` pairs, not unique departments or unique salaries separately.

> 💡 **Interview Tip**: `COUNT(DISTINCT column)` is extremely common in LeetCode problems. We'll cover this in Module 03 (Aggregations).

---

## 8. ORDER BY — Sorting Results

`ORDER BY` sorts the result set. Without it, SQL **does not guarantee** any particular row order.

### Syntax

```sql
SELECT columns
FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;
```

- `ASC` — Ascending (default, smallest first: A→Z, 1→9, oldest→newest)
- `DESC` — Descending (largest first: Z→A, 9→1, newest→oldest)

### Examples

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

```sql
-- Multi-column sort: by department (A-Z), then salary (high to low) within each department
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

**Sorting by column position (number):**

```sql
-- Sort by the 3rd column in the SELECT list
SELECT name, department, salary
FROM employees
ORDER BY 3 DESC;    -- Same as ORDER BY salary DESC
```

> ⚠️ **Interview Tip**: Avoid positional ordering (`ORDER BY 3`) in production — it's fragile and hard to read. But it's fine for quick LeetCode solutions.

**NULLs in ORDER BY:**

By default in PostgreSQL, `NULL`s sort **last** in `ASC` and **first** in `DESC`. You can control this:

```sql
ORDER BY column ASC NULLS FIRST    -- NULLs come first
ORDER BY column ASC NULLS LAST     -- NULLs come last (PostgreSQL default for ASC)
ORDER BY column DESC NULLS FIRST   -- NULLs come first (PostgreSQL default for DESC)
ORDER BY column DESC NULLS LAST    -- NULLs come last
```

> 💡 **MySQL difference**: MySQL sorts NULLs as the smallest value (first in ASC, last in DESC). PostgreSQL gives you `NULLS FIRST/LAST` for explicit control.

---

## 9. LIMIT & OFFSET — Pagination

### LIMIT — Restrict number of rows returned

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

### OFFSET — Skip rows before returning

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

This is commonly used for **pagination** (page 1, page 2, etc.):

```
Page 1: LIMIT 10 OFFSET 0   (rows 1-10)
Page 2: LIMIT 10 OFFSET 10  (rows 11-20)
Page 3: LIMIT 10 OFFSET 20  (rows 21-30)
```

> 💡 **LeetCode pattern**: "Find the Nth highest salary" often uses `LIMIT 1 OFFSET N-1` combined with `ORDER BY salary DESC`.

```sql
-- Second highest salary
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

> 💡 **PostgreSQL alternative**: PostgreSQL also supports `FETCH FIRST N ROWS ONLY` (ANSI SQL standard):
> ```sql
> SELECT name FROM employees ORDER BY salary DESC FETCH FIRST 3 ROWS ONLY;
> ```

---

## 10. NULL Handling

`NULL` means **unknown/missing value**. It is NOT the same as `0`, `''` (empty string), or `'NULL'` (the string).

### The Golden Rule: NULL is Not Equal to Anything

```sql
-- ❌ This will NEVER return rows, even if manager_id IS null
SELECT * FROM employees WHERE manager_id = NULL;

-- ✅ Correct way
SELECT * FROM employees WHERE manager_id IS NULL;
SELECT * FROM employees WHERE manager_id IS NOT NULL;
```

> ⚠️ **This is the #1 NULL trap in interviews**. `NULL = NULL` evaluates to `NULL` (unknown), not `TRUE`. Any comparison with NULL returns NULL, which is treated as FALSE in WHERE clauses.

### Three-Valued Logic

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

### COALESCE — Replace NULL with a default value

```sql
SELECT
    name,
    manager_id,
    COALESCE(manager_id, 0) AS manager_id_or_zero,
    COALESCE(manager_id, -1) AS manager_id_or_neg1
FROM employees;
```

`COALESCE(a, b, c, ...)` returns the **first non-NULL** value:

```sql
SELECT COALESCE(NULL, NULL, 'hello', 'world');
-- Result: 'hello'
```

### NULLIF — Return NULL if two values are equal

```sql
SELECT NULLIF(10, 10);   -- Returns NULL (because 10 = 10)
SELECT NULLIF(10, 20);   -- Returns 10 (because 10 ≠ 20)
```

**Common use**: Prevent division by zero:
```sql
-- Without NULLIF: crashes if count is 0
SELECT total / count AS average FROM stats;

-- With NULLIF: returns NULL instead of error
SELECT total / NULLIF(count, 0) AS average FROM stats;
```

### NULL in Aggregations

- `COUNT(*)` counts all rows, including those with NULLs
- `COUNT(column)` counts only non-NULL values in that column
- `SUM`, `AVG`, `MIN`, `MAX` all **ignore NULLs**

```sql
-- If salary has some NULLs:
SELECT
    COUNT(*)        AS total_rows,       -- Counts ALL rows
    COUNT(salary)   AS non_null_count,   -- Counts only rows where salary is not NULL
    AVG(salary)     AS avg_salary        -- Average of non-NULL salaries only
FROM employees;
```

---

## 11. SQL Execution Order ⭐ (CRITICAL)

This is one of the **most important concepts** in SQL. The query is NOT executed in the order you write it.

### Written Order vs. Execution Order

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

### The Execution Pipeline

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

### Why This Matters

**You can't use a column alias in WHERE** (because SELECT runs AFTER WHERE):

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

**You CAN use a column alias in ORDER BY** (because ORDER BY runs AFTER SELECT):

```sql
-- ✅ This works
SELECT salary * 12 AS annual
FROM employees
ORDER BY annual DESC;
```

> 💡 **PostgreSQL bonus**: PostgreSQL allows aliases in `GROUP BY` and `ORDER BY`, but NOT in `WHERE` or `HAVING`. MySQL is more lenient and allows aliases in `HAVING`.

> ⚠️ **Interview favorite**: "Why can't you use a column alias in WHERE?" — Answer: Because WHERE is evaluated before SELECT in the execution order.

---

## 12. Aliases (AS)

Aliases give temporary names to columns or tables. They make output cleaner and queries more readable.

### Column Aliases

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

### Table Aliases

Table aliases are essential when working with **JOINs** (Module 04) and **self-referencing queries**:

```sql
SELECT e.name, e.salary
FROM employees AS e
WHERE e.department = 'Engineering';

-- Short form (AS omitted):
SELECT e.name, e.salary
FROM employees e
WHERE e.department = 'Engineering';
```

> 💡 **Convention**: Use short, meaningful table aliases. Common patterns:
> - `employees e` or `employees emp`
> - `departments d` or `departments dept`
> - For self-joins: `e1`, `e2` (covered in Module 04)

---

## 13. Comments in SQL

```sql
-- This is a single-line comment

/* This is a
   multi-line comment */

SELECT
    name,          -- employee's full name
    salary         /* monthly salary in USD */
FROM employees;
```

---

## 14. Practice Problems

Try each problem yourself first, then expand the solution to check your answer.

### Setup: Creating Practice Data

Run this in the runner to set up the practice tables:

```sql
-- Run: python3 00-Setup/runner.py
-- Then paste this to set up the practice data:

CREATE TABLE IF NOT EXISTS employees (
    id          INTEGER PRIMARY KEY,
    name        VARCHAR NOT NULL,
    department  VARCHAR,
    salary      DECIMAL(10,2),
    manager_id  INTEGER,
    hire_date   DATE
);

INSERT INTO employees VALUES
    (1, 'Alice',   'Engineering', 95000,  NULL, '2020-01-15'),
    (2, 'Bob',     'Engineering', 85000,  1,    '2020-03-22'),
    (3, 'Charlie', 'Marketing',   72000,  1,    '2021-06-10'),
    (4, 'Diana',   'Marketing',   68000,  3,    '2021-08-05'),
    (5, 'Eve',     'Engineering', 92000,  1,    '2022-01-12'),
    (6, 'Frank',   'Sales',       78000,  NULL, '2019-11-30'),
    (7, 'Grace',   'Sales',       71000,  6,    '2023-02-14'),
    (8, 'Hank',    'Engineering', 88000,  1,    '2023-05-01');
```

---

### Problem 1: Basic SELECT ⭐ (Easy)

**Question**: Select the name and salary of all employees. Sort by name alphabetically.

<details>
<summary>💡 Hint</summary>

Use `SELECT` with specific columns and `ORDER BY`.

</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT name, salary
FROM employees
ORDER BY name ASC;
```

**Result:**
| name    | salary |
|---------|--------|
| Alice   | 95000  |
| Bob     | 85000  |
| Charlie | 72000  |
| Diana   | 68000  |
| Eve     | 92000  |
| Frank   | 78000  |
| Grace   | 71000  |
| Hank    | 88000  |

**Explanation**: `SELECT name, salary` picks only those two columns. `ORDER BY name ASC` sorts alphabetically (A→Z). `ASC` is optional since it's the default.

</details>

---

### Problem 2: WHERE Filtering ⭐ (Easy)

**Question**: Find all employees who earn more than $80,000. Show their name, department, and salary. Sort by salary descending.

<details>
<summary>💡 Hint</summary>

Use `WHERE` with the `>` operator.

</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT name, department, salary
FROM employees
WHERE salary > 80000
ORDER BY salary DESC;
```

**Result:**
| name  | department  | salary |
|-------|-------------|--------|
| Alice | Engineering | 95000  |
| Eve   | Engineering | 92000  |
| Hank  | Engineering | 88000  |
| Bob   | Engineering | 85000  |

**Explanation**: `WHERE salary > 80000` filters out anyone earning 80k or less. The 4 remaining employees are all in Engineering — makes sense, tech pays well! 😄

</details>

---

### Problem 3: AND + OR ⭐ (Easy)

**Question**: Find employees who are either in Engineering with salary > $90,000 OR in Marketing. Show name, department, salary.

<details>
<summary>💡 Hint</summary>

Use parentheses to group the AND condition, then OR with the second condition.

</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT name, department, salary
FROM employees
WHERE (department = 'Engineering' AND salary > 90000)
   OR department = 'Marketing';
```

**Result:**
| name    | department  | salary |
|---------|-------------|--------|
| Alice   | Engineering | 95000  |
| Charlie | Marketing   | 72000  |
| Diana   | Marketing   | 68000  |
| Eve     | Engineering | 92000  |

**Explanation**: Parentheses are crucial here. Without them, `AND` binds tighter than `OR`, so you'd accidentally get the same result in this case — but building the habit of using parentheses prevents bugs in complex queries.

</details>

---

### Problem 4: DISTINCT ⭐ (Easy)

**Question**: List all unique departments in the company. Sort alphabetically.

<details>
<summary>💡 Hint</summary>

Use `SELECT DISTINCT`.

</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT DISTINCT department
FROM employees
ORDER BY department;
```

**Result:**
| department  |
|-------------|
| Engineering |
| Marketing   |
| Sales       |

**Explanation**: Without `DISTINCT`, Engineering would appear 4 times (once for each Engineering employee). `DISTINCT` collapses duplicates.

</details>

---

### Problem 5: NULL Handling ⭐⭐ (Easy-Medium)

**Question**: Find all employees who do NOT have a manager (manager_id is NULL). Show their name and department.

<details>
<summary>💡 Hint</summary>

Remember: you cannot use `= NULL`. Use `IS NULL`.

</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT name, department
FROM employees
WHERE manager_id IS NULL;
```

**Result:**
| name  | department  |
|-------|-------------|
| Alice | Engineering |
| Frank | Sales       |

**Explanation**: These are the two top-level managers (no one manages them). The key trap: `WHERE manager_id = NULL` would return **zero rows** because `NULL = NULL` evaluates to `NULL`, not TRUE.

</details>

---

### Problem 6: COALESCE ⭐⭐ (Easy-Medium)

**Question**: Show each employee's name and their manager's ID, but replace NULL manager_ids with the text 'No Manager'.

<details>
<summary>💡 Hint</summary>

Use `COALESCE` to provide a default value. You may need to cast the integer to text first.

</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT
    name,
    COALESCE(CAST(manager_id AS VARCHAR), 'No Manager') AS manager_info
FROM employees;
```

Or using PostgreSQL's `::` cast shorthand:
```sql
SELECT
    name,
    COALESCE(manager_id::VARCHAR, 'No Manager') AS manager_info
FROM employees;
```

**Result:**
| name    | manager_info |
|---------|-------------|
| Alice   | No Manager  |
| Bob     | 1           |
| Charlie | 1           |
| Diana   | 3           |
| Eve     | 1           |
| Frank   | No Manager  |
| Grace   | 6           |
| Hank    | 1           |

**Explanation**: `COALESCE` returns the first non-NULL argument. Since `manager_id` is an INTEGER and `'No Manager'` is a string, we need to cast the integer to VARCHAR first so both arguments have the same type.

</details>

---

### Problem 7: LIMIT + ORDER BY ⭐⭐ (Medium — LeetCode Classic!)

**Question**: Find the **second highest salary** in the company. Return just the salary value.

<details>
<summary>💡 Hint</summary>

Sort salaries descending, skip the first one, take the next one. Think about edge cases: what if there are duplicate highest salaries?

</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

**Result:**
| salary |
|--------|
| 92000  |

**Explanation**:
1. `DISTINCT salary` removes duplicate salary values (e.g., if two people earned 95000)
2. `ORDER BY salary DESC` puts the highest salary first
3. `LIMIT 1 OFFSET 1` skips the first row (95000) and returns the next one (92000)

> This is literally **LeetCode Problem #176: Second Highest Salary**. The full solution requires handling the edge case where there IS no second highest (return NULL), which uses a subquery — we'll revisit this in Module 05.

</details>

---

### Problem 8: Execution Order ⭐⭐ (Medium — Conceptual)

**Question**: Will this query work? If not, why? If yes, what does it return?

```sql
SELECT name, salary * 12 AS annual_salary
FROM employees
WHERE annual_salary > 1000000
ORDER BY annual_salary DESC;
```

<details>
<summary>✅ Solution</summary>

**This will NOT work.** It will throw an error: `column "annual_salary" does not exist`.

**Why?** Because of SQL execution order:
1. `FROM employees` — get the table ✅
2. `WHERE annual_salary > 1000000` — tries to filter, but `annual_salary` alias doesn't exist yet because SELECT hasn't run ❌

**The fix:**
```sql
SELECT name, salary * 12 AS annual_salary
FROM employees
WHERE salary * 12 > 1000000
ORDER BY annual_salary DESC;
```

Note: `ORDER BY annual_salary` works because ORDER BY runs AFTER SELECT.

</details>

---

### Problem 9: Combined Concepts ⭐⭐ (Medium)

**Question**: Find the top 3 highest-paid employees who were hired after 2020. Show their name, salary, hire date, and a column called `seniority` that shows 'Senior' if hired before 2022, and 'Junior' otherwise. Sort by salary descending.

<details>
<summary>💡 Hint</summary>

Combine `WHERE` for date filtering, `CASE WHEN` for conditional logic (we'll cover this deeply in Module 02, but here's an early preview), `ORDER BY` + `LIMIT`.

</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT
    name,
    salary,
    hire_date,
    CASE
        WHEN hire_date < '2022-01-01' THEN 'Senior'
        ELSE 'Junior'
    END AS seniority
FROM employees
WHERE hire_date > '2020-12-31'
ORDER BY salary DESC
LIMIT 3;
```

**Result:**
| name    | salary | hire_date  | seniority |
|---------|--------|------------|-----------|
| Eve     | 92000  | 2022-01-12 | Junior    |
| Hank    | 88000  | 2023-05-01 | Junior    |
| Charlie | 72000  | 2021-06-10 | Senior    |

**Explanation**:
1. `WHERE hire_date > '2020-12-31'` excludes Alice (2020-01-15) and Bob (2020-03-22)
2. `CASE WHEN` creates a conditional column — like an if-else
3. `ORDER BY salary DESC LIMIT 3` gets the top 3 from the filtered results

> This is a **preview** of `CASE WHEN` — we'll go deep on it in Module 02.

</details>

---

### Problem 10: NULL Gotcha ⭐⭐⭐ (Medium — Tricky!)

**Question**: How many rows does this query return? Explain why.

```sql
SELECT * FROM employees
WHERE manager_id NOT IN (1, 3, 999);
```

<details>
<summary>💡 Hint</summary>

Think about what happens when `manager_id` is NULL. What does `NULL NOT IN (...)` evaluate to?

</details>

<details>
<summary>✅ Solution</summary>

**Returns 1 row** (only Grace, whose manager_id = 6).

Let's trace through each employee:
- Alice: `NULL NOT IN (1, 3, 999)` → `NULL` → filtered out ❌
- Bob: `1 NOT IN (1, 3, 999)` → `FALSE` → filtered out ❌
- Charlie: `1 NOT IN (1, 3, 999)` → `FALSE` → filtered out ❌
- Diana: `3 NOT IN (1, 3, 999)` → `FALSE` → filtered out ❌
- Eve: `1 NOT IN (1, 3, 999)` → `FALSE` → filtered out ❌
- Frank: `NULL NOT IN (1, 3, 999)` → `NULL` → filtered out ❌
- **Grace**: `6 NOT IN (1, 3, 999)` → `TRUE` → **included** ✅
- Hank: `1 NOT IN (1, 3, 999)` → `FALSE` → filtered out ❌

**The trap**: Alice and Frank have `NULL` manager_ids. `NULL NOT IN (...)` doesn't return TRUE — it returns NULL, which is treated as FALSE. So they're excluded even though you might expect them to be included.

**Safe alternatives:**
```sql
-- Option 1: Explicitly handle NULLs
WHERE manager_id NOT IN (1, 3, 999) OR manager_id IS NULL;

-- Option 2: Use NOT EXISTS (safest, covered in Module 05)
```

> ⚠️ **This is a CLASSIC interview trap.** Always be careful with `NOT IN` when the column can contain NULLs. `NOT EXISTS` is generally safer (Module 05).

</details>

---

## 🎯 Module 01 Summary

| Concept | Key Syntax | Watch Out For |
|---------|-----------|---------------|
| SELECT | `SELECT col1, col2 FROM table` | Avoid `SELECT *` in production |
| WHERE | `WHERE condition` | Single quotes for strings, not double |
| Comparison | `=, !=, <>, >, <, >=, <=` | `<>` is the ANSI standard for "not equal" |
| Logic | `AND, OR, NOT` | Precedence: NOT > AND > OR. Use parentheses! |
| DISTINCT | `SELECT DISTINCT col` | Applies to all selected columns combined |
| ORDER BY | `ORDER BY col ASC/DESC` | Without it, order is NOT guaranteed |
| LIMIT | `LIMIT n OFFSET m` | OFFSET is 0-based (skip m rows) |
| NULL | `IS NULL, IS NOT NULL` | Never use `= NULL` or `!= NULL` |
| COALESCE | `COALESCE(val, default)` | Returns first non-NULL argument |
| Execution Order | FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY→LIMIT | Can't use aliases in WHERE |

### What's Next?

**Module 02: Filtering & Pattern Matching** — We'll dive deep into `LIKE`, `IN`, `BETWEEN`, `CASE WHEN`, and type casting. These show up in almost every LeetCode problem.
