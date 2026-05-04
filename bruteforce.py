import time
import itertools
import string
# -------------------------------
# 3. Brute Force (Limited)
# -------------------------------
def brute_force(password, max_length=4):
    chars = string.ascii_lowercase
    start = time.time()

    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            guess = ''.join(attempt)
            if guess == password:
                end = time.time()
                return True, end - start

    return False, time.time() - start