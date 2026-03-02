# 💀 SOULKILLER — Antidetect Browser

> Powerful antidetect browser based on Camoufox (Firefox) with profile management, fingerprint spoofing, and proxy support.

**Help & Support:** [https://t.me/Lozhono](https://t.me/Lozhono)

---

## ✨ Features

- 🧬 **Fingerprint Spoofing** — generates unique browser fingerprints using BrowserForge (User-Agent, platform, CPU cores, RAM, screen resolution, etc.)
- 🌍 **GeoIP Auto-Detection** — automatically sets timezone and language based on proxy IP
- 🔒 **Proxy Support** — supports `http://user:pass@host:port` and `http://host:port:user:pass` formats
- 💾 **Profile Management** — each profile stores its own fingerprint, config, and proxy
- 🧩 **Extensions Support** — load Firefox extensions (`.xpi`) automatically from the `Extention/` folder
- 🔄 **Multi-Profile** — open multiple profiles simultaneously in separate threads
- 📋 **Session Restore** — browser restores last session on next launch
- 🛡️ **Anti-Bot Bypass** — based on Camoufox which patches WebDriver detection, Canvas, WebGL, AudioContext and more

---

## 📋 Requirements

- Python 3.11
- Windows 10/11

---

## ⚙️ Installation

**1. Install Python 3.11** from [python.org](https://www.python.org/downloads/release/python-3119/)

**2. Run installer:**
```
install.bat
```

Or manually:
```bash
pip install -r requirements.txt
python -m camoufox fetch
```

---

## 🚀 Usage

```bash
python main.py
```

Or double-click `run.bat`

---

## 📁 Project Structure

```
soulkiller/
├── main.py                 # Entry point
├── profiles/               # Browser profiles
│   └── profile_name/
│       ├── config.json     # Fingerprint config
│       ├── fingerprint.json
│       └── proxy.txt       # Proxy for this profile
├── Extention/              # Firefox extensions (.xpi)
├── files/
│   ├── create_profile.py   # Profile creation
│   └── open_profile.py     # Profile launcher
├── requirements.txt
├── install.bat
└── run.bat
```

---

## 🖥️ Menu

```
[1] Open Profile    — launch existing profile
[2] Create Profile  — create new profile with fingerprint
[3] Change Proxy    — update proxy for a profile
[4] Exit
```

---

## 🔧 Proxy Formats

Both formats are supported:

```
http://user:password@host:port
http://host:port:user:password
```

Example:
```
http://a7ce322ecdd8cec5053a3-zone-custom:password@p2.mangoproxy.com:2333
```

---

## 📦 Dependencies

| Package | Version |
|---------|---------|
| camoufox | 0.4.11 |
| browserforge | 1.2.4 |
| playwright | 1.58.0 |
| requests | 2.32.5 |
| geoip2 | 5.2.0 |
| screeninfo | 0.8.1 |

---

## ⚠️ Disclaimer

This tool is for educational purposes only. Use responsibly and in accordance with the terms of service of websites you visit.

---

## 📞 Support

Telegram: [https://t.me/Lozhono](https://t.me/Lozhono)
