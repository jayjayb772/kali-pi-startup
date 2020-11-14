import os

commands = {
    'nmap': 'sudo nmap -h',
    'sqlmap': 'sudo sqlmap -h',
    'wpscan': 'sudo wpscan -h',
    'dirb': 'sudo dirb -h',
    'burp': 'BurpSuiteCommunity &'

}


def nmap():
    os.system("gnome-terminal --geometry 80x15+0+0 -e 'bash -c \"" + commands['nmap'] + "; bash\" '")


def sqlmap():
    os.system("gnome-terminal --geometry 80x15+0+0 -e 'bash -c \"" + commands['sqlmap'] + "; bash\" '")


def wpscan():
    os.system("gnome-terminal --geometry 80x15+0+0 -e 'bash -c \"" + commands['wpscan'] + "; bash\" '")


def dirb():
    os.system("gnome-terminal --geometry 80x15+0+0 -e 'bash -c \"" + commands['dirb'] + "; bash\" '")


def burp():
    os.system("gnome-terminal --geometry 80x15+0+0 -e 'bash -c \"" + commands['burp'] + "\" '")
