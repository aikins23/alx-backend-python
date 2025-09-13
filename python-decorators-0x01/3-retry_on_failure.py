#!/usr/bin/python3
"""
Task 3: Retry Database Queries Decorator
Retries DB operations on failure.
"""

import time
import sqlite3
import functools


def with_db_connection(func):
    """Decorator to handle opening and closing DB connection"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper


def retry_on_failure(retries=3, delay=2):
    """Decorator to retry DB queries if they fail"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"⚠️ Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            # Raise last exception if all retries fail
            raise last_exception
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    """Fetch users, retrying on failure"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


if __name__ == "__main__":
    try:
        users = fetch_users_with_retry()
        print("✅ Users fetched:", users)
    except Exception as e:
        print("❌ Failed to fetch users after retries:", e)
