import random
import string
import math

def generate_password(length=12, include_upper=True, include_lower=True, include_digits=True, include_special=True):
    characters = ''
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def estimate_entropy(password):
    character_set_size = 0
    if any(c in string.ascii_uppercase for c in password):
        character_set_size += 26
    if any(c in string.ascii_lowercase for c in password):
        character_set_size += 26
    if any(c in string.digits for c in password):
        character_set_size += 10
    if any(c in string.punctuation for c in password):
        character_set_size += 32  # Assuming 32 special characters in string.punctuation

    password_length = len(password)
    entropy = math.log2(character_set_size) * password_length
    return entropy

def generate_passphrase(words=4, separator='-'):
    with open('/usr/share/dict/words', 'r') as f:  # Use system dictionary file
        dictionary = [line.strip() for line in f]

    passphrase = [random.choice(dictionary).capitalize() for _ in range(words)]
    return separator.join(passphrase)

if __name__ == "__main__":
    print("Advanced Password Generator\n")

    # Generate random password
    password = generate_password(length=16)
    print("Random Password:", password)

    # Estimate password strength
    entropy = estimate_entropy(password)
    print("Password Entropy:", entropy)

    # Generate passphrase
    passphrase = generate_passphrase()
    print("\nPassphrase:", passphrase)
