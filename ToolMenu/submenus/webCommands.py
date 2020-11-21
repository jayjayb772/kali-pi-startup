import os
from codeUtils.configs import configs

commands = {
    'nmap': 'sudo nmap -h',
    'sqlmap': 'sudo sqlmap -h',
    'wpscan': 'sudo wpscan -h',
    'dirb': 'sudo dirb -h',
    'burp': 'BurpSuiteCommunity &'

}

tStart = configs['terminal_configs']['terminal_start']

def nmap():
    os.system(tStart + commands['nmap'] + "")


def sqlmap():
    os.system(tStart + commands['sqlmap'] + "")


def wpscan():
    os.system(tStart + commands['wpscan'] + "")


def dirb():
    os.system(tStart + commands['dirb'] + "")


def burp():
    os.system(tStart + commands['burp'] + "")
