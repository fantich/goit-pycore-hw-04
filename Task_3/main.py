import sys
import os
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory_structure(directory: Path, indent=""):
    if not directory.is_dir():
        print(Fore.RED + f"Error: '{directory}' is not a directory or does not exist.")
        return

    try:
        items = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        for item in items:
            if item.is_dir():
                print(indent + Fore.BLUE + "📂 " + item.name)
                print_directory_structure(item, indent + " ┃ ")
            else:
                print(indent + Fore.GREEN + "📜 " + item.name)
    except PermissionError:
        print(Fore.RED + "Error: No access to one of the directories.")

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python main.py <path_to_directory>")
        sys.exit(1)

    directory_path = Path(sys.argv[1]).resolve()
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()