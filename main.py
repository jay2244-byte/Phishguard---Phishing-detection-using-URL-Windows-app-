# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# """
# PhishGuard - A Windows application to detect phishing websites

# This is the main entry point for the PhishGuard application.
# It initializes the GUI and starts the browser monitoring service.
# """

import sys
import os
import logging
import socket
import tempfile
import win32api
import win32con
import win32gui
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

from gui.main_window import MainWindow
from core.browser_monitor import BrowserMonitor
from core.phishing_detector import PhishingDetector

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'phishguard.log')),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('PhishGuard')


def is_already_running():
    """Check if another instance of PhishGuard is already running"""
    try:
        # Try to create a socket on a specific port
        # If it fails, another instance is already using that port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 47365))  # Use a unique port for PhishGuard
        sock.listen(1)
        return False
    except socket.error:
        return True

def activate_existing_instance():
    """Find and activate the existing PhishGuard window"""
    def enum_windows_callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            window_text = win32gui.GetWindowText(hwnd)
            if "PhishGuard" in window_text:
                # Restore the window if minimized
                if win32gui.IsIconic(hwnd):
                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                # Bring the window to the front
                win32gui.SetForegroundWindow(hwnd)
                return True
        return True
    
    win32gui.EnumWindows(enum_windows_callback, None)

def add_to_startup():
    """Add PhishGuard to Windows startup"""
    try:
        # Get the path to the executable
        if getattr(sys, 'frozen', False):
            # Running as compiled executable
            app_path = sys.executable
        else:
            # Running as script
            app_path = os.path.abspath(__file__)
            
        # Create registry key
        import winreg
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0, winreg.KEY_SET_VALUE
        )
        
        winreg.SetValueEx(key, "PhishGuard", 0, winreg.REG_SZ, f'"{app_path}"')
        winreg.CloseKey(key)
        logger.info("Added PhishGuard to startup")
        return True
    except Exception as e:
        logger.error(f"Error adding to startup: {e}")
        return False

def main():
    """Main function to start the PhishGuard application"""
    try:
        # Check if another instance is already running
        if is_already_running():
            # Try to activate the existing instance
            activate_existing_instance()
            logger.info("Another instance of PhishGuard is already running. Exiting.")
            # Show a message box
            if QApplication.instance() is None:
                app = QApplication(sys.argv)
            QMessageBox.information(None, "PhishGuard", "PhishGuard is already running.")
            return
        
        # Initialize the application
        app = QApplication(sys.argv)
        app.setApplicationName("PhishGuard")
        
        # Set application icon
        icon_path = ''
        if getattr(sys, 'frozen', False):
            # Running as compiled executable
            icon_path = os.path.join(os.path.dirname(sys.executable), 'resources', 'icon.svg')
        else:
            # Running as script
            icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'icon.svg')
            
        app.setWindowIcon(QIcon(icon_path))
        
        # Initialize the phishing detector
        phishing_detector = PhishingDetector()
        
        # Initialize the browser monitor
        browser_monitor = BrowserMonitor(phishing_detector)
        
        # Initialize the main window
        main_window = MainWindow(browser_monitor, phishing_detector)
        
        # Check command line arguments
        if len(sys.argv) > 1 and sys.argv[1] == "--minimized":
            # Start minimized to system tray
            logger.info("Starting minimized to system tray")
        else:
            # Show the main window
            main_window.show()
        
        # Start the browser monitor
        browser_monitor.start()
        
        # Start the application event loop
        sys.exit(app.exec_())
        
    except Exception as e:
        logger.error(f"Error starting PhishGuard: {e}")
        if QApplication.instance() is None:
            app = QApplication(sys.argv)
        QMessageBox.critical(None, "PhishGuard Error", f"An error occurred while starting PhishGuard:\n{str(e)}")
        return 1


if __name__ == "__main__":
    main()