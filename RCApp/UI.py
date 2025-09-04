from tkinter import *
import customtkinter as ctk
from customtkinter import CTkButton, CTkCanvas
from RCApp.commands import ButtonCommands, JoystickCommands


class AppUI:
    
    def __init__(self, root):
                
        #Defining Buttons and JoySticks
        self.root = root
        self.commands = ButtonCommands(root)
        self.power = self.commands.powerStatus
        self.joystick_commands = JoystickCommands(root)
        
        # Define color scheme
        self.color_scheme = {"LG":"#B1ABAB",    #Lighter-Gray
                        "MG": "#808080",        #Medium-Gray
                        "DG": "#505050",        #Darker-Gray
                        "Bl": "#202020",        #Black  
                        "G": "#00FF00",         #Green
                        "R": "#FF0000"}         #Red
        
        #Filling the background color of the main window
        self.root.configure(bg=self.color_scheme["LG"])
        ctk.set_appearance_mode("dark")

        #Populate Buttons and JoySticks for Controllers
        self.create_widgets()


    def create_widgets(self):

        # Main Label
        self.label = Label(self.root, text="Universal RC Remote Controller", font=("Arial", 14))
        self.label.place(x=275, y=25)


        # Control Buttons
        self.btn1 = CTkButton(self.root, text="Power", width=10 ,  hover_color= self.color_scheme["DG"], 
                              fg_color=self.color_scheme["R"], command=self.toggle_power)         
        self.btn1.place(x=580, y=70)

        self.btn2 = CTkButton(self.root, text="Stop", width=10 , hover_color= self.color_scheme["DG"], fg_color=self.color_scheme["R"])
        self.btn2.place(x=680, y=70)


        # Right Directional Pad Buttons
        self.d1 = CTkButton(self.root, text="D1", width=10, height=30 , fg_color= self.color_scheme["MG"],
                             hover_color= self.color_scheme["DG"], border_color=self.color_scheme["Bl"], border_width=2)
        self.d1.place(x=195, y=175)

        self.d2 = CTkButton(self.root, text="D2", width=10, height=30 , fg_color= self.color_scheme["MG"],
                             hover_color= self.color_scheme["DG"], border_color= self.color_scheme["Bl"], border_width=2)
        self.d2.place(x=190, y=275)

        self.d3 = CTkButton(self.root, text="D3", width=10, height=30 , fg_color= self.color_scheme["MG"],
                             hover_color= self.color_scheme["DG"], border_color= self.color_scheme["Bl"], border_width=2)
        self.d3.place(x=130, y=225)

        self.d4 = CTkButton(self.root, text="D4", width=10, height=30 , fg_color= self.color_scheme["MG"],
                             hover_color= self.color_scheme["DG"], border_color= self.color_scheme["Bl"], border_width=2)
        self.d4.place(x=250, y=225)
        

        # Left Joystick
        self.js1 = CTkCanvas(self.root, width=120, height=120, bg="gray", highlightthickness=0)
        self.js1.place(x=250, y=375)
        # self.js1.create_oval(20, 20, 100, 100, fill="gray")
        self.js1.create_oval(20, 20, 100, 100, fill="white")
        

        # Right Command Pad Buttons
        self.btn3 = CTkButton(self.root, text="Forward", width=10, fg_color= self.color_scheme["MG"],
                               hover_color= self.color_scheme["DG"], border_color= self.color_scheme["Bl"], border_width=2)
        self.btn3.place(x=595, y=175)

        self.btn4 = CTkButton(self.root, text="Backward", width=10, fg_color= self.color_scheme["MG"],
                               hover_color= self.color_scheme["DG"], border_color= self.color_scheme["Bl"], border_width=2)
        self.btn4.place(x=590, y=275)

        self.btn5 = CTkButton(self.root, text="Left", width=10, fg_color= self.color_scheme["MG"],
                               hover_color= self.color_scheme["DG"], border_color= self.color_scheme["Bl"], border_width=2)
        self.btn5.place(x=530, y=225)

        self.btn6 = CTkButton(self.root, text="Right", width=10, fg_color= self.color_scheme["MG"],
                               hover_color= self.color_scheme["DG"], border_color= self.color_scheme["Bl"], border_width=2)
        self.btn6.place(x=680, y=225)


        # Right Joystick
        self.js2 = CTkCanvas(self.root, width=120, height=120, bg="gray", highlightthickness=0)
        self.js2.place(x=450, y=375)
        # self.js2.create_oval(20, 20, 100, 100, fill="gray")
        self.js2.create_oval(20, 20, 100, 100, fill="white")


        # Additional Buttons
        self.aux1 = CTkButton(self.root, text="AUX1", width=40, height=10 , fg_color= self.color_scheme["MG"],
                             hover_color= self.color_scheme["DG"], border_color=self.color_scheme["Bl"], border_width=2)
        self.aux1.place(x=160, y=130)

        self.aux2 = CTkButton(self.root, text="AUX2", width=40, height=10 , fg_color= self.color_scheme["MG"],
                             hover_color= self.color_scheme["DG"], border_color= self.color_scheme["Bl"], border_width=2)
        self.aux2.place(x=320, y=130)

        self.aux3 = CTkButton(self.root, text="AUX3", width=40, height=10 , fg_color= self.color_scheme["MG"],
                             hover_color= self.color_scheme["DG"], border_color= self.color_scheme["Bl"], border_width=2)
        self.aux3.place(x=480, y=130)

        self.aux4 = CTkButton(self.root, text="AUX4", width=40, height=10 , fg_color= self.color_scheme["MG"],
                             hover_color= self.color_scheme["DG"], border_color= self.color_scheme["Bl"], border_width=2)
        self.aux4.place(x=640, y=130)


    def toggle_power(self):
        self.power = self.commands.toggle_power()
        if self.power == True:
            self.btn1.configure(fg_color = self.color_scheme["G"])
        elif self.power == False:
            self.btn1.configure(fg_color = self.color_scheme["R"])
