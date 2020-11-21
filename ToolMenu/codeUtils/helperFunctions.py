from configs import configs

dieL = configs['terminal_configs']['terminal_start_die_left']
dieR = configs['terminal_configs']['terminal_start_die_right']
liveL = configs['terminal_configs']['terminal_start_stay_alive_left']
liveR = configs['terminal_configs']['terminal_start_stay_alive_right']


def openTermStayAlive(cmd):
    return liveL + cmd + liveR


def openTermDie(cmd):
    return dieL + cmd + dieR
