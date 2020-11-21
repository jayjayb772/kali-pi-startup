import os
from codeUtils.helperFunctions import openTermStayAlive, openTermDie

commands = {
    'nmap': 'sudo nmap',
    'netdisc': 'sudo netdiscover -h',
    'wireshark': 'sudo wireshark &'
}


def nmap(scanType=" -h ", scanrange=" "):
    os.system(openTermStayAlive(commands[
        'nmap'] + " " + scanType + " " + scanrange))


def netdiscover():
    os.system(openTermStayAlive(commands['netdisc']))


def wireshark():
    os.system(openTermDie(commands['wireshark']))
