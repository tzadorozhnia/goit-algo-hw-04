import sys
from pathlib import Path
from colorama import Fore, init

# Ініціалізація colorama
init(autoreset=True)

def print_tree(directory: Path, prefix: str = ""):
    """Рекурсивний обхід директорії з кольоровим виводом."""
    try:
        for path in directory.iterdir():
            if path.is_dir():
                print(prefix + Fore.BLUE + "    " + path.name + "/")
                print_tree(path, prefix + "    ")
            else:
                print(prefix + Fore.GREEN + "    " + path.name)
    except PermissionError:
        print(prefix + Fore.RED + "[Доступ заборонено]")

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python HW_Mod4_3.py <шлях_до_директорії>")
        sys.exit(1)

    root_path = Path(sys.argv[1])

    if not root_path.exists():
        print(Fore.RED + f"Помилка: шлях {root_path} не існує.")
        sys.exit(1)

    if not root_path.is_dir():
        print(Fore.RED + f"Помилка: {root_path} не є директорією.")
        sys.exit(1)

    print(Fore.CYAN + f"Структура директорії: {root_path}\n")
    print(Fore.CYAN + root_path.name + "/")
    print_tree(root_path)


if __name__ == "__main__":
    main()