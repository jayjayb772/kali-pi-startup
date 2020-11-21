import os
from codeUtils.configs import configs

commands = {
    'nmap': 'sudo nmap',
    'netdisc': 'sudo netdiscover -h',
    'wireshark': 'sudo wireshark &'
}

tStart = configs['terminal_configs']['terminal_start']

def nmap(scanType=" -h ", scanrange=" "):
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands[
        'nmap'] + " " + scanType + " " + scanrange + "; bash\" '")


def netdiscover():
    os.system(tStart + commands['netdisc'] + "")


def wireshark():
    os.system(tStart + commands['wireshark'] + "")
