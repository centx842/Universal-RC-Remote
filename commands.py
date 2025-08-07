from tkinter import *


class ButtonCommands:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def forward(self):
        print("Moving Forward")

    def backward(self):
        print("Moving Backward")

    def left(self):
        print("Turning Left")

    def right(self):
        print("Turning Right")

    def stop(self):
        print("Stopping")