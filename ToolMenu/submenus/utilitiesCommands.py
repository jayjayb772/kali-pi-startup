import os

commands = {
    'ifconfig': 'sudo ifconfig',
    'pwncon':'sudo ~/pwnCon.sh',
    'vnc':'sudo ~/vnc.sh',
    'bt':'help'
}


def ifconfig():
    os.system("gnome-terminal -e 'bash -c \"" + commands['ifconfig'] + "; bash\" '")


def pwnCon():
    return


def vnc():
    return


def btToggle():
    return
