# 🐘 SQL Mastery — From Zero to LeetCode Ready

A structured SQL learning repository with **PostgreSQL-compatible** syntax, detailed notes, and hands-on practice — all runnable locally via DuckDB.

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- pip

### Setup
```bash
# Install dependencies
pip install -r 00-Setup/requirements.txt

# Verify everything works
python3 00-Setup/test_setup.py

# Start the interactive SQL REPL
python3 00-Setup/runner.py
```

## 📁 Project Structure

```
SQL/
├── 00-Setup/               # Environment setup files
│   ├── runner.py           # SQL runner — execute .sql files or use interactive REPL
│   ├── test_setup.py       # Verify your setup works
│   └── requirements.txt    # Python dependencies
│
├── 01-Foundations/          # SELECT, WHERE, ORDER BY, NULL handling
├── 02-Filtering/           # LIKE, IN, BETWEEN, CASE WHEN
├── 03-Aggregations/        # GROUP BY, HAVING, COUNT, SUM, AVG
├── 04-Joins/               # INNER, LEFT, RIGHT, FULL, CROSS, Self
├── 05-Subqueries/          # Scalar, correlated, EXISTS, IN
├── 06-Set-Operations/      # UNION, INTERSECT, EXCEPT
├── 07-Window-Functions/    # ROW_NUMBER, RANK, LAG, LEAD
├── 08-CTEs/                # WITH clause, recursive CTEs
├── 09-String-Date/         # String manipulation, date arithmetic
├── 10-Advanced-Patterns/   # Gaps & islands, top-N, pivoting
├── 11-Database-Design/     # Tables, schemas, ER diagrams
├── 12-Keys-Constraints/    # PK, FK, UNIQUE, CHECK
├── 13-Normalization/       # 1NF → BCNF, denormalization
├── 14-DDL-DML/             # CREATE, ALTER, INSERT, UPDATE, DELETE
├── 15-DBMS-Fundamentals/   # ACID, architecture, SQL categories
├── 16-Indexing/            # B-Tree, query plans, EXPLAIN
├── 17-Transactions/        # Isolation levels, locking, MVCC
├── 18-Scaling/             # Partitioning, sharding, CAP theorem
│
└── Practice/               # LeetCode problems organized by topic
    ├── LeetCode-SQL-50/
    ├── LeetCode-Advanced-50/
    └── Pattern-Problems/
```

## 🔧 How to Use

### Interactive REPL
```bash
python3 runner.py
```
Type SQL queries directly. Results are formatted as tables. Type `quit` to exit.

### Run a .sql File
```bash
python3 runner.py path/to/file.sql
```

### Run a Specific Query
```bash
python3 runner.py -q "SELECT 1 + 1 AS result"
```

## 🧠 SQL Engine

This project uses **DuckDB** — a high-performance, embeddable SQL engine with PostgreSQL-compatible syntax. ~95% of PostgreSQL syntax works identically in DuckDB, covering everything tested on LeetCode.

> **Note**: If you need full PostgreSQL, you can start your local server with `brew services start postgresql@16` and all `.sql` files will work unchanged.

## 📖 Learning Path

| Phase | Modules | Goal |
|-------|---------|------|
| SQL Basics | 01 → 02 → 03 | Solve LeetCode Easy |
| Joins & Subqueries | 04 → 05 → 06 | Easy + some Medium |
| Window Functions & CTEs | 07 → 08 | LeetCode Medium |
| Advanced SQL | 09 → 10 | Medium-Hard |
| Database Design | 11 → 14 | Schema design interviews |
| DBMS Theory | 15 → 18 | Theory interview questions |
| Practice Grind | Practice/ | LeetCode SQL 50 → Advanced 50 |
