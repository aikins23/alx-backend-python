#!/usr/bin/env python3
"""
Task 4: Using decorators to cache Database Queries
"""

import sqlite3
import functools

# Global dictionary to cache query results
query_cache = {}


def with_db_connection(func):
    """
    Decorator to handle SQLite DB connection
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")  # Example database file
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper


def cache_query(func):
    """
    Decorator to cache database query results
    """
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        if query in query_cache:
            print("✅ Returning cached result")
            return query_cache[query]

        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        print("💾 Caching result for query:", query)
        return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


# --- Test the caching ---
if __name__ == "__main__":
    # First call → caches result
    users = fetch_users_with_cache(query="SELECT * FROM users")
    print(users)

    # Second call → retrieves from cache
    users_again = fetch_users_with_cache(query="SELECT * FROM users")
    print(users_again)
