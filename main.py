import os
import sys
from files.open_profile import open_profile, get_available_profiles, change_proxy
from files.create_profile import create_profile

BANNER = """
\033[32m
╔══════════════════════════════════════════════════════╗
║                                                      ║
║    \033[37m╔═╗╔═╗╦ ╦╦\033[37m  \033[37m╦╔═╦╦  ╦  ╔═╗╦═╗\033[37m                      ║
║    \033[37m╚═╗║ ║║ ║║\033[37m  \033[37m╠╩╗║║  ║  ║╣ ╠╦╝\033[37m                      ║
║    \033[37m╚═╝╚═╝╚═╝╩═╝\033[37m\033[37m╩ ╩╩╩═╝╩═╝╚═╝╩╚═\033[37m                      ║
║                                                      ║
║       \033[36mHelp & Support: https://t.me/Lozhono\033[32m           ║
╚══════════════════════════════════════════════════════╝
\033[0m"""
MENU = """\033[32m
╔══════════════════════════════════════════════════════╗
║              \033[33mSelect the module:\033[32m                      ║
╠══════════════════════════════════════════════════════╣
║  \033[36m[1]\033[32m 🌐 Open Profile                                 ║
║  \033[36m[2]\033[32m ➕ Create Profile                               ║
║  \033[36m[3]\033[32m 🔄 Change Proxy                                 ║
║  \033[36m[4]\033[32m ❌ Exit                                         ║
╚══════════════════════════════════════════════════════╝
\033[0m"""

_banner_shown = False

def main():
    global _banner_shown
    
    if not _banner_shown:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(BANNER)
        _banner_shown = True

    while True:
        print(MENU)
        choice = input('\033[32m >> \033[0m').strip().lower()

        if choice == '1':
            get_available_profiles()
            open_profile()
        elif choice == '2':
            create_profile()
        elif choice == '3':
            get_available_profiles()
            change_proxy()
        elif choice == '4':
            print("\033[32m[+] Goodbye!\033[0m")
            sys.exit()
        else:
            print("\033[31m[!] Unknown choice. Try again.\033[0m")

if __name__ == "__main__":
    main()