from tkinter import *
from RemoteApp.UI import AppUI
from RemoteApp.commands import ButtonCommands

if __name__ == "__main__":
    window = Tk()
    window.title("Universal RC Remote Controller")
    window.geometry("800x600")

    # Initialize the UI
    app_ui = AppUI(window)

    # # Bind commands to buttons or other UI elements
    # app_ui.bind_commands(commands)

    # Start the main loop
    window.mainloop()
    
    # If Quit Button is pressed, destroy the window
    window.protocol("WM_DELETE_WINDOW", window.destroy)
    if hasattr(window, 'destroy'):
        window.destroy()