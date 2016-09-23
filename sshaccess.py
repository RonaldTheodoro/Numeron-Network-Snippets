from os import system
from os.path import join
from os.path import dirname
from os.path import abspath
from decouple import config


class SSHAccess:

    def __init__(self, ip):
        PUTTY_PATH = join(dirname(abspath(__file__)), 'programs', 'putty.exe')
        CMD = PUTTY_PATH + ' -ssh {}@{} -pw {}'
        system(CMD.format(config('SSHUSER'), ip, config('SSHPASSWORD')))

