import os

commands = {
    'airgeddon': 'sudo ~/Tools/airgeddon/airgeddon.sh',
    'pret': 'sudo python ~/Tools/PRET/pret.py -h',
    'routersploit': 'sudo python3 ~/Tools/routersploit/rsf.py',
    'metasploit': 'sudo msfconsole',
    'setk': 'sudo setoolkit'
}


def airgeddon():
    os.system("gnome-terminal -e 'bash -c \"" + commands['airgeddon'] + "; bash\" '")


def pret():
    os.system("gnome-terminal -e 'bash -c \"" + commands['pret'] + "; bash\" '")


def routersploit():
    os.system("gnome-terminal -e 'bash -c \"" + commands['routersploit'] + "; bash\" '")


def metasploit():
    os.system("gnome-terminal -e 'bash -c \"" + commands['metasploit'] + "; bash\" '")


def setk():
    os.system("gnome-terminal -e 'bash -c \"" + commands['setk'] + "; bash\" '")
