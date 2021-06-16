import tkinter as tk
from dotenv import load_dotenv


import submenus.wifiCommands as wifi
import submenus.localNetworkCommands as local
import submenus.utilitiesCommands as utils
import submenus.toolsCommands as tools
import submenus.webCommands as web
load_dotenv()

# import codeUtils.interfaceClass as iface


# wlan0 = iface.Interface("wlan0")
# eth0 = iface.Interface("eth0")
# currentIface = wlan0


class TouchMenu(tk.Tk):
    def __init__(self, *args, **kwargs, ):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, WifiMenu, LNRMenu, LocalNmapMenu, WRMenu, UtilitiesMenu, ToolsMenu, PretMenu, RTL433Menu, RTL433OutputMenu):
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
        btnNmap = tk.Button(self, text="nmap options", command=lambda: controller.show_frame(LocalNmapMenu), bg="grey",
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
        label = tk.Label(self, text="Local nmap Options for " + " ",  # currentIface.getIfaceName(),
                         font=("Courier Bold", 24), fg="white", bg="black")
        label.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        # nmap manual
        btnNmapManual = tk.Button(self, text="nmap (manual)", command=lambda: local.nmap(), bg="grey",
                                  font=("Courier Bold", 16), fg="white")
        btnNmapManual.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # nmap list hosts
        btnNmapListHost = tk.Button(self, text="nmap list hosts",
                                    command=lambda: local.nmap("-sn", " "),  # currentIface.getrange()),
                                    bg="grey",
                                    font=("Courier Bold", 16), fg="white")
        btnNmapListHost.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # nmap scan host ports
        btnNmapHostPorts = tk.Button(self, text="nmap list host ports",
                                     command=lambda: local.nmap("", " "),  # currentIface.getrange()), bg="grey",
                                     font=("Courier Bold", 16), fg="white")
        btnNmapHostPorts.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # nmap scan host ports with -A
        btnNmapHostPortsAll = tk.Button(self, text="nmap list host ports (-A option)",
                                        command=lambda: local.nmap("-A", " "),  # currentIface.getrange())
                                        bg="grey", font=("Courier Bold", 16), fg="white")
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
        label = tk.Label(self, text="Web Recon Menu",
                         font=("Courier Bold", 24), fg="white", bg="black")
        label.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
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
        label = tk.Label(self, text="Tools Menu",
                         font=("Courier Bold", 24), fg="white", bg="black")
        label.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        # airgeddon
        btnAirgeddon = tk.Button(self, text="Start Airgeddon", command=lambda: tools.airgeddon(), bg="grey",
                                 font=("Courier Bold", 16), fg="white")
        btnAirgeddon.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # PRET
        btnPRET = tk.Button(self, text="PRET options", command=lambda: controller.show_frame(PretMenu), bg="grey",
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

        # gqrx sdr
        btnGqrx = tk.Button(self, text="Start GQRX SDR", command=lambda: tools.gqrx(), bg="grey",
                            font=("Courier Bold", 16), fg="white")
        btnGqrx.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # rtl443 sdr tool
        btnRtl443 = tk.Button(self, text="Start the RTL443 SDR tool", command=lambda: controller.show_frame(RTL433Menu),
                              bg="grey",
                              font=("Courier Bold", 16), fg="white")
        btnRtl443.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        btnHome = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainMenu), bg="red")
        btnHome.pack(fill=tk.X, side=tk.BOTTOM)


class PretMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PRET Menu",
                         font=("Courier Bold", 24), fg="white", bg="black")
        label.pack(side=tk.TOP, fill=tk.X)
        target = tk.StringVar()

        # ip enter box
        lblTarget = tk.Label(self, bg="white", font=("Courier Bold", 12), fg="black",
                             text="Please type the printer's IP address below")
        lblTarget.pack(fill=tk.X, side=tk.TOP)
        entrTarget = tk.Entry(self, bg="white", font=("Courier Bold", 12), fg="black", textvariable=target)
        entrTarget.pack(fill=tk.X, side=tk.TOP)

        btnBack = tk.Button(self, text="Back to Tools Menu",
                            command=lambda: controller.show_frame(ToolsMenu), bg="red")
        btnBack.pack(fill=tk.X, side=tk.BOTTOM)

        btnHelp = tk.Button(self, text="Run pret help command", command=lambda: tools.pret(),
                            bg="grey", font=("Courier Bold", 16), fg="white")
        btnHelp.pack(fill=tk.X, side=tk.BOTTOM)

        # printer language buttons

        btnPS = tk.Button(self, text="Start Pret using PS", command=lambda: tools.pret(target.get(), "ps"),
                          bg="grey", font=("Courier Bold", 16), fg="white")
        btnPS.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        btnPCL = tk.Button(self, text="Start Pret using PCL", command=lambda: tools.pret(target.get(), "pcl"),
                           bg="grey", font=("Courier Bold", 16), fg="white")
        btnPCL.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        btnPJL = tk.Button(self, text="Start Pret using PJL", command=lambda: tools.pret(target.get(), "pjl"),
                           bg="grey", font=("Courier Bold", 16), fg="white")
        btnPJL.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)


class RTL433Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="RTL_433 Menu",
                         font=("Courier Bold", 24), fg="white", bg="black")
        label.pack(side=tk.TOP, fill=tk.X)

        # printer language buttons

        btnHelp = tk.Button(self, text="Run \"rtl_433 -h\" (Help)", command=lambda: tools.rtl433("-h", ""),
                            bg="grey", font=("Courier Bold", 16), fg="white")
        btnHelp.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        btnG = tk.Button(self, text="Run \"rtl_433 -G\" (Decode All)", command=lambda: tools.rtl433("-G 4", ""),
                         bg="grey", font=("Courier Bold", 16), fg="white")
        btnG.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        btnA = tk.Button(self, text="Run \"rtl_433 -A\" (Dump signals)", command=lambda: tools.rtl433("-A", ""),
                         bg="grey", font=("Courier Bold", 16), fg="white")
        btnA.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        btnOut = tk.Button(self, text="Output to file menu", command=lambda: controller.show_frame(RTL433OutputMenu),
                           bg="grey", font=("Courier Bold", 16), fg="white")
        btnOut.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        btnBack = tk.Button(self, text="Back to Tools Menu",
                            command=lambda: controller.show_frame(ToolsMenu), bg="red")
        btnBack.pack(fill=tk.X, side=tk.BOTTOM)
        


class RTL433OutputMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="RTL_433 Output Menu",
                         font=("Courier Bold", 24), fg="white", bg="black")
        label.pack(side=tk.TOP, fill=tk.X)
        file = tk.StringVar()

        # printer language buttons
        lblFile = tk.Label(self, bg="white", font=("Courier Bold", 12), fg="black",
                           text="Please type the name for the output")
        lblFile.pack(fill=tk.X, side=tk.TOP)
        entrFile = tk.Entry(self, bg="white", font=("Courier Bold", 12), fg="black", textvariable=file)
        entrFile.pack(fill=tk.X, side=tk.TOP)

        btnOut = tk.Button(self, text="Run \"rtl_433 -w\"", command=lambda: tools.rtl433("-w", file.get()),
                           bg="grey", font=("Courier Bold", 16), fg="white")
        btnOut.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        btnBack = tk.Button(self, text="Back to RTL433 Menu",
                            command=lambda: controller.show_frame(RTL433Menu), bg="red")
        btnBack.pack(fill=tk.X, side=tk.BOTTOM)


# endregion
# region Utilities
class UtilitiesMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Utilities Menu",
                         font=("Courier Bold", 24), fg="white", bg="black")
        label.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
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

        # macchange
        btnMacChange = tk.Button(self, text="set random mac address for wlan0", command=lambda: utils.macchange(),
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
