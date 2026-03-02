import os
import json
import ctypes
import threading
from pathlib import Path
from camoufox.sync_api import Camoufox


def launch_browser(clean_config, profile_path, name_profile, proxy_config=None):

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    extensions_dir = os.path.join(base_dir, "Extention")
    addons = [
    os.path.join(extensions_dir, f)
    for f in os.listdir(extensions_dir)
    if os.path.isdir(os.path.join(extensions_dir, f))
]


    try:
        with Camoufox(
            headless=False,
            persistent_context=True,
            user_data_dir=profile_path,
            os='windows',
            geoip=True,
            addons=addons,
            config=clean_config,
            i_know_what_im_doing=True,
            proxy=proxy_config,
            
            firefox_user_prefs={
                "browser.startup.page": 3, 
                "browser.sessionstore.resume_from_crash": True,
                "privacy.resistFingerprinting": False,
                "privacy.resistFingerprinting.letterboxing": False,
                "dom.disable_window_move_resize": False,
                "media.peerconnection.enabled": False,
            }
        ) as browser:
            print(f"[+] Browser '{name_profile}' opened.")        
            browser.wait_for_event("close", timeout=0) 

    except Exception as e:
        if "Target closed" in str(e) or "EPIPE" in str(e):
            pass
        else:
            print(f"[!] Error in profile '{name_profile}': {e}")
    finally:
        print(f"[+] Browser '{name_profile}' session finished.")

def change_proxy():
    name_profile = input("Enter profile name: ").strip()
    if not name_profile:
        print("Error: Profile name cannot be empty!")
        return

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    profile_path = os.path.join(base_dir, "profiles", name_profile)

    if not os.path.exists(profile_path):
        print(f"Error: Profile '{name_profile}' not found!")
        return

    proxy = input("Enter Proxy (protocol://user:pass@host:port) [Enter to remove]: ").strip()

    proxy_file = os.path.join(profile_path, "proxy.txt")

    if proxy:
        with open(proxy_file, "w", encoding="utf-8") as f:
            f.write(proxy)
        print(f"[+] Proxy saved for profile '{name_profile}'")
    else:
        if os.path.exists(proxy_file):
            os.remove(proxy_file)
            print(f"[+] Proxy removed for profile '{name_profile}'")
        else:
            print(f"[*] No proxy to remove")



def open_profile():
    name_profile = input("Enter profile name to start: ").strip()
    if not name_profile: return

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    profile_path = os.path.join(base_dir, "profiles", name_profile)

    if not os.path.exists(profile_path):
        print(f"Error: Profile '{name_profile}' not found!")
        return

    config_file = os.path.join(profile_path, "config.json")
    with open(config_file, "r", encoding="utf-8") as f:
        config_data = json.load(f)

    proxy_config = None
    proxy_file = os.path.join(profile_path, "proxy.txt")
    if os.path.exists(proxy_file):
        with open(proxy_file, "r", encoding="utf-8") as f:
            p_raw = f.read().strip()
        try:
            if "@" in p_raw:
                proto, rest = p_raw.split("://")
                auth, srv = rest.split("@")
                u, p = auth.split(":")
                proxy_config = {"server": f"{proto}://{srv}", "username": u, "password": p}
            else:
                proto, rest = p_raw.split("://")
                parts = rest.split(":")
                proxy_config = {"server": f"{proto}://{parts[0]}:{parts[1]}", "username": parts[2], "password": parts[3]}
        except:
            print("\033[31m[!] Proxy format error\033[0m")
            
    allowed_keys = ['window.history.length', 'navigator.hardwareConcurrency', 'navigator.maxTouchPoints']
    clean_config = {k: v for k, v in config_data.items() if k in allowed_keys}
    
    user32 = ctypes.windll.user32
    sw, sh = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    clean_config.update({'window.innerWidth': sw, 'window.innerHeight': sh - 100, 'window.outerWidth': sw, 'window.outerHeight': sh, 'screen.width': sw, 'screen.height': sh})

    print(f"[*] Launching '{name_profile}'...")
    threading.Thread(target=launch_browser, args=(clean_config, profile_path, name_profile, proxy_config), daemon=True).start()


def get_available_profiles():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    profiles_dir = os.path.join(base_dir, "profiles")

    if not os.path.exists(profiles_dir):
        print("[!] Profiles is not found")
        return

    folders = [f for f in os.listdir(profiles_dir) if os.path.isdir(os.path.join(profiles_dir, f))]

    print("\n" + "="*50)
    print(f"{'Profile':<20} | {'Proxy'}")
    print("-"*50)

    for folder in folders:
        proxy_file_path = os.path.join(profiles_dir, folder, "proxy.txt")
        proxy_value = ""

        if os.path.exists(proxy_file_path):
            try:
                with open(proxy_file_path, "r", encoding="utf-8") as f:
                    proxy_value = f.read().strip()
            except Exception:
                proxy_value = "[Error]"

        if proxy_value:
            print(f"{folder:<20} | {proxy_value}")
        else:
            print(f"{folder:<20} | ---")

    print("="*50 + "\n")