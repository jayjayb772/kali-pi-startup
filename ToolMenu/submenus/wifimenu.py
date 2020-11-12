import tkinter as tk


class WifiMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Wifi Menu")
        label.pack(pady=10, padx=10)
        print(self)
        print(parent)
        print(controller)
        #print(controller.mainMenu)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.hide_frame(MainMenu))
        button1.pack()
