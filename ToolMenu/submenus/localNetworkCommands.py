import os

commands = {
    'nmap': 'sudo nmap -h',
    'netdisc': 'sudo netdiscover -h',
    'wireshark': 'sudo wireshark &'
}


def nmap():
    os.system("gnome-terminal -e 'bash -c \"" + commands['nmap'] + "; bash\" '")


def netdiscover():
    os.system("gnome-terminal -e 'bash -c \"" + commands['netdisc'] + "; bash\" '")


def wireshark():
    os.system("gnome-terminal -e 'bash -c \"" + commands['wireshark'] + "\" '")
