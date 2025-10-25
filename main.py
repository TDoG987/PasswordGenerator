import typer
import string
import random


def get_allowed_chars(digits: bool, symbols: bool) -> str:
    allowed_chars = string.ascii_letters

    if digits:
        allowed_chars += string.digits
    
    if symbols:
        allowed_chars += "! @ # $ % ^ & * ( ) _ -"
    
    return allowed_chars


def generate_password(length: int, allowed_chars: str) -> str:
    password = ""

    for _ in range(length):
        password += random.choice(allowed_chars)
    
    return password

def main(digits: bool = False, symbols: bool = False):
    """Makes a random password with given flags"""
    pass


if __name__ == '__main__':
    typer.run(main)
