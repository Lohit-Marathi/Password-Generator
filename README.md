# 🔐 Password Generator

A simple command-line tool to generate strong, secure passwords — built with pure Python (no external libraries needed).

---

## Features

- Cryptographically secure password generation using Python's `secrets` module
- Configurable length and character types (uppercase, digits, symbols)
- Built-in password strength checker with helpful tips
- Generate multiple passwords at once

---

## Project Structure

```
password-generator/
│
├── src/
│   ├── __init__.py           # Package init
│   ├── password_generator.py # Core generation logic
│   ├── strength_checker.py   # Strength evaluation
│   └── utils.py              # Character sets and helpers
│
├── passgen.py                # CLI entry point
├── requirements.txt          # No external deps!
├── README.md
├── LICENSE
└── .gitignore
```

---

## Getting Started

**No installation needed** — just Python 3.6+.

```bash
# Clone the repo
git clone https://github.com/your-username/password-generator.git
cd password-generator

# Run it
python passgen.py
```

---

## Usage

```bash
# Default: 1 password, length 16, all character types
python passgen.py

# Custom length
python passgen.py -l 24

# Generate 5 passwords
python passgen.py -n 5

# Exclude special characters
python passgen.py --no-symbols

# Exclude uppercase
python passgen.py --no-upper

# All options together
python passgen.py -l 20 -n 3 --no-symbols
```

---

## Strength Score

Each password is rated out of 5 based on:

| Criterion          | Points |
|--------------------|--------|
| Length ≥ 8         | +1     |
| Length ≥ 12        | +1     |
| Has uppercase      | +1     |
| Has digit          | +1     |
| Has special char   | +1     |

| Score | Label       |
|-------|-------------|
| 0–1   | Weak        |
| 2     | Moderate    |
| 3–4   | Strong      |
| 5     | Very Strong |

---

## Why `secrets` instead of `random`?

Python's `random` module is **not** suitable for security purposes — it's predictable. The `secrets` module uses your OS's cryptographically secure random number generator, making it safe for generating passwords and tokens.

---

## Using in Python Code

You can also use the project directly inside your own Python scripts:

```python
from src.password_generator import generate_password, generate_multiple
from src.strength_checker import check_strength

# Single password
pwd = generate_password(length=20)
print(pwd)

# Check its strength
result = check_strength(pwd)
print(result["label"])   # e.g. "Very Strong"
print(result["tips"])    # improvement suggestions (empty if perfect)

# Multiple passwords
passwords = generate_multiple(count=5, length=16)
for p in passwords:
    print(p)
```

---

## Sample Output

```
$ python passgen.py -n 3 -l 20

Generating 3 password(s) of length 20...

  [1] Jk#9mXwQ2!rLpN6vBs@Y
      Strength : Very Strong (5/5)

  [2] tR7$bHnM4@cPeU1oWz#K
      Strength : Very Strong (5/5)

  [3] Gy8!qZxV3%dFjA5sRk@L
      Strength : Very Strong (5/5)

---

$ python passgen.py --no-symbols -l 12

Generating 1 password(s) of length 12...

  [1] Hm7KqR2nBxP4
      Strength : Strong (4/5)
      Tips     : Add special characters (e.g. @, #, !).
```

---
