# import tkinter as tk
# from ToolMenu.submenus.wifimenu import WifiMenu
# from ToolMenu.submenus.localreconmenu import LNRMenu
# from ToolMenu.submenus.webreconmenu import WRMenu
# from ToolMenu.submenus.toolsmenu import ToolsMenu
# from ToolMenu.submenus.utilitiesmenu import UtilitiesMenu
#
#
# class MainMenu(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Main Menu")
#         label.pack(pady=10, padx=10)
#         print(self)
#         print(parent)
#         print(controller)
#
#         button1 = tk.Button(self, text="Wifi page",
#                             command=lambda: controller.show_frame(WifiMenu))
#         button1.pack()
#         button2 = tk.Button(self, text="Local Network Recon",
#                             command=lambda: controller.show_frame(LNRMenu))
#         button2.pack()
#         button3 = tk.Button(self, text="Web Recon",
#                             command=lambda: controller.show_frame(WRMenu))
#         button3.pack()
#         button4 = tk.Button(self, text="Tools",
#                             command=lambda: controller.show_frame(ToolsMenu))
#         button4.pack()
#         button5 = tk.Button(self, text="Utilities",
#                             command=lambda: controller.show_frame(UtilitiesMenu))
#         button5.pack()