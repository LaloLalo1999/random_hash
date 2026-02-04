#!/usr/bin/env python3
"""
Random Hash Generator
Generates random 32-character hashes and searches for one starting with "00"
"""

import hashlib
import random
import string

ALPHANUMERIC_CHARACTERS = string.ascii_letters + string.digits


def generate_random_hash():
    """Generate a random 32-character hash using MD5.
    
    Note: MD5 is used here for demonstration purposes only.
    For security-critical applications, use SHA-256 or stronger algorithms.
    """
    # Generate a random string
    random_string = ''.join(random.choices(ALPHANUMERIC_CHARACTERS, k=16))
    # Create MD5 hash
    hash_object = hashlib.md5(random_string.encode())
    return hash_object.hexdigest()


def find_hash_with_double_zero(max_attempts=1000, log_every=100):
    """
    Generate random hashes until finding one that starts with "00".
    
    Args:
        max_attempts: Maximum number of attempts (default: 1000)
        log_every: Print progress every N attempts (default: 100). Set to 0 to disable.
    
    Returns:
        tuple: (success: bool, hash: str or None, attempts: int)
    """
    for attempt in range(1, max_attempts + 1):
        hash_value = generate_random_hash()
        if log_every and attempt % log_every == 0:
            print(f"Attempt {attempt}: {hash_value}")
        
        if hash_value.startswith("00"):
            print(f"\nSuccess! Found hash starting with '00': {hash_value}")
            return True, hash_value, attempt
    
    print(f"\nFailed to find hash starting with '00' after {max_attempts} attempts.")
    return False, None, max_attempts


def main():
    """Main function to run the hash finder."""
    print("Starting random hash generator...")
    print("Looking for a hash that starts with '00'...")
    print("-" * 60)
    
    success, hash_value, attempts = find_hash_with_double_zero(1000)
    
    print("-" * 60)
    if success:
        print(f"✓ Test PASSED: Found hash '{hash_value}' in {attempts} attempts")
        return 0
    else:
        print(f"✗ Test FAILED: No hash found after {attempts} attempts")
        return 1


if __name__ == "__main__":
    exit(main())
