# Custom Alphanumeric Wordlist Generator

A lightweight, dependency-free Python tool that generates 8-character alphanumeric wordlists based on strict pattern and adjacency rules. Built for custom password-policy testing in authorized security labs (e.g., TryHackMe, Hack The Box, DVWA, OWASP Juice Shop, or local environments).

---

## Features

- **Custom Pattern Rules:**
  - **Length:** Exactly 8 characters per entry.
  - **Character Set:** Full alphanumeric (`a-z`, `A-Z`, `0-9`).
  - **Digit Limit:** Maximum 3 digits per string (remaining characters are letters).
  - **Non-Adjacent Digits:** No two digits can appear side-by-side.
  - **Case-Insensitive Character Separation:** No repeated adjacent letters, regardless of case (e.g., `aa`, `Aa`, `aA`, `AA` are all rejected).
- **Disk-Safe Output:** Streamlined generation designed to output targeted samples rather than unbounded multi-terabyte files.
- **Zero External Dependencies:** Runs natively using standard Python 3 library modules (`itertools`, `string`, `random`, `sys`).

---

## Requirements

* Python 3.x+

---

## Getting Started

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
python3 wordlist_generator.py
