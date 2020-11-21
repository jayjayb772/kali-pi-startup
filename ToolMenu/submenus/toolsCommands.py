import os
from codeUtils.configs import configs

commands = {
    'airgeddon': 'sudo ~/Tools/airgeddon/airgeddon.sh',
    'pret': 'cd ~/Tools/PRET && sudo python ~/Tools/PRET/pret.py',
    'routersploit': 'cd ~/Tools/routersploit && sudo python3 ~/Tools/routersploit/rsf.py',
    'metasploit': 'sudo msfconsole',
    'setk': 'sudo setoolkit',
    'gqrx': 'gqrx',
    'rtl443': 'sudo rtl_433'
}

tStart = configs['terminal_configs']['terminal_start']


def airgeddon():
    os.system(tStart + commands['airgeddon'] + "")


def pret(target="-h", type=""):
    os.system(tStart + commands[
        'pret'] + " " + target + " " + type + "")


def routersploit():
    os.system(tStart + commands['routersploit'] + "")


def metasploit():
    os.system(tStart + commands['metasploit'] + "")


def setk():
    os.system(tStart + commands['setk'] + "")


def gqrx():
    os.system(tStart + commands['gqrx'] + "")


def rtl433(option="", file=""):
    if option == "-w" and file == "":
        file = "default-out-file"
        os.system(tStart + commands[
            'rtl443'] + " -w ~/rtl433_output/" + file + " -G 4 -A -v")
    else:
        os.system(
            tStart + commands['rtl443'] + " " + option + "")
