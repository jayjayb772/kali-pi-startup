import tkinter as tk

import submenus.wifiCommands as wifi
import submenus.localNetworkCommands as local
import submenus.utilitiesCommands as utils
import submenus.toolsCommands as tools
import submenus.webCommands as web
import codeUtils.interfaceClass as iface

wlan0 = iface.Interface("wlan0")
# eth0 = iface.Interface("eth0")
currentIface = wlan0


class TouchMenu(tk.Tk):
    def __init__(self, *args, **kwargs, ):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, WifiMenu, LNRMenu, LocalNmapMenu, WRMenu, UtilitiesMenu, ToolsMenu):
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

        button1 = tk.Button(self, text="Wi-Fi Attacks",
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
# region WifiMenu
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


# endregion
# region LNRMenu
class LNRMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Local Network Recon Menu",
                         font=("Courier Bold", 24), fg="white", bg="black")
        label.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        # nmap
        btnNmap = tk.Button(self, text="nmap (manual)", command=lambda: controller.show_frame(LocalNmapMenu), bg="grey",
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


def switchIface():
    global currentIface
    global wlan0
    global eth0
    if currentIface.getIfaceName() == "wlan0":
        currentIface = eth0
    else:
        currentIface = wlan0


class LocalNmapMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Local nmap Options for " + currentIface.getIfaceName(),
                         font=("Courier Bold", 24), fg="white", bg="black")
        label.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        # nmap manual
        btnNmapManual = tk.Button(self, text="nmap (manual)", command=lambda: local.nmap(), bg="grey",
                                  font=("Courier Bold", 16), fg="white")
        btnNmapManual.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # nmap list hosts
        btnNmapListHost = tk.Button(self, text="nmap list hosts",
                                    command=lambda: local.nmap("-sn", currentIface.getrange()),
                                    bg="grey",
                                    font=("Courier Bold", 16), fg="white")
        btnNmapListHost.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # nmap scan host ports
        btnNmapHostPorts = tk.Button(self, text="nmap list host ports",
                                     command=lambda: local.nmap("", currentIface.getrange()), bg="grey",
                                     font=("Courier Bold", 16), fg="white")
        btnNmapHostPorts.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # nmap scan host ports with -A
        btnNmapHostPortsAll = tk.Button(self, text="nmap list host ports (-A option)",
                                     command=lambda: local.nmap("-A", currentIface.getrange()), bg="grey",
                                     font=("Courier Bold", 16), fg="white")
        btnNmapHostPortsAll.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # switch currentIface
        btnSwitchIface = tk.Button(self, text="switch current interface",
                                   command=lambda: switchIface(), bg="grey",
                                   font=("Courier Bold", 16), fg="white", state=tk.DISABLED)
        btnSwitchIface.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        btnHome = tk.Button(self, text="Back to Local network recon menu",
                            command=lambda: controller.show_frame(LNRMenu), bg="red")
        btnHome.pack(fill=tk.X, side=tk.BOTTOM)


# endregion
# region WRMenu
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


# endregion
# region Tools
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


# endregion
# region Utilities
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

        # pwnCon
        btnMacChange = tk.Button(self, text="set random mac address for wlan0", command=lambda: utils.pwnCon(),
                                 bg="grey", font=("Courier Bold", 16), fg="white")
        btnMacChange.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # vnc
        btnVNC = tk.Button(self, text="Enable VNC", command=lambda: utils.vnc(), bg="grey", font=("Courier Bold", 16),
                           fg="white", state=tk.DISABLED)
        btnVNC.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # bluetooth
        btnBT = tk.Button(self, text="Toggle Bluetooth", command=lambda: utils.btToggle(), bg="grey",
                          font=("Courier Bold", 16),
                          fg="white", state=tk.DISABLED)
        btnBT.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
        # go home
        btnHome = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainMenu), bg="red")
        btnHome.pack(fill=tk.X, side=tk.BOTTOM)
        # reboot
        btnReboot = tk.Button(self, text="REBOOT", command=lambda: utils.reboot(), bg="red",
                              font=("Courier Bold", 16), fg="white")
        btnReboot.pack(fill=tk.X, side=tk.BOTTOM)

        # shutdown
        btnShutdown = tk.Button(self, text="SHUTDOWN", command=lambda: utils.shutdown(), bg="red",
                                font=("Courier Bold", 16), fg="white")
        btnShutdown.pack(fill=tk.X, side=tk.BOTTOM)


# endregion
# endregion


app = TouchMenu()
app.geometry("800x480")
app.mainloop()
