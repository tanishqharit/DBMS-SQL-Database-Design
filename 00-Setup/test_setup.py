#!/usr/bin/env python3
"""
Test Setup — Verifies that the SQL learning environment is fully working.

Run: python3 test_setup.py

Tests:
  1. DuckDB connection
  2. CREATE TABLE + INSERT
  3. Basic SELECT + WHERE
  4. JOINs
  5. GROUP BY + aggregations
  6. Window functions (ROW_NUMBER, RANK, LAG)
  7. CTEs (WITH clause)
  8. Subqueries
  9. String functions
  10. Date functions
"""

import sys
import duckdb

# ─────────────────────────────────────────────
# Test infrastructure
# ─────────────────────────────────────────────
PASSED = 0
FAILED = 0


def test(name, fn):
    """Run a test function and track pass/fail."""
    global PASSED, FAILED
    try:
        fn()
        PASSED += 1
        print(f"  ✅ PASS — {name}")
    except Exception as e:
        FAILED += 1
        print(f"  ❌ FAIL — {name}")
        print(f"           Error: {e}")


# ─────────────────────────────────────────────
# Setup: Create sample tables
# ─────────────────────────────────────────────
conn = duckdb.connect(":memory:")

# Create sample data that mimics common LeetCode table structures
conn.execute("""
    CREATE TABLE employees (
        id          INTEGER PRIMARY KEY,
        name        VARCHAR NOT NULL,
        department  VARCHAR,
        salary      DECIMAL(10,2),
        manager_id  INTEGER,
        hire_date   DATE
    );
""")

conn.execute("""
    INSERT INTO employees VALUES
        (1, 'Alice',   'Engineering', 95000,  NULL, '2020-01-15'),
        (2, 'Bob',     'Engineering', 85000,  1,    '2020-03-22'),
        (3, 'Charlie', 'Marketing',   72000,  1,    '2021-06-10'),
        (4, 'Diana',   'Marketing',   68000,  3,    '2021-08-05'),
        (5, 'Eve',     'Engineering', 92000,  1,    '2022-01-12'),
        (6, 'Frank',   'Sales',       78000,  NULL, '2019-11-30'),
        (7, 'Grace',   'Sales',       71000,  6,    '2023-02-14'),
        (8, 'Hank',    'Engineering', 88000,  1,    '2023-05-01');
""")

conn.execute("""
    CREATE TABLE departments (
        name    VARCHAR PRIMARY KEY,
        budget  DECIMAL(12,2),
        floor   INTEGER
    );
""")

conn.execute("""
    INSERT INTO departments VALUES
        ('Engineering', 500000, 3),
        ('Marketing',   200000, 2),
        ('Sales',       300000, 1),
        ('HR',          150000, 2);
""")

conn.execute("""
    CREATE TABLE projects (
        id          INTEGER PRIMARY KEY,
        name        VARCHAR,
        employee_id INTEGER,
        start_date  DATE,
        end_date    DATE
    );
""")

conn.execute("""
    INSERT INTO projects VALUES
        (1, 'Project Alpha',   1, '2023-01-01', '2023-06-30'),
        (2, 'Project Beta',    2, '2023-03-01', '2023-09-30'),
        (3, 'Project Gamma',   3, '2023-02-15', '2023-08-15'),
        (4, 'Project Delta',   5, '2023-04-01', NULL),
        (5, 'Project Epsilon', 1, '2023-07-01', '2023-12-31');
""")


# ─────────────────────────────────────────────
# Tests
# ─────────────────────────────────────────────
print()
print("╔══════════════════════════════════════════╗")
print("║   🧪 SQL Environment — Test Suite        ║")
print("╠══════════════════════════════════════════╣")
print()


# Test 1: Connection
def test_connection():
    result = conn.execute("SELECT 1 AS connected;").fetchone()
    assert result[0] == 1, "Connection failed"

test("DuckDB connection", test_connection)


# Test 2: Table creation + data
def test_tables():
    count = conn.execute("SELECT COUNT(*) FROM employees;").fetchone()[0]
    assert count == 8, f"Expected 8 employees, got {count}"

test("CREATE TABLE + INSERT (8 rows)", test_tables)


# Test 3: SELECT + WHERE
def test_select_where():
    rows = conn.execute("""
        SELECT name, salary
        FROM employees
        WHERE salary > 80000
        ORDER BY salary DESC;
    """).fetchall()
    assert len(rows) == 4, f"Expected 4 rows, got {len(rows)}"
    assert rows[0][0] == "Alice", f"Expected Alice first, got {rows[0][0]}"

test("SELECT + WHERE + ORDER BY", test_select_where)


# Test 4: JOINs
def test_joins():
    rows = conn.execute("""
        SELECT e.name, d.budget
        FROM employees e
        INNER JOIN departments d ON e.department = d.name
        WHERE d.budget > 250000;
    """).fetchall()
    assert len(rows) == 6, f"Expected 6 (Engineering=4 + Sales=2), got {len(rows)}"

test("INNER JOIN", test_joins)


def test_left_join():
    rows = conn.execute("""
        SELECT d.name, COUNT(e.id) AS emp_count
        FROM departments d
        LEFT JOIN employees e ON d.name = e.department
        GROUP BY d.name
        ORDER BY d.name;
    """).fetchall()
    # HR has 0 employees
    hr_row = [r for r in rows if r[0] == "HR"][0]
    assert hr_row[1] == 0, f"HR should have 0 employees, got {hr_row[1]}"

test("LEFT JOIN (including empty department)", test_left_join)


def test_self_join():
    rows = conn.execute("""
        SELECT e.name AS employee, m.name AS manager
        FROM employees e
        LEFT JOIN employees m ON e.manager_id = m.id
        WHERE m.name IS NOT NULL
        ORDER BY e.name;
    """).fetchall()
    assert len(rows) == 6, f"Expected 6 employees with managers, got {len(rows)}"

test("Self-JOIN (employee → manager)", test_self_join)


# Test 5: GROUP BY + Aggregations
def test_aggregations():
    rows = conn.execute("""
        SELECT
            department,
            COUNT(*) AS headcount,
            ROUND(AVG(salary), 2) AS avg_salary,
            MAX(salary) AS max_salary
        FROM employees
        GROUP BY department
        HAVING COUNT(*) >= 2
        ORDER BY avg_salary DESC;
    """).fetchall()
    assert len(rows) == 3, f"Expected 3 departments, got {len(rows)}"

test("GROUP BY + HAVING + AVG/MAX", test_aggregations)


# Test 6: Window functions
def test_row_number():
    rows = conn.execute("""
        SELECT
            name,
            department,
            salary,
            ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_in_dept
        FROM employees;
    """).fetchall()
    assert len(rows) == 8, f"Expected 8 rows, got {len(rows)}"

test("Window: ROW_NUMBER() OVER (PARTITION BY)", test_row_number)


def test_rank():
    rows = conn.execute("""
        SELECT
            name,
            salary,
            RANK() OVER (ORDER BY salary DESC) AS salary_rank,
            DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_salary_rank
        FROM employees;
    """).fetchall()
    assert rows[0][2] == 1, "Top salary should have rank 1"

test("Window: RANK() and DENSE_RANK()", test_rank)


def test_lag_lead():
    rows = conn.execute("""
        SELECT
            name,
            salary,
            LAG(salary) OVER (ORDER BY salary) AS prev_salary,
            LEAD(salary) OVER (ORDER BY salary) AS next_salary
        FROM employees
        ORDER BY salary;
    """).fetchall()
    # First row should have NULL lag
    assert rows[0][2] is None, "First row LAG should be NULL"
    # Last row should have NULL lead
    assert rows[-1][3] is None, "Last row LEAD should be NULL"

test("Window: LAG() and LEAD()", test_lag_lead)


def test_running_total():
    rows = conn.execute("""
        SELECT
            name,
            salary,
            SUM(salary) OVER (ORDER BY hire_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
        FROM employees
        ORDER BY hire_date;
    """).fetchall()
    # Running total of last row should equal total salary
    total = conn.execute("SELECT SUM(salary) FROM employees;").fetchone()[0]
    assert rows[-1][2] == total, f"Running total mismatch: {rows[-1][2]} vs {total}"

test("Window: Running total with SUM() OVER", test_running_total)


# Test 7: CTEs
def test_cte():
    rows = conn.execute("""
        WITH dept_stats AS (
            SELECT
                department,
                AVG(salary) AS avg_salary
            FROM employees
            GROUP BY department
        )
        SELECT e.name, e.salary, ds.avg_salary
        FROM employees e
        JOIN dept_stats ds ON e.department = ds.department
        WHERE e.salary > ds.avg_salary
        ORDER BY e.name;
    """).fetchall()
    assert len(rows) > 0, "Expected at least one employee above dept average"

test("CTE (WITH clause)", test_cte)


def test_recursive_cte():
    rows = conn.execute("""
        WITH RECURSIVE numbers AS (
            SELECT 1 AS n
            UNION ALL
            SELECT n + 1 FROM numbers WHERE n < 10
        )
        SELECT * FROM numbers;
    """).fetchall()
    assert len(rows) == 10, f"Expected 10 numbers, got {len(rows)}"
    assert rows[-1][0] == 10, f"Expected last number to be 10, got {rows[-1][0]}"

test("Recursive CTE (generate 1-10)", test_recursive_cte)


# Test 8: Subqueries
def test_subquery():
    rows = conn.execute("""
        SELECT name, salary
        FROM employees
        WHERE salary > (SELECT AVG(salary) FROM employees)
        ORDER BY salary DESC;
    """).fetchall()
    assert len(rows) > 0, "Expected employees above average salary"

test("Subquery (scalar in WHERE)", test_subquery)


def test_correlated_subquery():
    rows = conn.execute("""
        SELECT name, department, salary
        FROM employees e1
        WHERE salary = (
            SELECT MAX(salary)
            FROM employees e2
            WHERE e2.department = e1.department
        )
        ORDER BY salary DESC;
    """).fetchall()
    assert len(rows) >= 3, "Expected at least 3 dept top earners"

test("Correlated subquery (top earner per dept)", test_correlated_subquery)


def test_exists():
    rows = conn.execute("""
        SELECT e.name
        FROM employees e
        WHERE EXISTS (
            SELECT 1 FROM projects p WHERE p.employee_id = e.id
        )
        ORDER BY e.name;
    """).fetchall()
    assert len(rows) > 0, "Expected employees with projects"

test("EXISTS subquery", test_exists)


# Test 9: String functions
def test_strings():
    rows = conn.execute("""
        SELECT
            UPPER('hello') AS upper_val,
            LOWER('WORLD') AS lower_val,
            LENGTH('DuckDB') AS len_val,
            CONCAT('Hello', ' ', 'World') AS concat_val,
            SUBSTRING('PostgreSQL' FROM 1 FOR 8) AS substr_val,
            REPLACE('Hello World', 'World', 'SQL') AS replace_val,
            TRIM('  spaces  ') AS trim_val;
    """).fetchone()
    assert rows[0] == "HELLO", f"UPPER failed: {rows[0]}"
    assert rows[1] == "world", f"LOWER failed: {rows[1]}"
    assert rows[2] == 6, f"LENGTH failed: {rows[2]}"
    assert rows[3] == "Hello World", f"CONCAT failed: {rows[3]}"

test("String functions (UPPER, LOWER, LENGTH, CONCAT, etc.)", test_strings)


# Test 10: Date functions
def test_dates():
    rows = conn.execute("""
        SELECT
            CURRENT_DATE AS today,
            EXTRACT(YEAR FROM DATE '2024-06-15') AS year_val,
            EXTRACT(MONTH FROM DATE '2024-06-15') AS month_val,
            DATE '2024-06-15' + INTERVAL '30 days' AS plus_30,
            DATE '2024-06-15' - DATE '2024-01-01' AS day_diff;
    """).fetchone()
    assert rows[1] == 2024, f"EXTRACT YEAR failed: {rows[1]}"
    assert rows[2] == 6, f"EXTRACT MONTH failed: {rows[2]}"

test("Date functions (EXTRACT, INTERVAL, date arithmetic)", test_dates)


# ─────────────────────────────────────────────
# Results
# ─────────────────────────────────────────────
print()
print("╠══════════════════════════════════════════╣")
total = PASSED + FAILED
print(f"║   Results: {PASSED}/{total} passed", end="")
if FAILED == 0:
    print("  ✅ All good!        ║")
else:
    spaces = 24 - len(str(FAILED))
    print(f"  ❌ {FAILED} failed" + " " * max(spaces - len(str(FAILED)), 1) + "║")
print("╚══════════════════════════════════════════╝")
print()

if FAILED > 0:
    print("⚠️  Some tests failed. Check the errors above.")
    sys.exit(1)
else:
    print("🎉 Your SQL environment is ready! Start learning:")
    print("   → python3 runner.py        (interactive REPL)")
    print("   → python3 runner.py -q \"SELECT 'Hello SQL!' AS greeting;\"")
    print()

conn.close()
