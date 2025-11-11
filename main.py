import os
import sys
from tkinter import *
from RCApp.UI import AppUI


def resource_path(relative_path):
    """Get absolute path to resource (works for dev and PyInstaller binary)."""
    try:
        # PyInstaller stores data in a temporary _MEIPASS folder
        base_path = sys._MEIPASS
    except Exception:
        # When running in normal (non-bundled) mode
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    # Initialize Tkinter Window
    window = Tk()
    window.title("Universal RC Remote Controller")

    # Set resizability
    window.resizable(True, True)

    # Load and set window icon safely
    icon_path = resource_path("images/icon.png")
    icon_img = PhotoImage(file=icon_path)
    window.iconphoto(False, icon_img)

    # Initialize the UI
    app_ui = AppUI(window)

    # Ensure window closes cleanly
    window.protocol("WM_DELETE_WINDOW", window.destroy)

    # Start the main loop
    window.mainloop()
