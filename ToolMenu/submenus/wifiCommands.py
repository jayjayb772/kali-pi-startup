import os

commands = {
    'wifite_quick': 'sudo wifite --no-wps --skip-crack',
    'wifite_full': 'sudo wifite --skip-crack',
    'wireshark': 'sudo wireshark &'
}


def wifiteQuick():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['wifite_quick'] + "\" '")


def wifiteFull():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['wifite_full'] + "\" '")


def wireshark():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['wireshark'] + "\" '")


def btScan():
    return
