import os

commands = {
    'airgeddon': 'cd ~/Tools/airgeddon && sudo ~/Tools/airgeddon/airgeddon.sh',
    'pret': 'cd ~/Tools/PRET && sudo python ~/Tools/PRET/pret.py',
    'routersploit': 'cd ~/Tools/routersploit && sudo python3 ~/Tools/routersploit/rsf.py',
    'metasploit': 'sudo msfconsole',
    'setk': 'sudo setoolkit',
    'gqrx': 'gqrx',
    'rtl443': 'sudo rtl_433'
}


def airgeddon():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['airgeddon'] + "\" '")


def pret(target="-h", type=""):
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands[
        'pret'] + " " + target + " " + type + "; bash\" '")


def routersploit():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['routersploit'] + "\" '")


def metasploit():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['metasploit'] + "\" '")


def setk():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['setk'] + "\" '")


def gqrx():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['gqrx'] + "; bash\" '")


def rtl433(option="", file=""):
    if option == "-w" and file == "":
        file = "default-out-file"
        os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands[
            'rtl443'] + " -w ~/rtl433_output/" + file + " -G 4 -A -v; bash\" '")
    else:
        os.system(
            "gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['rtl443'] + " " + option + "; bash\" '")
