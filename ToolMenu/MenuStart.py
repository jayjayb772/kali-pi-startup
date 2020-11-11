import tkinter

root = tkinter.Tk()
root.title("KaliPad Menu")
text = tk.Text(root, width=15, height=3)
options = ["Wi-Fi attacks", "Local Network", "Utilities"]
menu_option = tkinter.StringVar()
menu_option.set(options[0])

def updateOptions():
    text.insert(tkinter.END, menu_option.get()
    


main_option_menu=tkinter.OptionMenu(root, menu_option, *options)
menu = tkinter.Menu(root)

main_option_menu.pack()
root.config(menu=menu)


root.mainloop()

