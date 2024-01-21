import time

class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.leak_rate = leak_rate  # Seconds to leak 1 item
        self.bucket = 0
        self.last_leak_time = time.time()

    def can_add(self):
        """Simulate adding an item to the bucket.

        Returns True if the item can added, False if the bucket is full.
        """
        now = time.time()
        self._leak(now)  # Leak before checking capacity to maintain constant rate

        if self.bucket < self.capacity:
            self.bucket += 1
            return True
        else:
            return False

    def _leak(self, now):
        """Simulates the bucket leaking."""
        elapsed_time = now - self.last_leak_time
        to_leak = int(elapsed_time / self.leak_rate)

        if to_leak <= 0:
            return

        if to_leak >= self.capacity:
            self.bucket = 0
        else:
            self.bucket -= to_leak

        self.last_leak_time = now


if __name__ == '__main__':
    # Example usage:
    bucket = LeakyBucket(capacity=5, leak_rate=2)

    while True:
        try:
            item = input("Enter an item (or 'q' to quit): ")
            if item == 'q':
                break

            if bucket.can_add():
                print("Item added to the bucket.")
            else:
                print("Bucket is full, try again later.")

            time.sleep(0.1)  # Simulate some processing time

        except KeyboardInterrupt:
            break
