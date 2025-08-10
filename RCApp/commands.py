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
    
    def togglePower(self):
        if self._powerStatus == False:
            self._powerStatus = True
            print("POWER ON!")
        else:
            self._powerStatus = False
            print("POWER OFF!")

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