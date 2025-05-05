import random
import string


def random_character():
    # Define the set of characters: digits, lowercase, and uppercase letters
    characters = string.digits + string.ascii_letters  # "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return random.choice(characters)

with open('secrets.txt', 'w') as file:
    for i in range(5000):
        secret = "ghp_"
        for i in range(36):
            character = random_character()
            secret += character
        secret += "\n"
        file.write(secret)