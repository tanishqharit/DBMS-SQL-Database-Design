# What is SQL?

**SQL** (Structured Query Language) is the standard language for interacting with **relational databases**. It lets you:

- **Query** data (ask questions about your data)
- **Insert** new data
- **Update** existing data
- **Delete** data
- **Create** and modify database structure

---

## SQL is Declarative

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

---

## SQL Dialects

SQL has a standard (ANSI SQL), but each database adds its own extensions:

| Database | Used By | Notes |
|----------|---------|-------|
| **PostgreSQL** 🐘 | Uber, Instagram, Spotify, Reddit | Our focus. Most feature-rich open-source DB |
| **MySQL** | Facebook, Twitter, YouTube | LeetCode uses this by default |
| **SQLite** | Mobile apps, embedded systems | Lightweight, file-based |
| **SQL Server** | Enterprise/Microsoft shops | T-SQL dialect |
| **Oracle** | Banks, large enterprises | PL/SQL dialect |

> 💡 **For LeetCode**: ~95% of syntax is identical across PostgreSQL and MySQL. I'll note differences when they matter.
