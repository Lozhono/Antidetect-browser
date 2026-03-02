import os
import json
from browserforge.fingerprints import FingerprintGenerator
from camoufox.sync_api import Camoufox

def create_profile():
    name_profile = input("Enter profile name: ").strip()
    if not name_profile:
        print("Error: Profile name cannot be empty!")
        return

    proxy = input("Enter Proxy (protocol://ip:port:user:pass) [Enter for none]: ").strip()

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    profile_path = os.path.join(base_dir, "profiles", name_profile)
    os.makedirs(profile_path, exist_ok=True)
    
    print(f"[*] Path created: {profile_path}")
    
    
    print("[*] Generating random fingerprint...")
    fg = FingerprintGenerator(os=['windows', 'macos', 'linux'])
    fingerprint = fg.generate()
    
    
    config_data = {
        'window.outerHeight': 1200,
        'window.outerWidth': 1920,
        'window.innerHeight': 1200,
        'window.innerWidth': 1920,
        'window.history.length': 4,
        'navigator.userAgent': fingerprint.headers.get('User-Agent', 'Mozilla/5.0'),
        'navigator.appCodeName': 'Mozilla',
        'navigator.appName': '',
        'navigator.appVersion': '5.0',
        'navigator.platform': fingerprint.navigator.platform,
        'navigator.hardwareConcurrency': getattr(fingerprint.navigator, 'hardwareConcurrency', 12),
        'navigator.deviceMemory': getattr(fingerprint.navigator, 'deviceMemory', 8),
        'navigator.maxTouchPoints': 10,
    }
    
    
    config_file = os.path.join(profile_path, "config.json")
    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=4, ensure_ascii=False)
    print(f"[+] Fingerprint config saved")
    print(f"    - User-Agent: {config_data['navigator.userAgent'][:50]}...")
    print(f"    - Resolution: {config_data['window.outerWidth']}x{config_data['window.outerHeight']}")
    print(f"    - Hardware Cores: {config_data['navigator.hardwareConcurrency']}")
    
    
    fp_full = {
        "headers": fingerprint.headers,
        "navigator": fingerprint.navigator.__dict__ if hasattr(fingerprint.navigator, '__dict__') else {},
        "screen": fingerprint.screen.__dict__ if hasattr(fingerprint.screen, '__dict__') else {},
    }
    
    fingerprint_file = os.path.join(profile_path, "fingerprint.json")
    with open(fingerprint_file, "w", encoding="utf-8") as f:
        json.dump(fp_full, f, indent=4, ensure_ascii=False, default=lambda o: o.__dict__ if hasattr(o, '__dict__') else str(o))
    print(f"[+] Full fingerprint saved")
    
    
    if proxy:
        proxy_file = os.path.join(profile_path, "proxy.txt")
        with open(proxy_file, "w", encoding="utf-8") as f:
            f.write(proxy)
        print(f"[+] Proxy saved")
    else:
        print("[*] No proxy provided")

    print(f"\n[+] Profile '{name_profile}' created successfully!")
    print("[*] Profile data saved to disk (config, fingerprint, proxy)")
    
    return profile_path


