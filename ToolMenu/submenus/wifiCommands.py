import os

commands = {
    'wifite_quick': 'sudo wifite --no-wps --skip-crack',
    'wifite_full': 'sudo wifite --skip-crack',
    'wireshark': 'sudo wireshark &'
}


def wifiteQuick():
    os.system("gnome-terminal -e 'bash -c \"" + commands['wifite_quick'] + "; bash\" '")


def wifiteFull():
    os.system("gnome-terminal -e 'bash -c \"" + commands['wifite_full'] + "; bash\" '")


def wireshark():
    os.system("gnome-terminal -e 'bash -c \"" + commands['wireshark'] + "\" '")


def btScan():
    return
