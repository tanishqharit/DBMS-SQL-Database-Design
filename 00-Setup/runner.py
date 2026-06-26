#!/usr/bin/env python3
"""
SQL Runner — Execute SQL queries using DuckDB (PostgreSQL-compatible).

Usage:
    python3 runner.py                    # Start interactive REPL
    python3 runner.py file.sql           # Run a .sql file
    python3 runner.py -q "SELECT ..."    # Run a single query
"""

import sys
import os
import duckdb


# ─────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────
DB_PATH = "leetcode.duckdb"  # Persistent database file

# Table formatting
MAX_COL_WIDTH = 30
TRUNCATE_CHAR = "…"


# ─────────────────────────────────────────────
# Formatting helpers
# ─────────────────────────────────────────────
def format_value(val, width):
    """Format a single value for table display."""
    if val is None:
        text = "NULL"
    else:
        text = str(val)

    if len(text) > width:
        text = text[: width - 1] + TRUNCATE_CHAR
    return text.ljust(width)


def print_results(columns, rows):
    """Pretty-print query results as a formatted table."""
    if not columns:
        return

    # Calculate column widths
    col_widths = []
    for i, col in enumerate(columns):
        max_data = max((len(str(row[i])) if row[i] is not None else 4 for row in rows), default=0)
        width = min(max(len(col), max_data), MAX_COL_WIDTH)
        col_widths.append(width)

    # Header
    header = " │ ".join(col.ljust(w) for col, w in zip(columns, col_widths))
    separator = "─┼─".join("─" * w for w in col_widths)

    print(f"\n {header}")
    print(f" {separator}")

    # Rows
    for row in rows:
        line = " │ ".join(format_value(val, w) for val, w in zip(row, col_widths))
        print(f" {line}")

    print(f"\n ({len(rows)} row{'s' if len(rows) != 1 else ''})\n")


# ─────────────────────────────────────────────
# SQL execution
# ─────────────────────────────────────────────
def execute_sql(conn, sql):
    """Execute SQL and print results. Handles multiple statements."""
    statements = [s.strip() for s in sql.split(";") if s.strip()]

    for stmt in statements:
        try:
            result = conn.execute(stmt)

            # Check if this is a query that returns results
            if result.description:
                columns = [desc[0] for desc in result.description]
                rows = result.fetchall()
                print_results(columns, rows)
            else:
                print(f" ✓ Statement executed successfully.")
        except duckdb.Error as e:
            print(f" ✗ Error: {e}")


def run_file(conn, filepath):
    """Read and execute a .sql file."""
    if not os.path.exists(filepath):
        print(f" ✗ File not found: {filepath}")
        sys.exit(1)

    with open(filepath, "r") as f:
        sql = f.read()

    print(f" 📄 Running: {filepath}\n" + " " + "─" * 40)
    execute_sql(conn, sql)


def repl(conn):
    """Interactive SQL REPL."""
    print("┌──────────────────────────────────────────┐")
    print("│    🐘 SQL REPL (DuckDB / PG-compatible)  │")
    print("│    Type SQL queries, 'quit' to exit       │")
    print("│    End queries with ;                      │")
    print("└──────────────────────────────────────────┘")
    print()

    buffer = []

    while True:
        try:
            prompt = "sql> " if not buffer else "  -> "
            line = input(prompt)
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye! 👋")
            break

        if line.strip().lower() in ("quit", "exit", "\\q"):
            print("Goodbye! 👋")
            break

        buffer.append(line)

        # Execute when we see a semicolon
        if ";" in line:
            full_sql = "\n".join(buffer)
            execute_sql(conn, full_sql)
            buffer = []


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────
def main():
    conn = duckdb.connect(DB_PATH)

    if len(sys.argv) == 1:
        # No args → interactive REPL
        repl(conn)

    elif sys.argv[1] == "-q" and len(sys.argv) > 2:
        # -q "query" → run single query
        query = " ".join(sys.argv[2:])
        execute_sql(conn, query)

    elif sys.argv[1].endswith(".sql"):
        # file.sql → run file
        run_file(conn, sys.argv[1])

    else:
        print(__doc__)

    conn.close()


if __name__ == "__main__":
    main()
