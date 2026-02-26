"""Utility constants and helper functions"""


import string

# Character sets used for password generation
UPPERCASE = string.ascii_uppercase           # A-Z
LOWERCASE = string.ascii_lowercase           # a-z
DIGITS = string.digits                       # 0-9
SYMBOLS = "!@#$%^&*()-_=+[]{}|;:,.<>?"       # special characters


def get_char_pool(use_upper= True, use_symbols=True, use_digits=True):
    """
       Build the character pool based on user preferences.
       
       Args:
          use_upper : Include uppercase letters
          use_symbols : Include symbols
          use_digits : Include digits
          
       Returns:
          str : Combined pool of characters
    """
    pool = LOWERCASE  # always include lowercase letters

    if use_upper:
        pool += UPPERCASE
    if use_symbols:
        pool += SYMBOLS
    if use_digits:
        pool += DIGITS

    return pool
