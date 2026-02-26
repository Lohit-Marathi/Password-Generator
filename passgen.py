"""
passgen.py -- Command line interface for the password generetor.

Usage:
     python passgen.py                              # one password , default settings
     python passgen.py -l 12                        # length 12
     python passgen.py -l 16 -n 5                   # 5 passwords of length 16  
     python passgen.py --no-symbols                 # exclude symbols
     python passgen.py --no-upper --no-digits    # only lowercase letters
"""


import argparse
from src.password_generator import generate_multiple
from src.strength_checker import check_strength

def parse_args():
    """parse command line arguments"""
    parser = argparse.ArgumentParser(
        description = "Generate secure , strong passwords"
    )

    parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password(s) (default: 16)")
    parser.add_argument("-n", "--count", type=int, default=1, help="Number of passwords to generate (default: 1)")
    parser.add_argument("--no-upper", dest="upper",action="store_false", help="Exclude uppercase letters")
    parser.add_argument("--no-symbols", dest="symbols",action="store_false", help="Exclude symbols")
    parser.add_argument("--no-digits", dest="digits", action="store_false", help="Exclude digits")
    return parser.parse_args()


def main():
    args = parse_args()

    print(f"\nGenerating {args.count} password(s) of length {args.length}...\n")


    passwords =  generate_multiple(
        count = args.count,
        length = args.length,
        use_upper = args.upper,
        use_symbols = args.symbols,
        use_digits = args.digits
    )

    for i, pwd in enumerate(passwords, start=1):
        result = check_strength(pwd)
        print(f"  [{i}] {pwd}")
        print(f"      Strength : {result['label']} ({result['score']}/5)")
        if result["tips"]:
            print(f"      Tips     : {', '.join(result['tips'])}")
        print()


if __name__ == "__main__":
    main()