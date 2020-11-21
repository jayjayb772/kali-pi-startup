import os
from codeUtils.helperFunctions import openTermStayAlive, openTermDie

commands = {
    'airgeddon': 'sudo ~/Tools/airgeddon/airgeddon.sh',
    'pret': 'sudo python ~/Tools/PRET/pret.py',
    'routersploit': 'sudo python3 ~/Tools/routersploit/rsf.py',
    'metasploit': 'sudo msfconsole',
    'setk': 'sudo setoolkit',
    'gqrx': 'gqrx',
    'rtl443': 'sudo rtl_433'
}




def airgeddon():
    os.system(openTermDie(commands['airgeddon']))


def pret(target="-h", type=""):
    os.system(openTermStayAlive(commands[
        'pret'] + " " + target + " " + type))


def routersploit():
    os.system(openTermDie(commands['routersploit']))


def metasploit():
    os.system(openTermDie(commands['metasploit']))


def setk():
    os.system(openTermDie(commands['setk']))


def gqrx():
    os.system(openTermDie(commands['gqrx']))


def rtl433(option="", file=""):
    if option == "-w" and file == "":
        file = "default-out-file"
        os.system(openTermStayAlive(commands[
            'rtl443'] + " -w ~/rtl433_output/" + file + " -G 4 -A -v"))
    else:
        os.system(
            openTermStayAlive(commands['rtl443'] + " " + option))
