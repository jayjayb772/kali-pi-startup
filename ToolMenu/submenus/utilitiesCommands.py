import os
from codeUtils.configs import configs

commands = {
    'ifconfig': 'sudo ifconfig',
    'pwncon': 'sudo ~/pwnCon.sh',
    'vnc': 'sudo ~/vnc.sh',
    'bt': 'help',
    'macchange': 'sudo ifconfig wlan0 down && sudo macchanger -r wlan0 && sudo ifconfig wlan0 up',
    'shutdown': 'sudo shutdown now',
    'reboot': 'sudo reboot now'
}

tStart = configs['terminal_configs']['terminal_start']

def ifconfig():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['ifconfig'] + "; bash\" '")


def pwnCon():
    return


def macchange():
    os.system(tStart + commands['macchange'] + "")


def vnc():
    return


def btToggle():
    return


def shutdown():
    os.system(tStart + commands['shutdown'] + "")


def reboot():
    os.system(tStart + commands['reboot'] + "")
