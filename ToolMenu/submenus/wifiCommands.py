import os

commands = {
    'wifite_quick': 'sudo wifite --no-wps --skip-crack'
}


def wifiteQuick():
    os.system("gnome-terminal -e 'bash -c \"" + commands['wifite_quick'] + "; bash\" '")
