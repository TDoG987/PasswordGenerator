import typer
import string
import random
import pyperclip


def get_allowed_chars(digits: bool, symbols: bool) -> str:
    allowed_chars = string.ascii_letters

    if digits:
        allowed_chars += string.digits

    if symbols:
        allowed_chars += "!@#$%^&*()_-"

    return allowed_chars


def generate_password(length: int, allowed_chars: str) -> str:
    password = ""

    for _ in range(length):
        password += random.choice(allowed_chars)
    
    return password


def save_password(key: str, password: str, file_path: str) -> None:
    with open(file_path, "r") as file:
        try:
            data = file.read()

        except FileNotFoundError:
            data = ""

    data += f"{key}: {password}\n"

    with open(file_path, "w") as file:
        file.write(data)


def copy_password_to_clipboard(password: str) -> None:
    pyperclip.copy(password)


def main(length: int, digits: bool = False, symbols: bool = False):
    """Makes a random password with given flags"""

    allowed_chars = get_allowed_chars(digits, symbols)

    password = generate_password(length, allowed_chars)

    print(f"Password: {password}")

    if input("Do you want to copy password to clipboard (y/n): ").lower() == "y":
        copy_password_to_clipboard(password)

    if input("Do you want to save password (y/n): ").lower() == "y":
        save_password(input("Key: "), password, input("File path: "))


if __name__ == '__main__':
    typer.run(main)
