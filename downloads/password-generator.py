#!/usr/bin/env python3
"""
🔑 Password Generator Pro - $5
Generate secure passwords with custom rules
"""
import secrets
import string
import sys

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True, exclude_similar=False):
    chars = ''
    if use_upper: chars += string.ascii_uppercase
    if use_lower: chars += string.ascii_lowercase
    if use_digits: chars += string.digits
    if use_symbols: chars += '!@#$%^&*()-_=+[]{}|;:,.<>?'
    if not chars: chars = string.ascii_letters + string.digits
    
    if exclude_similar:
        chars = chars.translate(str.maketrans('', '', 'Il1O0S5Z2'))
    
    return ''.join(secrets.choice(chars) for _ in range(length))

def main():
    print("🔑 Password Generator Pro")
    print("=" * 30)
    
    try:
        length = int(input("Length (default 16): ") or "16")
        use_upper = input("Uppercase? (Y/n): ").lower() != 'n'
        use_lower = input("Lowercase? (Y/n): ").lower() != 'n'
        use_digits = input("Digits? (Y/n): ").lower() != 'n'
        use_symbols = input("Symbols? (Y/n): ").lower() != 'n'
        
        count = int(input("How many passwords? (default 5): ") or "5")
        
        print("\n" + "=" * 30)
        print("Generated Passwords:")
        print("=" * 30)
        
        for i in range(count):
            pwd = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
            print(f"{i+1:2d}. {pwd}")
        
        print("\n✅ Passwords generated securely using system randomness")
    except KeyboardInterrupt:
        print("\n\nBye!")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
