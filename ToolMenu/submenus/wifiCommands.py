import os
from codeUtils.configs import configs

commands = {
    'wifite_quick': 'sudo wifite --no-wps --skip-crack',
    'wifite_full': 'sudo wifite --skip-crack',
    'wireshark': 'sudo wireshark &'
}

tStart = configs['terminal_configs']['terminal_start']


def wifiteQuick():
    os.system(tStart + commands['wifite_quick'] + "")


def wifiteFull():
    os.system(tStart + commands['wifite_full'] + "")


def wireshark():
    os.system(tStart + commands['wireshark'] + "")


def btScan():
    return
