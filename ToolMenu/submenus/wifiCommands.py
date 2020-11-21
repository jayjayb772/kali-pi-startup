import os
from codeUtils.helperFunctions import openTermStayAlive, openTermDie

commands = {
    'wifite_quick': 'sudo wifite --no-wps --skip-crack',
    'wifite_full': 'sudo wifite --skip-crack',
    'wireshark': 'sudo wireshark &'
}


def wifiteQuick():
    os.system(openTermDie(commands['wifite_quick']))


def wifiteFull():
    os.system(openTermDie(commands['wifite_full']))


def wireshark():
    os.system(openTermDie(commands['wireshark']))


def btScan():
    return
