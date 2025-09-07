#!/usr/bin/python3
seed = __import__('seed')


def stream_user_ages():
    """Generator that yields user ages one by one from DB."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row['age']
    connection.close()


def average_age():
    """Compute average age using the generator (memory-efficient)."""
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    return total / count if count > 0 else 0


if __name__ == "__main__":
    avg = average_age()
    print(f"Average age of users: {avg:.2f}")
