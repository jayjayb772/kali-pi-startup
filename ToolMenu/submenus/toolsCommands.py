import os

commands = {
    'airgeddon': 'cd ~/Tools/airgeddon && sudo ~/Tools/airgeddon/airgeddon.sh',
    'pret': 'cd ~/Tools/PRET && sudo python ~/Tools/PRET/pret.py',
    'routersploit': 'cd ~/Tools/routersploit && sudo python3 ~/Tools/routersploit/rsf.py',
    'metasploit': 'sudo msfconsole',
    'setk': 'sudo setoolkit'
}


def airgeddon():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['airgeddon'] + "\" '")


def pret(target="-h", type=""):
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands[
        'pret'] + " " + target + " " + type + "; bash\" '")
    print("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands[
        'pret'] + " " + target + " " + type + "; bash\" '")


def routersploit():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['routersploit'] + "\" '")


def metasploit():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['metasploit'] + "\" '")


def setk():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['setk'] + "\" '")
