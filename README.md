# 🐘 SQL Mastery — From Zero to LeetCode Ready

> A structured, hands-on SQL course you can run entirely on your laptop. Detailed notes, fill-in-the-blank practice problems, and a built-in PostgreSQL-compatible engine — no database server required.

[![SQL](https://img.shields.io/badge/SQL-PostgreSQL--compatible-336791)](#-sql-engine)
[![Engine](https://img.shields.io/badge/engine-DuckDB-FFF000)](https://duckdb.org)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org)

---

## 📑 Contents

- [Why this repo](#-why-this-repo)
- [Quick Start](#-quick-start)
- [How to Use the Runner](#-how-to-use-the-runner)
- [SQL Engine](#-sql-engine)
- [Sample Data](#-sample-data)
- [Course Roadmap](#-course-roadmap)
- [Module 01 — Foundations](#-module-01--foundations)
- [Learning Path](#-learning-path)
- [Repository Layout](#-repository-layout)

---

## 🎯 Why this repo

- **Learn by doing** — every concept has a note *and* a runnable problem.
- **Zero setup friction** — DuckDB is embedded; `pip install` and you're querying.
- **Interview-focused** — examples mirror the tables and patterns used across LeetCode SQL and DB design interviews.
- **Persistent practice DB** — load the seed data once; your tables stick around between sessions.

---

## 🚀 Quick Start

**Prerequisites:** Python 3.10+ and `pip`.

```bash
# 1. Install dependencies
pip install -r 00-Setup/requirements.txt

# 2. Load the seed data (run once — tables persist after this)
python3 00-Setup/runner.py 00-Setup/seed.sql

# 3. Start solving — open the REPL
python3 00-Setup/runner.py
```

That's it. You're ready to work through [Module 01](#-module-01--foundations).

---

## 🔧 How to Use the Runner

[`00-Setup/runner.py`](00-Setup/runner.py) is a small DuckDB wrapper with three modes:

| Mode | Command | Use for |
|------|---------|---------|
| **Interactive REPL** | `python3 00-Setup/runner.py` | Exploring, quick experiments (`quit` to exit) |
| **Run a file** | `python3 00-Setup/runner.py path/to/file.sql` | Checking your answer to a problem |
| **Run one query** | `python3 00-Setup/runner.py -q "SELECT 1 + 1 AS result"` | One-off checks |

Results print as clean, aligned tables. The database lives at `00-Setup/leetcode.duckdb` and **persists between runs**, so seeded tables stay loaded no matter which folder you launch from.

---

## 🧠 SQL Engine

This project runs on **[DuckDB](https://duckdb.org)** — a fast, embeddable SQL engine with PostgreSQL-compatible syntax. ~95% of PostgreSQL syntax works identically, covering everything tested on LeetCode.

> **Want full PostgreSQL?** Start a local server (`brew services start postgresql@16`) and the `.sql` files run unchanged.

---

## 🗃️ Sample Data

[`00-Setup/seed.sql`](00-Setup/seed.sql) loads LeetCode-style tables with deliberate edge cases (NULLs, ties, duplicates) so the problems feel realistic:

| Table | Rows | Used for |
|-------|------|----------|
| `Employee` | 10 | SELECT, WHERE, self-joins, manager hierarchies, NULL gotchas |
| `Department` | 4 | JOINs with `Employee` (incl. empty departments) |
| `Customer` | 7 | Filtering, NULL emails |
| `Orders` | 10 | JOINs, aggregations, date filtering |
| `Product` | 8 | Category grouping, sales analysis |
| `Sales` | 12 | Aggregations, running totals |
| `Activity` | 13 | Window functions, login streaks |
| `Scores` | 6 | Ranking (`RANK`, `DENSE_RANK`) |
| `Logs` | 7 | Consecutive-number patterns |

---

## 🗺️ Course Roadmap

> **Status:** Module 01 is complete. The rest is the planned curriculum — content lands module by module.

| # | Module | Topics | Status |
|---|--------|--------|--------|
| 01 | **Foundations** | SELECT, WHERE, ORDER BY, NULL handling | ✅ Done |
| 02 | Filtering | LIKE, IN, BETWEEN, CASE WHEN | 🔜 Planned |
| 03 | Aggregations | GROUP BY, HAVING, COUNT, SUM, AVG | 🔜 Planned |
| 04 | Joins | INNER, LEFT, RIGHT, FULL, CROSS, Self | 🔜 Planned |
| 05 | Subqueries | Scalar, correlated, EXISTS, IN | 🔜 Planned |
| 06 | Set Operations | UNION, INTERSECT, EXCEPT | 🔜 Planned |
| 07 | Window Functions | ROW_NUMBER, RANK, LAG, LEAD | 🔜 Planned |
| 08 | CTEs | WITH clause, recursive CTEs | 🔜 Planned |
| 09 | String & Date | String manipulation, date arithmetic | 🔜 Planned |
| 10 | Advanced Patterns | Gaps & islands, top-N, pivoting | 🔜 Planned |
| 11 | Database Design | Tables, schemas, ER diagrams | 🔜 Planned |
| 12 | Keys & Constraints | PK, FK, UNIQUE, CHECK | 🔜 Planned |
| 13 | Normalization | 1NF → BCNF, denormalization | 🔜 Planned |
| 14 | DDL & DML | CREATE, ALTER, INSERT, UPDATE, DELETE | 🔜 Planned |
| 15 | DBMS Fundamentals | ACID, architecture, SQL categories | 🔜 Planned |
| 16 | Indexing | B-Tree, query plans, EXPLAIN | 🔜 Planned |
| 17 | Transactions | Isolation levels, locking, MVCC | 🔜 Planned |
| 18 | Scaling | Partitioning, sharding, CAP theorem | 🔜 Planned |

---

## 📚 Module 01 — Foundations

> **Goal:** Write basic queries — selecting, filtering, sorting, and handling NULLs. Covers ~30% of LeetCode Easy problems.

### Notes

| # | Topic | Note |
|---|-------|------|
| 01 | What is SQL? | [01-What-is-SQL.md](01-Foundations/Notes/01-What-is-SQL.md) |
| 02 | Databases, Tables, Rows, Columns | [02-Tables-Rows-Columns.md](01-Foundations/Notes/02-Tables-Rows-Columns.md) |
| 03 | SELECT — Retrieving Data | [03-SELECT.md](01-Foundations/Notes/03-SELECT.md) |
| 04 | WHERE — Filtering Rows | [04-WHERE.md](01-Foundations/Notes/04-WHERE.md) |
| 05 | Comparison Operators | [05-Comparison-Operators.md](01-Foundations/Notes/05-Comparison-Operators.md) |
| 06 | Logical Operators (AND, OR, NOT) | [06-Logical-Operators.md](01-Foundations/Notes/06-Logical-Operators.md) |
| 07 | DISTINCT — Removing Duplicates | [07-DISTINCT.md](01-Foundations/Notes/07-DISTINCT.md) |
| 08 | ORDER BY — Sorting Results | [08-ORDER-BY.md](01-Foundations/Notes/08-ORDER-BY.md) |
| 09 | LIMIT & OFFSET — Pagination | [09-LIMIT-OFFSET.md](01-Foundations/Notes/09-LIMIT-OFFSET.md) |
| 10 | NULL Handling | [10-NULL-Handling.md](01-Foundations/Notes/10-NULL-Handling.md) |
| 11 | SQL Execution Order ⭐ | [11-Execution-Order.md](01-Foundations/Notes/11-Execution-Order.md) |
| 12 | Aliases (AS) | [12-Aliases.md](01-Foundations/Notes/12-Aliases.md) |
| 13 | Comments | [13-Comments.md](01-Foundations/Notes/13-Comments.md) |

### Practice Problems

| # | Problem | Difficulty | File |
|---|---------|------------|------|
| 01 | Basic SELECT | ⭐ Easy | [01-Basic-SELECT.sql](01-Foundations/Problems/01-Basic-SELECT.sql) |
| 02 | WHERE Filtering | ⭐ Easy | [02-WHERE-Filtering.sql](01-Foundations/Problems/02-WHERE-Filtering.sql) |
| 03 | AND + OR | ⭐ Easy | [03-AND-OR.sql](01-Foundations/Problems/03-AND-OR.sql) |
| 04 | DISTINCT | ⭐ Easy | [04-DISTINCT.sql](01-Foundations/Problems/04-DISTINCT.sql) |
| 05 | NULL Handling | ⭐⭐ Easy-Medium | [05-NULL-Handling.sql](01-Foundations/Problems/05-NULL-Handling.sql) |
| 06 | COALESCE | ⭐⭐ Easy-Medium | [06-COALESCE.sql](01-Foundations/Problems/06-COALESCE.sql) |
| 07 | Second Highest Salary | ⭐⭐ Medium | [07-Second-Highest-Salary.sql](01-Foundations/Problems/07-Second-Highest-Salary.sql) |
| 08 | Execution Order | ⭐⭐ Medium | [08-Execution-Order.sql](01-Foundations/Problems/08-Execution-Order.sql) |
| 09 | Combined Concepts | ⭐⭐ Medium | [09-Combined-Concepts.sql](01-Foundations/Problems/09-Combined-Concepts.sql) |
| 10 | NULL Gotcha | ⭐⭐⭐ Medium | [10-NULL-Gotcha.sql](01-Foundations/Problems/10-NULL-Gotcha.sql) |

> **How to practice:** Open a problem `.sql` file, write your query in the blank slot, then check it with
> `python3 00-Setup/runner.py 01-Foundations/Problems/01-Basic-SELECT.sql`.

---

## 🧗 Learning Path

| Phase | Modules | Goal |
|-------|---------|------|
| SQL Basics | 01 → 02 → 03 | Solve LeetCode Easy |
| Joins & Subqueries | 04 → 05 → 06 | Easy + some Medium |
| Window Functions & CTEs | 07 → 08 | LeetCode Medium |
| Advanced SQL | 09 → 10 | Medium-Hard |
| Database Design | 11 → 14 | Schema design interviews |
| DBMS Theory | 15 → 18 | Theory interview questions |

---

## 📁 Repository Layout

```
SQL/
├── 00-Setup/
│   ├── runner.py          # DuckDB runner — REPL, file, and -q query modes
│   ├── seed.sql           # Sample tables (run once to load)
│   ├── requirements.txt   # Python dependencies
│   └── leetcode.duckdb    # Persistent practice DB (git-ignored, auto-created)
│
└── 01-Foundations/
    ├── Notes/             # 13 teaching notes
    └── Problems/          # 10 practice problems (fill-in-the-blank .sql)
```

> `solutions.sql` and `*.duckdb` are git-ignored — your scratch answers and local database stay on your machine.
