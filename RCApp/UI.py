from tkinter import *
import customtkinter as ctk
from customtkinter import CTkButton, CTkCanvas, CTkTextbox, CTkFrame, CTkLabel
from RCApp.commands import ButtonCommands, JoystickCommands
from RCApp.utils import add_time_stamp


class AppUI:
    
    def __init__(self, root):
                
        #Defining Buttons and JoySticks
        self.root = root
        self.root.geometry("800x750")
        self.commands = ButtonCommands(root)
        self.power = self.commands.powerStatus
        self.joystick_commands = JoystickCommands(root)
        
        # Define color scheme
        self.color_scheme = {"W":"#FFFFFF",     #White
                        "LG":"#B1ABAB",         #Lighter-Gray
                        "MG": "#808080",        #Medium-Gray
                        "DG": "#505050",        #Darker-Gray
                        "Bl": "#202020",        #Black  
                        "G": "#00FF00",         #Green
                        "R": "#FF0000"}         #Red
        
        # Filling the background color of the main window
        self.root.configure(bg=self.color_scheme["LG"])

        # Setting the Main Frame on the App Window 
        self.set_main_frame()

        # Populate Buttons and JoySticks for Controllers
        self.create_widgets()


    def set_main_frame(self):
        
        # Main frame to hold everything
        self.main_frame = CTkFrame(self.root, fg_color=self.color_scheme["LG"])
        self.main_frame.pack(fill="both", expand=True)

        # Configure grid weights for resizability
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=0)  # Row 1 fixed for Main Label and Control Buttons
        self.main_frame.rowconfigure(1, weight=0)  # Row 2 fixed for Aux Button
        self.main_frame.rowconfigure(2, weight=1)  # Row 3 expands for Pads 
        self.main_frame.rowconfigure(3, weight=1)  # Row 4 expands for Joysticks 
        self.main_frame.rowconfigure(4, weight=0)  # Row 5 fixed for Log Board


    def create_widgets(self):

        # Main Label and Control Buttons in Row 1
        top_frame = CTkFrame(self.main_frame, fg_color=self.color_scheme["LG"])
        top_frame.grid(row=0, column=0, sticky="ew", pady=10)

        self.label = Label(top_frame, text="Universal RC Remote Controller", font=("Arial", 14))
        self.label.pack(side="left", padx=20)

        button_frame = CTkFrame(top_frame)
        button_frame.pack(side="right", padx=20)

        self.btn1 = CTkButton(button_frame, text="Power", width=10, hover_color=self.color_scheme["DG"], 
                              fg_color=self.color_scheme["R"], command=self.toggle_power)         
        self.btn1.pack(side="left", padx=5)

        self.btn2 = CTkButton(button_frame, text="Stop", width=10, hover_color=self.color_scheme["DG"], fg_color=self.color_scheme["R"],
                              command = lambda: self.send_msg("S"))
        self.btn2.pack(side="left", padx=5)


        # Additional Buttons in Row 2
        aux_frame = CTkFrame(self.main_frame, fg_color=self.color_scheme["LG"])
        aux_frame.grid(row=1, column=0, sticky="ew", pady=10)

        self.aux1 = CTkButton(aux_frame, text="AUX1", width=40, height=10 , fg_color= self.color_scheme["MG"],
                             hover_color= self.color_scheme["DG"], border_color=self.color_scheme["Bl"], 
                             command = lambda: self.send_msg("A1"), border_width=2)
        self.aux1.pack(side="left", expand=True)

        self.aux2 = CTkButton(aux_frame, text="AUX2", width=40, height=10 , fg_color= self.color_scheme["MG"],
                             hover_color= self.color_scheme["DG"], border_color= self.color_scheme["Bl"], 
                             command = lambda: self.send_msg("A2"), border_width=2)
        self.aux2.pack(side="left", expand=True)

        self.aux3 = CTkButton(aux_frame, text="AUX3", width=40, height=10 , fg_color= self.color_scheme["MG"],
                             hover_color= self.color_scheme["DG"], border_color= self.color_scheme["Bl"], 
                             command = lambda: self.send_msg("A3"), border_width=2)
        self.aux3.pack(side="left", expand=True)

        self.aux4 = CTkButton(aux_frame, text="AUX4", width=40, height=10 , fg_color= self.color_scheme["MG"],
                             hover_color= self.color_scheme["DG"], border_color= self.color_scheme["Bl"], 
                             command = lambda: self.send_msg("A4"), border_width=2)
        self.aux4.pack(side="left", expand=True)


        # Left and Right Directional Pad Buttons in Row 3
        pads_frame = CTkFrame(self.main_frame, fg_color=self.color_scheme["LG"])
        pads_frame.grid(row=2, column=0, sticky="nsew", pady=10)
        
        # Sub-Frame 1 (For Left Directional Pad)
        left_pad = CTkFrame(pads_frame, fg_color=self.color_scheme["LG"])
        left_pad.pack(side="left", expand=True, fill="both", padx=20)
        left_pad.rowconfigure([0,1,2], weight=1)
        left_pad.columnconfigure([0,1,2], weight=1)

        self.d1 = CTkButton(left_pad, text="D1", width=10, height=30, fg_color=self.color_scheme["MG"],
                            hover_color=self.color_scheme["DG"], border_color=self.color_scheme["Bl"], 
                            command = lambda: self.send_msg("D1"), border_width=2)
        self.d1.grid(row=0, column=1)

        self.d3 = CTkButton(left_pad, text="D3", width=10, height=30, fg_color=self.color_scheme["MG"],
                            hover_color=self.color_scheme["DG"], border_color=self.color_scheme["Bl"], 
                            command = lambda: self.send_msg("D2"), border_width=2)
        self.d3.grid(row=1, column=0)

        self.d4 = CTkButton(left_pad, text="D4", width=10, height=30, fg_color=self.color_scheme["MG"],
                            hover_color=self.color_scheme["DG"], border_color=self.color_scheme["Bl"], 
                            command = lambda: self.send_msg("D3"), border_width=2)
        self.d4.grid(row=1, column=2)

        self.d2 = CTkButton(left_pad, text="D2", width=10, height=30, fg_color=self.color_scheme["MG"],
                            hover_color=self.color_scheme["DG"], border_color=self.color_scheme["Bl"], 
                            command = lambda: self.send_msg("D4"), border_width=2)
        self.d2.grid(row=2, column=1)
        
        #Sub-Frame 2 (For Right Directional Pad)
        right_pad = CTkFrame(pads_frame, fg_color=self.color_scheme["LG"])
        right_pad.pack(side="right", expand=True, fill="both", padx=20)
        right_pad.rowconfigure([0,1,2], weight=1)
        right_pad.columnconfigure([0,1,2], weight=1)
        
        self.btn3 = CTkButton(right_pad, text="Forward", width=10, fg_color=self.color_scheme["MG"],
                              hover_color=self.color_scheme["DG"], border_color=self.color_scheme["Bl"],  
                            command = lambda: self.send_msg("F"), border_width=2)
        self.btn3.grid(row=0, column=1)

        self.btn5 = CTkButton(right_pad, text="Left", width=10, fg_color=self.color_scheme["MG"],
                              hover_color=self.color_scheme["DG"], border_color=self.color_scheme["Bl"], 
                            command = lambda: self.send_msg("L"), border_width=2)
        self.btn5.grid(row=1, column=0)

        self.btn6 = CTkButton(right_pad, text="Right", width=10, fg_color=self.color_scheme["MG"],
                              hover_color=self.color_scheme["DG"], border_color=self.color_scheme["Bl"], 
                            command = lambda: self.send_msg("R"), border_width=2)
        self.btn6.grid(row=1, column=2)

        self.btn4 = CTkButton(right_pad, text="Backward", width=10, fg_color=self.color_scheme["MG"],
                              hover_color=self.color_scheme["DG"], border_color=self.color_scheme["Bl"], 
                            command = lambda: self.send_msg("B"), border_width=2)
        self.btn4.grid(row=2, column=1)

        
        # JoySticks Buttons in Row 4
        js_frame = CTkFrame(self.main_frame, fg_color=self.color_scheme["LG"])
        js_frame.grid(row=3, column=0, sticky="ew", pady=10)
        
        # Left Joystick
        self.js1 = CTkCanvas(js_frame, width=120, height=120, bg=self.color_scheme["MG"], highlightthickness=0)
        self.js1.pack(side="left", expand=True, padx=20)
        # self.js1.create_oval(20, 20, 100, 100, fill="gray")
        self.js1.create_oval(20, 20, 100, 100, fill="white")

        # Right Joystick
        self.js2 = CTkCanvas(js_frame, width=120, height=120, bg=self.color_scheme["MG"], highlightthickness=0)
        self.js2.pack(side="right", expand=True, padx=20)
        # self.js2.create_oval(20, 20, 100, 100, fill="gray")
        self.js2.create_oval(20, 20, 100, 100, fill="white")



        # Log Board for Displaying Event Listeners and their Events in Row 5
        log_frame = CTkFrame(self.main_frame, fg_color=self.color_scheme["LG"])
        log_frame.grid(row=4, column=0, sticky="ew", pady=10)

        self.label = Label(top_frame, text="Command Log Board:", font=("Arial", 14))
        self.label.pack(side="left", padx=20)

        self.logBoard = CTkTextbox(log_frame, height=250, border_color=self.color_scheme["MG"],
                                   fg_color=self.color_scheme["W"], text_color=self.color_scheme["Bl"])
        self.logBoard.pack(fill="x", expand=True)
        self.logBoard.insert("0.0", "All Command Logs will appear here...")
        self.logBoard.delete("0.0", "end")
        self.logBoard.configure(state="disabled")  # Read-only


    def toggle_power(self):
        self.power = self.commands.toggle_power()
        if self.power == True:
            self.btn1.configure(fg_color = self.color_scheme["G"])
        elif self.power == False:
            self.btn1.configure(fg_color = self.color_scheme["R"])


    def send_msg(self, msg):

        #Concatenate TimeStamp onto Message
        text = f"{add_time_stamp()} Button: {msg}"

        #Print Message on Terminal 
        print(text)

        #Print Message on Check Box
        self.logBoard.configure(state="normal")
        self.logBoard.insert("end", text + "\n")
        self.logBoard.configure(state="disabled")
        self.logBoard.see("end")  # Scroll to the end
