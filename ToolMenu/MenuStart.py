import tkinter as tk
# from ToolMenu.submenus.mainmenu import MainMenu
from ToolMenu.submenus.wifimenu import WifiMenu
from ToolMenu.submenus.localreconmenu import LNRMenu
from ToolMenu.submenus.webreconmenu import WRMenu
from ToolMenu.submenus.toolsmenu import ToolsMenu
from ToolMenu.submenus.utilitiesmenu import UtilitiesMenu


# root = tkinter.Tk()
# root.title("KaliPad Menu")
# curMenu = tkinter.StringVar()
# menu_label = tkinter.Label(root, textvariable=curMenu, justify=tkinter.CENTER)
# menu_label.grid(row=1, columnspan=4)
# options = [["Wi-Fi attacks", "wifi_menu"], ["Local Network", "local_menu"], ["Utilities", "utils_menu"],
#            ["Tools", "tools_menu"]]
# curMenu.set("Wi-Fi Attacks")
#
#
# def wifi_menu():
#     curMenu.set("Wifi menu")
#     print("here")
#
#
# wifi_menu_button = tkinter.Button(root, text="Wi-Fi attacks", command=wifi_menu, justify= tkinter.CENTER)
# wifi_menu_button.grid(row=2, column=1)
#
#
# def local_menu():
#     curMenu.set("Local Menu")
#
#
# local_menu_button = tkinter.Button(root, text="Local Network", command=local_menu, justify= tkinter.CENTER)
# local_menu_button.grid(row=2, column=2)
#
#
# def utils_menu():
#     curMenu.set("Utilities Menu")
#
#
# utils_menu_button = tkinter.Button(root, text="Utilities", command=utils_menu, justify= tkinter.CENTER)
# utils_menu_button.grid(row=2, column=3)
#
#
# def tools_menu():
#     curMenu.set("Tools Menu")
#
#
# tools_menu_button = tkinter.Button(root, text="Tools", command=tools_menu, justify= tkinter.CENTER)
# tools_menu_button.grid(row=2, column=4)
#
# root.mainloop()

class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs, ):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, WifiMenu, LNRMenu, WRMenu, UtilitiesMenu, ToolsMenu):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        print(cont)
        frame = self.frames[cont]
        frame.tkraise()

    def hide_frame(self, cont):
        print(cont)
        frame = self.frames[cont]
        frame.tklower()




class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Menu")
        label.pack(pady=10, padx=10)
        print(self)
        print(parent)
        print(controller)

        button1 = tk.Button(self, text="Wifi page",
                            command=lambda: controller.show_frame(WifiMenu))
        button1.pack()
        button2 = tk.Button(self, text="Local Network Recon",
                            command=lambda: controller.show_frame(LNRMenu))
        button2.pack()
        button3 = tk.Button(self, text="Web Recon",
                            command=lambda: controller.show_frame(WRMenu))
        button3.pack()
        button4 = tk.Button(self, text="Tools",
                            command=lambda: controller.show_frame(ToolsMenu))
        button4.pack()
        button5 = tk.Button(self, text="Utilities",
                            command=lambda: controller.show_frame(UtilitiesMenu))
        button5.pack()


app = MyApp()
app.geometry("640x480")
app.mainloop()
