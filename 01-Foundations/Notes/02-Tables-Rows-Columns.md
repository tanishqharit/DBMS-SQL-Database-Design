# Databases, Tables, Rows, Columns

Think of a database like a spreadsheet application:

```
Database  =  The entire spreadsheet file (e.g., "company.xlsx")
Table     =  A single sheet (e.g., "employees" sheet)
Column    =  A column header (e.g., "name", "salary")
Row       =  A single record/entry (e.g., Alice's data)
```

---

## Example: `employees` Table

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

## Key Terminology

| Term | Also Called | Meaning |
|------|------------|---------|
| Table | Relation | A structured collection of data |
| Row | Record / Tuple | A single entry in a table |
| Column | Field / Attribute | A single property (e.g., "name") |
| Schema | — | The structure/design of a table (column names, types) |
| Database | — | A collection of related tables |

> 💡 In formal database theory, a table is called a "relation," rows are "tuples," and columns are "attributes." You might see these terms in DBMS theory (Module 15+), but in practice everyone says table/row/column.
