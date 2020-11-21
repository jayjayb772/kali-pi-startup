import os
from codeUtils.helperFunctions import openTermStayAlive, openTermDie

commands = {
    'ifconfig': 'sudo ifconfig',
    'pwncon': 'sudo ~/pwnCon.sh',
    'vnc': 'sudo ~/vnc.sh',
    'bt': 'help',
    'macchange': 'sudo ifconfig wlan0 down && sudo macchanger -r wlan0 && sudo ifconfig wlan0 up',
    'shutdown': 'sudo shutdown now',
    'reboot': 'sudo reboot now'
}


def ifconfig():
    os.system(openTermStayAlive(commands['ifconfig']))


def pwnCon():
    return


def macchange():
    os.system(openTermStayAlive(commands['macchange']))


def vnc():
    return


def btToggle():
    return


def shutdown():
    os.system(openTermDie(commands['shutdown']))


def reboot():
    os.system(openTermDie(commands['reboot']))
