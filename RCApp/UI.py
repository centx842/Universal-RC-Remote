from tkinter import *
import customtkinter as ctk
from customtkinter import CTkButton, CTkCanvas, CTkTextbox, CTkFrame, CTkLabel, CTkSlider
from RCApp.commands import ButtonCommands, JoystickCommands
from RCApp.utils import add_time_stamp


class AppUI:
    
    def __init__(self, root):
                
        #Defining Buttons and JoySticks
        self.root = root
        self.root.geometry("1000x750")
        self.commands = ButtonCommands(root)
        self.power = self.commands.powerStatus
        self.slider_steps = 3               # Number of steps in the slider (0 to 3)
        self.mode = "None"                  # Placeholder for communication channel (e.g., serial port)
        self.joystick_commands = JoystickCommands(root)
        # self.joystick_position = (0, 0)
        
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
        self.main_frame.rowconfigure(2, weight=1)  # Row 3 expands for Pads and Camera Feed
        self.main_frame.rowconfigure(3, weight=1)  # Row 4 expands for Joysticks 
        self.main_frame.rowconfigure(4, weight=0)  # Row 5 fixed for Log Board Heading
        self.main_frame.rowconfigure(5, weight=0)  # Row 6 fixed for Log Board


    def create_widgets(self):

        # ROW 1 --- Main Label and Control Buttons
        top_frame = CTkFrame(self.main_frame, fg_color=self.color_scheme["LG"])
        top_frame.grid(row=0, column=0, sticky="ew", pady=10)

        self.main_label = Label(top_frame, text="Universal RC Remote Controller", font=("Arial", 14))
        self.main_label.pack(side="left", padx=20)

        button_frame = CTkFrame(top_frame)
        button_frame.pack(side="right", padx=20)

        self.slider_value = CTkLabel(top_frame, font=("Arial", 14))
        self.slider_value.pack(side="right", padx=20)
        self.slider_value.configure(text="None")  # "None" as Default

        self.slider = CTkSlider(button_frame, width=120, button_hover_color=self.color_scheme["DG"], fg_color=self.color_scheme["MG"], 
                                button_color=self.color_scheme["DG"], number_of_steps=self.slider_steps , command=self.set_slider_value)  # Pass the callback with value argument
        self.slider.pack(side="left", padx=5)
        self.slider.set(0)
        self.slider_value.configure(text="None")

        self.btn2 = CTkButton(button_frame, text="Stop", width=10, hover_color=self.color_scheme["DG"], fg_color=self.color_scheme["R"],
                              command = lambda: self.send_msg("S"))
        self.btn2.pack(side="left", padx=5)
        
        self.btn1 = CTkButton(button_frame, text="Power", width=10, hover_color=self.color_scheme["DG"], 
                              fg_color=self.color_scheme["R"], command=self.toggle_power)         
        self.btn1.pack(side="left", padx=5)

        


        # ROW 2 --- Additional Buttons 
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


        # ROW 3 --- Left and Right Directional Pad Buttons
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

        # Sub-Frame 2 (Camera Feed) - Placed between left and right pads
        camera_frame = CTkFrame(pads_frame, fg_color=self.color_scheme["MG"], border_color=self.color_scheme["Bl"], border_width=2)
        camera_frame.pack(side="left", expand=True, fill="both", padx=20, pady=10)
        camera_label = CTkLabel(camera_frame, text="Camera Feed", font=("Arial", 14), fg_color=self.color_scheme["MG"], width=200, height=150)
        camera_label.pack(expand=True, fill="both", padx=10, pady=10)

        # ...inside create_widgets...
        # camera_frame = CTkFrame(pads_frame, fg_color=self.color_scheme["MG"], border_color=self.color_scheme["Bl"], border_width=2)
        # camera_frame.pack(side="left", expand=True, fill="both", padx=20, pady=10)
        # self.camera_label = CTkLabel(camera_frame, text="Camera Feed", font=("Arial", 14), fg_color=self.color_scheme["MG"], width=200, height=150)
        # self.camera_label.pack(expand=True, fill="both", padx=10, pady=10)

        # Sub-Frame 3 (For Right Directional Pad)
        right_pad = CTkFrame(pads_frame, fg_color=self.color_scheme["LG"])
        right_pad.pack(side="left", expand=True, fill="both", padx=20)
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

        
        # ROW 4 --- JoySticks Buttons
        js_frame = CTkFrame(self.main_frame, fg_color=self.color_scheme["LG"])
        js_frame.grid(row=3, column=0, sticky="ew", pady=10)
        
        # Left Joystick
        self.js1 = CTkCanvas(js_frame, width=120, height=120, bg=self.color_scheme["MG"], highlightthickness=0)
        self.js1.pack(side="left", expand=True, padx=20)
        self.js1.create_oval(20, 20, 100, 100, fill="gray")
        self.js1_knob = self.js1.create_oval(60, 60, 80, 80, fill="white")
        
        # Right Joystick
        self.js2 = CTkCanvas(js_frame, width=120, height=120, bg=self.color_scheme["MG"], highlightthickness=0)
        self.js2.pack(side="right", expand=True, padx=20)
        self.js2.create_oval(20, 20, 100, 100, fill="gray")
        self.js2_knob = self.js2.create_oval(60, 60, 80, 80, fill="white")

        # Pass canvas and knob references to JoystickCommands
        self.joystick_commands.set_joysticks(self.js1, self.js1_knob, self.js2, self.js2_knob)
        self.js1.bind("<Button-1>", self.joystick_commands.start_drag_js1)
        self.js1.bind("<B1-Motion>", self.joystick_commands.drag_js1)
        self.js1.bind("<ButtonRelease-1>", self.joystick_commands.end_drag_js1)
        self.js1_dragging = False
        self.js2.bind("<Button-1>", self.joystick_commands.start_drag_js2)
        self.js2.bind("<B1-Motion>", self.joystick_commands.drag_js2)
        self.js2.bind("<ButtonRelease-1>", self.joystick_commands.end_drag_js2)
        self.js2_dragging = False


        # ROW 5 --- Log Board Heading
        log_heading_frame = CTkFrame(self.main_frame, fg_color=self.color_scheme["LG"])
        log_heading_frame.grid(row=4, column=0, sticky="ew", pady=10)

        self.label = Label(log_heading_frame, text="Command Log Board:", font=("Arial", 14))
        self.label.pack(side="left", padx=20)

        
        # ROW 6 --- Log Board for Displaying Event Listeners and their Events
        log_frame = CTkFrame(self.main_frame, fg_color=self.color_scheme["LG"])
        log_frame.grid(row=5, column=0, sticky="ew", pady=10)

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


    def set_slider_value(self, value):
        if 0 <= value < 0.25:
            self.mode = "None"
        elif 0.25 <= value < 0.5:
            self.mode = "WiFi Mode"
        elif 0.5 <= value < 0.75:
            self.mode = "BT Mode"
        elif 0.75 <= value < 1.0:
            self.mode = "RF Mode"
        else:
            self.mode = "Unknown"
        self.slider_value.configure(text=self.mode)

        # Handle MQTT connection based on mode
        if self.mode == "WiFi Mode":
            self.commands.mqtt_client.connect()
        else:
            self.commands.mqtt_client.disconnect()


    def send_msg(self, msg):

        #Check if the Power Button is ON
        if self.power == True and self.mode != "None":
            
            #Concatenate TimeStamp onto Message
            text = f"{add_time_stamp()} | Mode: {self.mode} | Button: {msg}"

            #Print Message on Terminal 
            print(text)

            #Print Message on Check Box
            self.logBoard.configure(state="normal")
            self.logBoard.insert("end", text + "\n")
            self.logBoard.configure(state="disabled")
            self.logBoard.see("end")  # Scroll to the end

            #Send Message to the RC Vehicle
            self.commands.send_command(text)


    def get_camera_feed(self):
        pass


    def get_joystick_position(self):
        pass

