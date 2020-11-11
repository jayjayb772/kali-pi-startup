import tkinter

root = tkinter.Tk()
root.title("KaliPad Menu")
curMenu = tkinter.StringVar()
menu_label = tkinter.Label(root, textvariable=curMenu, justify=tkinter.CENTER)
menu_label.grid(row=1, columnspan=4)
options = [["Wi-Fi attacks", "wifi_menu"], ["Local Network", "local_menu"], ["Utilities", "utils_menu"],
           ["Tools", "tools_menu"]]
curMenu.set("Wi-Fi Attacks")


def wifi_menu():
    curMenu.set("Wifi menu")
    print("here")


wifi_menu_button = tkinter.Button(root, text="Wi-Fi attacks", command=wifi_menu, justify= tkinter.CENTER)
wifi_menu_button.grid(row=2, column=1)


def local_menu():
    curMenu.set("Local Menu")


local_menu_button = tkinter.Button(root, text="Local Network", command=local_menu, justify= tkinter.CENTER)
local_menu_button.grid(row=2, column=2)


def utils_menu():
    curMenu.set("Utilities Menu")


utils_menu_button = tkinter.Button(root, text="Utilities", command=utils_menu, justify= tkinter.CENTER)
utils_menu_button.grid(row=2, column=3)


def tools_menu():
    curMenu.set("Tools Menu")


tools_menu_button = tkinter.Button(root, text="Tools", command=tools_menu, justify= tkinter.CENTER)
tools_menu_button.grid(row=2, column=4)

root.mainloop()
