# 1-batch_processing.py
import mysql.connector

def stream_users_in_batches(batch_size):
    """Fetch users in batches from MySQL using a generator."""
    conn = mysql.connector.connect(
        host="localhost",
        user="alx",
        password="_@3G1M56iW1Nn]Lg",
        database="ALX_prodev"
    )
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM user_data")
    while True:
        rows = cur.fetchmany(batch_size)
        if not rows:
            break
        yield rows   

    cur.close()
    conn.close()


def batch_processing(batch_size):
    """Process users in batches and yield only users over age 25."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:
                yield user   