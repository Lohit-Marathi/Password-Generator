"""Core password generation logic."""

import secrets
from src.utils import get_char_pool, UPPERCASE, LOWERCASE, DIGITS, SYMBOLS

def generate_password(length = 16 , use_upper = True, use_symbols= True, use_digits=True):
    """Generate a single criptographically secure password."""
    if length < 8:
        raise ValueError("Password lenght should be at least 8 characters.")
    pool = get_char_pool(use_upper, use_symbols, use_digits)
    
    # Guarantee at least one character form each selected group
    required = [secrets.choice(LOWERCASE)]        # always include lowercase

    if use_upper:
        required.append(secrets.choice(UPPERCASE))
    if use_symbols:
        required.append(secrets.choice(SYMBOLS))
    if use_digits:
        required.append(secrets.choice(DIGITS))

    # Fill the rest of the password from the full pool
    remaining = [secrets.choice(pool) for _ in range(length - len(required))]

    # Combine and shuffle to avoid predictable patterns
    password = required + remaining
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)




def generate_multiple(count=5,length=16, use_upper=True, use_symbols=True, use_digits=True):
    """Generate multiple passwords at once
       
       Args:
           count : number of passwords to generate
           length : length of each password
           
           
       Returns:
           list[str] : list of generated passwords
    """
    return [
        generate_password(length, use_upper, use_symbols, use_digits)
        for _ in range(count)
    ]