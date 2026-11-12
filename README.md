# Python Tkinter Ping Tool 🏓

A simple, cross-platform graphical utility built with **Python** and **Tkinter** to test network connectivity and latency using your system's native `ping` command.

---

## ✨ Features

* **Smart URL Sanitization:** Automatically strips away protocols (`https://`, `http://`) and trailing paths/slashes from pasted web addresses, leaving just the clean domain or IP.
* **Non-Blocking UI:** Runs network pings in a background worker thread so the graphical window never freezes or grays out while waiting for responses.
* **Cross-Platform Compatibility:** Automatically detects your operating system and applies the correct packet count flag (`-n` for Windows, `-c` for macOS/Linux).
* **Modern Dark Theme Output:** Displays results in a clean, high-contrast monospace console view.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed on your system.
* No external third-party libraries required (uses Python standard libraries only: `tkinter`, `subprocess`, `threading`, `platform`, `urllib.parse`).

### Running the Application

1. Save the script as `ping_app.py`.
2. Open your terminal or command prompt in the folder where you saved the file.
3. Run the script:
   ```bash
   python ping_app.py
