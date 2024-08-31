import os


def clean_screen():
    return os.system('cls' if os.name == 'nt' else 'clear')
