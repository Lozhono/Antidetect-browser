# 💀 SOULKILLER — Antidetect Browser

> Antidetect browser based on **Camoufox** (Firefox engine) with profile management, fingerprint spoofing, proxy support and extension loading.

**Help & Support:** [https://t.me/Lozhono](https://t.me/Lozhono)

---

## ✨ Features

- 🧬 **Fingerprint Spoofing** — generates unique fingerprints via BrowserForge: User-Agent, platform, CPU cores, RAM, screen resolution and more
- 🌍 **GeoIP Auto-Detection** — automatically sets timezone and language based on proxy IP
- 🔒 **Proxy Support** — supports two formats:
  - `http://user:pass@host:port`
  - `http://host:port:user:pass`
- 💾 **Persistent Profiles** — each profile stores its own `config.json`, `fingerprint.json` and `proxy.txt`
- 🧩 **Extensions Auto-Load** — place extensions into `Extention/` folder — they load automatically on every launch
- 🔄 **Multi-Profile** — open multiple profiles simultaneously in separate background threads
- 📋 **Session Restore** — browser restores last open tabs on next launch (`browser.startup.page: 3`)
- 🛡️ **Anti-Bot Bypass** — Camoufox patches WebDriver, Canvas, WebGL, AudioContext and disables WebRTC leaks
- 🖥️ **Real Screen Size** — browser window uses your actual monitor resolution

---

## 📋 Requirements

- **Python 3.11** (not 3.12+, not 3.13+)
- **Windows 10 / 11**

---

## ⚙️ Installation

**1.** Install [Python 3.11](https://www.python.org/downloads/release/python-3119/)

**2.** Double-click `install.bat` — it will install all dependencies and download Camoufox browser automatically

---

## 🚀 Launch

```bash
python main.py
```

Or double-click `run.bat`

---

## 🖥️ Menu

```
╔══════════════════════════════════════════════════════╗
║              Select the module:                      ║
╠══════════════════════════════════════════════════════╣
║  [1] 🌐 Open Profile                                 ║
║  [2] ➕ Create Profile                               ║
║  [3] 🔄 Change Proxy                                 ║
║  [4] ❌ Exit                                         ║
╚══════════════════════════════════════════════════════╝
```

---

## 📁 Project Structure

```
soulkiller/
├── main.py                   # Entry point
├── install.bat               # Auto-installer
├── requirements.txt          # Dependencies
├── Extention/                # Firefox extensions (unpacked folders)
├── profiles/                 # Browser profiles (auto-created)
│   └── profile_name/
│       ├── config.json       # Spoofed browser config
│       ├── fingerprint.json  # Full fingerprint data
│       └── proxy.txt         # Proxy for this profile
└── files/
    ├── create_profile.py     # Profile creation logic
    ├── open_profile.py       # Profile launcher
    └── __init__.py
```

---

## 🔧 Proxy Formats

Both formats are supported:

```
http://user:password@p2.mangoproxy.com:2333
http://p2.mangoproxy.com:2333:user:password
```

---

## 🧩 Extensions

1. Download Firefox extension from [addons.mozilla.org](https://addons.mozilla.org)
2. Rename `.xpi` → `.zip` and extract
3. Put the extracted folder into `Extention/`
4. Extensions load automatically on every profile launch

---

## 📦 Dependencies

| Package | Version |
|---------|---------|
| camoufox | 0.4.11 |
| browserforge | 1.2.4 |
| playwright | 1.58.0 |
| patchright | 1.58.0 |
| requests | 2.32.5 |
| geoip2 | 5.2.0 |
| screeninfo | 0.8.1 |
| colorama | 0.4.6 |

---

## ⚠️ Disclaimer

This tool is intended for educational and research purposes only. Use responsibly and in accordance with the terms of service of websites you visit.

---

**Help & Support:** [https://t.me/Lozhono](https://t.me/Lozhono)
