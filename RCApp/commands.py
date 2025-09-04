from tkinter import *
import customtkinter as ctk



class ButtonCommands:

    def __init__(self, root):
        self.root = root
        self._powerStatus = False      

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


    def forward(self):
        if self._powerStatus == True:
            print("Moving Forward")

    def backward(self):
        if self._powerStatus == True:
            print("Moving Backward")

    def accelerate(self):
        if self._powerStatus == True:
            print("Increasing Speed!")

    def decelerate(self):
        if self._powerStatus == True:
            print("Decreasing Speed!")
    
    def left(self):
        if self._powerStatus == True:
            print("Turning Left")

    def right(self):
        if self._powerStatus == True:
            print("Turning Right")

    def stop(self):
        if self._powerStatus == True:
            print("Stopping")

class JoystickCommands:

    def __init__(self, root):
        self.root = root

    def move_up(self):
        print("Joystick moved up")

    def move_down(self):
        print("Joystick moved down")

    def move_left(self):
        print("Joystick moved left")

    def move_right(self):
        print("Joystick moved right")