#!/usr/bin/python3
"""
Batch processing users with generators
"""

from itertools import islice
stream_users = __import__('0-stream_users').stream_users


def stream_users_in_batches(batch_size):
    """
    Generator that yields users in batches of `batch_size`
    """
    users_iterator = stream_users()
    while True:
        batch = list(islice(users_iterator, batch_size))
        if not batch:
            break
        yield batch


def batch_processing(batch_size):
    """
    Process each batch to filter users over the age of 25
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:
                print(user)
