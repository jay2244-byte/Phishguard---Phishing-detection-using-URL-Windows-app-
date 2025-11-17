# PhishGuard

PhishGuard is a Windows application that helps protect you from phishing websites by monitoring your web browsers and alerting you when it detects a potential phishing site.

## Features

- **Real-time Browser Monitoring**: Monitors your web browsers to detect URL navigation
- **Advanced Phishing Detection**: Uses multiple indicators to identify potential phishing sites
- **User-friendly Interface**: Simple and intuitive interface with minimal design
- **Alert System**: Displays alerts when potential phishing sites are detected
- **System Tray Integration**: Runs in the background with system tray access
- **Easy Installation**: Simple installer for Windows

## Installation

### Prerequisites

- Windows 10 or later
- Python 3.8 or later (if installing from source)

### Installing from Source

1. Clone the repository or download the source code
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python main.py
   ```

### Creating an Installer

To create a standalone Windows installer:

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Run the installer script:
   ```
   python utils/installer.py
   ```
3. The installer will be created in the `dist` directory

## Usage

1. Launch PhishGuard from the Start menu or desktop shortcut
2. The application will run in the background and monitor your web browsers
3. When a potential phishing site is detected, an alert will be displayed
4. You can access the main interface by clicking on the PhishGuard icon in the system tray

## How It Works

PhishGuard uses a combination of techniques to detect potential phishing websites:

1. **URL Analysis**: Examines URLs for suspicious patterns, keywords, and structures
2. **Domain Analysis**: Checks for typosquatting, suspicious TLDs, and domain age
3. **Content Analysis**: Analyzes webpage content for phishing indicators
4. **Reputation Checking**: Compares against known legitimate domains

## Development

### Project Structure

```
PhishGuard/
├── core/                 # Core functionality
│   ├── __init__.py
│   ├── browser_monitor.py  # Browser monitoring module
│   └── phishing_detector.py  # Phishing detection module
├── gui/                  # User interface
│   ├── __init__.py
│   ├── alert_dialog.py     # Phishing alert dialog
│   └── main_window.py      # Main application window
├── resources/            # Application resources
│   ├── icon.svg           # Application icon
│   └── logo.svg           # Application logo
├── utils/                # Utility modules
│   ├── __init__.py
│   └── installer.py       # Installer creation utility
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

PhishGuard is provided as-is without any guarantees or warranty. While the application aims to detect phishing websites, it may not detect all phishing attempts. Users should always exercise caution when browsing the internet and never enter sensitive information on websites they don't trust.