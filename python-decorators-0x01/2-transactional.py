#!/usr/bin/python3
"""
Task 2: Transaction Management Decorator
Automatically commits or rollbacks database changes.
"""

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


def transactional(func):
    """Decorator to manage DB transactions (commit/rollback)"""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            raise e
    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    """Update user's email inside a transaction"""
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))


if __name__ == "__main__":
    # Update user's email with automatic transaction handling
    update_user_email(user_id=1, new_email="Crawford_Cartwright@hotmail.com")
    print("✅ Email updated successfully!")
