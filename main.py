from tkinter import *
from RCApp.UI import AppUI


if __name__ == "__main__":
    
    # Initializing the Tkinter Window
    window = Tk()
    window.title("Universal RC Remote Controller")
    
    # Set resizability
    window.resizable(True, True)

    # Load and set window icon
    icon_path = "images/icon.png"
    icon_img = PhotoImage(file=icon_path)
    window.iconphoto(False, icon_img)
    
    # Initialize the UI
    app_ui = AppUI(window)

    # Start the main loop
    window.mainloop()
    
    # If Quit Button is pressed, destroy the window
    window.protocol("WM_DELETE_WINDOW", window.destroy)
    if hasattr(window, 'destroy'):
        window.destroy()