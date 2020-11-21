import os
from codeUtils.helperFunctions import openTermStayAlive, openTermDie

commands = {
    'nmap': 'sudo nmap -h',
    'sqlmap': 'sudo sqlmap -h',
    'wpscan': 'sudo wpscan -h',
    'dirb': 'sudo dirb -h',
    'burp': 'BurpSuiteCommunity &'

}


def nmap():
    os.system(openTermStayAlive(commands['nmap']))


def sqlmap():
    os.system(openTermStayAlive(commands['sqlmap']))


def wpscan():
    os.system(openTermStayAlive(commands['wpscan']))


def dirb():
    os.system(openTermStayAlive(commands['dirb']))


def burp():
    os.system(openTermDie(commands['burp']))
