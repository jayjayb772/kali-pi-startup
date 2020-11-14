import os

commands = {
    'nmap': 'sudo nmap',
    'netdisc': 'sudo netdiscover -h',
    'wireshark': 'sudo wireshark &'
}


def nmap(scanType="-h", scanrange=""):
    os.system("gnome-terminal --geometry 80x15+0+0 -e 'bash -c \"" + commands['nmap'] + scanType + scanrange + "; bash\" '")


def netdiscover():
    os.system("gnome-terminal --geometry 80x15+0+0 -e 'bash -c \"" + commands['netdisc'] + "; bash\" '")


def wireshark():
    os.system("gnome-terminal --geometry 80x15+0+0 -e 'bash -c \"" + commands['wireshark'] + "\" '")
