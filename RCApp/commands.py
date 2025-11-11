from tkinter import *
from RCApp.utils import WiFiClient, CameraFeed


class ButtonCommands:

    def __init__(self, root):
        self.root = root
        self._powerStatus = False 
        self.wifi_client = WiFiClient()     

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
            self.wifi_client.send_command(text)  # Client internally checks WiFi connection prior sending message.


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

    def __init__(self):
        self._camStatus = False 
        self.camera_id = 0                      # Changed from 1 to 0 (default camera)
        self.feed = CameraFeed(self.camera_id)     


    #Set Method for Camera Label
    def set_camera_label(self, label):
        if self.feed:
            self.feed.set_label(label)


    #Get and Set Methods for the 'CameraStatus' attribute. 
    @property
    def camStatus(self):
        return self._camStatus

    @camStatus.setter
    def camStatus(self, status):
        self._camStatus = status

    
    def toggle_camera_feed(self):
        if self.camStatus == True:
            print("Stopping Camera Feed...")
            self.camStatus = False
            self.stop_camera()
        elif self.camStatus == False:
            print("Starting Camera Feed...")
            self.camStatus = True
            self.start_camera()
        return self.camStatus
    
    
    def start_camera(self):
        if not self.feed:
            print("Camera Feed Not Initialized...")
            return
        if self.feed.connect():
            self.feed.start_stream()
            print("Camera Started...")
        else:
            print("Failed to connect to camera.")
            self.camStatus = False


    def stop_camera(self):
        if self.feed:
            self.feed.disconnect()
            print("Camera Stopped...")
        else:
            print("No camera feed to stop.")