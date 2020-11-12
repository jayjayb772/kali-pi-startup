import tkinter as tk

from ToolMenu.submenus.wifiCommands import wifiteQuick


class TouchMenu(tk.Tk):

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
        frame = self.frames[cont]
        frame.tkraise()


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Menu")
        label.grid(row=0, columnspan=10, column=5, pady=10, padx=10)

        button1 = tk.Button(self, text="Wifi Attacks",
                            command=lambda: controller.show_frame(WifiMenu))
        button1.grid(row=2, rowspan=2, column=3, pady=10, padx=10)
        button2 = tk.Button(self, text="Local Network Recon",
                            command=lambda: controller.show_frame(LNRMenu))
        button2.grid(row=2, rowspan=2, column=5, pady=10, padx=10)
        button3 = tk.Button(self, text="Web Recon",
                            command=lambda: controller.show_frame(WRMenu))
        button3.grid(row=2, rowspan=2, column=7, pady=10, padx=10)
        button4 = tk.Button(self, text="Tools",
                            command=lambda: controller.show_frame(ToolsMenu))
        button4.grid(row=2, rowspan=2, column=9, pady=10, padx=10)
        button5 = tk.Button(self, text="Utilities",
                            command=lambda: controller.show_frame(UtilitiesMenu))
        button5.grid(row=2, rowspan=2, column=11, pady=10, padx=10)


# region submenus
class WifiMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Wifi Menu")
        label.pack(pady=10, padx=10)
        #wifite quick scan
        btnQuick = tk.Button(self, text="Wifite Quick Scan", command=lambda: wifiteQuick())

        #wifite full scan
        #wireshark
        #bluetooth scan
        btnHome = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainMenu))
        btnQuick.pack()
        btnHome.pack()


class ToolsMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Tools Menu")
        label.pack(pady=10, padx=10)
        #airrgeddon
        #PRET
        #routersploit
        #social engineering toolkit
        #metasploit
        btnHome = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainMenu))
        btnHome.pack()


class LNRMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Local Network Recon Menu")
        label.pack(pady=10, padx=10)
        #nmap
        #netdiscover
        #wireshark
        btnHome = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainMenu))
        btnHome.pack()


class UtilitiesMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Utilities Menu")
        label.pack(pady=10, padx=10)
        #ifconfig
        #pwnCon
        #vnc
        #bluetooth
        btnHome = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainMenu))
        btnHome.pack()


class WRMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Web Recon Menu")
        label.pack(pady=10, padx=10)
        #nmap
        #sqlmap
        #wpscan
        #dirb
        #burpsuite
        btnHome = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainMenu))
        btnHome.pack()


# endregion

app = TouchMenu()
app.geometry("640x480")
app.mainloop()
