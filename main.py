from pathlib import Path
import sys
from colorama import Fore, Style

def visualize_directory(path, indent=''):
    directory = Path(path)
    for item in directory.iterdir():
        if item.is_dir():
            color = Fore.BLUE
        else:
            color = Fore.GREEN
            
        print(indent + color + item.name + Style.RESET_ALL)
        if item.is_dir():
            visualize_directory(item, indent + '  ')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python visualize_directory.py 'directory_path'")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    if not Path(directory_path).is_dir():
        print("Error: Directory not found!")
        sys.exit(1)

    visualize_directory(directory_path)