from os import system
from os.path import join
from os.path import dirname
from os.path import abspath


class VNCAccess:

    def __init__(self, ip, terminal):
        VNC_PATH = join(
            dirname(abspath(__file__)), 'programs', 'VNCViewer.exe')
        system(VNC_PATH + ' {}:{} -geometry 500x500'.format(ip, terminal))

VNCAccess('10.18.88.100', '1')
