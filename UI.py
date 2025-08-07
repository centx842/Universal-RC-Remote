from tkinter import Tk, Label, Button

class AppUI:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self.root, text="Welcome to the Universal RC Remote Controller", font=("Arial", 14))
        self.label.grid(column=0, row=0, padx=10, pady=10)

        btn1 = Button(self.root, text="Power", width=10)
        btn1.grid(column=0, row=1, padx=5, pady=5)

        btn2 = Button(self.root, text="Forward", width=10)
        btn2.grid(column=1, row=1, padx=5, pady=5)

        bt3n3 = Button(self.root, text="Backward", width=10)
        bt3n3.grid(column=2, row=1, padx=5, pady=5)

        btn4 = Button(self.root, text="Left", width=10)
        btn4.grid(column=0, row=2, padx=5, pady=5)

        btn5 = Button(self.root, text="Right", width=10)
        btn5.grid(column=1, row=2, padx=5, pady=5)

        btn6 = Button(self.root, text="Stop", width=10)
        btn6.grid(column=2, row=2, padx=5, pady=5)
