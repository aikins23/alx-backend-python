#!/usr/bin/python3
"""
Task 0: Logging Database Queries
Creates a decorator to log SQL queries before execution.
"""
from datetime import datetime
import sqlite3
import functools


def log_queries(func):
    """Decorator to log SQL queries executed by a function"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # log the first positional argument if it looks like a query
        query = kwargs.get("query", args[0] if args else "UNKNOWN QUERY")
        print(f"[LOG] Executing query: {query}")
        return func(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    """Fetch all users from the database"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


if __name__ == "__main__":
    # Example usage: fetching users while logging the query
    users = fetch_all_users(query="SELECT * FROM users")
    print(users)
