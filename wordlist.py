import random
import string

letters = string.ascii_letters
digits = string.digits
MAX_LINES = 10_000_000   # ~90MB — safe for your 5GB VM

def generate_valid(length=8, max_digits=3):
    while True:
        combo = []
        digit_count = 0
        prev = ""
        for i in range(length):
            can_use_digit = (digit_count < max_digits) and (not prev.isdigit())
            if can_use_digit and random.random() < 0.3:
                c = random.choice(digits)
                digit_count += 1
            else:
                c = random.choice(letters)
                while prev.isalpha() and c.lower() == prev.lower():
                    c = random.choice(letters)
            combo.append(c)
            prev = c
        return "".join(combo)

seen = set()
with open("wordlist.txt", "w") as f:
    while len(seen) < MAX_LINES:
        w = generate_valid()
        if w not in seen:
            seen.add(w)
            f.write(w + "\n")

print(f"Done: {len(seen)} lines written")
