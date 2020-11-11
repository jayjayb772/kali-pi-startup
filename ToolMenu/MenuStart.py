from Tkinter import *

root = tkinter.TK()
root.title("KaliPad Menu")

options = ["Wi-Fi attacks", "Local Network", "Utilities"]
menu_option = tkinter.StringVar()
menu_option.set(options[0])

main_option_menu=tkinter.OptionMenu(root, menu_option, *options)

