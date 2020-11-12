import tkinter as tk

import submenus.wifiCommands as wifi
import submenus.localNetworkCommands as local
import submenus.utilitiesCommands as utils
import submenus.toolsCommands as tools
import submenus.webCommands as web


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
        label = tk.Label(self, text="Main Menu",
                         font=("Courier Bold", 24), fg="white", bg="black")
        label.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        button1 = tk.Button(self, text="Wifi Attacks",
                            command=lambda: controller.show_frame(WifiMenu),
                            font=("Courier Bold", 16), fg="white", bg="black")
        button1.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        button2 = tk.Button(self, text="Local Network Recon",
                            command=lambda: controller.show_frame(LNRMenu),
                            font=("Courier Bold", 16), fg="white", bg="black")
        button2.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        button3 = tk.Button(self, text="Web Recon",
                            command=lambda: controller.show_frame(WRMenu),
                            font=("Courier Bold", 16), fg="white", bg="black")
        button3.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        button4 = tk.Button(self, text="Tools",
                            command=lambda: controller.show_frame(ToolsMenu),
                            font=("Courier Bold", 16), fg="white", bg="black")
        button4.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        button5 = tk.Button(self, text="Utilities",
                            command=lambda: controller.show_frame(UtilitiesMenu),
                            font=("Courier Bold", 16), fg="white", bg="black")
        button5.pack(side=tk.TOP, expand=True, fill=tk.BOTH)


# region submenus
class WifiMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Wifi Menu",
                         font=("Courier Bold", 24), fg="white", bg="black")
        label.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        # wifite quick scan
        btnQuick = tk.Button(self, text="Wifite Quick Scan", command=lambda: wifi.wifiteQuick(), bg="grey",
                             font=("Courier Bold", 16), fg="white")
        btnQuick.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
        # wifite full scan
        btnFull = tk.Button(self, text="Wifite Full Scan", command=lambda: wifi.wifiteFull(), bg="grey",
                            font=("Courier Bold", 16), fg="white")
        btnFull.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
        # wireshark
        btnWireShark = tk.Button(self, text="Start Wireshark", command=lambda: wifi.wireshark(), bg="grey",
                                 font=("Courier Bold", 16), fg="white")
        btnWireShark.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
        # bluetooth scan
        btnBTScan = tk.Button(self, text="Start Bluetooth Scan", command=lambda: wifi.btScan(), bg="grey",
                              font=("Courier Bold", 16), fg="white", state=tk.DISABLED)
        btnBTScan.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        btnHome = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainMenu), bg="red")
        btnHome.pack(fill=tk.X, side=tk.BOTTOM)


class LNRMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Local Network Recon Menu",
                         font=("Courier Bold", 24), fg="white", bg="black")
        label.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        # nmap
        btnNmap = tk.Button(self, text="nmap (manual)", command=lambda: local.nmap(), bg="grey",
                            font=("Courier Bold", 16), fg="white")
        btnNmap.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # netdiscover
        btnNetdiscover = tk.Button(self, text="netdiscover (manual)", command=lambda: local.netdiscover(), bg="grey",
                                   font=("Courier Bold", 16), fg="white")
        btnNetdiscover.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # wireshark
        btnWireShark = tk.Button(self, text="Start Wireshark", command=lambda: local.wireshark(), bg="grey",
                                 font=("Courier Bold", 16), fg="white")
        btnWireShark.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        btnHome = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainMenu), bg="red")
        btnHome.pack(fill=tk.X, side=tk.BOTTOM)


class WRMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Web Recon Menu")
        label.pack(pady=10, padx=10)
        # nmap
        btnNmap = tk.Button(self, text="nmap options", command=lambda: web.nmap(), bg="grey",
                            font=("Courier Bold", 16), fg="white")
        btnNmap.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # sqlmap
        btnSqlmap = tk.Button(self, text="Sqlmap Options", command=lambda: web.sqlmap(), bg="grey",
                              font=("Courier Bold", 16),
                              fg="white")
        btnSqlmap.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # wpscan
        btnWpscan = tk.Button(self, text="WPScan Options", command=lambda: web.wpscan(), bg="grey",
                              font=("Courier Bold", 16),
                              fg="white")
        btnWpscan.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # dirb
        btnDirb = tk.Button(self, text="Dirbuster options", command=lambda: web.dirb(), bg="grey",
                            font=("Courier Bold", 16),
                            fg="white")
        btnDirb.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
        # burpsuite
        btnBurp = tk.Button(self, text="Start BurpSuite", command=lambda: web.burp(), bg="grey",
                            font=("Courier Bold", 16),
                            fg="white")
        btnBurp.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        btnHome = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainMenu), bg="red")
        btnHome.pack(fill=tk.X, side=tk.BOTTOM)


class ToolsMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Tools Menu")
        label.pack(pady=10, padx=10)
        # airgeddon
        btnAirgeddon = tk.Button(self, text="Start Airgeddon", command=lambda: tools.airgeddon(), bg="grey",
                                 font=("Courier Bold", 16), fg="white")
        btnAirgeddon.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # PRET
        btnPRET = tk.Button(self, text="PRET (Manual)", command=lambda: tools.pret(), bg="grey",
                            font=("Courier Bold", 16), fg="white")
        btnPRET.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # routersploit
        btnRouterspoilt = tk.Button(self, text="Start Routersploit", command=lambda: tools.routersploit(), bg="grey",
                                    font=("Courier Bold", 16), fg="white")
        btnRouterspoilt.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # metasploit
        btnMeta = tk.Button(self, text="Start the Metaploit Framework", command=lambda: tools.metasploit(), bg="grey",
                            font=("Courier Bold", 16), fg="white")
        btnMeta.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # social engineering toolkit
        btnSetk = tk.Button(self, text="Start the Social Engineering Toolkit", command=lambda: tools.setk(), bg="grey",
                            font=("Courier Bold", 16), fg="white")
        btnSetk.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        btnHome = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainMenu), bg="red")
        btnHome.pack(fill=tk.X, side=tk.BOTTOM)


class UtilitiesMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Utilities Menu")
        label.pack(pady=10, padx=10)
        # ifconfig
        btnIfconfig = tk.Button(self, text="Run ifconfig", command=lambda: utils.ifconfig(), bg="grey",
                                font=("Courier Bold", 16),
                                fg="white")
        btnIfconfig.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # pwnCon
        btnPwnCon = tk.Button(self, text="Enable Pwnagotchi Connection", command=lambda: utils.pwnCon(), bg="grey",
                              font=("Courier Bold", 16),
                              fg="white", state=tk.DISABLED)
        btnPwnCon.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # vnc
        btnVNC = tk.Button(self, text="Enable VNC", command=lambda: utils.vnc(), bg="grey", font=("Courier Bold", 16),
                           fg="white", state=tk.DISABLED)
        btnVNC.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # bluetooth
        btnBT = tk.Button(self, text="Toggle Bluetooth", command=lambda: utils.btToggle(), bg="grey",
                          font=("Courier Bold", 16),
                          fg="white", state=tk.DISABLED)
        btnBT.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        btnHome = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainMenu), bg="red")
        btnHome.pack(fill=tk.X, side=tk.BOTTOM)


# endregion

app = TouchMenu()
app.geometry("800x480")
app.mainloop()
