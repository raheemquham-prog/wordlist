import itertools
import string

letters = string.ascii_letters  # a-zA-Z
digits = string.digits          # 0-9

def is_valid(combo):
    digit_count = sum(c.isdigit() for c in combo)
    if digit_count > 3:
        return False
    for i in range(len(combo) - 1):
        a, b = combo[i], combo[i+1]
        if a.isdigit() and b.isdigit():          # no two digits adjacent
            return False
        if a.isalpha() and b.isalpha() and a.lower() == b.lower():  # no same letter adjacent (case-insensitive)
            return False
    return True

charset = letters + digits
count = 0
with open("wordlist.txt", "w") as f:
    for combo in itertools.product(charset, repeat=8):
        word = "".join(combo)
        if is_valid(word):
            f.write(word + "\n")
            count += 1

print(f"Generated {count} valid combinations")
