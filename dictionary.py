import time

# -------------------------------
# 2. Dictionary Attack
# -------------------------------
def dictionary_attack(password, wordlist_file):
    start = time.time()

    try:
        with open(wordlist_file, 'r', errors='ignore') as f:
            for word in f:
                if word.strip() == password:
                    end = time.time()
                    return True, end - start
    except FileNotFoundError:
        print("⚠ Wordlist file not found!")
        return False, 0

    return False, time.time() - start