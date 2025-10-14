from tkinter import *
# import customtkinter as ctk
from RCApp.utils import MQTTClient


class ButtonCommands:

    def __init__(self, root):
        self.root = root 
        self._powerStatus = False 
        self.mqtt_client = MQTTClient()     

    #Get Method for the 'PowerStatus' attribute. 
    @property
    def powerStatus(self):
        return self._powerStatus
    
    #Set Method for the 'PowerStatus' attribute. 
    @powerStatus.setter
    def powerStatus(self, status):
        self._powerStatus = status
    
    def toggle_power(self):
        if self.powerStatus == True:
            print("Power Off")
            self.powerStatus = False
        elif self.powerStatus == False:
            print("Power On")
            self.powerStatus = True
        return self.powerStatus

    def send_command(self, text):
        if self._powerStatus == True:
            self.mqtt_client.send_command(text)  # Client internally checks WiFi connection prior sending message.
            pass


class JoystickCommands:

    def __init__(self, root):
        self.root = root
        self.js1 = None
        self.js1_knob = None
        self.js2 = None
        self.js2_knob = None
        self.js1_dragging = False
        self.js2_dragging = False

    def set_joysticks(self, js1, js1_knob, js2, js2_knob):
        self.js1 = js1
        self.js1_knob = js1_knob
        self.js2 = js2
        self.js2_knob = js2_knob

    # Left Joystick bindings
    def start_drag_js1(self, event):
        self.js1_dragging = True

    def drag_js1(self, event):
        if self.js1_dragging:
            # Limit knob movement within joystick bounds
            x = min(max(event.x, 30), 90)
            y = min(max(event.y, 30), 90)
            self.js1.coords(self.js1_knob, x-10, y-10, x+10, y+10)

    def end_drag_js1(self, event):
        self.js1_dragging = False

    # Right Joystick bindings
    def start_drag_js2(self, event):
        self.js2_dragging = True

    def drag_js2(self, event):
        if self.js2_dragging:
            x = min(max(event.x, 30), 90)
            y = min(max(event.y, 30), 90)
            self.js2.coords(self.js2_knob, x-10, y-10, x+10, y+10)

    def end_drag_js2(self, event):
        self.js2_dragging = False


class CameraCommands:

    def __init__(self, root):
        self.root = root

    def start_camera(self):
        print("Camera Started")

    def stop_camera(self):
        print("Camera Stopped")