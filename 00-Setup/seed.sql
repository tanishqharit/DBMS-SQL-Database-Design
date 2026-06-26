-- ============================================
-- 🐘 SQL Mastery — Seed Data
-- ============================================
-- LeetCode-style tables used across all modules.
-- Run this once before starting any problems.
--
-- Usage:
--   python3 00-Setup/runner.py 00-Setup/seed.sql
-- ============================================


-- ────────────────────────────────────────────
-- TABLE 1: Employee
-- Used in: ~40% of LeetCode SQL problems
-- ────────────────────────────────────────────

CREATE OR REPLACE TABLE Employee (
    id              INTEGER PRIMARY KEY,
    name            VARCHAR NOT NULL,
    salary          INTEGER,
    departmentId    INTEGER,
    managerId       INTEGER
);

INSERT INTO Employee VALUES
    (1,  'Alice',    95000,  1, NULL),
    (2,  'Bob',      85000,  1, 1),
    (3,  'Charlie',  72000,  2, 1),
    (4,  'Diana',    68000,  2, 3),
    (5,  'Eve',      92000,  1, 1),
    (6,  'Frank',    78000,  3, NULL),
    (7,  'Grace',    71000,  3, 6),
    (8,  'Hank',     88000,  1, 1),
    (9,  'Ivy',      95000,  1, 1),
    (10, 'Jack',     62000,  2, 3);


-- ────────────────────────────────────────────
-- TABLE 2: Department
-- Used with: Employee table for JOIN problems
-- ────────────────────────────────────────────

CREATE OR REPLACE TABLE Department (
    id      INTEGER PRIMARY KEY,
    name    VARCHAR NOT NULL
);

INSERT INTO Department VALUES
    (1, 'Engineering'),
    (2, 'Marketing'),
    (3, 'Sales'),
    (4, 'HR');


-- ────────────────────────────────────────────
-- TABLE 3: Customer
-- Used in: ~25% of LeetCode SQL problems
-- ────────────────────────────────────────────

CREATE OR REPLACE TABLE Customer (
    id      INTEGER PRIMARY KEY,
    name    VARCHAR NOT NULL,
    email   VARCHAR,
    city    VARCHAR
);

INSERT INTO Customer VALUES
    (1, 'John',    'john@mail.com',    'New York'),
    (2, 'Jane',    'jane@mail.com',    'London'),
    (3, 'Mike',    'mike@mail.com',    'New York'),
    (4, 'Sarah',   NULL,               'Paris'),
    (5, 'Tom',     'tom@mail.com',     'London'),
    (6, 'Lisa',    'lisa@mail.com',    'Tokyo'),
    (7, 'David',   NULL,               'New York');


-- ────────────────────────────────────────────
-- TABLE 4: Orders
-- Used with: Customer table for JOIN problems
-- ────────────────────────────────────────────

CREATE OR REPLACE TABLE Orders (
    id          INTEGER PRIMARY KEY,
    customerId  INTEGER,
    amount      INTEGER,
    orderDate   DATE
);

INSERT INTO Orders VALUES
    (101, 1, 250,  '2023-01-15'),
    (102, 1, 180,  '2023-03-22'),
    (103, 2, 320,  '2023-02-10'),
    (104, 3, 150,  '2023-04-05'),
    (105, 1, 420,  '2023-06-18'),
    (106, 5, 90,   '2023-07-01'),
    (107, 2, 275,  '2023-08-14'),
    (108, 3, 310,  '2023-09-30'),
    (109, 6, 195,  '2023-05-22'),
    (110, 5, 440,  '2023-11-11');


-- ────────────────────────────────────────────
-- TABLE 5: Product
-- Used in: Sales analysis problems
-- ────────────────────────────────────────────

CREATE OR REPLACE TABLE Product (
    id          INTEGER PRIMARY KEY,
    name        VARCHAR NOT NULL,
    category    VARCHAR,
    price       INTEGER
);

INSERT INTO Product VALUES
    (1, 'Laptop',      'Electronics', 1200),
    (2, 'Phone',       'Electronics', 800),
    (3, 'Tablet',      'Electronics', 450),
    (4, 'Headphones',  'Electronics', 150),
    (5, 'Desk',        'Furniture',   350),
    (6, 'Chair',       'Furniture',   275),
    (7, 'Monitor',     'Electronics', 400),
    (8, 'Keyboard',    'Electronics', 75);


-- ────────────────────────────────────────────
-- TABLE 6: Sales
-- Used with: Product table
-- ────────────────────────────────────────────

CREATE OR REPLACE TABLE Sales (
    saleId      INTEGER PRIMARY KEY,
    productId   INTEGER,
    quantity    INTEGER,
    saleDate    DATE
);

INSERT INTO Sales VALUES
    (1, 1, 2, '2023-01-10'),
    (2, 2, 5, '2023-01-15'),
    (3, 3, 3, '2023-02-20'),
    (4, 1, 1, '2023-03-05'),
    (5, 4, 8, '2023-03-18'),
    (6, 5, 4, '2023-04-22'),
    (7, 2, 2, '2023-05-10'),
    (8, 6, 6, '2023-06-14'),
    (9, 7, 3, '2023-07-01'),
    (10, 1, 1, '2023-08-19'),
    (11, 3, 4, '2023-09-25'),
    (12, 8, 10, '2023-10-30');


-- ────────────────────────────────────────────
-- TABLE 7: Activity (for window function / streak problems)
-- ────────────────────────────────────────────

CREATE OR REPLACE TABLE Activity (
    userId      INTEGER,
    activityDate DATE,
    activityType VARCHAR
);

INSERT INTO Activity VALUES
    (1, '2023-01-01', 'login'),
    (1, '2023-01-02', 'login'),
    (1, '2023-01-03', 'login'),
    (1, '2023-01-05', 'login'),
    (1, '2023-01-06', 'login'),
    (2, '2023-01-01', 'login'),
    (2, '2023-01-03', 'login'),
    (2, '2023-01-04', 'login'),
    (2, '2023-01-05', 'login'),
    (2, '2023-01-06', 'login'),
    (2, '2023-01-07', 'login'),
    (3, '2023-01-02', 'login'),
    (3, '2023-01-05', 'login');


-- ────────────────────────────────────────────
-- TABLE 8: Scores (for ranking problems)
-- ────────────────────────────────────────────

CREATE OR REPLACE TABLE Scores (
    id      INTEGER PRIMARY KEY,
    score   DECIMAL(4,2)
);

INSERT INTO Scores VALUES
    (1, 3.50),
    (2, 3.65),
    (3, 4.00),
    (4, 3.85),
    (5, 4.00),
    (6, 3.65);


-- ────────────────────────────────────────────
-- TABLE 9: Logs (for consecutive number problems)
-- ────────────────────────────────────────────

CREATE OR REPLACE TABLE Logs (
    id      INTEGER PRIMARY KEY,
    num     INTEGER
);

INSERT INTO Logs VALUES
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 1),
    (6, 2),
    (7, 2);


-- ============================================
-- ✅ Seed data loaded successfully!
-- ============================================
SELECT 'Seed data loaded!' AS status,
       (SELECT COUNT(*) FROM Employee) AS employees,
       (SELECT COUNT(*) FROM Department) AS departments,
       (SELECT COUNT(*) FROM Customer) AS customers,
       (SELECT COUNT(*) FROM Orders) AS orders,
       (SELECT COUNT(*) FROM Product) AS products,
       (SELECT COUNT(*) FROM Sales) AS sales;
