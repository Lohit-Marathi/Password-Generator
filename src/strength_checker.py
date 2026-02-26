"""Check the strength of a given password."""

import re


def check_strength(password):
    """
    Evaluate password strength and return a score + label.

    Scoring criteria (1 point each):
        - Length >= 8
        - Length >= 12
        - Contains uppercase letter
        - Contains digit
        - Contains special character

    Args:
        password (str): The password to evaluate.

    Returns:
        dict: {
            'score' : int (0-5),
            'label' : str ('Weak' | 'Moderate' | 'Strong' | 'Very Strong'),
            'tips'  : list of improvement suggestions
        }
    """
    score = 0
    tips  = []

    # Check each criterion
    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        tips.append("Use at least 12 characters for better security.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        tips.append("Add uppercase letters (A-Z).")

    if re.search(r"\d", password):
        score += 1
    else:
        tips.append("Add digits (0-9).")

    if re.search(r"[!@#$%^&*()\-_=+\[\]{}|;:,.<>?]", password):
        score += 1
    else:
        tips.append("Add special characters (e.g. @, #, !).")

    # Map score to a human-readable label
    if score <= 1:
        label = "Weak"
    elif score == 2:
        label = "Moderate"
    elif score in (3, 4):
        label = "Strong"
    else:
        label = "Very Strong"

    return {"score": score, "label": label, "tips": tips}