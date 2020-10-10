from tkinter import StringVar

import pyaudio

INVITE = b'hello'
ACCEPTED = b"accepted"
CLOSE = b'closing'
ACCEPT = b'accepted'
DECLINE = b'no'


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class GuiVariables(metaclass=Singleton):

    def __init__(self):
        self.ip = StringVar()
        self.port = StringVar()
        self.destinated_port = StringVar()
        self.connected_to = StringVar()
        self.server_status = StringVar()
        self.client_status = StringVar()

        # test
        self.ip.set("192.168.8.119")
        self.destinated_port.set("6000")
        self.connected_to.set("Not connected")
        self.server_status.set("Server Stopped")
        self.client_status.set("Client Stopped")
        self.port.set("")


chunk_size = 1024
audio_format = pyaudio.paInt16
channels = 1
rate = 40000
