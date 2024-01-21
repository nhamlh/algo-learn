#!/usr/bin/env python3

import time
from collections import deque

class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.leak_rate = leak_rate  # Seconds to leak 1 item
        self.bucket = deque(maxlen=capacity)  # Use deque for efficient FIFO behavior
        self.last_leak_time = time.time()

    def put(self, item):
        """Attempts to add an item to the bucket.

        Returns True if the item was added, False if the bucket is full.
        """
        now = time.time()
        self._leak(now)  # Leak before checking capacity to maintain constant rate

        print(f"bucket capacity after leak: {len(self.bucket)}/{self.capacity}. Last leak time {self.last_leak_time}. Now {now}")

        if len(self.bucket) < self.capacity:
            self.bucket.append(item)
            return True
        else:
            return False

    def get(self):
        """Retrieves an item from the bucket, if available."""
        return self.bucket.popleft() if self.bucket else None

    def _leak(self, now):
        """Simulates the bucket leaking."""
        elapsed_time = now - self.last_leak_time
        to_leak = int(elapsed_time / self.leak_rate)

        if to_leak <= 0:
            return

        for _ in range(to_leak):
            if self.bucket:
                self.bucket.popleft()  # Remove leaked items one by one

        self.last_leak_time = now

# Example usage:
bucket = LeakyBucket(capacity=3, leak_rate=1)

while True:
    try:
        item = input("Enter an item (or 'q' to quit): ")
        if item == 'q':
            break

        if bucket.put(item):
            print("Item added to the bucket.")
        else:
            print("Bucket is full, try again later.")

        time.sleep(0.4)  # Simulate some processing time

    except KeyboardInterrupt:
        break

# Retrieve items at a controlled rate
while True:
    item = bucket.get()

    if item == None:
        exit()

    print(f"Retrieved item: {item}")
    time.sleep(0.5)  # Simulate processing the retrieved item
