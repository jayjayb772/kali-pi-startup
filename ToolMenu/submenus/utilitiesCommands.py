import os

commands = {
    'ifconfig': 'sudo ifconfig',
    'pwncon':'sudo ~/pwnCon.sh',
    'vnc':'sudo ~/vnc.sh',
    'bt':'help',
    'shutdown':'sudo shutdown now',
    'reboot':'sudo reboot now'
}


def ifconfig():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['ifconfig'] + "; bash\" '")


def pwnCon():
    return


def vnc():
    return


def btToggle():
    return


def shutdown():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['shutdown'] + "\" '")

def reboot():
    os.system("gnome-terminal --geometry 80x10+0+0 -e 'bash -c \"" + commands['reboot'] + "\" '")