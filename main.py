import typer
import string


def get_allowed_chars(digits: bool, symbols: bool):
    allowed_chars = string.ascii_letters

    if digits:
        allowed_chars += string.digits
    
    if symbols:
        allowed_chars += "! @ # $ % ^ & * ( ) _ -"
    
    return allowed_chars


def main(digits: bool = False, symbols: bool = False):
    """Makes a random password with given flags"""
    pass


if __name__ == '__main__':
    typer.run(main)